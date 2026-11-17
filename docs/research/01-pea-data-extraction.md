# Tiros PEA (Norda Stelo, eff. 10 Jul 2026, signed 29 Jul 2026): data extraction for an Excel mass-balance and economic model

Source for every item: /home/claude/source/Tiros_PEA_2026.pdf (NI 43-101 Technical Report & PEA, 408 PDF pages).
Citation format: **[p.N | PDF M]**, where N is the printed page number in the footer and M is the PDF page. **Throughout this report, printed page = PDF page + 1.**
"DERIVED" marks my own arithmetic, with the working shown. "NOT STATED" means I searched the full text and the item is not in the report.

---

## 0. Headline numbers for the modeller

### Takeaway
The base case processes 500,000 t/a ROM (9.534 Mt over 20 years) at 26.3% TiO2 and 10,852 ppm TREO. It produces 42,390 t/a coarse TiO2 product, 47,865 t/a fine TiO2 product and 6,213 dmt/a MREC. Reagents make up 86% of opex. Sulfuric acid is 186,986 t/a (96%) at US$170/t. NaOH is the single largest reagent cost. There are several material internal inconsistencies, listed in Q11 and Q12. The most important one: revenue is calculated on 4,367 t/a TREO (about 80.5% recovery), while Section 17 says 3,636 t/a (67%).

### Cited Findings: headline table

| Parameter | Value (units as printed) | Source |
|---|---|---|
| ROM feed, steady state | 500,000 t/a (tpa) | [p.275 \| PDF274] Table 17.2; [p.330 \| PDF329] Table 21.1 |
| ROM schedule | Y1 300 kt; Y2–19 500 ktpa; Y20 234 kt (234.4 ktpa in 22.1.1) | [p.342 \| PDF341]; [p.349 \| PDF348] |
| LOM ROM processed | 9.534 Mt (9.53 Mt) | [p.330 \| PDF329]; [p.261 \| PDF260] |
| Head grade TiO2 / TREO | 26.3% (26.27% in 17.3) / 10,852 ppm | [p.267 \| PDF266] Table 17.1; [p.274 \| PDF273] |
| Fe2O3 / Al2O3 / SiO2 | 31.95% / 11.47% / 22.95% | Table 17.1 [p.267 \| PDF266] |
| Feed TREO | 5,426 t/a | Table 17.2 [p.275 \| PDF274] |
| Operating hours | 365 d/a, 92% availability, 8,059 h/a (8,059.2); ~73 t/h ROM | [p.275 \| PDF274]; [p.342 \| PDF341] |
| Coarse TiO2 product | 42,390 t/a; 84.7% TiO2; –300/+75 µm (~75 µm in Table 19.1) | [p.275 \| PDF274]; [p.43 \| PDF42]; [p.314 \| PDF313] |
| Fine TiO2 product | 47,865 t/a; 57.9% TiO2; –20 µm | same |
| Global TiO2 recovery | 68.7% | Table 17.2 |
| MREC | 6,213.0 dmt/a; TREO equivalent 4,367.1 dmt/a (Table 22.2). Sec 17 states 3,636 t/a TREO to MREC | [p.349 \| PDF348]; [p.274 \| PDF273] |
| Global TREO recovery | 67.0% | Table 17.2 |
| H2SO4 (96%) | 186,986 t/a at US$170/t, giving US$31.8 M/y and US$63.6/t ROM | Table 17.4 [p.276 \| PDF275]; Table 21.8 [p.341 \| PDF340] |
| NaOH (98%) | 102,534 t/a at US$420/t, giving US$43.1 M/y and US$86.1/t ROM | same |
| HCl 34% | 82,192 t/a at US$200/t, giving US$16.4 M/y and US$32.9/t ROM | same |
| Gross opex | US$109.5 M/y; US$219.0/t ROM (incl. taxes) | Table 21.7 [p.340 \| PDF339] |
| Net (model) opex | US$92.8 M/y; US$186.3/t ROM; LOM US$1,776.1 M | Table 21.9 [p.341 \| PDF340] |
| Initial capex | US$191.2 M gross; US$159.6 M net; US$31.6 M tax | Table 21.2 [p.332 \| PDF331] |
| Sustaining capex | US$59.6 M gross (US$48.9 M net); US$2.9 M/y | [p.330 \| PDF329]; [p.349 \| PDF348] |
| Prices | TREO basket US$57.4/kg; payability 70%, so US$40.2/kg payable; TiO2 coarse US$900/t; fine US$650/t (FOB Santos) | [p.348–349 \| PDF347–348] |
| Royalties | CFEM 2.0% of gross revenue; landowner 1.0% | [p.350 \| PDF349] |
| Taxes | IRPJ 25% (15% + 10% surcharge); CSLL 9%; export sales untaxed | [p.351–352 \| PDF350–351] |
| FX / discount rate | BRL 5.00 per US$1.00; 8% real, ungeared | [p.347 \| PDF346] |
| NPV8 / IRR | Pre-tax US$1,138.8 M / 62.7%; post-tax US$714.9 M / 44.2%; payback 1.3 / 1.9 yr | Table 22.5 [p.353 \| PDF352] |

---

## 1. Feed: ROM tonnage, grades, moisture, density

### Takeaway
Plant feed is 500,000 t/a of high-grade (HG) material, 9.53 Mt over the life of mine (LOM). Grades are 26.3% TiO2 and 10,852 ppm TREO, with Fe2O3, Al2O3 and SiO2 given. The report gives no MREO, CaO, P2O5, Th or U grade for the plant feed and no ROM moisture.

### Cited Findings
- **ROM chemistry (Table 17.1):** TiO2 26.3%, Fe2O3 31.95%, Al2O3 11.47%, SiO2 22.95%, REE 10,852 ppm. [p.267 | PDF266]. Repeated in Table 17.2 [p.275 | PDF274]. Section 17.3 gives "26.27% TiO₂" [p.274 | PDF273].
- **LOM plan:** 9.53 Mt HG processed over about 20 years at a nominal 500,000 tpa; average 26.3% TiO2 and 10,852 ppm TREO. The pits also contain 25.98 Mt waste and 12.78 Mt medium-grade (MG) material, which is stockpiled and not processed. [p.46 | PDF45]; [p.261 | PDF260].
- **Strip ratio:** 2.7:1 waste to HG plant feed. Counting waste plus MG against HG, the ratio is 4.1:1. [p.261 | PDF260] Table 16.5.
- **MG stockpile grade:** 3,577 ppm TREO and 12.2% TiO2 (Table 16.7). Annual waste is 1.36 Mt/y and MG to stockpile 0.67 Mt/y in years 2–19. [p.262 | PDF261]
- **Resource classes in the production target:** about 4.921 Mt Measured, 4.535 Mt Indicated and 0.077 Mt Inferred, quoted as 99.2% M+I and 0.8% Inferred [p.342 | PDF341]. This contradicts Sections 1.14 and 16, which say there is "no Inferred category material" in plant feed [p.46 | PDF45; p.256 | PDF255].
- **MREO:** not stated for the plant feed. For context, the HG domain M+I resource is 103 Mt at 23% TiO2, 9,100 ppm TREO and 2,400 ppm MREO (MREO/TREO 26%). Table 1.1 [p.45 | PDF44].
- **REO basket composition:** the magnet oxides NdPr, Tb and Dy make up 84% of basket value [p.348 | PDF347]. The report does not give individual oxide percentages for the feed or the MREC.
- **CaO, P2O5, Th, U in ROM:** NOT STATED. Partial context only:
  - BK09 –75 µm fraction: P2O5 0.91% and Tr2O3 0.63% (Table 13.13) [p.211 | PDF210].
  - Historical Vicenza holes averaged 0.68% P2O5 [p.78 | PDF77].
  - Ti correlates positively with Th and U along the weathering profile [p.87 | PDF86].
  - SOX (strongly oxidized saprolite) is defined by CaO < 0.15% [p.87 | PDF86].
- **Density:**
  - Pit optimization uses an average dry density of 1.63 t/m³ and a 30% swell factor (Table 16.1) [p.257 | PDF256].
  - Resource density domains (Table 14.6) [p.239 | PDF238]: OVB mean 1.78, CPC (Capacete) 2.03, TBR 1.99.
  - Low-grade stockpile 1.87 t/m³ [p.293 | PDF292]; waste rock 1.8 t/m³ [p.298 | PDF297]; filtered tailings placed dry density 1.5 t/m³ [p.305 | PDF304].
