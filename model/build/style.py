"""Visual style for the Tiros-Brownsville model.

Look: an engineering-consultancy working paper, not a dashboard.
- Gridlines off, white page, thin horizontal rules only (no boxed grids, no filled header bars).
- Ink is near-black slate; one accent color (deep oxide green) for titles and totals.
- Inputs sit on a pale sand fill so they are easy to find; formulas are plain.
- Data status is shown as a short text tag in its own column, colored text, not cell fills.
"""
from openpyxl.styles import Font, PatternFill, Border, Side, Alignment

FONT = "Arial"

INK = "26313A"        # body text
MUTED = "6B7780"      # units, notes, sources
ACCENT = "1E5245"     # deep oxide green: titles, section heads, totals
RULE = "C9CFC9"       # hairline rules
RULE_DARK = "26313A"
INPUT_FILL = "F6EFDF" # pale sand: editable cells
BAND_FILL = "F3F5F2"  # very light band for section heads

# trust labels: the three categories the challenge brief asks for (text color only)
STATUS = {
    "Known": "1E5245",          # stated in the PEA or a published fact
    "Assumption": "9A6A14",     # our planning choice, often picked from a researched range
    "Needs testing": "A33B2B",  # depends on metallurgical testing or measurement not yet done
}

thin = Side(style="thin", color=RULE)
thick = Side(style="medium", color=RULE_DARK)
accent_side = Side(style="medium", color=ACCENT)


def f(size=10, bold=False, color=INK, italic=False):
    return Font(name=FONT, size=size, bold=bold, color=color, italic=italic)


TITLE = f(16, True, ACCENT)
SUBTITLE = f(10, False, MUTED, italic=True)
H1 = f(11, True, ACCENT)
HEAD = f(9, True, MUTED)
BODY = f(10)
BODY_B = f(10, True)
NOTE = f(9, False, MUTED)
TOTAL = f(10, True, ACCENT)

FILL_INPUT = PatternFill("solid", fgColor=INPUT_FILL)
FILL_BAND = PatternFill("solid", fgColor=BAND_FILL)

B_HEAD = Border(bottom=thick)
B_ROW = Border(bottom=thin)
B_TOTAL = Border(top=accent_side)
B_INPUT = Border(bottom=Side(style="thin", color="D8C9A6"))

LEFT = Alignment(horizontal="left", vertical="top")
LEFT_WRAP = Alignment(horizontal="left", vertical="top", wrap_text=True)
RIGHT = Alignment(horizontal="right", vertical="top")
RIGHT_WRAP = Alignment(horizontal="right", vertical="top", wrap_text=True)
CENTER = Alignment(horizontal="center", vertical="center")

# number formats
NUM0 = '#,##0;(#,##0);"–"'
NUM1 = '#,##0.0;(#,##0.0);"–"'
NUM2 = '#,##0.00;(#,##0.00);"–"'
NUM3 = '#,##0.000;(#,##0.000);"–"'
PCT0 = '0%;(0%);"–"'
PCT1 = '0.0%;(0.0%);"–"'
USD0 = '"$"#,##0;("$"#,##0);"–"'
USD1 = '"$"#,##0.0;("$"#,##0.0);"–"'
USD2 = '"$"#,##0.00;("$"#,##0.00);"–"'
USDM = '"$"#,##0.0"M";("$"#,##0.0"M");"–"'
