"""Every input in the model, in one place.

Each entry: (name, label, value, unit, trust label, source, why)
- name   : Excel defined name used in formulas (keep short, no spaces)
- trust  : Known | Assumption | Needs testing  (the three categories in the challenge brief)
- source : where the number comes from (PEA page = printed page of the July 2026 NI 43-101 PEA)
- why    : one short line. PEA values say only "From the PEA (p.X)" (and the test, if it came from one); assumptions say plainly how the number was reached.
A string starting with '=' is written as a formula.
Section headers are tuples of one string.

v0.8 keeps only inputs that change the answer. Removed inputs and the reasons are listed in
docs/engineering-decisions.md (decisions D25 to D27).
"""

PEA = "Tiros PEA (Norda Stelo, Jul 2026)"

INPUTS = [

    ('1  Plant size',),
    ('ROM_tpm', 'Ore fed to the process (run-of-mine ore)', 5000, 't/month', 'Known', 'Challenge brief',
     "Set by the challenge brief. Enter 41,667 to see the PEA's full size."),
    ('PEA_tpa', 'PEA plant size, for scaling', 500000, 't/yr', 'Known', f"{PEA} p.275, Table 17.2",
     'From the PEA (p.275).'),

    ('2  Ore, split and products',),
    ('Head_TREO', 'Rare-earth oxides in the ore (TREO)', 0.010852, 'fraction', 'Known', f"{PEA} p.267, Table 17.1",
     'From the PEA (p.267).'),
    ('Frac_fines', 'Share of ore that is fine (−75 µm): what the wet-fines variant of Case 2 ships', 0.711, 'fraction of ore', 'Needs testing', f"{PEA} p.217, Table 13.17 (sample BK19)",
     'From the PEA: bench test on sample BK19 (p.217).'),
    ('Frac_calcine', 'Share of ore left as dry calcine after the fines kiln: what Case 2 ships', 0.6, 'fraction of ore', 'Needs testing', f"{PEA} p.217 and p.271",
     'From the PEA: bench test on sample BK19 (p.217).'),
    ('Moist_ship', 'Moisture wet fines must be dried to before shipping', 0.1, 'fraction (wet basis)', 'Needs testing', 'Shipping research notes',
     'A cautious guess until a flow test is done. Only used if Case 2 ships wet fines.'),
    ('Y_coarse', 'Coarse TiO2 product (84.7% TiO2)', '=42390/PEA_tpa', 't per t ore', 'Known', f"{PEA} p.275, Table 17.2",
     'From the PEA (p.275).'),
    ('Y_fine', 'Fine TiO2 product (57.9% TiO2)', '=47865/PEA_tpa', 't per t ore', 'Known', f"{PEA} p.275, Table 17.2",
     'From the PEA (p.275).'),
    ('Rec_TREO', 'Rare earths recovered into the carbonate', 0.67, 'fraction', 'Needs testing', f"{PEA} p.274–275",
     "From the PEA's process design (p.274–275). The PEA's economic model uses 80.5%."),
    ('MREC_grade', 'Rare-earth oxide content of the carbonate (MREC)', 0.703, 'fraction', 'Needs testing', f"{PEA} p.349, Table 22.2 (derived)",
     "From the PEA's economic model (p.349)."),

    ('3  Chemicals per tonne of ore',),
    ('Acid_t', 'Sulfuric acid (96%)', '=186986/PEA_tpa', 't per t ore', 'Needs testing', f"{PEA} p.276",
     'From the PEA (p.276). Includes acid recycling the PEA calls untested.'),
    ('NaOH_t', 'Caustic soda (NaOH)', '=102534/PEA_tpa', 't per t ore', 'Known', f"{PEA} p.341, Table 21.8",
     'From the PEA (p.341).'),
    ('HCl_t', 'Hydrochloric acid (34%), coarse circuit', '=82192/PEA_tpa', 't per t ore', 'Known', f"{PEA} p.341, Table 21.8",
     'From the PEA (p.341).'),

    ('4  Chemical prices, delivered',),
    ('P_acid_BR', 'Sulfuric acid delivered to Tiros · normal year', 170, '$/t', 'Known', f"{PEA} p.341",
     'From the PEA (p.341).'),
    ('P_acid_TX', 'Sulfuric acid delivered to Brownsville · normal year', 175, '$/t', 'Assumption', 'Sulfur & acid notes',
     'US Gulf Coast price before the 2026 shortage ($155/t), plus about $20 to truck it to Brownsville.'),
    ('P_acid_BR_26', 'Sulfuric acid delivered to Tiros · 2026 crisis', 430, '$/t', 'Assumption', 'Sulfur & acid notes',
     'Brazilian port price in Aug–Sep 2026 ($350–370/t) plus trucking to Tiros. Middle of a $400–460 range.'),
    ('P_acid_TX_26', 'Sulfuric acid delivered to Brownsville · 2026 crisis', 400, '$/t', 'Assumption', 'Sulfur & acid notes',
     'US Gulf Coast price at its 2026 peak, plus trucking to Brownsville. Middle of a $380–420 range.'),
    ('P_NaOH_BR', 'Caustic soda delivered to Tiros', 560, '$/t', 'Assumption', 'Caustic & HCl notes',
     "The PEA's $420/t plus sea freight, Brazil's import duty and trucking to Tiros. Low end of a $550–700 range."),
    ('P_NaOH_TX', 'Caustic soda delivered to Brownsville', 520, '$/t', 'Assumption', 'Caustic & HCl notes',
     'Texas makes most US caustic soda, so no sea freight or import duty. Low end of a $500–650 range.'),
    ('P_HCl', 'Hydrochloric acid (34%) delivered to Tiros', 200, '$/t', 'Known', f"{PEA} p.341",
     'From the PEA (p.341).'),

    ('5  Shipping',),
    ('Ship_cost', 'Case 2: shipping calcine or fines from Tiros to the Brownsville plant (bulk)', 85, '$/t as shipped', 'Assumption', 'Shipping notes',
     'Case 2 only. Truck to the Brazilian port (~$35) + port fees (~$8) + bulk sea freight (~$30) + unloading in Brownsville (~$12).'),
    ('Dry_cost', 'Drying wet fines before shipping', 13, '$/t of fines', 'Assumption', 'Shipping notes',
     'Cost to dry wet filter cake from about 25% to 10% moisture. Only used if Case 2 ships wet fines.'),
    ('Truck_BR', 'Products: Tiros to the export port', 53, '$/t', 'Known', f"{PEA} p.348, Table 22.1",
     'From the PEA (p.348).'),
    ('MREC_ship', 'Case 3: shipping carbonate (MREC) from the Brazilian port to Brownsville (containers)', 185, '$/t', 'Assumption', 'Shipping notes',
     'Case 3 only. Sea freight and handling (~$42) plus ~$100/t because a small tonnage ships in bags in containers. The truck to the port is in the line above.'),

    ('6  Site costs',),
    ('Other_t', 'Mining, power, maintenance and minor reagents (same in every case)', '=(5.641e6+23.6e6*0.086+0.65e6+2397*190+3726*130+10890*90+6096*210+1540*1449)/PEA_tpa', '$/t ore', 'Known', f"{PEA} p.340–345, Tables 21.7–21.9",
     'From the PEA: contract mining, power, maintenance and minor reagents (p.340–345), per tonne of ore.'),
    ('Lab_BR', 'Cost per employee, Brazil', '=2.4e6/116', '$/yr', 'Known', f"{PEA} p.346",
     'From the PEA (p.346).'),
    ('Lab_TX', 'Cost per employee, Texas (fully loaded)', 95000, '$/yr', 'Assumption', 'US BLS, May 2023',
     'Average Texas chemical plant pay with benefits, rounded down because Brownsville pays below the state average.'),
    ('GA_site', 'Site overheads per site', 1.0, '$M/yr', 'Assumption', f"{PEA} p.341",
     'The PEA has $1.5M/yr for its full-size plant. A smaller site still needs a manager, safety staff and a lab.'),
    ('Tail_BR', 'Dry-stack waste disposal, Brazil', 3.0, '$/t', 'Known', f"{PEA} p.344",
     'From the PEA (p.344).'),
    ('Tail_TX', 'Industrial landfill disposal, Texas', 45, '$/t', 'Assumption', 'EREF 2025; Texas waste notes',
     'No Gulf Coast price found. US average landfill fee is $62/ton and lower in the South; $45 includes a short haul.'),

    ('7  Product prices',),
    ('P_coarse', 'Coarse TiO2 product price', 900, '$/t', 'Known', f"{PEA} p.316",
     'From the PEA (p.316).'),
    ('P_fine', 'Fine TiO2 product price', 650, '$/t', 'Known', f"{PEA} p.316",
     'From the PEA (p.316).'),
    ('P_TREO', 'Rare-earth basket price', 57.4, '$/kg oxide', 'Known', f"{PEA} p.316",
     'From the PEA (p.316).'),
    ('Payab', 'Share of rare-earth value paid for a carbonate', 0.7, 'fraction', 'Known', f"{PEA} p.316",
     'From the PEA (p.316).'),
    ('Royalty', 'Royalties (federal 2% + landowner 1%)', 0.03, 'fraction of revenue', 'Known', f"{PEA} p.350",
     'From the PEA (p.350).'),

    ('8  Building costs and money',),
    ('Capex_PEA', 'PEA initial build cost', 191.2, '$M', 'Known', f"{PEA} p.332, Table 21.2",
     'From the PEA (p.332).'),
    ('Sh_fines', 'Share of build cost that is the acid (fines) circuit', 0.45, 'fraction', 'Assumption', f"{PEA} p.331–332, Table 21.3",
     'The PEA does not split its build cost by area. The acid circuit holds most of the equipment (two of three kilns, tanks, filters), so it gets 45%.'),
    ('Scale_exp', 'Scaling exponent (six-tenths rule)', 0.6, '', 'Assumption', 'Standard estimating rule',
     'Standard rule for early estimates: cost grows with plant size to the power 0.6.'),
    ('US_factor', 'US build cost relative to Brazil', 1.15, '×', 'Assumption', f"{PEA} p.332, Table 21.2",
     'US construction labor costs more than in Brazil, but Brazilian taxes (17% of the PEA cost) fall away. Net about 1.15.'),
    ('TX_site', 'Extra build cost for a Brownsville site, at PEA full size', 43, '$M', 'Assumption', '',
     'Site works for a second plant at US cost (~$33M) plus ~$10M to receive and store shipped material. No site or quote yet.'),
    ('Sust_t', 'Sustaining capital', '=2.892e6/PEA_tpa', '$/t ore', 'Known', f"{PEA} p.357",
     'From the PEA (p.357).'),
    ('Disc', 'Discount rate', 0.08, '', 'Known', f"{PEA} p.347",
     'From the PEA (p.347).'),
    ('Life', 'Project life', 20, 'years', 'Known', f"{PEA} p.330",
     'From the PEA (p.330).'),

    ('9  Case 3: separating Tiros carbonate in Brownsville (MREC Texas tab)',),
    ('Rec_sep', 'Rare earths recovered by separation', 0.95, 'fraction', 'Needs testing', 'Aclara technical reports (Apr 2026)',
     "From Aclara's April 2026 report: its separation plant recovers 93–95%. Tiros carbonate has never been separated."),
    ('Sep_var', 'Separation running cost per kg processed (excl. staff)', 10, '$/kg TREO', 'Assumption', 'Aclara (Apr 2026); Rainbow (Dec 2024)',
     "From Aclara's April 2026 report: $12.6/kg to separate, less ~$2.5/kg for staff, which the model counts separately."),
    ('Sep_capex_ref', 'Separation plant build cost at reference size', 277, '$M', 'Assumption', 'Aclara technical reports (Apr 2026)',
     "From Aclara's April 2026 report: build cost of its Louisiana separation plant, without working capital."),
    ('Sep_tpa_ref', 'Separation plant reference size', 4378, 't/yr TREO', 'Assumption', 'Aclara technical reports (Apr 2026)',
     "From Aclara's April 2026 report: the rare-earth oxide its Louisiana plant is built to separate each year."),
    ('Support', 'Government support, as a share of build cost', 0.25, 'fraction', 'Assumption', 'Aclara (Apr 2026); Ucore (2025–26); CRS (Oct 2026)',
     "US grants covered 17–38% of recent separation plants' build cost (Aclara, Ucore), plus ~5% from the 45X tax credit. Set to 0% to see the plant without support."),
]
