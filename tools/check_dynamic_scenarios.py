#!/usr/bin/env python3
"""OPTIONAL scenario-recalculation QA using an available artifact_tool engine.

Unlike the standard tests, this imports the submitted XLSX and computes its
existing formulas after transient, in-memory input edits. It never exports an
edited copy. This is an optional verification utility; artifact_tool is not a
requirement for readers to use the original Python/openpyxl workbook builder.
"""
import json
from pathlib import Path

try:
    from artifact_tool import Blob, SpreadsheetFile
except ImportError as exc:
    raise SystemExit("Optional check unavailable: artifact_tool is not installed") from exc

ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / "model" / "Tiros_Brownsville_Model.xlsx"
BASE = [19.038587936630293, -70.13012232616151, -73.62415934029838]
BRAZIL_ACID_220 = [8.023451269854412, -70.13012232616151, -84.63929600707426]
TEXAS_ACID_225 = [19.038587936630293, -81.14525899293739, -73.62415934029838]
CRISIS = [-38.2401227306043, -119.698237326653, -130.90287000753295]


def assert_vector(actual, expected, label):
    for observed, target in zip(actual, expected, strict=True):
        if abs(observed - target) > 1e-5:
            raise AssertionError(f"{label}: {observed} != {target}")


def main():
    wb = SpreadsheetFile.import_xlsx(Blob.load(str(BOOK)))
    inp = wb.worksheets.get_item("Inputs")

    def npvs():
        result = json.loads(wb.inspect({
            "kind": "table", "range": "Summary!D16:F17", "include": "values",
            "table_max_rows": 2, "table_max_cols": 3
        }).ndjson)
        return result["values"]

    assert_vector(npvs()[0], BASE, "normal baseline")
    assert_vector(npvs()[1], CRISIS, "crisis baseline")

    # Change only one normal-price input in the imported, in-memory model.
    # The 2026-crisis rows must remain unchanged.
    inp.get_range("C27").values = [[220]]  # P_acid_BR: $170 -> $220/t
    assert_vector(npvs()[0], BRAZIL_ACID_220, "Brazil price stress")
    assert_vector(npvs()[1], CRISIS, "Brazil price stress crisis independence")
    inp.get_range("C27").values = [[170]]

    inp.get_range("C28").values = [[225]]  # P_acid_TX: $175 -> $225/t
    assert_vector(npvs()[0], TEXAS_ACID_225, "Texas price stress")
    assert_vector(npvs()[1], CRISIS, "Texas price stress crisis independence")
    inp.get_range("C28").values = [[175]]
    assert_vector(npvs()[0], BASE, "restored baseline")
    print("PASS: original workbook formulas recalculated in memory")
    print("  Base NPV $M:", [round(x, 3) for x in BASE])
    print("  Brazil normal acid +$50/t:", [round(x, 3) for x in BRAZIL_ACID_220])
    print("  Texas normal acid +$50/t:", [round(x, 3) for x in TEXAS_ACID_225])
    print("  Submitted Excel workbook on disk was not modified")


if __name__ == "__main__":
    main()
