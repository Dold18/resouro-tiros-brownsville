# ================================================================= MREC TEXAS (Case 3)
# Executed inside build_model.py before the Model tab (shares its helpers: put, title_block, height, S, mx_ws).
# v0.8: Tiros carbonate only. The hub (other producers' feed and toll fees) was removed (decision D27).

PRICE_FMT = '[<10]"$"0.00;"$"#,##0'
PK = '"$"#,##0.00;("$"#,##0.00);"–"'
ws = mx_ws
RR = {}
r = title_block(ws, "MREC Texas",
                "Case 3: separate Tiros's own mixed rare-earth carbonate (MREC) in Brownsville instead of selling it. "
                "An order-of-magnitude estimate. Sand cells can be changed.")


def band(rr, label):
    for col in "BCDEFGH":
        ws[f"{col}{rr}"].fill = S.FILL_BAND
    put(ws, f"B{rr}", label, S.H1, fill=S.FILL_BAND)


def rl(key, rr, label, unit, cells, fmt, note="", bold=False, total=False, inp_=False):
    RR[key] = rr
    font = S.TOTAL if total else (S.BODY_B if bold else S.BODY)
    border = S.B_TOTAL if total else S.B_ROW
    put(ws, f"B{rr}", label, font, border=border, align=S.LEFT_WRAP)
    put(ws, f"C{rr}", unit, S.NOTE, border=border, align=S.LEFT)
    for col, v in cells:
        put(ws, f"{col}{rr}", v, font, fmt=fmt, align=S.RIGHT,
            fill=S.FILL_INPUT if inp_ else None, border=S.B_INPUT if inp_ else border)
    put(ws, f"H{rr}", note, S.NOTE, align=S.LEFT_WRAP, border=border)
    ws.row_dimensions[rr].height = max(height(note, 135), height(label, 52))


# ---------------- Read this first
band(r, "Read this first")
r += 1
LOOK = [
    "1.  Compare 'Extra value per kg of Tiros oxide' with 'Running cost per kg separated' in Part 2. Tiros's rare earths "
    "are mostly light (lanthanum, cerium, NdPr), so separating them earns little more than selling the mixed carbonate.",
    "2.  At 5,000 t/month of ore the plant loses money. More ore helps but does not close the gap: see 'What if Tiros "
    "sends more ore?' at the bottom of the Model tab, where Case 3 = Case 1 + this plant.",
    "3.  What would change it: much higher prices for separated oxides, a far cheaper plant, or a separator's toll offer "
    "for Tiros carbonate. The last line of Part 2 gives the extra value per kg needed to break even.",
]
for t in LOOK:
    put(ws, f"B{r}", t, S.BODY, align=S.LEFT_WRAP)
    ws.merge_cells(f"B{r}:H{r}")
    ws.row_dimensions[r].height = 27
    r += 1
r += 1

# ---------------- Part 1: value of one kg
band(r, "Part 1   What one kilogram of Tiros rare-earth oxide is worth")
r += 1
for col, h in [("B", "Rare earths (as oxides)"), ("C", "Group"), ("D", "Share of the oxide"),
               ("E", "Price: PEA long-term"), ("F", "Price: outside China, Oct 2026"),
               ("H", "Where the numbers come from")]:
    put(ws, f"{col}{r}", h, S.HEAD, border=S.B_HEAD, align=S.RIGHT_WRAP if col in "DEF" else S.LEFT_WRAP)