- **ROM moisture:** NOT STATED. Material is described as "shallow, soft, and highly weathered … friable," so crushing is not needed; disaggregation is by trommel scrubber [p.267 | PDF266].
- **Bond ball-mill work index (+75 µm only):** BK09 15.7 kWh/t; BK11 16.7 kWh/t [p.205 | PDF204].
- **Pilot-feed proxy sample BK19:** 24.1% TiO2 and 0.94% TREO; 36.5% Fe2O3, 17.5% SiO2, 9.84% Al2O3 (Table 13.17) [p.217 | PDF216].
- **Mining factors:** recovery 95%, dilution 5% [p.334 | PDF333].

### Inferences
- DERIVED: Feed TiO2 = 500,000 × 26.27% = 131,350 t/a (131,500 t/a at 26.3%). Feed TREO = 500,000 × 10,852 ppm = 5,426 t/a, which matches Table 17.2.
- DERIVED: LOM contained TREO = 9.534 Mt × 10,852 ppm = 103,463 t.

### Gaps
- Plant-feed MREO grade, oxide-by-oxide REO distribution, CaO, P2O5, Th, U, ROM moisture and ROM SG: NOT STATED.

---

## 2. Mass split: coarse (+75 µm) vs fines (–75 µm), rejects and intermediate yields

### Takeaway
The report does NOT publish the METSIM mass balance. There are no stream tonnages for the plant design. The only complete mass and assay balance is the BK19 bench test (Table 13.17). In that test:
- 67.8% of feed mass is natural –75 µm, plus 3.33% fines from grinding the oversize.
- 28.9% of feed mass reports to the +75 µm circuit.
- 58.1% of feed mass reaches the acid bake.
- The leach residue is 30.8% of feed mass.

### Cited Findings
- **Size split cut points:** scrubber, then a 300 µm screen (oversize goes to a rod mill), then a 75 µm screen. 75–300 µm goes to the coarse circuit; <75 µm goes to the fines (REE) circuit [p.267–268 | PDF266–267].

**BK19 full-circuit balance (Table 13.17, % of fresh feed)** [p.217–218 | PDF216–217]

| Stream | Mass % | TREO % | TiO2 % | TREO dist % | TiO2 dist % |
|---|---|---|---|---|---|
| Fresh feed | 100.0 | 0.94 | 24.1 | 100 | 100 |
| Combined oversize (+75 µm) | 28.9 | 0.54 | 27.1 | 16.7 | 32.5 |
| Fines from grinding (–75 µm) | 3.33 | 0.98 | 25.6 | 3.47 | 3.54 |
| Coarse LIMS magnetics (reject) | 12.7 | 0.17 | 11.7 | 2.29 | 6.21 |
| Coarse LIMS non-magnetics | 16.2 | 0.84 | 39.2 | 14.4 | 26.3 |
| Gravity float / light fraction (reject) | 3.98 | 0.28 | 18.3 | 1.17 | 3.03 |
| Gravity heavy fraction | 12.2 | 1.02 | 46.0 | 13.2 | 23.3 |
| Coarse kiln off-gas | 0.85 | | | | |
| Calcine | 11.3 | 1.10 | 49.5 | 13.2 | 23.3 |
| Calcine magnetics (reject) | 0.23 | 0.71 | 32.1 | 0.18 | 0.31 |
| Calcine non-magnetics | 11.1 | 1.10 | 49.8 | 13.0 | 23.0 |
| Dissolved solids to HCl leach liquor | 4.21 | | | 10.7 | 0.24 |
| HCl leach residue = TiO2 concentrate | 6.88 | | 79.5 | 2.33 | 22.7 |
| Natural fines (–75 µm) | 67.8 | 1.11 | 22.7 | 79.9 | 63.9 |
| Fines LIMS magnetics (reject) | 3.36 | 0.14 | 13.2 | 0.49 | 1.85 |
| Fines LIMS non-magnetics (printed as "Mag fraction – LIMS"; a label error) | 64.4 | 1.16 | 23.2 | 79.4 | 62.1 |
| Fines kiln off-gas | 4.04 | | | | |
| Calcine | 60.4 | 1.24 | 24.7 | 79.4 | 62.1 |
| Calcine LIMS magnetics (reject) | 0.35 | | | 0.05 | 0.19 |
| Calcine LIMS non-magnetics | 60.0 | | | 79.3 | 61.9 |
| WHIMS magnetics (reject) | 1.95 | | | 2.15 | 1.88 |
| WHIMS non-magnetics = acid-bake solids feed | **58.1** | 1.25 | 24.9 | **77.2** | **60.0** |
| Acid-bake leach residue | **30.8** | 0.14 | 8.01 | 4.51 | 10.2 |
| Dissolved solids, leach liquor ("TREO concentrate") | N.A. | 0.63 | | **72.5** | **49.8** |

- **Other size splits:**
  - Table 13.7, BK19: +75 µm is 29.2% wt, 33.9% TiO2, 21.7% CeO2 and 13.5% La2O3. –75 µm is 67.5% wt, 62.6% TiO2, 74.5% CeO2 and 84.3% La2O3. Ground +75 µm fines are 3.37% wt [p.204 | PDF203].
  - BK11: +75 µm 25.0% wt, 27.1% TiO2; –75 µm 75.0% wt, 72.9% TiO2 [p.204 | PDF203].
  - Text summary: "BK11 carried 25.0% +75 microns … BK19 … 32.5% … +75 carried 25.6% of the TiO2 for BK11 and 37.4% … for BK19" [p.203 | PDF202].
  - BK09 (Table 13.2): <300/>75 µm is 30.1% wt, 34.9% TiO2 and 20.8% total REO; <75 µm is 69.9% wt; <38 µm is 62.1% wt, 57.4% TiO2 and 74.4% REO [p.193 | PDF192].
  - Text 13.5.2: BK09 split 25.8% +75 µm and 74.2% –75 µm [p.205 | PDF204]. Fig 13.8: BK09 –20 µm is 60.08% of the –75 µm [p.211 | PDF210].
  - BK11: 67.47% wt –20 µm, carrying 64.72% TiO2 and 80.40% Ce2O3 (Table 13.4) [p.196 | PDF195].
  - Section 25.1: about 87% of REE is in –53 µm [p.360 | PDF359].
- **BK09 coarse balance (Table 13.10, kg per 1,000 kg ROM)** [p.208 | PDF207]:

| Stream | kg | TiO2 % |
|---|---|---|
| +74 µm fraction | 258 | 17.1 |
| Non-magnetics (1,000 G) | 122 | 20.2 |
| Heavy fraction | 62 | 41.2 |
| Reduced (calcined) material | 59 | 41.2 |
| Non-magnetics (2,000 G) | 32 | 59.5 |
| Conductor fraction | 23 | 62.2 |
| Final concentrate | 18 | 76.8 |

- **BK09 fines LIMS at 800 G (Table 13.13, ROM basis)** [p.211 | PDF210]: magnetics (Mag75B) 285.98 g/kt, carrying 27.19% TiO2, 29.43% Tr2O3 and 37.58% Fe2O3. Non-magnetics (NonMag75B) 412.93, carrying 46.14% TiO2 and 58.69% Tr2O3.
- **Tonnes/yr of fines to the acid bake (PEA design): NOT STATED.**
- **Pit-optimization factors (Table 16.1):** TREO mass recovery 15%, TiO2 mass recovery 30% [p.257 | PDF256].
- **Tailings generation:** "assumed tailings generation rate of approximately 80% of ROM feed" [p.344 | PDF343]. Dewatered tailings deposition 1.24 kt/d (750 m³/d) [p.305 | PDF304].

### Inferences (DERIVED, applying BK19 proportions to 500,000 t/a; not PEA design values)

| Stream | Working | Result |
|---|---|---|
| Acid-bake solids feed | 58.1% × 500,000 | ≈ 290,500 t/a |
| Total –75 µm (natural + ground) | (67.8% + 3.33%) × 500,000 | ≈ 355,650 t/a |
| +75 µm | 28.9% × 500,000 | ≈ 144,500 t/a |
| Acid-bake leach residue | 30.8% × 500,000 | ≈ 154,000 t/a |
| All magnetic rejects | (12.7 + 0.23 + 3.36 + 0.35 + 1.95)% = 18.59% | ≈ 93,000 t/a |
| Gravity light reject | 3.98% | ≈ 19,900 t/a |
| Kiln off-gas mass loss | (0.85 + 4.04)% = 4.89% | ≈ 24,450 t/a |

