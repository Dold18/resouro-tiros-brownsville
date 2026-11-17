#!/usr/bin/env python3
"""Safely rebuild the teammate's ORIGINAL v1.0 source and compare the result.

The committed submission is never opened for writing. Rebuilding occurs in a
temporary directory. Comparison is of workbook structure, named inputs, the
underlying formulas, and input/static cells, NOT Excel's cached formula values.

Usage:
    python tools/rebuild_and_verify.py
    python tools/rebuild_and_verify.py --output ./rebuild-v1.0.xlsx

Requires only Python's standard library plus the original generator's declared
`openpyxl` dependency (see requirements.txt). No spreadsheet is modified in place.
"""
from __future__ import annotations

import argparse
from decimal import Decimal, InvalidOperation
from hashlib import sha256
from math import isclose
from pathlib import Path
import re
import shutil
import subprocess
import sys
from tempfile import TemporaryDirectory
from zipfile import ZipFile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
SUBMITTED = ROOT / "model" / "Tiros_Brownsville_Model.xlsx"
SOURCE = ROOT / "model" / "build"
SHA256_FINAL = "aa6aa7cc745665109e5d11ed9378343f1c70c8aac99ba92c3ac748dd3a9ba98b"
NS = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
NUMERAL = re.compile(r"(?<![\w.$])(?:\d+(?:\.\d+)?|\.\d+)(?:[eE][+-]?\d+)?(?![\w])")
REQUIRED_SOURCE = ("build_model.py", "inputs.py", "sources.py", "style.py", "mrec_block.py")


def canonical_formula(formula: str | None) -> str:
    """Canonicalize numeric spelling only (e.g., 5.641e6 vs. 5641000).

    The final submitted workbook was saved after Excel formula normalization,
    whereas the source generator includes Python scientific-notation literals.
    """
    def normal(m: re.Match[str]) -> str:
        try:
            n = Decimal(m.group(0))
        except InvalidOperation:
            return m.group(0)
        return format(n.normalize(), "f")
    return NUMERAL.sub(normal, formula or "")


def workbook_cells(path: Path):
    """Read XLSX XML without modifying its spreadsheet cells or formula caches."""
    with ZipFile(path) as archive:
        book = ET.fromstring(archive.read("xl/workbook.xml"))
        sheet_names = [s.attrib["name"] for s in book.findall("m:sheets/m:sheet", NS)]
        defined = {
            x.attrib["name"]: (x.text or "").replace("'Inputs'!", "Inputs!")
            for x in book.findall("m:definedNames/m:definedName", NS)
        }
        shared = []
        if "xl/sharedStrings.xml" in archive.namelist():
            table = ET.fromstring(archive.read("xl/sharedStrings.xml"))
            shared = [
                "".join((t.text or "") for t in si.findall(".//m:t", NS))
                for si in table.findall("m:si", NS)
            ]
        contents = {}
        for i, name in enumerate(sheet_names, start=1):
            xml = ET.fromstring(archive.read(f"xl/worksheets/sheet{i}.xml"))
            formulas, values = {}, {}
            for cell in xml.findall(".//m:sheetData/m:row/m:c", NS):
                address = cell.attrib["r"]
                f = cell.find("m:f", NS)
                v = cell.find("m:v", NS)
                if f is not None:
                    formulas[address] = canonical_formula(f.text)
                    continue
                if v is not None:
                    value = shared[int(v.text)] if cell.attrib.get("t") == "s" else v.text
                elif cell.attrib.get("t") == "inlineStr":
                    value = "".join((t.text or "") for t in cell.findall(".//m:is/m:t", NS))
                else:
                    value = ""
                values[address] = value
            contents[name] = (formulas, values)
        return sheet_names, defined, contents


def values_equivalent(a: str | None, b: str | None) -> bool:
    if (a or "") == (b or ""):
        return True
    try:
        return isclose(float(a), float(b), rel_tol=1e-12, abs_tol=1e-8)
    except (ValueError, TypeError, OverflowError):
        return False


def verify_semantics(rebuilt: Path, submitted: Path = SUBMITTED) -> dict:
    src_names, src_def, src_data = workbook_cells(submitted)
    out_names, out_def, out_data = workbook_cells(rebuilt)
    if src_names != out_names:
        raise AssertionError(f"Worksheet order changed: {out_names!r}")
    if src_def != out_def:
        raise AssertionError("Defined name locations changed")
    formula_total = 0
    literal_total = 0
    for sheet in src_names:
        expected_f, expected_v = src_data[sheet]
        actual_f, actual_v = out_data[sheet]
        if expected_f != actual_f:
            for cell in sorted(set(expected_f) | set(actual_f)):
                if expected_f.get(cell) != actual_f.get(cell):
                    raise AssertionError(f"Formula mismatch at {sheet}!{cell}: {expected_f.get(cell)} != {actual_f.get(cell)}")
        for cell in set(expected_v) | set(actual_v):
            if not values_equivalent(expected_v.get(cell), actual_v.get(cell)):
                raise AssertionError(f"Static cell mismatch at {sheet}!{cell}: {expected_v.get(cell)!r} != {actual_v.get(cell)!r}")
        formula_total += len(expected_f)
        literal_total += len(expected_v)
    return {"sheets": len(src_names), "named_inputs": len(src_def), "formulas": formula_total, "static_cells": literal_total}


def safe_rebuild(output: Path | None = None) -> dict:
    """Generate a temp XLSX, compare, and optionally save a SEPARATE rebuild."""
    before = sha256(SUBMITTED.read_bytes()).hexdigest()
    if before != SHA256_FINAL:
        raise AssertionError("Submitted workbook hash differs from the final submission; aborting")
    if output is not None and output.resolve() == SUBMITTED.resolve():
        raise ValueError("Refusing to overwrite the exact submitted workbook")
    for name in REQUIRED_SOURCE:
        if not (SOURCE / name).is_file():
            raise FileNotFoundError(f"Missing original teammate source: {name}")
    with TemporaryDirectory(prefix="resouro-v1-rebuild-") as tmp:
        workdir = Path(tmp)
        scripts = workdir / "model" / "build"
        scripts.mkdir(parents=True)
        for source_name in REQUIRED_SOURCE:
            shutil.copy2(SOURCE / source_name, scripts / source_name)
        subprocess.run(
            [sys.executable, str(scripts / "build_model.py")],
            cwd=workdir, check=True, capture_output=True, text=True,
        )
        rebuilt = workdir / "model" / "Tiros_Brownsville_Model.xlsx"
        if not rebuilt.is_file():
            raise AssertionError("Original generator did not create the workbook")
        stats = verify_semantics(rebuilt)
        if output is not None:
            output.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(rebuilt, output)
    after = sha256(SUBMITTED.read_bytes()).hexdigest()
    if before != after:
        raise AssertionError("The submitted workbook changed during verification")
    stats["submitted_sha256_unchanged"] = True
    return stats


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Optional destination for a separate, generated XLSX")
    args = parser.parse_args()
    result = safe_rebuild(args.output)
    print("PASS — original v1.0 generator reproduces the submitted workbook structure")
    print(f"  {result['sheets']} sheets, {result['named_inputs']} named inputs, "
          f"{result['formulas']} formulas, {result['static_cells']} static cells")
    print("  Final submitted workbook SHA-256 unchanged")
    print("  Note: Excel formula caches are not independently recalculated by the generator")
    if args.output:
        print(f"  Separate rebuilt workbook: {args.output}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, ValueError, FileNotFoundError, subprocess.CalledProcessError) as exc:
        print(f"FAIL — {exc}", file=sys.stderr)
        raise SystemExit(1)