ws.row_dimensions[r].height = 26
r += 1
ELEM = [
    ("NdPr", "Neodymium + praseodymium (NdPr)", "Light", 0.266, 157, 115,
     "Share: the resource's magnet oxides are 27% of the total (PEA p.44), less Dy and Tb; sample BK19 gives 24% "
     "(p.197–199). Prices: PEA $157 (p.348); outside China $95–140 (Benchmark Aug, REEx Oct 2026), midpoint $115."),
    ("Dy", "Dysprosium", "Heavy", 0.003, 1640, 3000,
     "Share: set with Tb so NdPr + Dy + Tb carry the PEA's own magnet value, 84% of $57.40 (p.348). Prices: PEA $1,640; "
     "outside China $3,250–3,500 (S&P, Benchmark, Sep 2026), rounded down."),
    ("Tb", "Terbium", "Heavy", 0.0006, 3609, 7000,
     "Share: as for Dy. Prices: PEA $3,609; outside China $6,745–7,500 (Benchmark, S&P, Sep 2026)."),
    ("OH", "Other heavy: samarium, europium, gadolinium, yttrium, holmium to lutetium", "Heavy", 0.0654, 24.6, 24.6,
     "Share: BK09 has ~4% heavy rare earths (p.192) plus ~2.5% samarium. Price: weighted China prices (SMM Apr, REEx Oct "
     "2026). Outside-China quotes are 10–100× higher but from a handful of trades, so not credited."),
    ("LaCe", "Lanthanum + cerium", "Light", "=1-SUM(D{a}:D{b})", 1.59, 1.59,
     "Share: the rest, so the shares add to 100% (BK19: La 21%, Ce 41%). Price: China, lanthanum $0.75 and cerium "
     "$2.00 (SMM, Apr 2026); no deep market outside China."),
]
first = r
for i, (k, label, grp, share, p1, p2, note) in enumerate(ELEM):
    rr = r + i
    RR[k] = rr
    is_f = isinstance(share, str)
    put(ws, f"B{rr}", label, S.BODY, border=S.B_ROW, align=S.LEFT_WRAP)
    put(ws, f"C{rr}", grp, S.NOTE, border=S.B_ROW, align=S.LEFT)
    put(ws, f"D{rr}", share.format(a=first, b=rr - 1) if is_f else share, S.BODY, fmt='0.00%', align=S.RIGHT,
        fill=None if is_f else S.FILL_INPUT, border=S.B_ROW if is_f else S.B_INPUT)
    for col, p_ in (("E", p1), ("F", p2)):
        put(ws, f"{col}{rr}", p_, S.BODY, fmt=PRICE_FMT, align=S.RIGHT, fill=S.FILL_INPUT, border=S.B_INPUT)
    put(ws, f"H{rr}", note, S.NOTE, align=S.LEFT_WRAP, border=S.B_ROW)
    ws.row_dimensions[rr].height = max(height(note, 135), height(label, 52))
last = r + len(ELEM) - 1
r = last + 2
PC = ["E", "F"]
D_ = f"$D${first}:$D${last}"


def pc(key, label, tmpl, note="", bold=False, total=False):
    global r
    rl(key, r, label, "$/kg", [(c, tmpl.format(c=c, **RR)) for c in PC], PK, note, bold, total)
    r += 1


pc("basket", "All the rare earths, at full price (the basket)", "=SUMPRODUCT(" + D_ + ",{c}" + f"{first}:{{c}}{last})",
   "Share × price, added up. The PEA's basket is $57.40 (p.316). Ours is lower because the PEA does not say how it values "
   "the 16% of its basket that is not NdPr, Dy or Tb; at market prices those are worth only ~$2.70/kg.", bold=True)
pc("carb", "Paid for it as mixed carbonate (Cases 1 and 2)", "={c}{basket}*Payab",
   "Basket × 70% (PEA p.316). Buyers of a mixed carbonate keep ~30% to pay for separating it.")
pc("sep", "Paid for it as separated oxides (Case 3)", "=Rec_sep*{c}{basket}",
   "95% recovery × every rare earth sold separated, at full price.")
pc("x", "Extra value per kg of Tiros oxide from separating", "={c}{sep}-{c}{carb}",
   "Separated − carbonate. The Model tab adds this to Case 3's rare-earth revenue (PEA prices).", total=True)
r += 1

# ---------------- Part 2: the plant for Tiros carbonate
band(r, "Part 2   A separation plant in Brownsville for Tiros carbonate")
r += 1
KC = ["D"]
RR["title"] = r
put(ws, f"B{r}", "", S.HEAD, border=S.B_HEAD)
put(ws, f"C{r}", "Unit", S.HEAD, border=S.B_HEAD)
put(ws, f"D{r}", "Tiros carbonate", S.HEAD, align=S.RIGHT_WRAP, border=S.B_HEAD)
put(ws, f"H{r}", "How it is worked out", S.HEAD, border=S.B_HEAD)
ws.row_dimensions[r].height = 26
r += 1


def kl(key, label, unit, tmpl, fmt, note="", bold=False, total=False, values=None):
    global r
    if values is not None:
        rl(key, r, label, unit, list(zip(KC, values)), fmt, note, bold, total, inp_=True)
    else:
        rl(key, r, label, unit, [(c, tmpl.format(c=c, **RR)) for c in KC], fmt, note, bold, total)
    r += 1


kl("staff", "Staff at the plant", "people", None, S.NUM0,
   "Assumption. A 24-hour plant needs four or five shift crews plus lab, maintenance and management, and full "
   "separation has many circuits. ~45 for the smallest plant. Held fixed when the Model tab scales up the ore, so "
   "larger sizes look slightly better than they are.", values=[45])