- PEA split of TiO2 recovery (DERIVED, treating product tonnes as contained TiO2; see Q11): coarse 42,390 / 131,350 = 32.3% of feed TiO2; fine 47,865 / 131,350 = 36.4%; total 68.7%. BK19 testwork gave 22.7% coarse + 49.8% fine to liquor = 72.5%.
- Tailings at 80% of ROM = 400,000 t/a. Deposition of 1.24 kt/d × 365 = 452,600 t/a (DERIVED).

### Gaps
- METSIM stream table, design fines-to-bake tonnage, slimes/desliming reject tonnage, and ultrafines handling: NOT STATED. Section 26.1 recommends studying "options to deal with and possible rejection of ultra fines" [p.384 | PDF383].

---

## 3. Coarse circuit

### Takeaway
The coarse route is:
1. LIMS at 1,000 G
2. Gravity (densimetric) separation
3. Thickener and filter
4. Rotary-kiln reductive calcination at 600°C for 60 min using CO gas
5. Air and water cooling to 50°C
6. LIMS at about 2,000 G
7. Electrostatic separation
8. HCl leach (16 wt%, 90–100°C, about 90 min)
9. Filtration

The product is 42,390 t/a at 84.7% TiO2.

### Cited Findings
- **LIMS 1,000 G:** reduces "iron content from 42.3% to 17.4%" in the non-magnetics. Magnetics are thickened, filtered and sent to tailings [p.268 | PDF267].
- **Gravity separation:** SiO2 drops from 16.0% to 4.5% in the heavy fraction. The light fraction (kaolinite and quartz) is thickened, filtered and sent to tailings [p.269 | PDF268].
- **Calcination:** rotary kiln at 600°C, 60 min residence, controlled atmosphere, reducing Fe³⁺ to Fe²⁺. The reductant is CO generated externally. The kiln discharge is air-cooled to about 100°C and then water-cooled to about 50°C [p.269–270 | PDF268–269].
  - Testwork used 3% charcoal and 120 min, with later tests at 60 min [p.207 | PDF206].
- **LIMS about 2,000 G:** brings non-magnetics to about 5% Fe [p.270 | PDF269]. Inconsistencies: Figure 17.1 labels this stage "Magnetic separation II 1000 Gauss" [p.265 | PDF264], and BK19 testwork used 1,000 G [p.209 | PDF208].
- **Electrostatic separation:** dry feed required; the conductor fraction reaches <1.0% SiO2 [p.270 | PDF269]. BK09 test went from 11.6% to 8.2% SiO2 [p.207 | PDF206].
- **HCl leach:** 90–100°C, about 90 min, about 16 wt% HCl. Consumption is about 0.056 t active HCl per t ROM, equal to 0.164 t of 34% HCl per t ROM. Expected product grade ">80%" [p.270 | PDF269]. Testwork solid/liquid ratio 1/10 [p.207 | PDF206].
- **Coarse product:** 42,390 t/a (Table 17.2) [p.275 | PDF274]; 84.7% TiO2, –300/+75 µm [p.43 | PDF42]. LOM 808,326 dmt [p.348 | PDF347].
  - Testwork grades: BK09 76.8%; BK19 79.5%, without the electrostatic stage [p.208, p.210 | PDF207, PDF209].
- **Coarse-area reagents (Table 17.3):** HCl 82,192 t/a; CO(g) 685 t/a [p.276 | PDF275].
- **REE lost in the coarse circuit:** 10.7% of feed REE dissolves into the coarse HCl leach liquor (BK19), and this is not recovered in the design [p.219 | PDF218].
- **Coarse-area water:** 130 m³/h (Table 17.5) [p.277 | PDF276].

### Inferences
- DERIVED: 0.164 × 500,000 = 82,000 t/a of 34% HCl, which matches the 82,192 t/a. 82,192 × 0.34 = 27,945 t/a of 100% HCl, which matches 0.056 t/t.
- DERIVED: coarse TiO2 recovery = 32.3% of feed TiO2 if 42,390 t is contained TiO2; 27.3% if 42,390 t is concentrate at 84.7% (42,390 × 0.847 / 131,350).

### Gaps
- Coarse-circuit TiO2 recovery stated explicitly as a design value, and coarse product moisture: NOT STATED.

---

## 4. Fines circuit (acid bake, leach, Ti hydrolysis, impurity removal, MREC)

### Takeaway
The fines route is:
1. LIMS at 800 G
2. Reduction roast at 600°C for 1 h with CO or carbon
3. Cooling
4. Dry LIMS
5. Acid bake with 96% H2SO4 at 300°C for about 1 h (testwork dose 1.5811 kg H2SO4 per kg solids)
6. Acid regeneration at about 600°C (Fig 13.12 and 17.2 say 680°C)
7. Water leach at 80°C
8. Filtration
9. Ti precipitation with 10% NaOH
10. Fe/Al/K/Ca removal with Mg(OH)2
11. MREC precipitation with Na2CO3

No lime, limestone or ammonium bicarbonate is used.

### Cited Findings
- **LIMS 800 G and roast:** magnetics go to tailings. The non-magnetics go to a rotary kiln, then air cooling to about 100°C and water cooling to 50°C, then a dry LIMS [p.272 | PDF271].
  - Figure 17.2 shows "Reduction roasting (600°C) 1 hour with carbon" and charcoal [p.266 | PDF265].
  - Testwork MET-53 calcined at 600°C with coal; the table note says "16.6 wt.% coal for 1 h" [p.213–214 | PDF212–213].
- **Acid bake:** "Acid Baking Rotary Kiln, using concentrated sulfuric acid … reactive paste … thermal treatment 300°C for ~1 hour". Fe, Al and Ti also react, "increasing acid consumption" [p.272 | PDF271].
  - Testwork dose: **1.5811 kg H2SO4 per kg rock**, roast 1 h at 300°C [p.213–214 | PDF212–213].
- **Acid regeneration:** "assumed in the process design … approximately 600°C, producing an SO₃-bearing gas … hydrated to regenerate concentrated H₂SO₄ for recycling to the acid-bake stage. Acid regeneration is a conceptual and untested design assumption" [p.272 | PDF271].
  - Figure 13.12 shows "Acid Regeneration Bake at 680ºC for 1h" [p.222 | PDF221]. Figure 17.2 shows "Acid baking regeneration (680°C)" [p.266 | PDF265].
- **Water leach:** Fig 17.2 shows "Water leach (80°C)". Testwork was at 80°C and 15 wt% solids [p.213 | PDF212]. Sequential washing in agitated reactors; the residue (mainly SiO2) is filtered to a "low-moisture solid residue" sent to tailings [p.272 | PDF271].
- **Leach extraction:**
  - MET-53 stage leach recovery: REE 90.9%, TiO2 82.9% [p.213 | PDF212].
  - Full MET-53 conversions: SiO2 7.94%, Al2O3 64.08%, Fe2O3 84.26%, MgO 68.14%, TiO2 82.93%, P2O5 91.72%, Tr2O3 90.91% [p.214 | PDF213].
  - BK19: 72.5% of feed TREO and 49.8% of feed TiO2 report to leach liquor [p.219 | PDF218].
- **Ti removal by hydrolysis:** "controlled neutralization using 10 wt% NaOH … to promote hydrolysis and precipitation of hydrated titanium oxide. … This step has not been demonstrated for the Tiros process liquor." It carries a risk of sodium–rare-earth double-sulfate losses [p.273 | PDF272].
- **Impurity removal:** staged Mg(OH)2 additions precipitate Fe and Al first, then K, Ca and other ions. The filter cake goes to tailings [p.273 | PDF272]. Mg-based reagents were chosen "to avoid gypsum formation in the sulfate media" [p.371 | PDF370].
- **MREC precipitation:** Na2CO3 solution at 25% w/w; filter, reslurry wash, then filter press [p.273 | PDF272; p.276 | PDF275].
- **Fine TiO2 product:** 47,865 t/a [p.275 | PDF274]; 57.9% TiO2, –20 µm [p.43 | PDF42]. LOM 912,727 dmt [p.348 | PDF347].
- **TREO to MREC:** "approximately 3,636 t/a TREO" at 67.0% recovery (Table 17.2). MREC tonnage and TREO grade "To be confirmed" [p.275 | PDF274].
  - The economic model uses MREC 6,213.0 dmt/a and TREO equivalent 4,367.1 dmt/a (Table 22.2) [p.349 | PDF348].
  - Stated MREC grades conflict: "MREC average grade is 52% on a dry basis" [p.349 | PDF348]; target purity about 95% dry, with "PEA process design criteria indicating a concentrate grade of 96.4%" (Table 19.1) [p.314 | PDF313].
