"""Builds model/Tiros_Brownsville_Model.xlsx.

Run from the repo root:  python model/build/build_model.py
Then recalculate (LibreOffice) so cached values exist for viewers that don't calculate.
"""
import os
import sys

from openpyxl import Workbook
from openpyxl.chart import BarChart, LineChart, Reference
from openpyxl.chart.label import DataLabelList
from openpyxl.workbook.defined_name import DefinedName
from openpyxl.worksheet.datavalidation import DataValidation

sys.path.insert(0, os.path.dirname(__file__))
import style as S  # noqa: E402
from inputs import INPUTS  # noqa: E402
from sources import SOURCES  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT = os.path.join(ROOT, "model", "Tiros_Brownsville_Model.xlsx")
VERSION = "v1.0 (final) · 7 Nov 2026"

wb = Workbook()


# ---------------------------------------------------------------- helpers
def sheet(title, widths):
    ws = wb.create_sheet(title)
    ws.sheet_view.showGridLines = False
    for col, w in widths.items():
        ws.column_dimensions[col].width = w
    return ws


def put(ws, ref, value, font=S.BODY, fmt=None, align=None, fill=None, border=None):
    c = ws[ref]
    c.value = value
    c.font = font
    if fmt:
        c.number_format = fmt
    if align:
        c.alignment = align
    if fill:
        c.fill = fill
    if border:
        c.border = border
    return c


def title_block(ws, title, subtitle):
    ws.row_dimensions[1].height = 8
    put(ws, "B2", title, S.TITLE)
    ws.row_dimensions[2].height = 26
    put(ws, "B3", subtitle, S.SUBTITLE)
    return 5


def name(ws, nm, ref):
    wb.defined_names[nm] = DefinedName(nm, attr_text=f"'{ws.title}'!{ref}")


