"""Writes report/figures/fig_results.tex from the recalculated model."""
import sys, openpyxl
xlsx, out = sys.argv[1], sys.argv[2]
wb = openpyxl.load_workbook(xlsx, data_only=True)
m = wb['Model']; mx = wb['MREC Texas']
rows = {m[f'B{r}'].value: r for r in range(1, 90) if m[f'B{r}'].value}
npv = [m[f'{c}{rows["Net present value at normal prices"]}'].value for c in 'DEF']
npv26 = [m[f'{c}{rows["Net present value at 2026 crisis prices"]}'].value for c in 'DEF']
scale = []  # (t/month, case1, case2, case3) from Model section F
for r in range(1, 200):
    if m[f'B{r}'].value == "Net present value at this ore rate (normal prices)":
        scale.append((m[f'C{r}'].value, *[m[f'{c}{r}'].value for c in 'DEF']))
names = r"Case 1\\Brazil,Case 2\\Texas,Case 3\\MREC processing\\Texas"
co = lambda v: " ".join(f"({i},{x:.1f})" for i, x in enumerate(v))
tex = open(out + ".in").read()
tex = tex.replace("@NAMES@", names).replace("@NPV@", co(npv)).replace("@NPV26@", co(npv26))
for k in range(3):  # ore-rate series (used only if the template asks for them)
    tex = tex.replace(f"@SC{k+1}@", " ".join(f"({row[0]},{row[k+1]:.1f})" for row in scale))
open(out, "w").write(tex)
print(npv, npv26)