- **Fines-area reagents (Table 17.4)** [p.276 | PDF275]:

| Reagent | t/a |
|---|---|
| Mg(OH)2 (95%) | 2,397 |
| Na2CO3 (95%) | 3,725 |
| CO(g) | 10,205 |
| H2SO4 (96%) | 186,986 |
| NaOH (98%) | 102,534 |

- **Lime, limestone, ammonium bicarbonate, oxalic acid:** NOT USED and NOT STATED. The ammonium sulfate ionic-clay leach was tested but abandoned, giving 0.21–7.68% TREO recovery (Table 13.18) [p.219–220 | PDF218–219]. A nitric acid route (Altilium) was also tested and gave no Ti extraction [p.219 | PDF218].
- **Fine-area water:** 54.5 m³/h [p.277 | PDF276].

### Inferences (DERIVED)
- H2SO4 (96%) per t ROM = 186,986 / 500,000 = **0.374 t/t (374 kg/t ROM)**. On a 100% basis: 179,507 t/a, or 359 kg/t ROM.
- H2SO4 per t of acid-bake feed, using the BK19 58.1% proxy (290,500 t/a): 186,986 / 290,500 = 0.644 t (96%) per t. The testwork gross dose is 1.5811 t/t and stage consumption is 1.111 t/t.
- NaOH = 205 kg/t ROM; Mg(OH)2 = 4.8 kg/t ROM; Na2CO3 = 7.5 kg/t ROM.
- MREC TREO grade implied by Table 22.2: 4,367.1 / 6,213.0 = **70.3%**. This matches neither 52% nor 95–96.4%.
- Stage TREO extraction implied by BK19: 72.5% / 77.2% = 93.9% of the TREO entering the bake.

### Gaps
- Acid-bake residence time beyond "~1 h", acid:solids ratio in the design, leach residue moisture, MREC moisture, hydrolysis pH and temperature, and fine-TiO2 product moisture: NOT STATED.
- Recovery of Ti and REE from the leach liquor has not been tested at all: "testwork was not yet carried out to recover titanium and rare earths from the leach liquor" [p.360 | PDF359].

---

## 5. Sulfuric acid: consumption, recycling, price, source

### Takeaway
The report contains only one design acid figure: 186,986 t/a of 96% H2SO4 at US$170/t (inclusive of transport), giving US$31.8 M/y. Acid is purchased and delivered by tanker truck. A regeneration unit is assumed in the design, but no recycle % is given. An on-site sulfur-burning acid plant is NOT in the base case; it is listed as an opportunity to study. **The report never mentions the press-release acid-consumption correction or a revised reagent price. "Before" values cannot be extracted from this document.**

### Cited Findings
- **Consumption:** H2SO4 (96%) 186,986 t/a (Table 17.4) [p.276 | PDF275], identical in Table 21.8 [p.341 | PDF340].
- **Price:** US$170/t, giving US$31.8 M/y and US$63.6/t ROM (Table 21.8) [p.341 | PDF340]. Reagent costs are "inclusive of transport" (Table 21.7) [p.340 | PDF339].
- **Supply:** "transported in a tanker truck and transferred to a storage tank; It is received at a concentration of 96%" [p.276 | PDF275]. The supplier and origin are NOT STATED.
- **Testwork raw consumption:** MET-53 stage consumption 1.111 kg per kg leached, on material that is about 42% of initial feed, "representing an overall raw acid consumption of about 459 kg sulphuric acid / t of feed (before any acid regeneration)" [p.214 | PDF213].
  - Table 13.16 [p.215 | PDF214], MET-53: 949.91 g fed, 667.67 g consumed, 282.24 g free. That is A = 1.111 kg consumed per kg feed and B = 0.470 kg unreacted per kg feed.
  - The other temperatures in the same table give 1.128–1.179 kg/kg consumed.
- **Recycling:** an acid-regeneration unit at about 600°C (SO₃ gas, hydrated to H2SO4) is "assumed in the process design … conceptual and untested" [p.272 | PDF271]. **The recycle % is NOT STATED.**
- **Site acid plant:**
  - "The possible production of sulphuric acid with a site acid plant should be studied" (25.1.2 opportunity 5) [p.363 | PDF362].
  - "The potential for a sulphuric acid generation plant to reduce overall OPEX costs can be studied" [p.385 | PDF384].
  - "Integration and optimization of the sulfuric acid regeneration plant will … mitigate supply risks" [p.371 | PDF370].
- **Sulfur price:** NOT STATED.
- **Risk statement:** the fines fraction has "elevated consumption of sulfuric acid, which represents a high sensitivity to operating costs" [p.371 | PDF370].
- **Correction / revised price:** NOT STATED in the report. The report only cites the 14/15 June 2026 release and a "Tiros Project PEA Supplementary Information, 17 June 2026" document in its references [p.409 | PDF408]. Figure 16.2 is sourced to a "Resouro press release – June 17, 2026" [p.260 | PDF259]. Neither the original consumption nor the original price is reproduced.

### Inferences (DERIVED)
- Testwork raw acid at PEA scale: 459 kg/t × 500,000 t/a = 229,500 t/a before regeneration (100% basis presumed). Design net is 179,507 t/a on a 100% basis. This implies about 21.8% lower net acid than the raw testwork figure. (Comparing 96% tonnage directly gives 186,986 / 229,500 = 81.5%.) This is the only implied "regeneration credit"; the report does not state it.
- In MET-53, free (unreacted) acid is 0.470 / 1.5811 = 29.7% of the dose. This is the theoretical ceiling for recovering unreacted acid. Acid consumed in sulfating gangue (Fe, Al, Mg, P) is not recoverable unless sulfates are thermally decomposed.
- Acid at US$63.6/t ROM is 29% of gross opex (63.6 / 219.0).
- Sensitivity: ±US$10/t acid changes opex by ±US$1.87 M/y. ±10% acid tonnage changes it by ±US$3.18 M/y.

### Gaps
- Pre-correction acid tonnage and price, the press-release figures, recycle %, regeneration energy, acid origin and logistics, and sulfur price: NOT STATED. The modeller needs the 17 June 2026 Supplementary Information release to reconcile this.

---

## 6. Other reagents and consumables

### Takeaway
Total reagent mass is 394,822 t/a at a cost of US$94.5 M/y (US$189.0/t ROM). Unit costs include transport. NaOH (US$43.1 M) and H2SO4 (US$31.8 M) dominate. The report gives no supplier origins or separate freight rates for reagents.

### Cited Findings
**Table 21.8 reagent operating costs (gross basis)** [p.341 | PDF340]:

| Reagent | t/a | US$/t | US$ M/y | US$/t ROM |
|---|---|---|---|---|
| HCl 34% | 82,192 | 200 | 16.4 | 32.9 |
| H₂SO₄ 96% | 186,986 | 170 | 31.8 | 63.6 |
| Na₂CO₃ | 3,726 | 130 | 0.5 | 1.0 |
| Mg(OH)₂ | 2,397 | 190 | 0.5 | 0.9 |
| NaOH | 102,534 | 420 | 43.1 | 86.1 |
| CO | 10,890 | 90 | 1.0 | 2.0 |
| Charcoal | 6,096 | 210 | 1.3 | 2.6 |
| **Total** | **394,822** | — | **94.5** | **189.0** |

- **CO:** 10,890 t/a equals Table 17.3 coarse (685) plus Table 17.4 fine (10,205) [p.276 | PDF275]. CO is "produced from charcoal through combustion and calcination" [p.276 | PDF275].
- **Na2CO3:** 3,726 t/a in Table 21.8 vs 3,725 t/a in Table 17.4 (rounding).
- **NaOH:** received as a bagged solid and made up to 10% solution [p.276 | PDF275]. **Mg(OH)2:** bagged solid, made up to a 10 wt% slurry [p.277 | PDF276]. **HCl:** tanker truck, diluted to 16% [p.276 | PDF275].
- **LPG (kilns):** about 1.54 kt/y at US$1.449/kg incl. transport, giving US$2.2 M/y (US$4.5/t ROM) [p.345 | PDF344; p.340 | PDF339]. Diesel is used for backup generation only; quantity and price NOT STATED [p.278 | PDF277].
- **Origin, port of import, Santos import logistics and reagent freight rate:** NOT STATED. Reagents are only described as "inclusive of transport." The Port of Santos is mentioned only for product logistics.

