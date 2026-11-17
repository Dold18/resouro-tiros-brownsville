# Engineering decisions: where should the acid steps happen, and what should Brownsville do?

*Tiros–Brownsville challenge · model v0.6 · 6 November 2026*

> **Final model v1.0 (7 November 2026) is v0.8 with no numeric changes.** **Update, model v0.8 (7 November 2026): three cases, Tiros ore only.** The model now has three cases, and this document keeps its v0.6 names in the sections below. How they map:
> - **Case 1: Brazil** = Option 1 (all in Brazil).
> - **Case 2: Texas** = Option 3 (dry calcine to Texas). Option 2 (wet fines) is still available as a choice in the Case 2 column.
> - **Case 3: MREC processing Texas** = Option 1, then Tiros's own carbonate is separated in Brownsville.
>
> The rare-earth module was simplified (D26) and the hub for other producers' carbonate removed (D27). Sections 6 onward still describe the hub as it was analyzed in v0.5–v0.7; it is no longer part of the project. The report built on this model is in `report/`.

**Bottom line:** keep the sulfuric-acid steps in Brazil. On cost, moving rock to the acid (Texas) loses to moving acid to the rock (Brazil) in every case we tested: small plant or full size, normal or 2026-crisis acid prices, with or without acid recycling. It still loses when we stack every reasonable assumption in Texas's favor (section 5).

The best Brazil set-up is to buy acid at first. Once the plant is at full size, build a sulfur-burning acid plant at Tiros. The PEA itself lists that as an opportunity.

Brownsville's natural role is downstream: a **rare-earth separation module**, Steve's idea, now in the model (section 6).
- **Tiros alone is too small for it.** Separating only Tiros's own carbonate never pays, at any size or price we tested. Tiros's rare earths are mostly light, so separation adds about US$7–13 per kg, roughly what it costs.
- **As a hub it can pay.** A Brownsville plant pays only if it also separates other producers' carbonate for a fee, with the government support every comparable US plant has had. Stage 2 (full separation) for Tiros plus 4,000 t/yr of other producers' oxide is worth about **US$102M**. It needs them to pay about US$17/kg, near the top of what light-rich Brazilian producers would accept.
- **So Brownsville is a partnership business.** It is not a step in the Tiros process.

If Resouro still wants the acid steps in Texas for strategic reasons, a better split than shipping wet fines is to **roast the fines in Brazil and ship the dry calcine**. It ships about 23% fewer tonnes, needs no dryer, and avoids most of the risk of the cargo turning to slurry at sea. In both Texas options, everything from the sulfuric-acid bake onward happens in Brownsville.

This document explains every choice in `model/Tiros_Brownsville_Model.xlsx`, so the team can defend it and Steve can challenge it.
- **Page numbers** refer to the printed pages of the **NI 43-101 Technical Report and Preliminary Economic Assessment (PEA)** for Tiros (Norda Stelo, July 2026), our primary source.
- **Supporting research** is in `docs/research/`.
- **Money** is shown in US$ millions (US$564M), and unit rates in US$ per tonne (see `docs/style-guide.md`).

---

## 1. The answer in numbers

The table shows net present value (NPV) before tax, in US$ millions: today's value of all future profit, minus the build cost. Higher is better.

