# Questions for Resouro that would improve the model

*Tiros–Brownsville team · for the document request to Resouro · model v0.6 · 6 November 2026*

**Bottom line:** these are the questions whose answers would most change our model. Each one says what we need and which model input it feeds. Where we could measure it, it also says how much the answer moves the net present value (NPV, today's value of future profit minus the build cost).

Questions are of two kinds:
- **Number:** we need a figure or a dataset.
- **Structure:** the answer changes how the model is built.

The 10 questions in section 1 matter most. Section 2 groups all the questions under the eight areas in our document request. Section 3 covers the Brownsville rare-earth module.

**How the impacts were measured.** We changed one input at a time in the model at the brief's 5,000 t/month of ore, at normal (non-crisis) prices, and recorded the change in NPV before tax. The base values are:

| Case | Base NPV |
|---|---|
| All in Brazil (Case 1) | US$19M |
| Texas: dry calcine (Case 2) | −US$70.1M |

The Brazil-versus-Texas gap is the difference between those two.

## 1. The ten that matter most

| # | Question | Kind | Model input | Effect of the answer |
|---|---|---|---|---|
| 1 | Does the ~5,000 t/month in the brief mean raw ore from the mine, or material already upgraded in Brazil? And what does the September 2026 Brownsville plan assume? | Structure | `ROM_tpm`, option set-up | Decides which of our three options matches Resouro's plan, and the basis of every number |
| 2 | Why Brownsville? Is it cost, US-origin product rules, government funding, a partner, or customers? | Structure | Option set-up; Summary's break-even premium | The model compares cost only. If the reason is strategic, the question becomes "what does Texas cost?" rather than "is it cheaper?" |
| 3 | Which rare-earth recovery is right for the product: 67% (process design, p.274) or 80.5% (economic model, p.349)? Have any liquor-to-carbonate tests been run since the PEA? | Number | `Rec_TREO` | 80.5% raises every option by about US$33.6M |
| 4 | What is the basis for 205 kg of caustic soda per tonne of ore? Does it overlap with the acid that regeneration is supposed to recover? | Number | `NaOH_t`, `Acid_t` | If half of it is not needed, every option rises by about US$31–34M |
| 5 | Are the 42,390 t/yr and 47,865 t/yr titanium products tonnes of concentrate, or tonnes of contained TiO₂? | Number | `Y_coarse`, `Y_fine` | If contained TiO₂, product tonnes and revenue rise: about +US$31.3M for each option |
| 6 | Thorium and uranium assays for ore, fines, calcine, leach residue and carbonate. Is any stream above 0.05% uranium plus thorium? | Number | Not in the model (see `Tail_TX`) | If 20% of the Texas residue needed radioactive-waste disposal at ~US$500/t, the Texas options would fall about US$26.5M further behind. It also decides Texas licensing. |
| 7 | Composition and volume of the plant's wastewater (the sodium sulfate from the caustic soda), and how Resouro plans to treat it | Number | Not in the model | At US$100 per tonne of sodium sulfate, every option would fall about US$21M. In Texas, a wastewater permit is what stopped Lynas's Seadrift plant. |
| 8 | Which delivered prices were quoted for caustic soda (US$420/t) and acid (US$170/t), and from which suppliers? | Number | `P_NaOH_BR`, `P_acid_BR` | Caustic soda at US$700/t instead of our US$560/t costs every option about US$16.9M |
| 9 | Plant mass balance (the METSIM stream table): tonnes and moisture of the coarse, fines and calcine streams | Number | `Frac_fines`, `Frac_calcine`, `Dry_cost` | A calcine yield of 50% or 70% instead of 60% moves the Texas option by about ±US$7.5M. It sets how much would be shipped. |
| 10 | Capital cost split by plant area (mine, coarse circuit, kiln, acid bake and leach, rare-earth recovery, site works) | Number | `Sh_fines` | Needed to move part of the plant to Texas. ±30% on capital moves Case 1 by about US$16M. |

## 2. All questions, by the areas in our document request

### Ore and feedstock characterization
1. Full chemistry of the ore by size fraction (+75 µm, −75 µm): TiO₂, total rare-earth oxides, iron, aluminum, silica, calcium, magnesium, phosphorus, thorium, uranium. *(Number → `Head_TREO`; thorium and uranium are not in the model)*
2. Individual rare-earth oxide distribution, especially the magnet rare earths (neodymium, praseodymium, dysprosium, terbium). The basket price of US$57.40/kg depends on it. *(Number → `P_TREO`; ±30% on this price moves every option by about US$50M)*
3. How much do grade and the coarse/fine split vary across the pit over 20 years? Is BK19 representative? *(Structure: tells us whether to model one ore type or several)*
4. Which minerals consume the acid (iron, aluminum, phosphorus phases), in what amounts, and can more of them be removed before the acid bake? *(Number → `Acid_t`. Removing acid-consuming minerals earlier is the cheapest lever on acid in either country.)*

### Metallurgical testwork
5. Raw acid use in kg per tonne of fines, and per tonne of ore, from all bake tests, not only MET-53 (459 kg/t). *(Number → `Acid_t`; ±25% moves every option by about US$9.4M)*
6. Has acid regeneration been tested at all? At what temperature (the text says 600 °C, the figures 680 °C) and with what recovery? *(Number → `Acid_t`, which already assumes ~22% recycling; with none, every option loses about US$10.4M, and 50% recycling gains about US$13.5M)*
7. Any SGS Lakefield, SGS Geosol or CIT SENAI work since the PEA, especially end-to-end runs from leach to carbonate. *(Number → `Rec_TREO`, `MREC_grade`)*
8. Filter-cake moisture achieved on the −75 µm fines, and the filter type used. *(Number → `Dry_cost`. Only matters if wet fines are shipped.)*
9. Has a flow-moisture or transportable-moisture-limit test been done on the fines or the calcine? *(Number → `Moist_ship`. Decides whether the material can ship in bulk.)*
10. Magnesium hydroxide is used instead of lime to avoid gypsum (p.371). What solids does the neutralization actually produce, and how much? *(Structure: decides which Texas waste stream we model)*

### Process flowsheets and balances
11. Stream-by-stream mass balance and water balance from the METSIM model. *(Number → split fractions, waste tonnages)*
12. Reagent balance: where each tonne of acid, caustic soda and hydrochloric acid goes. *(Number → `NaOH_t`, `Acid_t`; wastewater treatment is not in the model)*
13. The MREC grade the design actually expects: 52%, 70% or 95%. It appears as all three in the PEA. *(Number → `MREC_grade`)*
14. Is there a natural point to split the plant between two countries? We propose after the kiln, shipping dry calcine. Does the flowsheet allow that, or does the bake need hot calcine straight from the kiln? *(Structure: decides whether Case 2 are technically possible)*

### Capital and operating costs
15. Capital cost by process area, and the size of each major equipment item. *(Number → `Sh_fines`)*
16. Staff numbers by area. A split plant needs two crews, so this is a major driver of the Texas options. *(Number → staff rows; Texas wages ±US$25,000/yr move the gap by about US$8.4M)*
17. Power use by area. *(Not needed now: the model prices all power the same at both sites, because the acid circuit uses only ~19% of it.)*
18. Which costs are fixed, and which scale with tonnage? Many will not shrink to the brief's 5,000 t/month. *(Structure: replaces our six-tenths scaling)*
19. Has Resouro priced a sulfur-burning acid plant at Tiros for the PFS (Pre-Feasibility Study)? *(Not in the v0.6 model. Our v0.5 analysis found an acid plant at Tiros adds about US$92M at full size; see the engineering decisions, D9.)*

### Products and markets
20. The Project Blue market reports for the titanium dioxide products, and the target specifications buyers require. *(Number → `P_coarse`, `P_fine`)*
21. Who would buy the carbonate, and would any buyer pay more for material processed in the US than in Brazil? *(Summary: break-even premium. Case 2 needs about +53% on the rare-earth price to match Case 1 at 5,000 t/month, and about +30% at full size.)*
22. Is the price for the titanium products at the Brazilian port (FOB Santos) or delivered? Where are the customers? *(Structure: sets product logistics for each site)*

### Brownsville logistics and infrastructure
23. Has Resouro identified a Brownsville site, with utilities, a rail spur, and land for residue storage? *(Number → `TX_site`, `Tail_TX`. Storing residue on site instead of landfilling it at US$45/t would close about US$10.7M of the gap.)*
24. Any freight quotes for Brazil to Brownsville, and the expected ship size? *(Number → `Ship_cost`; US$73–100/t instead of US$85 moves the gap by about US$4–5M either way)*
25. Does a customs ruling exist on how a shipped intermediate (fines or calcine) would be classified for US tariffs? *(Structure: if it is not exempt, every Texas option gets worse)*

### Environmental and regulatory
26. Waste classification tests on the leach residue and the iron/aluminum cake (leach tests, pH). *(Number → `Tail_TX`)*
27. Has Resouro discussed a Brownsville facility with the Texas Commission on Environmental Quality (TCEQ)? *(Structure: permitting time and risk)*
28. Would Brazil allow export of a thorium-bearing intermediate? Do Brazil's nuclear regulator (CNEN) rules, or the government's push for domestic processing, restrict it? *(Structure: may rule out Case 2)*

### Pilot plans and downstream
29. What pilot work is planned, at what scale and where? Could Brownsville host it? *(Structure: if Brownsville is meant as a pilot or demonstration plant, the model should judge it on cost per tonne tested, not NPV)*
30. Is the arrangement with Rare Earth Technologies (RETI, Cincinnati) the planned route for separating the rare earths? Would separation happen in Brownsville? What share of the carbonate is dysprosium, terbium and NdPr? *(Structure: our recommended role for Brownsville; see section 6 of the engineering decisions. Modeled on the MREC Texas tab.)*
31. Has Resouro tested whether the coarse titanium product could feed a titanium tetrachloride (TiCl₄) plant? The PEA says it cannot without upgrading (p.315). *(Structure: decides whether a TiCl₄ add-on belongs in the model)*

## 3. The Brownsville rare-earth module (MREC Texas tab)

Base: a full-separation plant for Tiros carbonate only (436 t/yr of oxide at 5,000 t/month), worth −US$91.5M against selling the carbonate. Case 3 = Case 1 + this plant − shipping the carbonate. (Effects below recalculated for model v0.8.)

| # | Question | Kind | Model input | Effect of the answer |
|---|---|---|---|---|
| 1 | What is the element make-up of Tiros's carbonate (every rare earth, plus thorium and uranium)? Has any carbonate been made? | Number | Shares (MREC Texas, Part 1) | Sets what separation is worth. Our split is built from the BK19 and BK09 assays and checked against the PEA basket. |
| 2 | Is a Brownsville separation plant part of the September 2026 Brownsville plan? | Structure | `sep` row on the Model tab | Separating Tiros's carbonate loses money at every ore rate tested (−US$92M at 5,000 t/month; Case 3 trails Case 1 by US$144M at full size). |
| 3 | Could Tiros send more than 5,000 t/month to the first plant? | Number | Ore rates, Model section F | Case 1: US$19M at 5,000 t/month, US$86M at 10,000, US$233M at 20,000, US$575M at full size. The biggest lever in the model. |
| 4 | What are the terms of the Rare Earth Technologies (RETI) agreement: toll fee, recovery, products returned? | Number | `Rec_sep`, `Sep_var` | A real toll fee below the extra value of ~US$13/kg would make tolling worth more than selling carbonate, with no Brownsville plant. |
| 5 | Would Resouro seek grants or loans (Department of War, Export–Import Bank, state incentives) for a Brownsville plant? | Number | `Support` | No support: −US$109M instead of −US$92M. |
| 6 | Which separation technology and contractor would Resouro consider (conventional solvent extraction, Ucore's RapidSX, others)? | Number | `Sep_capex_ref` | Using Aclara's October 2026 cost basis (US$494M) gives −US$132M. |
| 7 | Has a Texas wastewater route been looked at for a separation plant? | Structure | Running cost (`Sep_var`) | US$3/kg more running cost gives −US$104M. Wastewater stopped Lynas's Texas plant. |