### Inferences (DERIVED)
- Recomputed reagent costs: 82,192 × 200 = 16.44; 186,986 × 170 = 31.79; 102,534 × 420 = 43.06; 10,890 × 90 = 0.98; 6,096 × 210 = 1.28; 3,726 × 130 = 0.48; 2,397 × 190 = 0.46. Total US$94.49 M, consistent with Table 21.8.
- NaOH at 102,534 t/a (205 kg/t ROM) is unusually large relative to Ti-hydrolysis needs. It is the single largest cost line (US$86.1/t ROM) and its basis is not explained.

### Gaps
- Reagent sources, delivered vs ex-works split, and lime/limestone/flocculant/consumables (none listed): NOT STATED.

---

## 7. Residues and waste: tailings, residues, NORM, water

### Takeaway
All process residues go to one filtered dry-stack co-disposal facility (Upper South Pile, USP) with an engineered liner. Design figures are 1.24 kt/d deposition, 9.0 Mt / 6.0 Mm³ required tailings capacity, and 15% target moisture. The report does not give separate tonnages for leach residue, Mg-neutralization cake or Ti-hydrolysis solids. Th/U deportment is not quantified; NORM is "under evaluation."

### Cited Findings
- **Dry stack:** filtered tailings deposited at 1.24 kt/d (750 m³/d), up to a maximum of 9.0 Mt (5.5 Mm³). The starter facility needs 450 kt (280,000 m³). USP total capacity is 27.9 Mm³ against about 9.0 Mm³ required for waste rock plus tailings [p.305 | PDF304].
- **Table 18.6 design criteria** [p.305–306 | PDF304–305]:
  - Required tailings storage 9.0 Mt / 6.0 M m³
  - Placed dry density 1.5 t/m³; target moisture 15% w/w (<15%)
  - Slopes 3H:1V, 40 m overall height; footprint 970,000 m²
  - Waste rock in USP 1.7 Mt / 3.0 M m³
  - Evaporation 1,450 mm; precipitation 1,415 mm
- **Tailings opex allowance:** US$6.0 M/y (US$12/t ROM), based on 2.0 Mtpa at US$3.00/t. The report itself notes this exceeds the roughly 80%-of-ROM tailings rate [p.344 | PDF343].
- **Tailings geochemistry:**
  - Low acid generation: NPR > 2, NAG pH > 4.5, S²⁻ < 0.1%.
  - USEPA 1313 leach tests exceed CONAMA 420/2009 and 357/2005 limits for As, Cd, Co, Cr, Hg, Ni, Pb, V and Zn. A liner is retained [p.304 | PDF303].
  - Classed Non-Acid Forming (NAF) [p.323 | PDF322].
- **Residue streams:**
  - Acid-bake leach residue: "low-moisture solid residue … sent to the tailing's facility" [p.272 | PDF271].
  - Mg(OH)2 impurity cake: "low-moisture filter cake for disposal to the tailings storage facility" [p.273 | PDF272].
  - Tonnages for each: NOT STATED.
  - Gypsum: avoided by design through the use of Mg(OH)2 [p.371 | PDF370].
- **NORM / Th / U:**
  - Programs include "Radionuclide characterization, including naturally occurring radioactive materials (NORM)" [p.323 | PDF322] and "Radiological measurements and controls in waste piles and processing facilities" [p.321 | PDF320].
  - Risk: "radionuclide occurrence and potential environmental implications remain under evaluation" [p.376 | PDF375].
  - Testwork is needed on "radionuclide levels" in the Ti concentrate [p.384 | PDF383] and on "radionuclide considerations" for product acceptance [p.371 | PDF370].
  - No Th/U assays or deportment are given.
- **Water discharge:** the thickener overflows go to water treatment. A Water Recovery System is to be designed in the PFS [p.277 | PDF276]. Risk: "Final water discharge quality needs definition of the water treatment processes" [p.363 | PDF362]. Discharge volumes are NOT STATED.

### Inferences (DERIVED)
- 1.24 kt/d × 365 = 452.6 kt/a, consistent with ROM minus products: 500,000 − 42,390 − 47,865 − 6,213 = 403,532 t/a, plus reagent-derived precipitates and moisture.
- 9.0 Mt / 20 yr ≈ 450 kt/a.

### Gaps
- Split of tailings by stream (magnetics, gravity lights, leach residue, Mg cake, Ti-hydrolysis reject), Th/U deportment and dose, and effluent quality and volume: NOT STATED.

---

## 8. Opex breakdown, power, water, labour

### Takeaway
Gross opex is US$109.5 M/y (US$219.0/t ROM), of which reagents are US$94.5 M (86.3%). Net model opex is US$92.8 M/y (US$186.3/t ROM). Power is 23.6 GWh/y at US$0.086/kWh. Raw water is 391 m³/h. There are 116 direct staff (191 including contract mining).

### Cited Findings
**Table 21.7, gross opex** [p.340 | PDF339]:

| Category | US$ M/y | US$/t ROM | % |
|---|---|---|---|
| Reagents (incl. transport) | 94.5 | 189.0 | 86.3 |
| LPG (incl. transport) | 2.2 | 4.5 | 2.0 |
| Personnel | 2.4 | 4.7 | 2.2 |
| Plant maintenance | 0.6 | 1.3 | 0.6 |
| Electrical energy | 2.0 | 4.1 | 1.9 |
| Tailings stockpiles | 6.0 | 12.0 | 5.5 |
| Mine operation | 1.8 | 3.5 | 1.6 |
| **Total** | **109.5** | **219.0** | **100** |

**Table 21.9, net model opex** [p.341 | PDF340]:

| Category | US$ M/y | US$/t ROM | LOM US$ M |
|---|---|---|---|
| Mining | 5.6 | 11.3 | 107.6 |
| Plant | 80.4 | 161.6 | 1,540.7 |
| G&A | 1.5 | 3.0 | 28.6 |
| Logistics | 5.2 | 10.4 | 99.2 |
| **Total** | **92.8** | **186.3** | **1,776.1** |

- Gross basis includes taxes; net basis is "net of recoverable taxes" (US$92.6 M/y in 22.1.5) [p.350 | PDF349].
- **Plant maintenance:** 2% of the mechanical equipment cost base [p.344 | PDF343].
- **Mining cost (pit optimization):** US$3.5/t ore and US$3.0/t waste [p.257 | PDF256]. Mining is contractor-run [p.334 | PDF333].
- **Power:**
  - 23.6 GWh/y at US$0.086/kWh, giving US$2.0 M/y [p.345 | PDF344].
  - Demand 2,994 kW / 3,382 kVA (Table 18.1): Ti route 452 kW, REE route 352 kW, utilities and reagents 428 kW, raw water 1,251 kW, admin 511 kW [p.283 | PDF282].
  - Supply from the CEMIG grid via a 37 km, 13.8 kV line from the São Gotardo II substation [p.283 | PDF282].
- **Water:** Table 17.5 gives 391 m³/h total: coarse 130, fine 54.5, reagents 154, cooling make-up 1.89, others 50.7 [p.277 | PDF276]. Raw water demand is about 390 m³/h from the Borrachudo River via a 6.8 km pipeline (nominal 463.0, max 555.6 m³/h) [p.282 | PDF281].
- **Labour:** 191 total, of which 75 are outsourced mining. Direct headcount is 116 (100 operations + 16 maintenance), costing US$2.4 M/y [p.346 | PDF345].
- **Thermal energy:** LPG for the kilns (above). Kiln thermal duty: NOT STATED.

### Inferences (DERIVED)
- Power check: 2,994 kW × 8,059 h = 24.1 GWh, close to 23.6 GWh.
- Water: 391 m³/h × 8,059 h = 3.15 Mm³/a (3.43 Mm³/a at 8,760 h).
- Labour: US$2.4 M / 116 = about US$20.7k per head per year.

### Gaps
- Consumables and wear parts, laboratory and insurance as separate lines, kiln fuel per stage, and the acid-regeneration energy load: NOT STATED.