| # | What happens | Small plant (5,000 t/month), normal prices | Small plant, 2026 crisis prices | Full size (41,667 t/month), normal prices | Full size, 2026 crisis prices |
|---|---|---|---|---|---|
| **1** | **All in Brazil, buy acid (the PEA layout)** | **19** | **−38** | **564** | **87** |
| 2 | Wet fines to Texas (Steve's split) | −91 | −140 | 1 | −412 |
| 3 | Dry calcine to Texas (alternative split) | −70 | −120 | 152 | −261 |
| – | *All in Brazil with its own sulfur-burning acid plant (v0.5 only)* | *20* | *−30* | *656* | *245* |

Crisis prices: acid US$430/t at Tiros and US$400/t at Brownsville. The model shows both price sets side by side (Model, section E; Summary). The last row comes from model v0.5. The own-acid-plant option was taken out of the model in v0.6 to keep it simple (D25), but the finding stands: at full size, an acid plant at Tiros is worth even more than buying acid.

**What happens where in the two Texas options:**

| Step | Option 2: wet fines | Option 3: dry calcine |
|---|---|---|
| Mine, washing, coarse circuit (hydrochloric-acid leach) | Brazil | Brazil |
| Fines kiln (600 °C) and dry magnetic separation | **Texas** | Brazil |
| Sulfuric-acid bake (300 °C) and water leach | **Texas** | **Texas** |
| Impurity removal, fine TiO₂ hydrolysis, carbonate (MREC) precipitation | **Texas** | **Texas** |

We dropped shipping raw ore to Texas in v0.4 (it lost in every case) and moved the own-acid-plant option out of the model in v0.6.

**How to read it:**

- **All in Brazil always wins.** At full size, an own sulfur-burning acid plant at Tiros would add about US$92M of value at normal prices and about US$158M at crisis prices (v0.5). At the brief's size it only ties with buying acid.
- **Option 3 is always the best Texas option.** It beats Steve's wet-fines split by about US$20M at the small size and US$150M at full size.
- **Texas does not lose because of acid.** It loses because of:
  - a second site with US wages and overheads,
  - shipping more than a tonne and a half of material per tonne of acid saved,
  - paying to dispose in Texas of the roughly 80% of that material that becomes waste.
- **What it would take for Texas to break even.** Buyers would have to pay about **30% more** for US-processed rare earths for Option 3 to match Option 1 at full size, or **53% more** at the small size.

**Check on the model:** with the PEA's own settings (80.5% rare-earth recovery, US$420/t caustic soda, full size):
- **Revenue:** the model gives US$244.8M/yr, against the PEA's US$244.5M (p.357).
- **Pre-tax NPV:** the model gives US$985M, against the PEA's US$1,139M (p.353).

The NPV gap comes from our simpler cash flow: no ramp-up year and no working capital, plus a few cost lines we treat differently (section 4). We do not need to match the PEA's NPV. We need a fair comparison between options, and every option uses the same assumptions.

---

## 2. The three questions we were asked to test

### 2.1 Is it cheaper to move the rock to the acid, or the acid to the rock?

The acid to the rock, by a wide margin. The deciding fact is how many tonnes must cross the ocean for each tonne of acid the process uses:

| What crosses the ocean | Tonnes per tonne of acid used |
|---|---|
| Wet fines to Texas (dried to 10% moisture) | 2.11 |
| Dry calcine to Texas | 1.62 |
| Acid to Brazil | 1.00 |
| **Sulfur to Brazil, made into acid there** | **0.32** |

Each tonne of sulfur makes about 3 tonnes of acid, and sulfur is a dry, stable, easy bulk cargo. Brazil already imports over 2 million tonnes a year of it for fertilizer.

**What the shipping costs, per tonne of acid:**
- **Dry calcine to Texas:** about US$85 per tonne shipped (truck to port, port fees, bulk freight, Brownsville handling). That is about US$140 per tonne of acid avoided.
- **Sulfur to Brazil:** about US$25–35 per tonne of acid.

Texas's cheaper Gulf Coast sulfur saves only about US$30–40 per tonne of acid, so it cannot cover the extra freight. Section 5.1 sets out the numbers.

This tonnage comparison counts acid only. Brazil must also bring in caustic soda (about 0.55 t per tonne of acid) and send its products out, while a Texas plant buys caustic soda locally. Counting those, the tonnage gap narrows (see the research summary, section on tonnage). The spreadsheet already includes both through delivered prices and product logistics, and the Texas options still cost more.

**The 2026 price shock makes the case for Brazil stronger, not weaker.**
- The Strait of Hormuz closed in late February 2026, and Russia and Kazakhstan restricted sulfur exports. Delivered acid at Tiros is now about US$430/t, against US$170/t in the PEA.
- A sulfur-burning plant at Tiros would cut that to about US$345/t, including its build cost.
- Texas acid is also expensive now (about US$400/t delivered to Brownsville), because acid prices everywhere follow sulfur.

### 2.2 What waste would end up in Texas?

**About 80% of whatever is shipped stays in Texas as waste.** For Option 3 at full size that is about 250,000 t/yr of solid residue, mostly silica and iron/aluminum cake. At the small size it is about 30,000 t/yr.

**Correction to our earlier thinking: there is very little gypsum.** The PEA deliberately uses magnesium hydroxide rather than lime "to avoid gypsum formation" (p.371). The real Texas waste problem is **wastewater**:

- **Where it comes from:** the caustic soda (sodium hydroxide) that neutralizes the acid liquor turns into dissolved **sodium sulfate**. That is about 1.8 t per tonne of caustic soda, or about **178,000 t/yr at full size**.
- **Why it matters:** a wastewater permit is what stopped Lynas's rare-earth plant at Seadrift, Texas.
  - That plant had up to US$258M of Department of Defense funding.
  - It stalled through 2025 on "unresolved wastewater disposal permit issues".
  - Lynas's August 2026 annual report says it "will no longer proceed".
- **Not costed:** the PEA does not cost wastewater treatment at all ("needs definition", p.363). The model has an input for it, set to zero, so the team can test it.

**Radioactivity (thorium and uranium).** The PEA gives no thorium or uranium assays; it calls them "under evaluation" (p.376). What matters is which streams they end up in:

- In Texas, material with 0.05% or more uranium plus thorium by weight is "source material". Processing it needs a licence from the Texas Commission on Environmental Quality (TCEQ).
- Residue below about 30 picocuries per gram of radium (pCi/g) is exempt as naturally occurring radioactive material (NORM).
- The only licensed radioactive-waste site in Texas is in Andrews County, about 1,000 km from Brownsville, with no public prices.
- The model includes an input for the share of residue needing that disposal, set to 0% until assays exist.

**Permitting time:** about 12–18 months in Texas if uncontested. With radioactive licensing and contested hearings, 24–36+ months.

**Local context:** Brownsville has active environmental-justice opposition; federal approvals for two LNG terminals were overturned in 2024. It also has water shortages, with reservoirs at 22% in 2024.

### 2.3 Can fine, clay-rich material even be shipped?

Yes, but wet fines are the hardest and riskiest option.

**Wet fines (Option 2)**
- **Liquefaction:** damp, fine cargo can liquefy in a ship's hold and capsize the ship. Liquefaction caused 70 of 104 bulk-carrier crew deaths in 2013–2022.
- **Rules:** under the International Maritime Solid Bulk Cargoes Code, untested fines must be treated as a "Group A" cargo that may liquefy. They need a lab test and a moisture certificate before every loading.
- **Drying:** clay-rich fines come off a pressure filter at about 25% moisture. We assume they must be dried to 10% before shipping; the real limit needs a lab test.
- **In the model:** the cost of removing about 0.22 t of water per tonne of fines. The dryer's build cost is part of the Texas site extras (D17).

**Dry calcine (Option 3)**
- **Why it is dry:** the fines are already roasted at 600 °C in the PEA flowsheet, before the acid bake (p.272). Moving the split to after the kiln means the material leaves Brazil dry.
- **Advantages:** no dryer, much lower liquefaction risk, and about 15% less mass to ship, because the magnetic iron minerals stay in Brazil.
- **Handling:** it is a dusty powder, so it needs covered handling.
- **Containers versus bulk:** the model assumes bulk shipping. Bags in containers would cost about US$100/t more. That would drop Option 3 below Option 2 at the small size, so bulk shipping is what makes it the better split.

**Tariffs.**
- The July 2026 25% US tariff on Brazilian goods exempts titanium ores and concentrates and rare-earth minerals.
- A separate 12.5% tariff from 24 July 2026 was not checked.
- A shipped intermediate might not count as an exempt "ore or concentrate". **This needs a customs broker's opinion before any Texas option goes further.**

---

## 3. Decision log

Each entry gives the decision, why we made it, and what would change it. Every input in the model also carries one of the three labels the challenge brief asks for:
- *Known:* from the PEA, or a published fact.
- *Assumption:* our planning choice, often from a researched range.
- *Needs testing:* depends on testing not yet done.

**D1 – Same ore basis for every option.**
- **Decision:** all three options process the same ore, 5,000 t/month by default, from the challenge brief. *(Assumption)*
- **Why:** only the location of the work changes, so the comparison is fair.
- **To see full size:** set *Ore fed to the process* on Inputs to 41,667 t/month, and raise the staff numbers on the Model tab (we used 116 for an all-Brazil plant, from p.346).
- **Would change if:** the Brownsville plan defines 5,000 t/month as something other than ore, for example concentrate.

**D2 – Mass split from the BK19 bench test.**
- **Decision:** *(Needs testing)*
  - 71.1% is fines (the rest, 28.9%, goes to the coarse circuit).
  - 60.0% is left as dry calcine after roasting and magnetic clean-up.
- **Why:** the PEA does not publish its plant mass balance. BK19 (Table 13.17, p.217) is the only full-circuit balance in the report.
- **Would change if:** we receive the METSIM mass balance after the NDA.

**D3 – Rare-earth recovery 67%, not 80.5%.**
- **Decision:** 67% of the rare earths reach the carbonate product. *(Needs testing)*
- **Why:**
  - 67% is the process-design figure (p.274–275).
  - The PEA's economic model quietly uses 80.5% (p.349), which adds about US$29M/yr of revenue at full size.
  - The liquor-to-product steps have never been tested (p.360), so we use the lower figure. It affects every option equally.
- **Would change if:** testwork confirms more.

**D4 – Titanium products as the PEA's economic model uses them.**
- **Decision:** 42,390 t/yr coarse product at US$900/t and 47,865 t/yr fine product at US$650/t, at full size. *(Known)*
- **Why:** these tonnages equal exactly 68.7% of the titanium dioxide in the ore. That suggests they are *contained* titanium dioxide, but they are priced per tonne of concentrate. We follow the PEA's own revenue calculation and flag the ambiguity (section 4).
- **Would change if:** Resouro clarifies the basis.

**D5 – Acid: the PEA's design figure, 0.374 t per tonne of ore.**
- **Decision:** 186,986 t/yr of 96% acid at 500,000 t/yr (p.276). *(Needs testing)*
- **Why:** it already assumes about 22% of the acid is recycled. Test MET-53 used 459 kg per tonne of ore before recycling (p.214), and regeneration is "conceptual and untested" (p.272). With no recycling, running cost rises about US$18/t ore. The ranking does not change. (Until v0.5 the model had separate raw-acid and recycling inputs.)
- **Would change if:** regeneration testwork succeeds or fails.

**D6 – Caustic soda at US$560/t delivered to Tiros, not the PEA's US$420.**
- **Decision:** *(Assumption)*
- **Why:**
  - US$420/t matches a US Gulf port price *before* ocean freight, import duty and about 800 km of trucking.
  - Brazil imports most of its caustic soda from the US Gulf, and research puts delivered Tiros at US$550–700/t.
  - Caustic soda is the PEA's largest cost line (US$43.1M/yr).
  - Brownsville is set at US$520/t, because Texas makes most US caustic soda.
- **Would change if:** Resouro has supplier quotes.

**D7 – Normal-year and 2026-crisis acid prices, side by side.**
- **Decision:** four acid prices: normal year (US$170/t at Tiros, the PEA's; US$175/t at Brownsville) and 2026 crisis (US$430 and US$400). The model and Summary show the value of every option at both. *(Normal Tiros price: Known; the rest: Assumption)*
- **Why:** Steve raised the Strait of Hormuz and Russia. Acid swung from about US$155 to US$400/t on the US Gulf within three months of 2026. Until v0.5 a switch held eight acid and sulfur prices; four inputs, shown side by side, do the same job without a switch. The crisis hurts every option and widens Brazil's lead (section 1).

**D8 – Proposed split: after the kiln (Option 3), not before it (Option 2).**
- **Why:** see section 2.3. Less tonnage, no dryer, much lower liquefaction risk, and iron rejected in Brazil.
- **Note:** this is only the best *Texas* option. The all-Brazil option beats it.

**D9 – Sulfur-burning acid plant scaled from a real 2025 project (v0.5 only).**
- **Decision:** *(Assumption)*
  - US$55M for 450 t/day, based on Marimaca, Chile (2025), scaled with the six-tenths rule.
  - Running cost US$20/t of acid, with a US$10/t steam/power credit.
- **Why:** at 5,000 t/month the plant would make only about 64 t/day. That is far below where vendors normally build, so its cost is uncertain. **We only recommend it at full size (about 545 t/day).**

**D10 – Build cost split by area.**
- **Decision:** the PEA gives US$191.2M (p.332) but not by process area. We assume 45% is the fines chemical (acid) circuit, the part that can move to Texas. The other 55% (site works ~30%, coarse circuit ~25%) always stays at Tiros. *(Assumption)*
- **Other assumptions:**
  - Smaller plants scale with the six-tenths rule.
  - US construction costs 1.15× Brazil. The PEA's cost already includes about 17% Brazilian taxes, Texas exempts manufacturing equipment from sales tax, and US labor costs more; net about 1.0–1.2×, so we use 1.15. (v0.3 used 1.35×, which was too high.)
  - In Option 3 the fines kiln really stays in Brazil, but the model prices the whole fines circuit at the US factor. This slightly overstates Option 3's build cost, by under US$1M at the small size.
  - A Brownsville site adds US$43M at PEA size: half of Brazil's site works at US cost, plus about US$10M to receive imported material and to dry or bag it in Brazil (D17).
- **Would change if:** an area breakdown arrives with the economic model.

**D11 – Staff.**
- **Decision:** cost per employee is about US$20,700/yr in Brazil (*Known*, p.346) and US$95,000/yr fully loaded in Texas (*Assumption*).
- **Headcounts:** a 5,000 t/month plant needs about 60 people on one site. A two-site split needs about 78 people in total.
- **Why it matters:** this is one of the biggest reasons the Texas options cost more. The team should check it with an operator.

**D15 – One power price.**
- **Decision:** all power is priced at the PEA's 8.6 ¢/kWh, at both sites. *(Known)*
- **Why:** Texas power is cheaper (6.4 ¢/kWh, US Energy Information Administration, 2025). But the acid circuit uses only about 19% of the plant's power (PEA Table 18.1), so the difference is about US$12,000/yr at 5,000 t/month. Removed in v0.5 to keep the model simple.

**D16 – Raw ore to Texas dropped.**
- **Decision:** removed in v0.4.
- **Why:** it is not realistic. It ships about 3.3 t of ore, much of it water and waste, per tonne of acid, and was last in every case.

**D17 – Fewer guesses (v0.5).** Factors that were placeholders, or that barely moved the answer, were merged or removed so a reader has fewer numbers to trust:
- **Shipping:** truck, Brazilian port, sea freight and Brownsville handling are now one input, US$85/t. Only bulk shipping is modeled.
- **Texas site extras:** Brownsville site works, receiving equipment and drying or bagging are now one input, US$43M at PEA size, scaled with plant size.
- **Delivery from Brownsville:** products made there are sold at the port next to the plant, so no delivery cost is added.
- **Power:** one price for both sites (D15).

At 5,000 t/month this improves the Texas options by about US$8M, mostly because the merged site cost now scales with plant size. No ranking changes.

**D25 – A shorter model (v0.6).** The model went from 99 inputs to 51 (53 once the two crisis acid prices were added back as a side-by-side column) and to about one page per tab. Nothing that changes the answer was removed.

| Removed or merged | Why | What it would show |
|---|---|---|
| Own-acid-plant option (and its 9 sulfur, acid-plant and price inputs) | At the brief's size it ties with buying acid, and it is a Brazil-only refinement, not part of the Brazil-versus-Texas question | +US$92M at full size (v0.5); kept in section 1 and D9 |
| Acid and sulfur price switch (12 inputs) | Four acid prices (normal and crisis, side by side) do the job | Nothing: both price sets are shown |
| Raw acid use and recycling (2 inputs) | Replaced by the PEA's design figure | No recycling: about −US$10M per option |
| Mining, power, maintenance and minor reagents (6 inputs, 4 lines) | The same in every option, so one line, US$27.50/t ore | No change |
| Coarse share, calcine moisture, cake moisture | Folded into the fines share, "calcine ships dry" and one drying cost | Under US$0.5M |
| Radioactive-waste share and cost, wastewater cost | Both were set to zero, so they did nothing | Kept as questions and tests; −US$26.5M and −US$21M if real |
| US price premium | Zero; the Summary's break-even line does the job | No change |
| Separate site-works and coarse-circuit shares | Only the acid-circuit share matters for the Brazil/Texas split | No change |
| Rare-earth module: ten elements → five groups | Only NdPr, dysprosium and terbium differ by price case | No change |
| Rare-earth module: four price cases → two | China-market and US-floor cases sat between the other two | Kept in research note 6 |
| Rare-earth module: grants and 45X credit (3 inputs) → one support share | Simpler; same total | Stage 1 for Tiros alone is US$11M better than in v0.5, mainly from the new Stage 1 cost basis (D21) |

Earlier versions are in the GitHub history.

**D26 – Three cases and a simpler rare-earth module (v0.7).**
- **Decision:** the model is now three cases side by side: Brazil, Texas (dry calcine), and MREC processing Texas. The separation plant is one full-separation plant, shown for Tiros alone and as a hub; the hub column feeds Case 3. *(Team decision, 7 Nov 2026)*
- **Why:** the separation plant is a supporting part of the project, and its value rests on other producers, fees and grants that no one has offered. A short tab keeps the finding without inviting readers to extrapolate from it. Putting it in the same table as the other two cases lets one Summary compare all three.
- **What changed:** Stage 1 (first-cut plant) and its 5 inputs removed; the Hub charts tab (5 charts) replaced by two sensitivity tables and charts on the MREC Texas tab; one input added for shipping carbonate to Brownsville (US$185/t, bagged in containers). Inputs: 53 → 49.
- **Numbers:** Cases 1 and 2 are unchanged (US$19.0M and −US$70.1M). Case 3 is US$119.8M = Case 1 + the hub (US$101.9M) − carbonate freight (US$1.1M). Separating Tiros's carbonate alone with full separation is worth −US$91.5M.
- **Would change if:** Resouro wants the first-cut plant back in, or a separator offers terms for Tiros carbonate.

**D27 – No hub: Tiros ore only, and a scaling table (v0.8).**
- **Decision:** the model considers only Tiros ore. The idea of a Brownsville plant separating other producers' carbonate for a fee is removed; Case 3 now separates Tiros's own carbonate. A new section F on the Model tab shows each case's value at other Tiros ore rates (5,000 to 41,667 t/month, editable). *(Team decision, 7 Nov 2026: the hub is not what the challenge asks for.)*
- **Numbers at 5,000 t/month:** Case 3 is −US$73.6M (Case 1 + separation plant −US$91.5M − carbonate freight US$1.1M). At the PEA's full size, Case 1 is US$575M, Case 2 US$188M and Case 3 US$431M; Case 3 trails Case 1 at every size.
- **How the scaling works:** costs and revenue that grow with ore are scaled in step; staff and site overheads stay fixed; build cost follows the six-tenths rule. It reproduces full model reruns exactly (checked at 20,000 and 41,667 t/month). Staff held fixed flatters large sizes slightly (the PEA has 116 staff at full size: Case 1 US$564M).
- **What changed:** input `Fee_toll` removed (49 → 48); the MREC Texas tab is one column; Summary shows the scaling table and chart instead of the hub.

**D12 – Before-tax value, simple cash flow.**
- **Decision:** build cost in year 0, the same margin each year for 20 years, discounted at 8% (the PEA's rate).
- **Why:** before tax, because Brazil and the US tax differently. Keeping tax out avoids hiding a location effect inside a tax assumption. Section 5.3 gives a rough after-tax check; it does not change the ranking.
- **Would change if:** the comparison is close enough for tax to tip it.

**D13 – Same product prices and royalties everywhere.**
- **Decision:** Brazil's royalties (federal mining royalty 2% plus landowner 1%) apply in every option, since the ore is mined in Brazil. Product prices are the PEA's in every option.
- **US premium:** no buyer has offered one, so none is in the model. The Summary shows the premium a Texas option would need to break even.

**D14 – Waste disposal costs.**
- **Brazil:** dry stack at US$3/t, the PEA's unit rate (p.344). The PEA's US$6M/yr allowance is based on 2.0 Mt/yr, which is more than the plant makes, so we apply the unit rate to actual tonnes. *(Known)*
- **Texas:** non-hazardous landfill at US$45/t including haul. No current price was found. *(Assumption)*
- **Radioactive disposal:** not in the model until assays exist. If 20% of the Texas residue needed it at about US$500/t, the Texas options would fall about US$26.5M further behind.

---

## 4. Problems we found in the PEA

These are worth raising politely with Steve. None of them changes our ranking, but some change the absolute numbers.

1. **Rare-earth recovery.** Section 17 says 67% (3,636 t/yr). The economic model uses 80.5% (4,367 t/yr). That difference is worth about US$29M/yr.
2. **Titanium product basis.** 42,390 + 47,865 t equals exactly 68.7% of the titanium dioxide in the ore, so these look like *contained* titanium dioxide, yet they are priced per tonne of concentrate. If they are concentrate tonnes, overall titanium recovery is only about 48%.
3. **Coarse product revenue.** Table 22.3 implies US$1,130/t, but the cash flow uses US$900/t.
4. **Carbonate grade.** It is stated as 52%, 70%, 95% and 96.4% in different places.
5. **Build cost tables.** They do not add up:
   - US$109.6M + US$30.8M + US$36.6M = US$177M, not US$191.2M.
   - Contingency is given as US$31.6M, US$35.1M and US$36.6M in different places.
6. **Acid regeneration.** It is untested, and the regeneration temperature is given as 600 °C in the text and 680 °C in the figures. The press release mentioned an acid-consumption correction, but the report itself contains only one acid figure.
7. **Caustic soda use.** 205 kg per tonne of ore is large for titanium hydrolysis alone, and its basis is not explained. Our research arithmetic suggests that neutralizing the unreacted acid alone would take about 80% of that caustic soda. If the same unreacted acid is also counted as regenerated, the PEA may be counting it twice.
8. **Water treatment and radioactivity.** Neither is costed.

---

## 5. Could Brownsville still make financial sense?

*Sections 5.1–5.3 were run on model v0.5, which still had the acid-plant option and the acid and sulfur price cases. The v0.6 model gives the same answers within about US$3M.*

**Short answer:** not on processing cost, even when everything reasonable goes Texas's way. Texas only closes the gap with a meaningful price premium or ongoing government support tied to US processing. Most US support so far is aimed at non-Chinese supply wherever it is processed, including in Brazil.

### 5.1 "Isn't acid cheaper in Texas?" Partly yes, and it is not enough.

The intuition is right about **sulfur** and about the **2026 crisis**:
- Gulf Coast refineries make most US sulfur, so Brownsville pays roughly half what Tiros pays for it in a normal year.
- Texas avoids Brazil's dependence on imported sulfur and acid.

It is close to wrong about **bought acid in a normal year**: the PEA's US$170/t at Tiros is about the same as our US$175/t at Brownsville.

Per tonne of acid (100% basis), from the model's inputs:

| | Tiros (Brazil) | Brownsville (Texas) | Texas saving |
|---|---|---|---|
| Buy acid, normal year | US$170 | US$175 | about US$0 (Texas up to US$45 cheaper if Tiros really pays US$220) |
| Buy acid, 2026 crisis | US$430 | US$400 | US$30 |
| Make from sulfur, normal year | US$90 + plant | US$50 + plant | US$40 |
| Make from sulfur, 2026 crisis | US$323 + plant | US$293 + plant | US$30 |

**The fair comparison is make-versus-make, not Texas-make versus Brazil-buy.** Brazil can build the same sulfur-burning plant and import the same Gulf sulfur for about US$26–33/t of freight, which is about US$10 per tonne of acid. At full size the plant uses about 180,000 t/yr of acid, so Texas's acid advantage is worth roughly **US$5–8M per year**.

**What it costs to use that cheaper acid.** Moving calcine to Brownsville costs about **US$138 per tonne of acid**. Disposing of the residue in Texas adds about **US$59 per tonne**. So Texas would need acid about US$200/t cheaper than Brazil, close to free, just to break even on those two items.

### 5.2 Where the Texas option loses money

Option 3 (dry calcine) against Option 1 (all in Brazil), at full size and normal prices:

| Item | Extra cost per year for Texas |
|---|---|
| Shipping calcine to Brownsville | US$25.8M |
| Waste disposal in Texas | US$11.1M |
| Staff (second crew, US wages) | US$5.3M |
| Second site overheads | US$1.0M |
| Acid | US$0.9M |
| Caustic soda (cheaper in Texas) | −US$4.1M |
| Getting products to market (no inland haul in Texas) | −US$2.8M |
| Waste disposal in Brazil (less waste left there) | −US$0.7M |
| **Running cost, net** | **US$36.5M** |
| **Extra build cost** (US premium on the chemical circuit, plus the Brownsville site) | **US$55.9M once** |

Together these come to about US$414M of NPV. Acid is a rounding error in that list. Shipping and Texas waste make up over 80% of the extra running costs.

### 5.3 Stacking every reasonable assumption in Texas's favor

We changed the model one step at a time, keeping each change, at full size:

| Step | Change, kept from step to step | Option 1 | Own acid plant | Option 3 |
|---|---|---|---|---|
| 0 | Base case, normal prices | US$564M | US$656M | US$150M |
| 1 | 2026 crisis prices | US$86.8M | US$245M | −US$263M |
| 2 | Texas makes its own acid from Gulf sulfur | same | same | −US$116M |
| 3 | Residue stored on site in Texas at US$8/t, not landfilled at US$45/t | same | same | −US$26.1M |
| 4 | Cheap return-trip sea freight: shipping US$73/t instead of US$85/t | same | same | US$9.6M |
| 5 | 55 Texas staff at US$80,000 | same | same | US$27.0M |
| 6 | Steps 2–5 at normal prices | US$564M | US$656M | US$456M |

The base case already uses a US build factor of 1.15×, so that is no longer a separate step.

Option 1 = all in Brazil, buying acid · Own acid plant = all in Brazil with a sulfur-burning acid plant · Option 3 = dry calcine to Texas.

**Result:** even with every lever pulled, Texas trails Option 1 by about US$108M and the own-acid-plant case by about US$200M. Closing that would need buyers to pay about **8–14% more** for rare earths processed in the US.

At the brief's 5,000 t/month, all levers together (at crisis prices) still leave Texas about US$51–59M behind Brazil. A full capital grant would not fix it, because the running-cost gap alone is about US$74M of NPV.

### 5.4 Factors outside the model, both ways

| Factor | Helps Texas? | What we found |
|---|---|---|
| Lower US corporate tax (21% federal vs 34% in Brazil) | Somewhat | A rough after-tax check of the best Texas case gives about US$326M for Option 3 against about US$389M for the own-acid-plant case and US$339M for Option 1. Brazil still wins. |
| US tax credit for critical-mineral processing (Section 45X) | Not for this plant | It pays 10% of production costs, but only for products purified to about 99%: separated rare-earth oxides or 99% titanium. A mixed carbonate or a 58% TiO₂ product does not qualify. The credit also phases out from 2031 and ends after 2033. It would support a US *separation* plant, our recommended Brownsville role (section 6). |
| US price floors | Possibly, later | The Department of Defense guaranteed MP Materials US$110/kg for NdPr products for 10 years (July 2025). In 2026 the US proposed price floors through trade agreements (Section 232 proclamation, 14 Jan 2026; Vice President's announcement, 4 Feb 2026). These are aimed at non-Chinese supply generally, and no floor for mixed carbonate exists. |
| US government funding | Not necessarily | US money is also going to Brazilian processing: the US development bank (DFC) is lending Serra Verde in Goiás roughly US$465–565M (reports differ). Aclara plans a US separation plant fed by Brazilian concentrate, which is the same split we recommend. |
| Cheap natural gas for the kiln | Slightly, Option 2 only | The PEA burns LPG at US$1,449/t. Natural gas in Texas could save about US$1.9M/yr at full size, but only if the kiln is in Texas. |
| Acid supply security | Somewhat | Brazil imports all its sulfur; Texas makes its own. A sulfur stockpile plus an acid plant at Tiros largely removes this risk. Sulfur stores easily for months. |
| Brazil's policy on domestic processing | Hurts Texas | President Lula has said domestic processing is a condition of any US minerals deal. Exporting thorium-bearing fines or calcine may face Brazilian resistance, plus nuclear-regulator (CNEN) rules. |
| Texas wastewater permit, flooding, hurricanes, water | Hurts Texas | See section 2.2. Lynas's Seadrift plant was cancelled. |

### 5.5 What would genuinely change our recommendation

1. **A contract paying 15% or more extra for carbonate made in the US**, or a US price floor for mixed rare earths processed in the US.
2. **A Brazilian ban or tax on exporting finished rare-earth products, but not intermediates.** We have seen no sign of this; the current pressure runs the other way.
3. **Resouro's own reasons in the Brownsville plan.** For example, Brownsville may be a pilot or demonstration plant, judged on what it proves rather than on NPV.

---

## 6. The Brownsville rare-earth module

**Short answer:** Steve is right that the rare earths are where Tiros makes its money: about 70% of the PEA's revenue. But the money in *separating* them in Brownsville comes from separating other producers' carbonate as a hub, not from Tiros's own.
- **Tiros alone is too small for it.** Separating only Tiros's carbonate loses money in every case we tested, at the brief's size and at full PEA size, under all four price cases. Tiros's rare earths are mostly light, so separating them adds only about US$7–13 per kg, roughly what separation costs to run.
- **As a hub it can pay.** A Brownsville plant that also processes other producers' carbonate for a fee can be worth around US$100M, but it depends on three things:
  - how much carbonate other producers send,
  - the fee they will accept,
  - government grants.
- **It is a partnership business,** not a step in the Tiros process. It does not change the Tiros flowsheet, and it pairs with Option 1.

The numbers are on the model's **RE module** tab. Sources are in `docs/research/06-rare-earth-module.md`.

**How to read the RE module tab.** It has three parts. Five lines carry the story:

| Where | Line | What it tells you |
|---|---|---|
| Part 1 | *Extra from Stage 1 / Stage 2, per kg of Tiros oxide* | How much more a kilogram of Tiros rare earths earns separated than sold as carbonate: about US$10–13 at PEA prices. |
| Part 2 | *Running cost per kg processed* | What separating costs per kilogram. When it is close to or above the line above, separating Tiros's own carbonate cannot pay. |
| Part 2 | *Net present value at PEA prices* | The bottom line for each set-up. Negative for Tiros alone; positive only for the Stage 2 hub. |
| Part 2 | *Toll fee needed to break even* | The fee other producers must pay. Compare it with what they gain by tolling: about US$6–11/kg (Stage 1) or US$10–19/kg (Stage 2) for a light-rich Brazilian carbonate. |
| Part 2 | *Net present value at outside-China prices* | Barely differs from PEA prices. The heavy-rare-earth premium outside China does not rescue the module, because Tiros has little dysprosium or terbium. |

The levers are the two sand rows in Part 2 (other producers' feed, staff) and Inputs section 9 (fees, costs, support).

**The Hub charts tab** turns this into five pictures, each with a note on what to look for:
1. **Income vs cost per kg processed.** Tiros alone costs about US$22/kg against US$10/kg of income; a Stage 2 hub earns about US$19/kg against about US$17/kg of cost.
2. **Hub value vs other producers' feed.** The Stage 2 hub breaks even at about 2,500 t/yr of other producers' oxide; the Stage 1 hub at about 6,500 t/yr.
3. **Hub value vs toll fee.** Break-even at about US$11/kg (Stage 1) and US$17/kg (Stage 2).
4. **Where the value of a kilogram sits.** NdPr dominates at both price levels.
5. **What moves the Stage 2 hub most.** The fee, the feed and the running cost each swing it by US$250–400M; build cost and support by about US$100M; recovery barely at all.

### 6.1 What the module does

The mixed rare-earth carbonate (MREC) is a *middling* product: all the rare earths together, in one powder. Buyers pay only about **70% of the value** of the rare earths it contains (PEA p.316), because someone else still has to separate them.

Separation uses *solvent extraction*: many stages of mixing a rare-earth solution with an organic liquid that picks up some elements more than others. We model it in two stages:

| Stage | What it does | Products |
|---|---|---|
| **Stage 1: first cut** | Dissolves the carbonate, then makes two cuts: light from heavy, and lanthanum–cerium from NdPr | NdPr oxide (for magnet makers); a lanthanum–cerium product; a **heavy concentrate** (samarium and heavier), sold to heavy separators |
| **Stage 2: full separation** | Adds the many extra steps that split the heavy concentrate | Separate oxides of every rare earth, including dysprosium and terbium |
| **Stage 3: metal and magnets** | With partners; not costed | NdPr metal and magnets |

**A correction to the idea as first stated:** a light/heavy split alone leaves a mixed light product that magnet makers cannot use. They need NdPr oxide. So Stage 1 also removes lanthanum and cerium. That is the standard first plant, as in Ucore's Louisiana Production Line 1 and Rainbow's South African design.

### 6.2 Does it change the Tiros process?

**No, apart from one quality question.**
- Tiros still makes the carbonate in Brazil, exactly as in Option 1. Brownsville receives about 620 t/yr of carbonate at the brief's size, or about 5,200 t/yr at full size. That is a small, dry, high-value cargo, likely covered by the tariff exemption for rare-earth minerals.
- **The quality question:** separation plants want a clean carbonate. Aclara, for example, feeds its US plant with a "super pure" carbonate. Tiros's carbonate purity, and its thorium and uranium content, have not been tested.

### 6.3 What one kilogram of Tiros rare-earth oxide is worth

The PEA does not publish the carbonate's element make-up. We built one from its assays:
- **Light elements:** BK19 gives the lanthanum, cerium, neodymium and praseodymium (p.197–199).
- **Heavy share:** BK09 gives about 4% heavy rare earths (p.192).
- **Magnet share:** the resource says magnet oxides are 27% of the total (p.44).
- **Dysprosium and terbium:** chosen so NdPr + Dy + Tb carries the PEA's own magnet value, US$48.9/kg against the PEA's US$48.2/kg (p.348). *(Needs testing)*

| US$ per kg of Tiros oxide | PEA long-term prices | Outside-China prices, Oct 2026 |
|---|---|---|
| Whole basket | 51.5 | 46.5 |
| of which NdPr | 41.8 | 30.6 |
| of which samarium and heavier | 8.7 | 14.8 |
| Paid as carbonate (70%) | 36.1 | 32.5 |
| **Extra from Stage 1** | **10.0** | **6.7** |
| **Extra from Stage 2** | **12.9** | **11.6** |

At China-market and US-floor prices (tested in v0.5) the extra is smaller still: about US$7/kg for Stage 1 and US$8–9/kg for Stage 2.

**What this shows:**
- **Tiros is a light rare-earth deposit.** Dysprosium and terbium are about 0.36% of its oxide: about 0.9 t of Dy and 0.15 t of Tb a year at the brief's size.
- **Outside-China prices don't help much.** The heavy premium applies to very little material, and NdPr is cheaper outside China (about US$115/kg) than in the PEA (US$157).
- **Stage 1 earns least where heavies are worth most.** The heavy concentrate is paid only 65% of its value, below the 70% the carbonate already earns.

### 6.4 The three set-ups

At the brief's 5,000 t/month and PEA prices:

| | Stage 1, Tiros only | Stage 1 as a hub | Stage 2, full separation hub |
|---|---|---|---|
| Rare-earth oxide processed | 436 t/yr | 4,436 t/yr | 4,436 t/yr |
| Extra value from Tiros's own rare earths | US$4.4M/yr | US$4.4M/yr | US$5.6M/yr |
| Toll fees from other producers | – | US$40M/yr (US$10/kg) | US$80M/yr (US$20/kg) |
| Running cost | US$6.9M/yr | US$36.3M/yr | US$53.9M/yr |
| Margin | −US$2.5M/yr | US$8.0M/yr | US$31.7M/yr |
| Build cost | US$38M | US$153M | US$279M |
| Government support (25%) | US$10M | US$38M | US$70M |
| **Net present value at PEA prices** | **−US$54M** | **−US$36M** | **US$102M** |
| Net present value at outside-China prices | −US$68M | −US$50M | US$96M |
| **Toll fee needed to break even** | – | **US$10.9/kg** | **US$17.4/kg** |

**Will other producers pay those fees?** A producer only tolls if it gains more than it would by selling carbonate. For a light-rich Brazilian carbonate like Meteoric's Caldeira (NdPr 31%, dysprosium and terbium about 1%), Stage 1 gains it about US$6–11/kg and Stage 2 about US$10–19/kg, depending on prices.
- **Stage 1's break-even fee (US$10.9)** sits at the very top of that range, so a Stage 1 hub is marginal.
- **Stage 2's break-even fee (US$17.4)** is reachable only at PEA-level or outside-China prices, or with some heavy-rich feed. Heavy-rich clay carbonates gain far more: Serra Verde's basket is about US$190/kg at outside-China prices, and Aclara charges US$40/kg on its own heavy-rich carbonate.

### 6.5 What moves the answer most

Stage 2 hub, brief's size, PEA prices (base US$102M):

| Change | Net present value |
|---|---|
| Other producers' oxide 2,000 t/yr (base 4,000) | −US$31M |
| Other producers' oxide 8,000 t/yr | US$396M |
| Other producers' oxide 12,000 t/yr | US$708M |
| Toll fee US$15/kg (base US$20) | −US$95M |
| Toll fee US$25/kg | US$298M |
| Build cost on Aclara's October 2026 basis (US$494M reference) | −US$62M |
| Running cost US$3/kg higher | −US$29M |
| No government support | US$32M |
| Separation recovery 90% (base 95%) | US$91M |

**Scale and the fee dominate.** Tiros's own rare earths barely move the result. At full PEA size, separating *only* Tiros's 3,636 t/yr of oxide is worth −US$33M (Stage 1) and −US$177M (Stage 2).

### 6.6 How we would build it: a staged plan with gates

| Step | What | Go ahead only when |
|---|---|---|
| **0. Now to pilot** | Tiros makes carbonate in Brazil (Option 1). Toll-separate test lots with an existing separator, such as Rare Earth Technologies (RETI), which has a non-binding agreement with Resouro, or Ucore in Louisiana. | Assays show Tiros carbonate meets a separator's feed specification, including thorium and uranium. |
| **1. Stage 1 hub in Brownsville** | First-cut plant: NdPr oxide to Texas magnet makers, heavy concentrate to heavy separators outside China. | About 7,000–8,000 t/yr or more of total feed is under contract, at fees of about US$10/kg or more; grants are secured; and a wastewater route is permitted. |
| **2. Stage 2** | Add the heavy separation steps. | Heavy-rich feed (clay carbonates) is under contract, and outside-China heavy prices or floors hold. |
| **3. Metal and magnets** | NdPr metal and magnets, with partners. | A magnet maker commits. Texas has the US's magnet plants: MP Materials in Fort Worth (and a 10,000 t/yr plant planned at Northlake) and Noveon in San Marcos. |

### 6.7 Precedents

| Project | What it is | What it tells us |
|---|---|---|
| Aclara, Louisiana | Full separation of carbonate from its Carina mine in Goiás, Brazil. About 4,378 t/yr; US$277M (April 2026), later US$494M. | The exact split we recommend, Brazilian carbonate to a US Gulf Coast plant, is being financed. Its economics rest on a US$40/kg fee from a heavy-rich carbonate. |
| Ucore, Louisiana | Carbonate to NdPr: about 600 t/yr for US$60M, growing to about 3,600 t/yr for US$135M. Department of War funding. | The model's Stage 1 cost basis. |
| Neo Performance Materials (Estonia) and Carester (France) | Neo will toll-separate Carester's carbonate, keep the light rare earths and return the heavies. | The Stage 1 business model already exists. |
| Lynas, Seadrift, Texas | Planned light and heavy separation from imported carbonate, with Department of Defense funding. | Cancelled in August 2026 after wastewater permit problems. A Brownsville plant must plan its wastewater from day one. |

### 6.8 Decisions behind the module

**D18 – Rare-earth split built from the PEA's assays.** See 6.3. *(Needs testing)*
- **Would change if:** Resouro shares a carbonate assay.

**D19 – Four price cases, not one.** PEA long-term, China market (October 2026), US price floors, and outside China (October 2026).
- **Only NdPr, dysprosium and terbium differ by case.** Outside-China quotes for yttrium, gadolinium and samarium are 10–100 times China's, but come from a handful of trades, so we use China prices for them throughout. *(Assumption)*

**D20 – Heavy concentrate paid at 65% of its value.** No published terms exist. It sits just below the carbonate's 70% and Aclara's 66%. *(Assumption)*

**D21 – Build cost from two real US Gulf Coast plants.**
- **Stage 1:** Ucore, US$135M for about 3,600 t/yr (its first machine plus Production Line 1 and oxide finishing), scaled with the six-tenths rule. Small plants cost more than the rule says (Ucore's 600 t/yr machine alone is US$60M), so Stage 1 for Tiros alone is if anything too cheap.
- **Stage 2:** Aclara, US$277M at 4,378 t/yr, scaled with the six-tenths rule.
- **No US factor is added,** because both are US plants. *(Assumption)*

**D22 – Running cost.**
- **Stage 1:** US$7/kg plus staff.
- **Stage 2:** US$10/kg plus staff.
- **Why:** Aclara's full-separation cost is US$12.6/kg all-in, and Rainbow's whole process is US$12.91/kg. *(Assumption)*

**D23 – Toll fees.**
- **Stage 1:** US$10/kg.
- **Stage 2:** US$20/kg.
- **Why:** set near what a Caldeira-like producer would gain (6.4). *(Assumption)*
- **Check:** the break-even fee line on the RE module tab shows how far from that a result is.

**D24 – Government support: 25% of build cost.** *(Assumption)*
- **Grants:** about 20%. Aclara received 17% from Louisiana; Ucore about 38% of its first machine from the Department of War.
- **45X tax credit:** about 5% more. It pays 10% of production costs until 2030 and phases out by 2034.

---

## 7. Questions for Steve and Resouro

The full list, ranked by how much each answer moves the model, is in `docs/model-questions.md`. The most important:

1. Why Brownsville? Is it about cost, US-origin product rules, funding, or customers?
2. Is the 5,000 t/month raw ore, or a product already upgraded in Brazil?
3. Does Resouro have thorium and uranium assays for the fines, residue and carbonate?
4. What is the basis for 205 kg of caustic soda per tonne of ore?
5. Which rare-earth recovery figure should we trust, 67% or 80.5%?
6. Is a sulfur-burning acid plant at Tiros already being studied for the PFS (Pre-Feasibility Study)?
7. Is separation in Brownsville, alone or with a partner such as RETI, part of the Brownsville plan?
8. What is the element make-up of Tiros's carbonate, and has any carbonate been made and assayed?
9. Has Resouro talked with other Brazilian producers (Meteoric, Serra Verde) about a shared separation plant?

## 8. Tests this points to

These feed deliverable 5:

1. Acid use and regeneration on a representative fines sample, including how much acid can really be recovered.
2. Thorium and uranium assays: where they end up between residue, liquor and carbonate.
3. Moisture limit for safe shipping (flow-table test) on filtered fines and on calcine, if any Texas option is pursued.
4. End-to-end liquor tests, from titanium hydrolysis to impurity removal to carbonate, to confirm the 67% recovery.
5. Wastewater composition and treatment options for the sodium sulfate.
6. Filtration tests on the clay-rich fines (cake moisture, filter rate).
7. Make a test carbonate and assay every rare earth, plus thorium and uranium, to judge separation in Brownsville (section 6).
8. Toll-separate a test lot of carbonate with an existing separator, to measure recovery and product purity.

---

## Sources for sections 5 and 6

The rare-earth module's sources are listed in `docs/research/06-rare-earth-module.md`.


- Section 45X: [Congressional Research Service, The Section 45X Advanced Manufacturing Production Credit (Oct 2026)](https://www.everycrsreport.com/files/2026-10-20_IF12809_05acf96472c224d41401a34fc1832512801ec8bd.html); purity rules in [26 CFR 1.45X-4](https://www.customsmobile.com/regulations/26/1.45X-4)
- MP Materials price floor: [MP Materials announcement, July 2025 (SEC filing)](https://www.sec.gov/Archives/edgar/data/1801368/000119312525157310/d43796dex991.htm)
- Section 232 and price floors: [White & Case, Jan 2026](https://www.whitecase.com/insight-alert/president-trump-orders-critical-minerals-trade-negotiations-section-232-action); [Yahoo Finance, Feb 2026](https://finance.yahoo.com/news/trump-administration-floats-using-tariffs-to-implement-price-floor-on-rare-earth-minerals-191500089.html); [Mining.com on Project Vault, Feb 2026](https://www.mining.com/legal-analysis-what-project-vault-means-for-critical-minerals-regulation/)
- Aclara Project Dynamo: [Aclara technical reports, Apr 2026 (Newswire)](https://www.newswire.com/news/aclara-announces-results-from-technical-reports-on-its-integrated-heavy-rare); [Metal Tech News, 14 Oct 2026](https://www.metaltechnews.com/story/2026/10/14/mining-tech/aclara-plans-157-percent-more-rare-earth-oxides/2985.html)
- China's export controls on medium and heavy rare earths: [Asian Metal, Apr 2025](https://www.asianmetal.com/news/2178266/China-announces-export-control-on-seven-key-medium-to-heavy-rare-earth-elements); [SMM on the Dy/Tb price gap](https://news.metal.com/newscontent/103310477-Dysprosium-and-Terbium-Supplies-Are-Tight-Overseas,-Price-Spread-Between-Rare-Earths-at-Home-and-Abroad-Widens-[[SMM-Analysis]])
- Lynas Seadrift: [Lynas FY26 Annual Report (ASX, 26 Aug 2026)](https://announcements.asx.com.au/asxpdf/20260826/pdf/0737nx07s3tnf7.pdf)
- US financing in Brazil: [Net Zero Circle](https://www.netzerocircle.org/news/us-financing-moves-ahead-of-a-formal-rare-earths-agreement-with-brazil); [US DFC offers US$565M to Brazilian rare-earth project (SMM, Feb 2026)](https://news.metal.com/pt/newscontent/103760636-US-DFC-Offers-565M-Financing-to-Brazilian-Rare-Earth-Project); [US aims to process critical minerals in Brazil (Feb 2026)](https://www.pulse.bot/global-economy/news/us-aims-to-process-critical-minerals-in-brazil-7ae71b7e-a991-4015-b4f9-2aef1c8f3dcb)

---

## Glossary

| Term | Plain meaning |
|---|---|
| Acid bake | Mixing the fines with strong sulfuric acid and heating them (about 300 °C) so the rare earths become soluble |
| Calcine | Material that has been roasted in a kiln. Here: fines after the 600 °C roast, which leave the kiln dry |
| Caustic soda | Sodium hydroxide (NaOH), a strong alkali used to neutralize acid liquor |
| Dy, Tb | Dysprosium and terbium, heavy rare earths used in high-temperature magnets |
| DFC | US International Development Finance Corporation, the US government's development bank |
| Heavy concentrate | The mixed samarium-and-heavier rare earths left after the first separation cut |
| Group A cargo | A bulk cargo that can liquefy at sea if it is too wet |
| MREC | Mixed rare-earth carbonate, the rare-earth product |
| NdPr | Neodymium–praseodymium, the main magnet rare earths |
| NORM | Naturally occurring radioactive material |
| NPV | Net present value: today's value of future profit minus the build cost |
| PEA | Preliminary Economic Assessment, the July 2026 technical report this model is built on |
| Section 45X | A US tax credit for producing certain clean-energy components and purified critical minerals in the US |
| Solvent extraction | The usual way to separate rare earths: many stages of mixing a rare-earth solution with an organic liquid that picks up some elements more than others |
| Six-tenths rule | A rule of thumb: a plant twice as big costs about 2^0.6 ≈ 1.5 times as much |
| Sulfur-burning acid plant | A plant that burns sulfur to make sulfuric acid, giving off useful heat |
| Hub | A separation plant that processes several producers' carbonate |
| Toll processing | Paying another company to process your material for a fee, while you keep ownership |
| TCEQ | Texas Commission on Environmental Quality |
| TML | Transportable moisture limit: the most moisture a cargo may contain to ship safely |
