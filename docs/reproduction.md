# Reproduction and model limits

## Origin and preservation

The final workbook in `model/Tiros_Brownsville_Model.xlsx` is the unmodified file in `Final Deliverables.zip`. The generator in `model/build/build_model.py` is the teammate's original **v1.0 (final) — 7 Nov 2026** source. The teammate ZIP contains a slightly different XLSX binary; XML-level comparison of the two files found identical worksheet names, 48 defined input names and their definitions, and all formulas/static content, apart from floating-point representational differences in stored values. The final archive XLSX is used without alteration.

## Running the generator — safe workflow

The original teammate source is preserved with the required `model/build/mrec_block.py` module. **Do not run** `python model/build/build_model.py` directly in the published folder unless you intend to overwrite the local copy of the submitted workbook.

```bash
python -m pip install -r requirements.txt
python tools/rebuild_and_verify.py
python -m unittest discover -s tests -v
```

The wrapper copies the original v1.0 source to a temporary directory, builds with `openpyxl`, and compares worksheet names, named inputs, formulas and static cells. The submitted workbook's SHA-256 remains unchanged. To export a separate generated workbook:

```bash
python tools/rebuild_and_verify.py --output rebuilt-v1.0.xlsx
```

`openpyxl` writes Excel formulas but does not evaluate formula caches. A bytewise XLSX comparison is inappropriate because caches, serialized numeric notation and metadata can vary. See [software architecture](software-architecture.md) and [verification results](verification-results.md) for the structural and optional in-memory calculation checks.

## Building the LaTeX report

The original report's LaTeX source and chart/flowsheet sources are preserved in `report/`:

```bash
cd report
latexmk -pdf tiros_brownsville_report.tex
```

LaTeX tooling and packages must be installed to rebuild. The distributed PDF is the unmodified final submission. The PDF includes typeset numerical statements which may not update automatically if the model inputs change. The optional `report/figures/gen_fig.py` rebuilds the results figure from the recalculated XLSX; `fig_pfd.tex` also includes team-authored stream values.

## Model limitations

This is a **conceptual pre-tax screening model**, not a measured closed mass/element balance or design warrant. Original source assumptions and testing needs are labeled on the `Inputs` tab. Ore grade, titanium product identity and pricing basis, chemical demand and recycle, recovery, logistics, regulatory classification and pilot performance remain subject to testing and commercial verification. Screened model values are not a claim of investment or site feasibility.

## Testing

```bash
python -m unittest discover -s tests -v
```

The portfolio suite includes **11 passing tests** checking unchanged submitted artifacts, source dependencies, formula references and safe reproducibility. They do not verify every chemical, commercial or environmental assumption. The broader original teammate source archive had 142 unit tests for supplemental research models, which were exercised during portfolio preparation; those experimental modules are intentionally omitted from this focused submission-centered repository.