---

## 9. Capex breakdown

### Takeaway
Initial capex is US$191.2 M gross (US$159.6 M net plus US$31.6 M tax). It is reported only by discipline (direct and indirect), not by process area. The report gives no separate capex for the coarse circuit, the fines/acid bake, REE recovery, acid regeneration or tailings. Sustaining capex is US$59.6 M, mostly mine development. The direct/indirect tables do not sum to the total (see Inferences).

### Cited Findings
- **Table 21.2** [p.332 | PDF331]:

| Item | Net US$ M | Tax US$ M | Gross US$ M | % of total |
|---|---|---|---|---|
| Direct | 99.3 | 22.6 | 121.9 | 63.8 |
| Indirect | 28.3 | 4.4 | 32.7 | 17.1 |
| Contingency | 32.1 | 4.5 | 36.6 | 19.1 |
| **Total** | **159.6** | **31.6** | **191.2** | |

- **Table 21.3 direct, gross US$ M** [p.332–333 | PDF331–332]:
  - Mine development 3.2; earthworks 16.4; concrete 3.8; structural steel 10.0; architectural 7.7
  - Mechanical equipment, platework and tanks 37.1; mobile equipment 0.0; piping 6.0; electrical 6.0; I&C 3.9
  - 13.8 kV line and substation 9.0; water pipeline 6.6
  - **Total direct 109.6**
- **Table 21.4 indirect, gross US$ M** [p.333 | PDF332]:
  - Freight 1.5; construction indirects 4.6; spares 2.2; vendor assistance 1.3; commissioning 0.8
  - Land 2.6; first fill 1.1; EPCM 10.4; owner's cost 6.4
  - **Total indirect 30.8**
- **Table 21.5 sustaining, gross US$ M** [p.333 | PDF332]: mine development 47.8; earthworks 3.3; mine closure 1.6; subtotal 52.7; additional allowance 6.9; **total 59.6**.
- **Cash flow treatment:** sustaining US$2,892k/yr, LOM US$57,835k; closure US$112k/yr from year 5, LOM US$1,799k [p.357 | PDF356]. The text says US$100,000/yr from year 5, about US$1.6 M [p.329 | PDF328].
- **Working capital:** 90 days of opex; US$15.1 M at start, rising to US$23.2 M in year 2 [p.349 | PDF348].
- **Exclusions and basis:** escalation and financing excluded; no salvage value; no separate equipment or plant replacement capital [p.332 | PDF331; p.338 | PDF337]. Accuracy ±50%, Class 5 [p.330 | PDF329].
- **By process area** (mining / beneficiation / calcination / acid bake / REE recovery / tailings): NOT STATED. Mobile equipment is in opex as a contractor cost [p.334 | PDF333].
- **Plant footprint:** about 60,000 m² (200 m × 300 m) [p.286 | PDF285].

### Inferences (DERIVED)
- Table 21.3 + Table 21.4 + contingency = 109.6 + 30.8 + 36.6 = 177.0, not 191.2. This leaves a gap of US$14.2 M. The Table 21.2 gross direct (121.9) and indirect (32.7) differ from the detailed tables by 12.3 and 1.9.
- Contingency is stated three different ways:
  - US$35.1 M "gross contingency" [p.330 | PDF329; p.377 | PDF376]
  - US$36.6 M [p.332 | PDF331; p.349 | PDF348]
  - Section 1.19 says "US$31.6 million of contingency" [p.48 | PDF47], but 31.6 is the tax figure.
- Section 22.1.2 calls 36.6 "19.1% of the total direct plus indirect costs." It is actually 19.1% of the 191.2 total (36.6 / 140.4 = 26%).
- Capex intensity: 191.2 / 0.5 Mtpa = US$382/t annual capacity.

### Gaps
- Area-level capex, acid-regeneration plant capex, and a separately identified tailings/dry-stack capex: NOT STATED.

---

## 10. Prices, payability, logistics, royalties, taxes, FX, discount rate

### Takeaway
- TREO basket US$57.4/kg (US$57.43 in Section 1.17) × 70% payability = US$40.2/kg payable, applied to contained TREO.
- TiO2 coarse US$900/t and fine US$650/t, stated as per tonne of concentrate, FOB Santos.
- Sea freight US$80/t; site-to-Santos logistics US$10.4/t ROM.
- CFEM 2% plus landowner 1%; IRPJ 25% plus CSLL 9%; BRL 5.00/US$; 8% real discount rate.

### Cited Findings
- **TREO basket:**
  - US$57.4/kg; NdPr, Tb and Dy are 84% of value. Dy oxide US$1,640/kg CIF Europe; Tb US$3,609/kg; NdPr oxide US$157.0/kg. Payability 70%, sea freight US$80/t, FOB Santos basis [p.348 | PDF347; p.350 | PDF349].
  - Section 1.17 gives "US$57.43/kg … payable price of approximately US$40.20/kg REO-equivalent," sourced from Argus Media (via the Carina project report) [p.47 | PDF46].
  - Table 22.6 shows the "average (full run)" payable as US$39.2/kg while every year shows 40.2, an inconsistency [p.357 | PDF356].
- **TiO2 prices:**
  - Section 19.4: "US$900.0/t for the updated 84.7% TiO2 coarse anatase concentrate and US$650.0/t for the updated 57.9% TiO2 fine anatase concentrate" [p.316 | PDF315]. That is, per tonne of concentrate.
  - Table 22.6 labels the unit "US$/kg," a typo [p.357 | PDF356].
  - Project Blue ranges: fine US$485–789/t (at about 77% TiO2), coarse US$510–829/t (at about 81% TiO2). US$900/t was supplied by Resouro (previous internal assumption US$1,000/t) and is above the Project Blue range [p.316 | PDF315; p.375 | PDF374].
- **Logistics:**
  - Site to Port of Santos US$10.4/t ROM (US$5.2 M/y) [p.341–342 | PDF340–341].
  - Table 22.1 "Product Logistics US$ 53.00/t Prod" [p.348 | PDF347].
  - Road (LMG-352 to BR-262/BR-354) and/or FCA rail [p.281 | PDF280; p.317 | PDF316].
  - Trucking rate per t-km: NOT STATED.
- **Royalties:**
  - CFEM 2.0% of gross revenue (US$4.9 M/y avg); landowner 1.0% (US$2.4 M/y) [p.350 | PDF349].
  - Legal basis: CFEM 1–3.5% by substance, 2% for REE; the landowner default is half of CFEM [p.70 | PDF69].
  - Pit optimization used a combined 4% [p.257 | PDF256].
- **Taxes:**
  - IRPJ 15% + 10% surcharge = 25%; CSLL 9%. Depreciation on a units-of-production basis.
  - All products exported, so no sales taxes.
  - Tax reform: CBS from 2027, IBS from 2033 [p.351–352 | PDF350–351].
- **Exchange rate:** BRL 5.00 per US$1.00 [p.352 | PDF351].
- **Discount rate:** 8% real, ungeared, mid-period discounting [p.347 | PDF346]. Pit optimization used a 12% WACC [p.257 | PDF256].

### Inferences (DERIVED)
- MREC revenue check: 4,367.1 t × US$57.4 × 0.70 = US$175.5 M, which equals Table 22.3 MREC US$175.3 M. So revenue is calculated on TREO-equivalent tonnes, not MREC tonnes.
- Sea freight check: US$80/t × 4,367 t = US$349k/yr, which equals Table 22.6 "Transport Santos to Europe (349)." So freight is applied per t of TREO, not per t of MREC (which would be US$497k). Also, "Gross Revenue FOB Santos" (244,521) equals "Production Value CIF Europe" (244,521), so the freight is shown but apparently not deducted [p.357 | PDF356].
- Product logistics: US$5,214k / 96,468 t of products = US$54.0/t, close to the US$53.00/t stated.

### Gaps
- Individual REO prices beyond Dy, Tb and NdPr; MREC basket composition; ocean freight for TiO2; trucking US$/t-km; port charges: NOT STATED.

---

## 11. Economic results and sensitivities

### Takeaway
NPV8 is US$714.9 M post-tax and US$1,138.8 M pre-tax; IRR is 44.2% post-tax and 62.7% pre-tax. Steady-state revenue is about US$244.5 M/y in the cash flow (US$254.0–254.3 M in the text and table). Several material inconsistencies exist in production, recovery and revenue; they are flagged below.

