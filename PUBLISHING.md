# Publish this portfolio project

Before making it public, confirm the team is comfortable sharing the original source files and that no competition or sponsor restriction applies. No open-source license has been added without the authors' agreement.

Create a **new empty public repository** named `resouro-tiros-brownsville` on GitHub; do not initialize a README. Extract this ZIP, open Terminal in the extracted folder, and run:

```bash
python -m pip install -r requirements.txt
python tools/rebuild_and_verify.py
python -m unittest discover -s tests -v
git init -b main
git add .
git commit -m "Publish final Resouro Tiros–Brownsville competition portfolio"
git remote add origin https://github.com/Dold18/resouro-tiros-brownsville.git
git push -u origin main
```

This is a separate portfolio repository; it does **not** merge or modify `Dold18/tiros-brownsville` or the teammate's original source repo. The primary submitted report and model are unchanged. The original model generator is preserved under `model/build/`, including its required `mrec_block.py` dependency. Use `tools/rebuild_and_verify.py` to rebuild safely in a temporary directory without changing the final workbook. The optional dynamic-recalculation utility requires `artifact_tool` and is not needed for publishing.