kl("tiros", "Tiros rare-earth oxide separated", "t/yr", "=ROM_tpm*12*Head_TREO*Rec_TREO", S.NUM0,
   "Ore × 1.085% × 67% recovery (Inputs). 436 t/yr at 5,000 t/month; 3,636 t/yr at the PEA's full size.", bold=True)
kl("extra", "Extra value from separating", "$/yr", "={c}{tiros}*1000*$E${x}", S.USD0,
   "Oxide (kg) × extra per kg at PEA prices (Part 1).")
kl("run", "Running cost", "$/yr", "={c}{tiros}*1000*Sep_var+{c}{staff}*Lab_TX+GA_site*1000000", S.USD0,
   "Oxide (kg) × $10/kg for reagents, power and wastewater + staff × $95,000 + $1.0M site overheads.")
kl("fixed", "of which fixed (staff and overheads)", "$/yr", "={c}{staff}*Lab_TX+GA_site*1000000", S.USD0,
   "Does not grow with ore. Used by the Model tab's scaling table.")
kl("margin", "Margin from the plant", "$/yr", "={c}{extra}-{c}{run}", S.USD0,
   "Extra value − running cost.", total=True)
kl("cap", "Build cost", "$M", "=Sep_capex_ref*({c}{tiros}/Sep_tpa_ref)^Scale_exp", S.USD1,
   "Aclara's $277M for 4,378 t/yr (Louisiana), scaled with the six-tenths rule.")
kl("sup", "Government support", "$M", "=-{c}{cap}*Support", S.USD1,
   "Build cost × 25%: grants (Aclara 17%, Ucore 38%) plus the 45X tax credit (Inputs: Support).")
kl("net_cap", "Build cost after support", "$M", "={c}{cap}+{c}{sup}", S.USD1, "Build cost − support.", bold=True)
kl("ann", "Value today of $1 a year for 20 years", "×", "=(1-(1+Disc)^(-Life))/Disc", '0.00', "8% over 20 years.")
kl("npv", "Net present value at PEA prices", "$M", "=-{c}{net_cap}+{c}{margin}*{c}{ann}/1000000", S.USD1,
   "−build cost after support + margin × 9.82. Before tax; measured against selling the carbonate unseparated "
   "(Case 1). Case 3 = Case 1 + this line − shipping the carbonate.", total=True)
kl("npv_out", "Net present value at outside-China prices", "$M",
   "={c}{npv}+{c}{tiros}*1000*($F${x}-$E${x})*{c}{ann}/1000000", S.USD1,
   "The same, with Tiros's products valued at outside-China prices (Part 1, right-hand column).")
kl("pk_x", "Extra value per kg of Tiros oxide", "$/kg", "={c}{extra}/({c}{tiros}*1000)", PK, "From Part 1 (PEA prices).")
kl("pk_c", "Running cost per kg separated", "$/kg", "={c}{run}/({c}{tiros}*1000)", PK,
   "Compare with the line above. Aclara: $12.6/kg at 4,378 t/yr, ten times Tiros's size.")
kl("pk_be", "Extra value per kg needed to break even", "$/kg",
   "=({c}{net_cap}*1000000/{c}{ann}+{c}{run})/({c}{tiros}*1000)", PK,
   "Running cost plus repaying the build cost, per kg. Compare with the extra value actually earned.", bold=True)
r += 1

# ---------------- Part 3: later modules
band(r, "Part 3   Later modules (described, not costed)")
r += 1
for head_, text in [
    ("Metal and magnets",
     "Turn NdPr oxide into metal and magnets with partners. Texas is the US magnet centre: MP Materials in Fort Worth "
     "(~1,000 t/yr, growing to 3,000; a 10,000 t/yr plant planned at Northlake for 2028) and Noveon in San Marcos "
     "(~2,000 t/yr)."),
    ("Titanium tetrachloride (TiCl4) and titanium sponge",
     "Needs ~85–95% TiO2 feed with low silica. The PEA says Tiros's coarse product must be upgraded first (p.315). "
     "A later module, after upgrading tests."),
]:
    put(ws, f"B{r}", head_, S.BODY_B, align=S.LEFT_WRAP)
    put(ws, f"D{r}", text, S.NOTE, align=S.LEFT_WRAP)
    ws.merge_cells(f"D{r}:H{r}")
    ws.row_dimensions[r].height = 30
    r += 1
MX_ROWS = RR