### Cited Findings
- **Results (Table 22.5):** pre-tax NPV8 US$1,138.8 M, IRR 62.7%, payback 1.3 yr. Post-tax NPV8 US$714.9 M, IRR 44.2%, payback 1.9 yr. Average EBITDA US$144.6 M. Total cash flow US$2,535.8 M pre-tax and US$1,673.9 M post-tax [p.353 | PDF352]. Table 22.1 gives average EBITDA US$144.4 M and total EBITDA US$2,746.7 M [p.348 | PDF347].
- **Revenue by product, years 2–19 (Table 22.3):** MREC US$175.3 M (68.9%); TiO2 coarse US$47.9 M (18.9%); TiO2 fine US$31.1 M (12.2%); total US$254.3 M. The text says US$254.0 M [p.350 | PDF349].
- **Cash flow, steady-state year (Table 22.6)** [p.357 | PDF356]:

| Line | US$k |
|---|---|
| Gross revenue | 244,521 |
| CFEM | (4,890) |
| Landowner royalty | (2,445) |
| Net revenue | 237,186 |
| Opex, total | (92,818) / (92,502) |
| — Mining | (5,641) |
| — Processing | (80,464) |
| — G&A | (1,500) |
| — Logistics | (5,214) |
| EBITDA | about 144,367–144,684 |
| Sustaining | (2,892) |
| Income tax | about (46,000) |
| Post-tax free cash flow | about 95,500 |

- LOM totals: revenue US$4,662,723k; income tax US$861,907k.
- **LOM production (Table 22.1):** MREC 118,474 dmt; TREO in MREC 83,275 dmt; TiO2 coarse 808,326 dmt; TiO2 fine 912,727 dmt [p.348 | PDF347].
- **Post-tax sensitivities** [p.50 | PDF49; p.355 | PDF354; p.381 | PDF380]:

| Variable | Change | Post-tax NPV8 (US$ M) |
|---|---|---|
| TREO price | −10% / −20% / −30% / −40% | 606.8 / 498.7 / 390.6 / 283.2 |
| TREO price | +30% | 1,039.2 |
| TiO2 price | −30% / +30% | 587.0 / 842.8 |
| REE recovery | −30% / +30% | 391.8 / 1,038.1 |
| TiO2 recovery | −30% / +30% | 596.8 / 833.0 |
| Opex | −30% / +30% | 897.6 / 532.1 |
| Capex | −30% / +30% | 772.2 / 657.5 |

- The figures show ±40% for all variables, but only these values are given in text [p.354–356 | PDF353–355].

### Inferences (DERIVED): key inconsistencies to flag
1. **TREO recovery:**
   - Section 17 gives 67.0%, so 3,636 t/a TREO [p.274–275 | PDF273–274]; Table 1.2 also says "Steady-state REE in product 3,636 tpa" [p.49 | PDF48].
   - The economic model uses 4,367.1 t/a TREO: 4,367.1 / 5,426 = **80.5%**. LOM: 83,275 / 103,463 = 80.5%.
   - This matches the 80% TREO recovery in pit optimization (Table 16.1).
   - At 67% (3,636 t), MREC revenue would be 3,636 × 40.18 = US$146.1 M/y, about US$29 M/y less than modelled.
2. **TiO2 product tonnes vs grade:**
   - 42,390 + 47,865 = 90,255 t equals 68.7% × 131,350 t feed TiO2. So the product tonnages equal recovered *contained TiO2*.
   - Yet the products are sold at a per-tonne-of-concentrate price, and the concentrates are 84.7% and 57.9% TiO2.
   - If the tonnages are concentrate, contained TiO2 is 35,904 + 27,714 = 63,618 t, an overall recovery of only 48.4%.
   - If the tonnages are contained TiO2, physical concentrate tonnes would be 50,047 (coarse) and 82,668 (fine), and revenue at the same prices would be higher.
   - The report does not resolve this.
3. **Coarse TiO2 revenue:** 42,390 × US$900 = US$38.15 M, but Table 22.3 shows US$47.9 M (implied US$1,130/t). The cash flow total 244,521 is consistent with US$900/t: 175.26 + 38.15 + 31.11. So Table 22.3 and the US$254.0–254.3 M text total are inconsistent with the cash flow, by about US$9.8 M.
4. **MREC grade:** 52% (22.1.1) vs implied 70.3% (4,367 / 6,213) vs 95% target and 96.4% "design criteria" (Table 19.1).
5. **Opex labels:** Table 22.1 mislabels opex rows ("Mining US$ M 109.5; Processing US$/t ROM 219.0; G&A US$ M 92.6; Total Site Costs 186.3") [p.348 | PDF347].
6. **Section 22.1.3 closure:** says US$1.8 M "from year 5 to year" (truncated); Section 20/21 say US$1.6 M.

### Gaps
- Pre-tax sensitivity values, IRR sensitivities in numbers, and sensitivities to acid or reagent price specifically: NOT STATED. The figures only show "main reagents" as a category.

---

## 12. Section 25 and 26 risks, uncertainties, recommended testwork and budgets

### Takeaway
The key process risks are untested acid regeneration, Ti hydrolysis, impurity removal and MREC precipitation (no liquor-to-product testwork has been done); co-precipitation and double-sulfate REE losses; high Mg(OH)2 and H2SO4 consumption; fine-tailings filtration; water discharge quality; and product acceptance, including radionuclides. **No budget is given for the metallurgical testwork or the pilot plant.** Budgets are given only for drilling, mining studies and infrastructure studies.

### Cited Findings
- **25.1.1 metallurgy risks** [p.363 | PDF362]:
  1. Leach solution management, fine-TiO2 recovery, impurity management, MREC production and acid regeneration are untested assumptions needing pilot testing.
  2. Solid tailings strategy and dry stacking of fine particles.
  3. Final water discharge quality.
  4. Ore and metallurgical variability across the pits.
  5. Product samples needed for marketing.
- **25.1.2 opportunities** [p.363 | PDF362]:
  - REE recovery: leach optimization; recovering the REE lost to the coarse HCl liquor.
  - Acid reduction: regeneration, better magnetic separation, calcination and bake temperature optimization.
  - Coarse product quality improvements.
  - By-products: Fe-oxide magnetic concentrate and Fe sulphate.
  - Site sulfuric acid plant.
- **25.6.1 risks** [p.370–371 | PDF369–370]:
  - The MREC route has not been demonstrated at pilot scale.
  - Co-precipitation losses during Ti recovery and impurity removal, due to high Fe/Al/Ti/P loading.
  - High Mg(OH)2 demand.
  - High thermal energy and acid demand in the bake.
  - Product specs (95% MREC; TiO2 chlorination suitability) are conceptual.
  - Radionuclide considerations.
- **25.6.2 opportunities** [p.371 | PDF370]: selective double-sulphate precipitation ahead of Ti and impurity removal; liquor recirculation; integration of the acid-regeneration plant.
- **25.11.1 opex risk:** reagent dominance, specifically HCl, H2SO4 and NaOH [p.379 | PDF378].
- **25.13.1 schedule risk:** includes acid recycling testwork cycles [p.382 | PDF381].
- **Recommended testwork (26.1 / 26.5)** [p.384–385 | PDF383–384; p.400 | PDF399]:
  - Validate the downstream hydrometallurgy.
  - Ti concentrate chlorination suitability, penalty impurities and radionuclides.
  - Fe/Al/Ti/P rejection with Nd/Pr/Dy/Tb loss minimization.
  - Quantify REE double-sulphate losses in Ti removal and neutralization.
  - Quantify H2SO4 and Mg(OH)2 consumption and optimize bake thermal conditions.
  - Produce representative MREC to test the 95% purity target.
  - Recover REE from the coarse circuit.
  - H2SO4 regeneration and recirculation testwork.
  - Alternative leach routes.
  - Optimize the coarse/fines size-split point.
  - Ultrafines rejection.
  - Fe-product and sulphate by-products.
  - Alternative product-quality technologies.
  - Dry-stack settling, filtration and rheology.
  - Water discharge treatment.
  - Equipment selection: magnetic, density and electrostatic separation, sizing and desliming.
  - Study a sulphuric acid generation plant.
  - Then a continuous pilot plant.
- **Budgets stated:**

