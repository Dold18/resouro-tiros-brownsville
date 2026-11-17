# Style guide

*Tiros–Brownsville team · version 1.4 · 6 November 2026*

This guide covers the spreadsheet first, then Word documents, Markdown files and charts. Choices marked **(team decision)** were agreed on 6 November 2026; the rest follow from them. The research notes in `docs/research/` are working notes and are exempt.

## 1. Decisions at a glance

| Topic | Rule |
|---|---|
| Colors | Oxide green and sand, on a white page **(team decision)** |
| Trust labels | Known / Assumption / Needs testing, the brief's own wording **(team decision)** |
| Money | US$ millions for totals (US$564M); full dollars for yearly cost lines in the Model tab and for unit rates **(team decision)** |
| Spelling | US: sulfur, aluminum, color **(team decision)** |
| Font | Arial everywhere |
| Units | Metric tonnes (t), US dollars, °C, µm |
| Abbreviations | Spell out on first use in every file; glossary at the end of long documents |
| Page references | "PEA p.276" = printed page of the July 2026 NI 43-101 report |

## 2. Colors

One accent color, one input color, and greys. No other colors, no gradients, no colored header bars.

| Name | Hex | Used for |
|---|---|---|
| Ink | `#26313A` | Body text |
| Oxide green | `#1E5245` | Titles, section headings, totals, chart bars, and the *Known* label |
| Sand | `#F6EFDF` | Fill for cells a reader may change (inputs). Nothing else is sand. |
| Band | `#F3F5F2` | Very light fill behind section headings in the spreadsheet |
| Muted grey | `#6B7780` | Units, notes, sources, captions |
| Rule grey | `#C9CFC9` | Thin horizontal lines between rows |
| Amber | `#9A6A14` | The *Assumption* label |
| Brick red | `#A33B2B` | The *Needs testing* label. Also negative highlights, used sparingly. |

## 3. Trust labels

Every input carries exactly one of the three labels the challenge brief asks for. A label is colored text, never a cell fill.

| Label | Meaning | Examples |
|---|---|---|
| **Known** | Stated in the PEA, or a published fact | Head grade 26.3% TiO₂ (PEA p.267); 3.0 t of acid per t of sulfur |
| **Assumption** | Our planning choice, often picked from a researched range. The Source column says which. | Caustic soda at $560/t delivered to Tiros; Texas landfill at $45/t |
| **Needs testing** | Depends on metallurgical testing or a measurement not yet done | Rare-earth recovery 67%; acid regeneration 21.8%; thorium in the residue |

**Calculated inputs.** A calculated input carries the label of the weakest number it is built from. For example, the fines fraction is 1 minus the coarse fraction, so it is *Needs testing*.

**In documents,** use the same three words, written in italics, when a number's status matters: "*Needs testing*: 67% recovery".

## 4. Numbers and units

### Money
The format is the one used in the first version of the model (v0.1).

**In the spreadsheet**
| Where | Format | Example |
|---|---|---|
| Inputs: one-off amounts (build costs, acid plant, site overheads) | US$ millions, one decimal, unit "$M" or "$M/yr" | $191.2 with unit $M |
| Inputs: unit rates | Whole dollars from $100 up; cents below $100 | $560 /t · $63.60 /t · $0.086 /kWh |
| Model tab: yearly costs, revenue and margin | Full dollars, unit "$/yr" | $31,786,040 |
| Model tab: build costs and net present value | US$ millions, one decimal, unit "$M" | $53.6 |
| Summary tab: revenue, running cost and margin | US$ millions, one decimal, unit "$M/yr" | $25.8 |
| Summary tab: build cost and net present value | US$ millions, one decimal, unit "$M" | $19.0 |
| Chart | US$ millions, one decimal, values labelled on the bars | $19.0 |
| Negatives | In parentheses | ($84.9) |

**In documents**
- **Totals:** in US$ millions with an "M", written "US$564M" or "US$31.8M/yr". Use one decimal where it matters, and drop a trailing ".0".
- **Big tables:** a table full of totals may state "in US$ millions" in its caption and show plain numbers, as the results table in the decisions document does.
- **Below US$500,000:** write the full amount: US$95,000/yr.
- **Unit rates:** in full: US$170/t, US$0.086/kWh.
- **Ranges:** US$5–8M, US$550–700/t.
- **Negatives:** a minus sign before the currency: −US$84.9M.
- **Currency:** always write "US$" in documents. The spreadsheet's unit column already says it is dollars.

### Tonnes and other units
| Item | Rule |
|---|---|
| Mass | Metric tonnes, written "t". Rates as t/yr, t/month, t/day. Never "tons", except when quoting a US source, and then say "short tons". |
| Grades | % for main elements (26.3% TiO₂). ppm only when quoting the PEA, with the % in brackets: 10,852 ppm (1.09%). |
| Shares | % with one decimal in the spreadsheet (28.9%). Stored as fractions (0.289). |
| Particle size | µm (microns); "+75 µm" means coarser than 75 microns |
| Temperature | °C |
| Years | "2026"; fiscal years as "FY26 (Jul 2025–Jun 2026)" |
| Zero | Shown as "–" in the spreadsheet |