def height(text, chars=150, base=12.5):
    return max(15, base * (1 + len(text) // chars))


# ---------------------------------------------------------------- sheets (order = tab order)
wb.remove(wb.active)
readme = sheet("Read Me", {"A": 2, "B": 28, "C": 100})
summary = sheet("Summary", {"A": 2, "B": 46, "C": 12, "D": 19, "E": 19, "F": 19, "G": 3, "H": 60})
inp = sheet("Inputs", {"A": 2, "B": 52, "C": 14, "D": 16, "E": 13, "F": 30, "G": 100})
mdl = sheet("Model", {"A": 2, "B": 50, "C": 12, "D": 17, "E": 17, "F": 17, "G": 3, "H": 100})
mx_ws = sheet("MREC Texas", {"A": 2, "B": 48, "C": 12, "D": 19, "E": 19, "F": 17, "G": 3, "H": 100})
src = sheet("Sources", {"A": 2, "B": 40, "C": 110})

# ================================================================= INPUTS
r = title_block(inp, "Inputs",
                "Every number the model uses: 48 in all. Change the sand-colored cells. The label says how far to trust each one.")
for i, h in enumerate(["Input", "Value", "Unit", "Label", "Source", "Why this value"]):
    put(inp, f"{'BCDEFG'[i]}{r}", h, S.HEAD, border=S.B_HEAD, align=S.RIGHT if h == "Value" else S.LEFT)
inp.freeze_panes = f"A{r + 1}"
r += 1
for item in INPUTS:
    if len(item) == 1:
        r += 1
        for col in "BCDEFG":
            inp[f"{col}{r}"].fill = S.FILL_BAND
        put(inp, f"B{r}", item[0], S.H1, fill=S.FILL_BAND)
        r += 1
        continue
    nm, label, value, unit, status, source, why = item
    is_formula = isinstance(value, str) and value.startswith("=")
    put(inp, f"B{r}", label, S.BODY, border=S.B_ROW, align=S.LEFT_WRAP)
    c = put(inp, f"C{r}", value, S.BODY, align=S.RIGHT, border=S.B_ROW if is_formula else S.B_INPUT,
            fill=None if is_formula else S.FILL_INPUT)
    if unit.startswith("fraction"):
        c.number_format = S.PCT1
    elif unit.startswith("$") and "M" in unit:
        c.number_format = S.USD1
    elif unit.startswith("$"):
        c.number_format = S.USD2 if (is_formula or value < 100) else S.USD0
    elif "t per t" in unit:
        c.number_format = '0.0000'
    elif unit == "×":
        c.number_format = '0.00"×"'
    elif nm in ("Disc",):
        c.number_format = S.PCT0
    elif nm in ("Scale_exp",):
        c.number_format = '0.00'
    else:
        c.number_format = S.NUM0
    if nm == "Head_TREO":
        c.number_format = '0.000%'
    put(inp, f"D{r}", unit, S.NOTE, border=S.B_ROW, align=S.LEFT)
    put(inp, f"E{r}", status, S.f(9, True, S.STATUS[status]), border=S.B_ROW, align=S.LEFT)
    put(inp, f"F{r}", source, S.NOTE, border=S.B_ROW, align=S.LEFT_WRAP)
    put(inp, f"G{r}", why, S.NOTE, border=S.B_ROW, align=S.LEFT_WRAP)
    inp.row_dimensions[r].height = max(height(why, 135), height(label, 55))
    name(inp, nm, f"$C${r}")
    r += 1

# ================================================================= MREC TEXAS (built first: Case 3 reads it)
exec(open(os.path.join(os.path.dirname(__file__), "mrec_block.py"), encoding="utf-8").read())
MX = "'MREC Texas'!"
HUBC = "$D$"  # the Tiros-carbonate column on the MREC Texas tab

# ================================================================= MODEL
SCEN = [
    # key, title, tag, shipped, separate in Texas, staff BR, staff TX
    ("1", "Brazil", "Everything at Tiros; carbonate sold (the PEA layout)", "Nothing", "No", 60, 0),
    ("2", "Texas", "Fines roasted at Tiros, dry calcine shipped; acid steps in Brownsville", "Dry calcine", "No", 44, 34),
    ("3", "MREC processing Texas", "As Case 1, then Tiros carbonate is separated in Brownsville", "Nothing", "Yes", 60, 0),
]
COLS = ["D", "E", "F"]
NOTE = "H"

r = title_block(mdl, "Model",
                "Three cases for Tiros and Brownsville: Brazil, Texas, and MREC processing Texas. Read down a column. "
                "Change the sand cells at the top; the right-hand column says how each line is worked out.")
put(mdl, "B5", "", S.HEAD, border=S.B_HEAD)
put(mdl, "C5", "Unit", S.HEAD, border=S.B_HEAD)
for i, sc in enumerate(SCEN):
    put(mdl, f"{COLS[i]}5", f"Case {sc[0]}", S.HEAD, align=S.RIGHT, border=S.B_HEAD)
    put(mdl, f"{COLS[i]}6", sc[1], S.BODY_B, align=S.LEFT_WRAP)
    put(mdl, f"{COLS[i]}7", sc[2], S.NOTE, align=S.LEFT_WRAP)
put(mdl, f"{NOTE}5", "How it is worked out, and where the value comes from", S.HEAD, border=S.B_HEAD)
mdl.freeze_panes = "D8"
R = {}
row = [8]


def section(ws, label, cols="BCDEFGH"):
    row[0] += 1
    for col in cols:
        ws[f"{col}{row[0]}"].fill = S.FILL_BAND
    put(ws, f"B{row[0]}", label, S.H1, fill=S.FILL_BAND)
    row[0] += 1


def line(key, label, unit, tmpl, fmt=S.NUM0, note="", bold=False, total=False, values=None, dv=None):
    rr = row[0]
    R[key] = rr
    font = S.TOTAL if total else (S.BODY_B if bold else S.BODY)
    border = S.B_TOTAL if total else S.B_ROW
    put(mdl, f"B{rr}", label, font, border=border, align=S.LEFT)
    put(mdl, f"C{rr}", unit, S.NOTE, border=border, align=S.LEFT)
    for i, col in enumerate(COLS):
        if values is not None:
            put(mdl, f"{col}{rr}", values[i], S.BODY, fmt=fmt, align=S.RIGHT, fill=S.FILL_INPUT, border=S.B_INPUT)
            if dv is not None:
                dv.add(f"{col}{rr}")
        else:
            put(mdl, f"{col}{rr}", tmpl.format(c=col, **R), font, fmt=fmt, align=S.RIGHT, border=border)
    put(mdl, f"{NOTE}{rr}", note, S.NOTE, align=S.LEFT_WRAP, border=border)
    mdl.row_dimensions[rr].height = height(note, 135)
    row[0] += 1


dv_ship = DataValidation(type="list", formula1='"Nothing,Wet fines,Dry calcine"', allow_blank=False)
mdl.add_data_validation(dv_ship)
dv_sep = DataValidation(type="list", formula1='"No,Yes"', allow_blank=False)
mdl.add_data_validation(dv_sep)

section(mdl, "A.  Set-up  (change these)")
line("ship", "What is shipped from Brazil to Brownsville", "", None, fmt="@", values=[s[3] for s in SCEN], dv=dv_ship,
     note="Your choice. Nothing: everything at Tiros. Dry calcine (Case 2): the fines are roasted at Tiros and shipped "
          "dry; the acid bake onward is in Texas. Wet fines: an older variant of Case 2 in which the fines leave before "
          "their kiln; it ships 30% more tonnes and needs a dryer (set Tiros staff 40, Brownsville 38). The mine and the "
          "coarse circuit always stay at Tiros.")
line("sep", "Separate the carbonate in Brownsville", "", None, fmt="@", values=[s[4] for s in SCEN], dv=dv_sep,
     note="Yes in Case 3: Tiros's carbonate (MREC) is shipped to a separation plant in Brownsville. Its numbers come "
          "from the MREC Texas tab.")
line("stBR", "Staff at Tiros", "people", None, values=[s[5] for s in SCEN],
     note="Assumption. The PEA plant (8× larger) has 116 people (p.346); a small plant still needs 24-hour crews, so ~60. "
          "Fewer when the fines circuit moves to Texas.")
line("stTX", "Staff in Brownsville (acid steps)", "people", None, values=[s[6] for s in SCEN],
     note="Assumption. A second site needs its own crews, manager, lab and maintenance: ~78 people over two sites "
          "instead of 60 on one. The separation plant's staff are on the MREC Texas tab.")
line("fTX", "Where the acid steps run", "", '=IF({c}{ship}="Nothing",0,1)', fmt='"Texas";"";"Brazil"',
     note="Follows from what is shipped.")
line("fSep", "Where the carbonate is separated", "", '=IF({c}{sep}="Yes",1,0)', fmt='"Brownsville";"";"Sold unseparated"',
     note="Follows from the row above.")

section(mdl, "B.  Material flow")
line("rom", "Ore processed", "t/yr", "=ROM_tpm*12", note="Ore per month × 12 (Inputs: ROM_tpm, from the brief).")
line("ship_dry", "Case 2: calcine or fines shipped to Brownsville (dry)", "t/yr",
     '=IF({c}{ship}="Wet fines",{c}{rom}*Frac_fines,IF({c}{ship}="Dry calcine",{c}{rom}*Frac_calcine,0))',
     note="Ore × 60.0% for dry calcine or 71.1% for wet fines (BK19 test, PEA p.217).")
line("ship_wet", "Case 2: calcine or fines shipped to Brownsville (as shipped)", "t/yr",
     '=IF({c}{ship}="Wet fines",{c}{ship_dry}/(1-Moist_ship),{c}{ship_dry})', bold=True,
     note="Wet fines carry 10% water (Inputs: Moist_ship); calcine leaves the kiln dry. This is the tonnage that pays freight.")
line("p_coarse", "Coarse TiO2 product", "t/yr", "={c}{rom}*Y_coarse",
     note="Ore × 0.0848 t/t: the PEA's 42,390 t/yr at 500,000 t/yr (p.275). Always made at Tiros.")
line("p_fine", "Fine TiO2 product", "t/yr", "={c}{rom}*Y_fine",
     note="Ore × 0.0957 t/t: the PEA's 47,865 t/yr at 500,000 t/yr (p.275). Made where the acid steps run.")
line("treo", "Rare-earth oxide in the carbonate", "t/yr", "={c}{rom}*Head_TREO*Rec_TREO", fmt=S.NUM1,
     note="Ore × 1.085% rare-earth oxide (p.267) × 67% recovery (p.274).")
line("mrec", "Mixed rare-earth carbonate (MREC)", "t/yr", "={c}{treo}/MREC_grade", fmt=S.NUM1,
     note="Oxide ÷ 70.3% oxide content of the carbonate (from the PEA's economic model).")
line("mrec_sh", "Case 3: carbonate shipped to Brownsville", "t/yr", "={c}{fSep}*(1-{c}{fTX})*{c}{mrec}",
     fmt=S.NUM1, note="Case 3: the whole carbonate output. Zero if the acid steps are already in Texas.")
line("prod_TX", "Products made in Texas", "t/yr", "={c}{fTX}*({c}{p_fine}+{c}{mrec})",
     note="Fine TiO2 + carbonate, when the acid steps are in Texas.")
line("prod_BR", "Products made in Brazil", "t/yr", "={c}{p_coarse}+{c}{p_fine}+{c}{mrec}-{c}{prod_TX}",
     note="All products minus those made in Texas.")
line("waste_BR", "Solid waste left in Brazil", "t/yr", "={c}{rom}-{c}{ship_dry}-{c}{prod_BR}",
     note="Ore in − material shipped − products made in Brazil.")
line("waste_TX", "Solid waste left in Texas", "t/yr", "=MAX(0,{c}{ship_dry}-{c}{prod_TX})", bold=True,
     note="Material shipped − products made in Texas: mainly acid-leach residue (silica) and iron/aluminum cake.")

section(mdl, "C.  Running costs per year")
line("c_acid", "Sulfuric acid", "$/yr", "={c}{rom}*Acid_t*IF({c}{fTX}=1,P_acid_TX,P_acid_BR)", fmt=S.USD0,
     note="Ore × 0.374 t of 96% acid per t ore (PEA p.276) × normal-year delivered price where the acid steps run: $170 at Tiros, $175 at Brownsville. Crisis prices are in section E.")
line("c_naoh", "Caustic soda", "$/yr", "={c}{rom}*NaOH_t*IF({c}{fTX}=1,P_NaOH_TX,P_NaOH_BR)", fmt=S.USD0,
     note="Ore × 0.205 t per t ore (PEA p.341) × $560/t at Tiros or $520/t at Brownsville.")
line("c_hcl", "Hydrochloric acid (coarse circuit)", "$/yr", "={c}{rom}*HCl_t*P_HCl", fmt=S.USD0,
     note="Ore × 0.164 t per t ore × $200/t (PEA p.341). Always at Tiros.")
line("c_other", "Mining, power, maintenance, minor reagents", "$/yr", "={c}{rom}*Other_t", fmt=S.USD0,
     note="Ore × $27.50 per t ore, all PEA figures (Inputs: Other_t). The same in every case.")
line("c_lab", "Staff", "$/yr", "={c}{stBR}*Lab_BR+{c}{stTX}*Lab_TX", fmt=S.USD0,
     note="Tiros staff × $20,690 (PEA p.346) + Brownsville staff × $95,000.")
line("c_ga", "Site overheads", "$/yr", "=(1+{c}{fTX})*GA_site*1000000", fmt=S.USD0,
     note="$1.0M per site: one site, or two if Brownsville is used.")
line("c_waste", "Waste disposal", "$/yr", "={c}{waste_BR}*Tail_BR+{c}{waste_TX}*Tail_TX", fmt=S.USD0,
     note="Brazil waste × $3/t dry stack (PEA p.344) + Texas waste × $45/t landfill.")
line("c_ship", "Case 2: shipping calcine (bulk, ~36,000 t/yr)", "$/yr",
     '={c}{ship_wet}*Ship_cost+IF({c}{ship}="Wet fines",{c}{ship_dry}*Dry_cost,0)', fmt=S.USD0,
     note="Case 2 ships a large bulk tonnage of roasted ore to be processed in Brownsville: tonnes × $85/t from Tiros "
          "to the Brownsville plant (truck, port, bulk ship, unloading). Plus $13/t to dry wet fines, if chosen.")
line("c_plog", "Getting products to market", "$/yr", "={c}{prod_BR}*Truck_BR", fmt=S.USD0,
     note="Brazil products × $53/t to Santos (PEA p.348). Brownsville products are sold at its port.")
line("c_msh", "Case 3: shipping carbonate (containers, ~620 t/yr)", "$/yr", "={c}{mrec_sh}*MREC_ship", fmt=S.USD0,
     note="Case 3 ships only the finished product, a small tonnage, in bags in containers: tonnes × $185/t from the "
          "Brazilian port (the truck to the port is already in 'Getting products to market').")
line("c_sep", "Separation plant in Brownsville", "$/yr", "={c}{fSep}*" + MX + HUBC + str(MX_ROWS["run"]), fmt=S.USD0,
     note="Case 3: $10/kg of oxide separated + 45 staff + overheads (MREC Texas tab).")
line("opex", "Total running cost", "$/yr", "=SUM({c}" + "{c_acid}" + ":{c}{c_sep})", fmt=S.USD0, total=True,
     note="Sum of the lines above.")

section(mdl, "D.  Revenue and margin per year")
line("rev_ti", "Titanium products", "$/yr", "={c}{p_coarse}*P_coarse+{c}{p_fine}*P_fine", fmt=S.USD0,
     note="Coarse TiO2 × $900 + fine TiO2 × $650 (PEA p.316). The same in every case.")
line("rev_re", "Rare earths", "$/yr",
     "={c}{treo}*1000*(P_TREO*Payab+{c}{fSep}*" + MX + "$E$" + str(MX_ROWS["x"]) + ")", fmt=S.USD0,
     note="Oxide (kg) × $57.40 × 70% as carbonate (PEA p.316). Case 3 adds the extra value of selling it separated, "
          "about $13/kg (MREC Texas tab, Part 1).")
line("rev", "Revenue", "$/yr", "={c}{rev_ti}+{c}{rev_re}", fmt=S.USD0, bold=True,
     note="Sum of the two lines above.")
line("roy", "Royalties", "$/yr", "=({c}{rev_ti}+{c}{treo}*1000*P_TREO*Payab)*Royalty", fmt=S.USD0,
     note="3% (PEA p.350) of the products' value as made in Brazil: titanium plus carbonate. Not charged on the extra "
          "value from separating.")
line("margin", "Operating margin", "$/yr", "={c}{rev}-{c}{roy}-{c}{opex}", fmt=S.USD0, total=True,
     note="Revenue − royalties − running cost.")

section(mdl, "E.  Building cost and value")
line("scale", "Size factor vs the PEA plant", "×", "=({c}{rom}/PEA_tpa)^Scale_exp", fmt='0.000',
     note="(Ore ÷ 500,000)^0.6, the six-tenths rule: a plant 1/8 the size costs about 0.29× as much.")
line("k_br", "Mine, site works and coarse circuit (Brazil)", "$M", "=Capex_PEA*(1-Sh_fines)*{c}{scale}", fmt=S.USD1,
     note="$191.2M (PEA p.332) × 55% × size factor. Always at Tiros.")
line("k_fines", "Acid (fines) circuit", "$M", "=Capex_PEA*Sh_fines*{c}{scale}*IF({c}{fTX}=1,US_factor,1)", fmt=S.USD1,
     note="$191.2M × 45% × size factor, × 1.15 if built in Texas.")
line("k_tx", "Extra for a Brownsville site", "$M", "={c}{fTX}*TX_site*{c}{scale}", fmt=S.USD1,
     note="$43M at PEA size × size factor (Inputs: TX_site). Case 2 only (the acid steps in Texas).")
line("k_sep", "Separation plant in Brownsville, after support", "$M",
     "={c}{fSep}*" + MX + HUBC + str(MX_ROWS["net_cap"]), fmt=S.USD1,
     note="Case 3: Aclara's $277M plant scaled to Tiros's 436 t/yr, less 25% government support (MREC Texas tab).")
line("capex", "Total build cost", "$M", "=SUM({c}" + "{k_br}" + ":{c}{k_sep})", fmt=S.USD1, total=True,
     note="Sum of the lines above.")
line("ann", "Value today of $1 a year for 20 years", "×", "=(1-(1+Disc)^(-Life))/Disc", fmt='0.00',
     note="At the PEA's 8% discount rate (p.347).")
line("npv", "Net present value at normal prices", "$M",
     "=-{c}{capex}+({c}{margin}-{c}{rom}*Sust_t)*{c}{ann}/1000000", fmt=S.USD1, total=True,
     note="−build cost + (margin − sustaining capital of $5.78/t ore, p.357) × 9.82. Before tax, because Brazil and the "
          "US tax differently.")
line("acid26", "Sulfuric acid at 2026 crisis prices", "$/yr", "={c}{rom}*Acid_t*IF({c}{fTX}=1,P_acid_TX_26,P_acid_BR_26)",
     fmt=S.USD0, note="The same acid at crisis prices: $430/t at Tiros, $400/t at Brownsville (Inputs section 4). "
     "Nothing else changes.")
line("npv26", "Net present value at 2026 crisis prices", "$M", "={c}{npv}-({c}{acid26}-{c}{c_acid})*{c}{ann}/1000000",
     fmt=S.USD1, total=True, note="Normal-price value − the extra acid cost each year × 9.82.")
line("rank", "Rank (1 = highest value, normal prices)", "", "=RANK({c}{npv},$D${npv}:$F${npv})", fmt="0", bold=True,
     note="Ranks the three cases. The order is the same at crisis prices.")
line("moved", "Tonnes shipped to Texas per tonne of acid used", "t/t",
     '=IF({c}{fTX}=0,"–",{c}{ship_wet}/({c}{rom}*Acid_t))', fmt='0.00',
     note="Tonnes shipped ÷ tonnes of acid. Compare with 0.32 t of sulfur that Brazil would import to make the same acid.")

section(mdl, "F.  What if Tiros sends more ore?  (change the ore rates in column C)")
line("fixed", "Running costs that do not grow with ore", "$/yr",
     "={c}{c_lab}+{c}{c_ga}+{c}{fSep}*" + MX + HUBC + str(MX_ROWS["fixed"]), fmt=S.USD0,
     note="Staff and site overheads (and, in Case 3, the separation plant's staff and overheads). Held fixed as ore "
          "grows, so larger sizes look slightly better than they are: the PEA has 116 staff at full size, not 60.")
line("vm", "Margin per tonne of ore, before fixed costs", "$/t ore", "=({c}{margin}+{c}{fixed})/{c}{rom}", fmt=S.USD2,
     note="Everything else (reagents, freight, waste, revenue, royalties) grows in step with the ore.")
SCALE = [5000, 7500, 10000, 15000, 20000, 30000, 41667]
SCALE_ROWS = []
for i_, t_ in enumerate(SCALE):
    rr_ = row[0]
    line(f"sc{i_}", "Net present value at this ore rate (normal prices)", "", 
         "=-{c}{capex}*($C" + str(rr_) + "*12/{c}{rom})^Scale_exp+({c}{vm}*$C" + str(rr_) + "*12-{c}{fixed}-$C" + str(rr_)
         + "*12*Sust_t)*{c}{ann}/1000000", fmt=S.USD1, bold=(t_ == 5000),
         note=("Build cost grows with the six-tenths rule; margin grows with ore, less the fixed costs. Reproduces the "
               "value above at the model's own ore rate.") if i_ == 0 else
              ("41,667 t/month is the PEA's full size (500,000 t/yr).") if t_ == 41667 else "")
    put(mdl, f"C{rr_}", t_, S.BODY_B, fmt='#,##0" t/mo"', align=S.RIGHT, fill=S.FILL_INPUT, border=S.B_INPUT)
    SCALE_ROWS.append(rr_)


# ================================================================= SUMMARY
r = title_block(summary, "Summary",
                f"Tiros–Brownsville: three cases for where the work happens, and what Brownsville should do.   {VERSION}")
put(summary, f"B{r}", "1.  The three cases", S.H1)
r += 1
put(summary, f"C{r}", "Unit", S.HEAD, border=S.B_HEAD)
put(summary, f"B{r}", "", S.HEAD, border=S.B_HEAD)
for i, sc in enumerate(SCEN):
    put(summary, f"{COLS[i]}{r}", f"Case {sc[0]}", S.HEAD, align=S.RIGHT, border=S.B_HEAD)
r += 1
NAMES_ROW = r
for i, sc in enumerate(SCEN):
    put(summary, f"{COLS[i]}{r}", f"=Model!{COLS[i]}6", S.BODY_B, align=S.RIGHT_WRAP)
summary.row_dimensions[r].height = 26
r += 1
srows = [
    ("Ore processed at Tiros", "t/yr", "rom", S.NUM0),
    ("Case 2: calcine shipped to Brownsville", "t/yr", "ship_wet", S.NUM0),
    ("Case 3: carbonate shipped to Brownsville", "t/yr", "mrec_sh", S.NUM0),
    ("Solid waste left in Texas", "t/yr", "waste_TX", S.NUM0),
    ("Revenue", "$M/yr", "rev", "M"),
    ("Running cost", "$M/yr", "opex", "M"),
    ("Operating margin", "$M/yr", "margin", "M"),
    ("Build cost", "$M", "capex", S.USD1),
    ("Net present value, normal prices", "$M", "npv", S.USD1),
    ("Net present value, 2026 crisis prices", "$M", "npv26", S.USD1),
    ("Rank", "", "rank", "0"),
]
for label, unit, key, fmt in srows:
    tot = key in ("npv", "npv26")
    put(summary, f"B{r}", label, S.TOTAL if tot else S.BODY, border=S.B_TOTAL if tot else S.B_ROW, align=S.LEFT)
    put(summary, f"C{r}", unit, S.NOTE, border=S.B_TOTAL if tot else S.B_ROW, align=S.LEFT)
    for col in COLS:
        v = f"=Model!{col}{R[key]}" + ("/1000000" if fmt == "M" else "")
        put(summary, f"{col}{r}", v, S.TOTAL if tot else S.BODY, fmt=S.USD1 if fmt == "M" else fmt, align=S.RIGHT,
            border=S.B_TOTAL if tot else S.B_ROW)
    if key == "npv":
        NPV_ROW = r
    r += 1
put(summary, f"B{r}", "Extra rare-earth price needed to match Case 1", S.BODY, border=S.B_ROW, align=S.LEFT)
put(summary, f"C{r}", "% on basket", S.NOTE, border=S.B_ROW, align=S.LEFT)
for col in COLS:
    put(summary, f"{col}{r}",
        f"=IF(Model!{col}{R['fTX']}=0,\"–\",MAX(0,(Model!$D${R['npv']}-Model!{col}{R['npv']})*1000000/"
        f"(Model!{col}{R['ann']}*Model!{col}{R['treo']}*1000*P_TREO*Payab*(1-Royalty))))",
        S.BODY_B, fmt=S.PCT0, align=S.RIGHT, border=S.B_ROW)
put(summary, f"H{r}", "Case 2 only: how much more buyers would have to pay for rare earths processed in the US before "
    "moving the acid steps to Texas is worth as much as keeping them in Brazil.", S.NOTE, align=S.LEFT_WRAP)
summary.row_dimensions[r].height = 26
r += 2
put(summary, f"B{r}", "Why Case 2 loses: tonnes crossing the ocean per tonne of acid used", S.BODY_B)
r += 1
for label, v, note in [
        ("Ship dry calcine to Texas (Case 2)", f"=Model!E{R['ship_wet']}/(Model!E{R['rom']}*Acid_t)", ""),
        ("Ship wet fines to Texas (older variant)", f"=Model!E{R['rom']}*Frac_fines/(1-Moist_ship)/(Model!E{R['rom']}*Acid_t)", ""),
        ("Ship acid to Brazil", "=1", ""),
        ("Ship sulfur to Brazil and make the acid there", "=0.96/3", "1 t of sulfur makes ~3 t of acid (chemistry); 96% acid.")]:
    put(summary, f"B{r}", label, S.BODY, border=S.B_ROW)
    put(summary, f"C{r}", "t per t acid", S.NOTE, border=S.B_ROW)
    put(summary, f"D{r}", v, S.BODY_B, fmt='0.00', align=S.RIGHT, border=S.B_ROW)
    put(summary, f"H{r}", note, S.NOTE)
    r += 1
r += 1

put(summary, f"B{r}", "2.  What if Tiros sends more ore?  (net present value, normal prices)", S.H1)
r += 1
put(summary, f"B{r}", "Ore from Tiros", S.HEAD, border=S.B_HEAD)
put(summary, f"C{r}", "t/month", S.HEAD, border=S.B_HEAD)
for i, sc in enumerate(SCEN):
    put(summary, f"{COLS[i]}{r}", f"Case {sc[0]}  ($M)", S.HEAD, align=S.RIGHT, border=S.B_HEAD)
SCALE_HEAD = r
r += 1
for rr_ in SCALE_ROWS:
    put(summary, f"B{r}", f"=IF(Model!C{rr_}=41667,\"PEA full size\",IF(Model!C{rr_}=5000,\"The brief's size\",\"\"))",
        S.NOTE, border=S.B_ROW, align=S.LEFT)
    put(summary, f"C{r}", f"=Model!C{rr_}", S.BODY, fmt='#,##0', border=S.B_ROW, align=S.LEFT)
    for col in COLS:
        put(summary, f"{col}{r}", f"=Model!{col}{rr_}", S.BODY, fmt=S.USD1, align=S.RIGHT, border=S.B_ROW)
    r += 1
SCALE_LAST = r - 1
put(summary, f"H{SCALE_HEAD + 1}", "More ore raises Case 1's value fast: fixed costs and build cost grow more slowly "
    "than output. Case 3 stays below Case 1 at every size: separating Tiros's light-rich carbonate never earns its "
    "plant back. Change the rates on the Model tab, section F.", S.NOTE, align=S.LEFT_WRAP)
summary.merge_cells(f"H{SCALE_HEAD + 1}:H{SCALE_HEAD + 4}")
r += 1

put(summary, f"B{r}", "3.  Case 3 in detail: separating Tiros carbonate (MREC Texas tab)", S.H1)
r += 1
for label, unit, key, fmt, tot in [
        ("Rare-earth oxide separated", "t/yr", "tiros", S.NUM0, False),
        ("Extra value per kg from separating", "$/kg", "pk_x", S.USD2, False),
        ("Running cost per kg separated", "$/kg", "pk_c", S.USD2, False),
        ("Build cost, after government support", "$M", "net_cap", S.USD1, False),
        ("Net present value of the plant (vs selling the carbonate)", "$M", "npv", S.USD1, True),
        ("Extra value per kg needed to break even", "$/kg", "pk_be", S.USD2, False)]:
    put(summary, f"B{r}", label, S.TOTAL if tot else S.BODY, border=S.B_TOTAL if tot else S.B_ROW, align=S.LEFT)
    put(summary, f"C{r}", unit, S.NOTE, border=S.B_TOTAL if tot else S.B_ROW, align=S.LEFT)
    put(summary, f"D{r}", f"={MX}D{MX_ROWS[key]}", S.TOTAL if tot else S.BODY, fmt=fmt, align=S.RIGHT,
        border=S.B_TOTAL if tot else S.B_ROW)
    r += 1
put(summary, f"H{r - 2}", "Case 3 = Case 1 + this line − shipping the carbonate to Brownsville.", S.NOTE, align=S.LEFT_WRAP)
r += 2

chart = BarChart()
chart.type = "bar"
chart.style = 2
chart.title = "Three cases: net present value before tax ($M)"
for rr_ in (NPV_ROW, NPV_ROW + 1):
    chart.add_data(Reference(summary, min_col=4, max_col=6, min_row=rr_, max_row=rr_), from_rows=True,
                   titles_from_data=False)
chart.set_categories(Reference(summary, min_col=4, max_col=6, min_row=NAMES_ROW, max_row=NAMES_ROW))
from openpyxl.chart.series import SeriesLabel
chart.legend.position = "b"
for s_, colr, nm_ in zip(chart.series, (S.ACCENT, S.MUTED), ("Normal prices", "2026 crisis prices")):
    s_.tx = SeriesLabel(v=nm_)
    s_.graphicalProperties.solidFill = colr
    s_.graphicalProperties.line.solidFill = colr
    s_.dLbls = DataLabelList()
    s_.dLbls.showVal = True
    for a in ("showSerName", "showCatName", "showLegendKey"):
        setattr(s_.dLbls, a, False)
    s_.dLbls.position = "outEnd"
    s_.dLbls.numFmt = '"$"#,##0;("$"#,##0)'
chart.x_axis.tickLblPos = "low"
chart.x_axis.delete = False
chart.y_axis.delete = False
chart.y_axis.majorGridlines = None
chart.y_axis.numFmt = '"$"#,##0'
chart.height = 6.5
chart.width = 18
summary.add_chart(chart, f"B{r}")
hub_chart = LineChart()
hub_chart.title = "Net present value as Tiros sends more ore ($M)"
for i_, col in enumerate(COLS):
    hub_chart.add_data(Reference(summary, min_col=4 + i_, max_col=4 + i_, min_row=SCALE_HEAD, max_row=SCALE_LAST),
                       titles_from_data=True)
hub_chart.set_categories(Reference(summary, min_col=3, min_row=SCALE_HEAD + 1, max_row=SCALE_LAST))
for s_, colr in zip(hub_chart.series, (S.ACCENT, "A33B2B", S.MUTED)):
    s_.graphicalProperties.line.solidFill = colr
    s_.graphicalProperties.line.width = 28000
    s_.smooth = False
hub_chart.x_axis.title = "Ore from Tiros (t/month)"
hub_chart.y_axis.numFmt = '"$"#,##0'
hub_chart.x_axis.tickLblPos = "low"
hub_chart.x_axis.delete = False
hub_chart.y_axis.delete = False
hub_chart.y_axis.majorGridlines = None
hub_chart.legend.position = "b"
hub_chart.height = 7
hub_chart.width = 18
summary.add_chart(hub_chart, f"B{r + 15}")

# ================================================================= READ ME
r = title_block(readme, "Tiros–Brownsville economic model", VERSION)
blocks = [
    ("What it answers",
     "Where should each part of the Tiros process happen, and what should Brownsville do? Three cases:\n"
     "1  Brazil: everything at Tiros, carbonate sold (the PEA layout).\n"
     "2  Texas: fines roasted at Tiros and shipped dry; the sulfuric-acid steps run in Brownsville.\n"
     "3  MREC processing Texas: as Case 1, then Tiros's mixed rare-earth carbonate (MREC) is separated in Brownsville.\n"
     "Built on the July 2026 NI 43-101 PEA for Tiros. Sized for the brief's 5,000 t/month of ore."),
    ("How to use it",
     "1. Read Summary for the answers.\n"
     "2. Change numbers on Inputs (sand cells only). Each has a source and a reason.\n"
     "3. Change the set-up rows at the top of Model, the ore rates in Model section F, and the staff on MREC Texas.\n"
     "Everything else is calculated."),
    ("Tabs",
     "Summary – the three cases on one page, with Case 3's separation plant in detail.\n"
     "Inputs – all 48 numbers, with source, trust label and why each value was chosen.\n"
     "Model – the three cases, one column each, and what each is worth if Tiros sends more ore (section F).\n"
     "MREC Texas – the Brownsville separation plant behind Case 3.\n"
     "Sources – references."),
    ("Trust labels",
     "Known – stated in the PEA, or a published fact.\n"
     "Assumption – our planning choice, usually from a researched range; the 'Why' column says which.\n"
     "Needs testing – depends on metallurgical testing not yet done."),
    ("Limits",
     "Order-of-magnitude only, like the PEA (±50%). Before tax. Only Tiros ore is considered. Earlier versions with "
     "more detail (a wet-fines case, an own-acid-plant option, a two-stage separation plant, a hub for other producers' "
     "carbonate) are in the GitHub history; the reasons for every cut are in docs/engineering-decisions.md."),
]
rr = r
for head, text in blocks:
    put(readme, f"B{rr}", head, S.H1, align=S.LEFT_WRAP)
    put(readme, f"C{rr}", text, S.BODY, align=S.LEFT_WRAP)
    readme.row_dimensions[rr].height = max(16, 13.5 * sum(1 + len(t) // 140 for t in text.split("\n")))
    rr += 2
put(readme, f"B{rr}", "Color key", S.H1)
put(readme, f"C{rr}", "Sand cell = an input you can change", S.BODY, fill=S.FILL_INPUT, border=S.B_INPUT)
rr += 1
for st, col in S.STATUS.items():
    put(readme, f"C{rr}", st, S.f(10, True, col))
    rr += 1

# ================================================================= SOURCES
r = title_block(src, "Sources", "Where the numbers come from.")
put(src, f"B{r}", "Source", S.HEAD, border=S.B_HEAD)
put(src, f"C{r}", "Detail / link", S.HEAD, border=S.B_HEAD)
r += 1
for a, b in SOURCES:
    put(src, f"B{r}", a, S.BODY, border=S.B_ROW, align=S.LEFT_WRAP)
    c = put(src, f"C{r}", b, S.NOTE, border=S.B_ROW, align=S.LEFT_WRAP)
    if b.startswith("http"):
        c.hyperlink = b
        c.font = S.f(9, False, S.ACCENT)
    r += 1

# ---------------------------------------------------------------- print setup
for ws in wb.worksheets:
    ws.page_setup.orientation = "landscape"
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0
    ws.sheet_properties.pageSetUpPr.fitToPage = True
wb.active = 1
os.makedirs(os.path.dirname(OUT), exist_ok=True)
wb.save(OUT)
print("saved", OUT)