| Program | Cost | Source |
|---|---|---|
| Table 26.5 infill: RC 11,600 m at BRL 400 | BRL 4,640,000 | [p.397 \| PDF396] |
| Table 26.5 infill: twin holes 1,200 m at BRL 900 | BRL 1,080,000 | same |
| Table 26.5 infill: strategic validation 600 m | BRL 540,000 | same |
| Table 26.5 infill: auger 330 m | BRL 92,400 | same |
| Table 26.5 infill: SGS assays 6,349 samples | BRL 1,079,330 | same |
| Table 26.5 infill: QA/QC | BRL 172,720 | same |
| Table 26.5 infill: MLA mineralogy | BRL 250,000 | same |
| Table 26.5 infill: XRD | BRL 250,000 | same |
| Regional exploration (Table 26.6) | BRL 1,042,400 | same |
| Mining Phase 1 (Table 26.8) | US$1.40 M | [p.399 \| PDF398] |
| Mining Phase 2 (Table 26.9) | US$3.15 M | [p.400 \| PDF399] |
| Low-grade stockpile and waste facilities (Table 26.10), made up of geochem US$275k + geotech US$625k + geosynthetics quotes US$200k | US$1.1 M | [p.401–403 \| PDF400–402] |
| Water management (Table 26.10) | US$0.1 M | same |
| Metallurgical testwork / pilot plant | NOT STATED | |

### Inferences (DERIVED)
- Table 26.5 infill total = BRL 8,104,450, about US$1.62 M at BRL 5.00.

### Gaps
- Metallurgical testwork budget, pilot plant budget and PFS cost: NOT STATED.

---

## 13. Mentions of the USA, Texas, Brownsville, export of intermediates, downstream modules

### Takeaway
There is no mention of Texas or Brownsville. The only US link is a non-binding MOU with Rare Earth Technology Inc. (Cincinnati, Ohio) on REE separation and processing. The intermediates are all exported FOB Santos, with REO priced CIF Europe. The report says the TiO2 products are NOT suited to chloride-route pigment, Ti sponge or UGA without further upgrading. This conflicts with Section 17, which calls the coarse product an "upgraded anatase concentrate," and with Sections 25 and 26, which discuss chlorination suitability.

### Cited Findings
- **US MOU:** "confidential Memorandum of Understanding (MOU) in place with Rare Earth Technology Inc. of Cincinnati, Ohio, USA … related to REE separation and processing, including technical analysis and a proposition for an ore beneficiation flowsheet … testing for results to include in a future PFS." It is non-binding, with no terms [p.318 | PDF317].
- **Other US mentions:** OTCQB listing [p.52 | PDF51]; USEPA Method 1313 [p.304 | PDF303]. Texas and Brownsville: NOT MENTIONED (searched).
- **Export:** "Because all MREC and TiO₂ Oxides production will be exported, no taxes will be levied on sales" [p.351 | PDF350]. Pricing is FOB Santos; REO is priced CIF Europe [p.348 | PDF347].
- **TiCl4 and sponge:**
  - "The proposed products are not expected to be suitable for chloride-route pigment production, titanium sponge production, or upgraded anatase concentrate production, without further upgrading, because the particle size is generally finer than preferred and the silica content is higher" [p.315 | PDF314].
  - Products are better aligned with sulphate-route pigment, welding flux, slag and ceramic glaze [p.313 | PDF312].
  - Market context: 9.45 Mt TiO2 feedstock demand in 2025; chloride-route 3.08 Mt; sulphate-route 4.9 Mt [p.313 | PDF312].
  - Contrast: Section 17 calls the coarse product an "upgraded anatase concentrate … suitability as a feedstock for … pigment production, including any required chlorination performance … remain to be confirmed" [p.270 | PDF269]. Section 26.1 recommends evaluating "suitability … for commercial chlorination processes" [p.384 | PDF383].
- **REE separation:** MREC is "suitable for downstream separation and refining" [p.273 | PDF272]. No separation module is in scope. Commercial terms for separation and refining are NOT STATED.
- **Expansion:** a staged expansion to "5 to 10 Mtpa" is to be assessed [p.51 | PDF50].

### Inferences
- For a Brownsville concept, the PEA treats Tiros as a Brazil-sited integrated plant that exports TiO2 concentrates and MREC. Any US-based processing of intermediates would be outside the PEA basis.

### Gaps
- Downstream TiCl4, sponge or REE-separation modules, US logistics and the Santos-to-US freight rate: NOT STATED.

---

## 14. Mineralogy relevant to acid consumption, and fines handling

### Takeaway
The acid consumers are the Fe oxides/oxyhydroxides (magnetite, Ti-magnetite, goethite, limonite, hematite), Al in kaolinite, chlorite and other clays, Mg, and P in crandallite-group phosphates and apatite. These dissolve heavily at 300°C bake conditions (Fe2O3 84%, Al2O3 64%, MgO 68%, P2O5 92% conversion in MET-53). The ore is clay-rich and very fine. Fines handling and filtration are flagged as risks, but no filter-cake moisture is given apart from the 15% dry-stack target.

### Cited Findings
- **BK11 mineralogy (TIMA)** [p.201 | PDF200]:
  - Ti is about 70% anatase and about 9% ilmenite; the rest is in Ti-magnetite (about 15% Ti) and Fe oxides.
  - REE minerals: monazite, Ce oxide, crandallite group, and unidentified alteration REE minerals.
  - Fe minerals: magnetite, Ti-magnetite, goethite, limonite.
  - Abundant clays: chlorite, kaolinite, ferrocarpholite.
  - Anatase P80 50 µm, P50 9–10 µm; REE mineral P80 9–25 µm.
  - Limonite and crandallite-group minerals are concentrated in the –20 µm fraction.
- **Figure 13.5 modal chart** [p.202 | PDF201]: the –20 µm fraction contains notable limonite, kaolinite, crandallite group and quartz. It also lists apatite, carbonates and feldspars. Numeric modal percentages are only shown graphically.
- **Altilium sample:** kaolinite 23%, hematite 16%, anatase 18%, illite-muscovite 12%, quartz 9%, magnetite 6% [p.219 | PDF218].
- **Geology:** REE hosted in crandallite-group phosphates (gorceixite, florencite), monazite/rhabdophane and cerianite; possibly clay-adsorbed [p.88 | PDF87].
- **Acid-consuming conversions (MET-53, 600°C calcine, 300°C bake)** [p.214–215 | PDF213–214]: SiO2 7.94%, Al2O3 64.08%, Fe2O3 84.26%, MgO 68.14%, TiO2 82.93%, P2O5 91.72%, Tr2O3 90.91%.
- **BK19 leach liquor distributions** [p.218 | PDF217]: Fe2O3 38.6% and Al2O3 74.7% of feed report to the liquor, alongside 72.5% TREO and 49.8% TiO2.
- **Composition of the BK09 –20 µm calcine feed (MET-32):** SiO2 27.50, Al2O3 16.70, Fe2O3 28.00, MgO 0.68, TiO2 15.30, P2O5 1.57, Tr2O3 0.663 (%) [p.214 | PDF213].
- **Text on gangue:** "the other minerals present … such as Fe, Al and Ti also react, increasing acid consumption" [p.272 | PDF271].
- **Fines handling:**
  - The trommel scrubber with high-pressure water disperses the clay matrix [p.267 | PDF266].
  - "Efficient solid–liquid separation is critical for maximizing REE recovery" [p.273 | PDF272].
  - Risk: a tailings plan is needed "that can handle fine sized particles" [p.363 | PDF362].
  - Recommendation: dry-stack "settling and filtration and rheological characterization" [p.384 | PDF383].
  - Electrostatic feed must be dry [p.270 | PDF269].
- **Filter-cake moisture:** NOT STATED beyond "low-moisture" and the 15% w/w dry-stack target [p.305 | PDF304].

### Inferences (DERIVED)
- Acid consumed per kg of bake feed in MET-53 is 1.111 kg, against REO at only 0.663% of the feed. This means about 99% of acid demand goes to gangue (Fe, Al, Ti, P, Mg). This is the basis for the "acid split" problem: Fe and Al removal before the bake (magnetics, desliming) gives the biggest acid saving.
- Fe2O3 at 28% and Al2O3 at 16.7% in the bake feed dominate the stoichiometric demand.

### Gaps
- Quantitative modal mineralogy in table form, apatite and carbonate percentages in the plant feed, fines settling and filtration rates, and filter-cake moistures: NOT STATED.
