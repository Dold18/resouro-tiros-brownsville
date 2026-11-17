# File provenance and submission boundary

## The exact two submitted files

The authoritative user-provided archive was `Final Deliverables.zip` (7–8 November 2026). The public-repo working copy preserves the two files byte for byte:

| Repo file | SHA-256 | Source |
|---|---|---|
| `report/tiros_brownsville_report.pdf` | `7a51b44d6439d6bb4f8f13414a74d9182bfbcafd709151663167b4b02c6dfc2a` | Final Deliverables ZIP |
| `model/Tiros_Brownsville_Model.xlsx` | `aa6aa7cc745665109e5d11ed9378343f1c70c8aac99ba92c3ac748dd3a9ba98b` | Final Deliverables ZIP |

## Preserved teammate source

The model's `model/build/*.py` files (including the original `mrec_block.py` executed by the generator), original `report/tiros_brownsville_report.tex`, and vector figure sources come from the supplied `tiros-brownsville-main (3).zip` teammate repository snapshot. The final report PDF in that snapshot has the *same SHA-256 hash* as the actual submitted PDF.

The teammate ZIP's v1.0 workbook has a different SHA-256 from the final submission, but the same worksheet definitions and formulas. Only the final submitted workbook is published in `model/`.

The supporting research notes from the source repo are retained in `docs/` and **were not part of the two-file final submission archive**. The previously developed alternative hypothetical model suite and the separate environmental award statement are **not represented as final-deliverable files** in this release.

## Portfolio additions

- `README.md`, `docs/reproduction.md`, `docs/software-architecture.md`, `docs/verification-results.md`, `docs/README.md`, `.gitignore`, `requirements.txt`, `PUBLISHING.md`, and this provenance record.
- `figures/process-flowsheet.png` and `figures/results-comparison.png` are raster previews from the original team-authored PDF figures. `figures/model-summary.png` is a screenshot-style rendering directly from the exact submitted Excel workbook (not a new dashboard).
- `tests/test_submission_consistency.py` and `tests/test_regenerated_model.py` provide post-submission integrity and safe reproducibility tests. `tools/rebuild_and_verify.py` executes the original generator in a temporary working directory; `tools/check_dynamic_scenarios.py` is an optional post-submission in-memory formula-recalculation QA script.

## Team credit and publication

Jacob Dold · Lukas Hirschmann · Mathias Bauer. Attribution follows the submitted report, without assigning individual technical work to specific members. Review collaborator permissions and contest disclosure requirements before making the source material publicly available. No external-use license is granted by default.
