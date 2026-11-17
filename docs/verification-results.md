# Verification record — Resouro final v1.0 submission

**Reference artifacts:** the actual 14-page report and six-sheet Excel workbook from the team's submitted `Final Deliverables.zip`. Both remain byte-for-byte unchanged in this portfolio package.

## Source reproduction (executed)

From the project root:

```bash
python tools/rebuild_and_verify.py
python -m unittest discover -s tests -v
```

**Result:** the original teammate `build_model.py`, `inputs.py`, `sources.py`, `style.py` and required `mrec_block.py` executed successfully in a temporary directory.

| Check | Observed |
|---|---|
| Workbook sheets | 6 / 6 match |
| Named inputs | 48 / 48 match |
| Excel formulas | 271 / 271 semantically match |
| Static/label cells | 895 compared, with numerical serialization tolerance |
| Submitted workbook SHA-256 after rebuilding | Unchanged |
| Portfolio unit tests | **11 / 11 passed** |

The rebuild is compared by cell structure and formulas, **not by XLSX binary hashes**: the original submission contains calculated Excel caches while `openpyxl` typically produces formulas without recalculating those values. Equivalent numerical spellings in source-generated versus Excel-saved formulas are normalized for comparison.

## Independent in-memory formula recalculation (executed)

The submitted workbook was imported into `artifact_tool`, recalculated in memory, and subjected to two isolated changes to the normal acid-price assumptions. No modified workbook was exported or substituted for the submission.

All values below are **pre-tax NPV in US$ millions**, with cases ordered Brazil / Texas acid processing / MREC Texas.

| Calculation | Brazil | Texas | MREC Texas |
|---|---:|---:|---:|
| Original normal-price baseline | +19.039 | −70.130 | −73.624 |
| Brazil acid price **$170 → $220/t** | +8.023 | −70.130 | −84.639 |
| Texas acid price **$175 → $225/t** | +19.039 | −81.145 | −73.624 |
| Original 2026-crisis-price baseline (unchanged in both shocks) | −38.240 | −119.698 | −130.903 |

This checks that normal-price acid-cost inputs affect the relevant case and do not accidentally alter the independently parameterized crisis scenario. Restoring the inputs returned the normal baseline values.

Optional check (requires a separate `artifact_tool` installation, not needed by the original project):

```bash
python tools/check_dynamic_scenarios.py
```

The standard `requirements.txt` includes only the teammate generator's original `openpyxl` dependency, so readers can run the primary build-and-verify suite without this optional calculation engine.

## What these checks do not establish

- A chemically closed mass balance, verified recovery assumptions, or achieved titanium product quality.
- Vendor-confirmed reagent, utility, waste or freight cost estimates.
- Funding, commercial offtake, environmental permits or project bankability.
- Full independent verification of the published source report or business case.

These are **software and artifact-reproducibility checks** for the team's conceptual screening tool. All original technical assumptions and their confidence labels are preserved on the `Inputs` tab.