## 5. Spreadsheet layout

### Overall
- **Tabs, in order:** Read Me, Summary, Inputs, Model, RE module, Hub charts, Sources. The file opens on Summary.
- **Gridlines** off on every tab. Rows are separated by thin grey rules only, never boxed grids.
- **Title block** on every tab:
  - Row 2: the title, Arial 16 bold, oxide green.
  - Row 3: a one-line subtitle, Arial 10 italic, muted grey.
  - The table starts at row 5.
- **Column A** is a narrow margin. Content starts in column B.
- **Column headers:** Arial 9 bold, muted grey, with a dark rule underneath. No fill.
- **Section headings** inside a tab: numbered ("5  Acid and sulfur prices"), Arial 11 bold oxide green, on the light band.
- **Totals:** bold oxide green with a green rule above. One total per block.
- **Freeze panes** below the header row, and left of the first value column on the Model tab.

### Cells
- **Inputs:** sand fill with a thin sand underline. Only inputs are sand.
- **Formulas:** no fill, ink color.
- **Keep it short.** An input stays only if it changes the answer. One that is the same in every option is merged into one line; one set to zero is removed and kept as a question instead.
- **One assumption per cell.** Formulas refer to named inputs (`=ROM_tpm*12`), never typed-in numbers.
- **Dropdowns** for choices: what is shipped.
- **Alignment:**
  - Text: top-left.
  - Numbers: top-right.
  - Long notes wrap in their own column.

### Each input row reads, left to right
Input name (plain words) · Value · Unit · Trust label · Source (with PEA page) · Why this value

Every *Assumption* must say why that value was chosen: the range it came from, or that it is a placeholder.

### Model tab
- One column per option, read top to bottom.
- A "How it is calculated" note column on the right, in plain words. Every line says where its values come from: the input name, and the PEA page or source behind it.

### Charts
- One series color: oxide green. A second series, if needed, is muted grey; a third, rule grey. Each chart has a 'What to look for' note beside it.
- **Labels:**
  - No legend when there is only one series.
  - Values labelled at the end of each bar, in US$ millions.
  - Category labels outside the plot, on the low side of the axis, so negative bars do not cover them.
- **No 3D,** no shadows, no gridlines.
- **Titles:** a plain statement of what the chart shows, with the unit, for example "Net present value before tax ($M)".

## 6. Word documents and Markdown

- **Fonts:**
  - Arial throughout.
  - Title: 20 pt bold, oxide green.
  - Heading 1: 14 pt bold, oxide green.
  - Heading 2: 12 pt bold, oxide green.
  - Body: 11 pt, ink.
- **Byline:** under the title, give the team name, the version and the date, for example "*Tiros–Brownsville challenge · model v0.1 · 4 November 2026*".
- **Open with the answer.** The first paragraph states the conclusion and its key number. No "This document outlines…".
- **Plain words:**
  - Spell out every abbreviation on first use: "mixed rare-earth carbonate (MREC)".
  - Keep sentences under about 25 words, and paragraphs to three sentences.
- **Tables** for anything compared across options or items. Bullets only for parallel items.
- **Citations:**
  - PEA facts: (PEA p.276).
  - Outside facts: a link, or the research note that holds the link.
- **Glossary** at the end of any document longer than three pages.
- **Word files** are generated from the Markdown with `docs/templates/reference.docx`, which carries these fonts and colors (see `docs/build_docs.sh`). Edit the Markdown, then rebuild. Don't hand-edit the .docx.

## 7. Names and files

| Item | Rule |
|---|---|
| Options | Always "Option 1" to "Option 3", with the same short names everywhere: All in Brazil · Wet fines to Texas · Dry calcine to Texas. The own-acid-plant case (v0.5) is named "own acid plant" |
| Rare-earth module | "Stage 1" (first cut: NdPr oxide, lanthanum–cerium product, heavy concentrate), "Stage 2" (full separation), "Stage 3" (metal and magnets). Set-ups: Stage 1, Tiros only · Stage 1 as a hub · Stage 2 hub. Price cases: PEA long-term · Outside China (October 2026) |
| Places | "Tiros" for the Brazil site, "Brownsville" for the Texas site, "Brazil" and "Texas" for the countries or states |
| The PEA | "the PEA" after first use: "NI 43-101 Technical Report and Preliminary Economic Assessment (PEA), Norda Stelo, July 2026" |
| File names | Words joined with hyphens (`engineering-decisions.md`), except the model `Tiros_Brownsville_Model.xlsx` |
| Versions | Version and date on the Read Me tab, the Summary subtitle, and each document's byline |
