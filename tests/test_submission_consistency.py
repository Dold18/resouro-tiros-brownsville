"""Portfolio-level verification of the exact final November 2026 submission.

Independent of optional Excel dependencies. Does not recalculate spreadsheet formulas;
checks original report identity, workbook formulas and cached base outputs.
"""
import hashlib
from pathlib import Path
import unittest
from zipfile import ZipFile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / 'model' / 'Tiros_Brownsville_Model.xlsx'
REPORT = ROOT / 'report' / 'tiros_brownsville_report.pdf'
N = {'m': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
EXPECTED_PDF_SHA256='7a51b44d6439d6bb4f8f13414a74d9182bfbcafd709151663167b4b02c6dfc2a'
EXPECTED_BOOK_SHA256='aa6aa7cc745665109e5d11ed9378343f1c70c8aac99ba92c3ac748dd3a9ba98b'


def workbook():
    """Read final XLSX XML with stdlib; no workbook edits or recalculation."""
    with ZipFile(BOOK) as z:
        w = ET.fromstring(z.read('xl/workbook.xml'))
        names = [e.attrib['name'] for e in w.findall('m:sheets/m:sheet', N)]
        formulas, values = {}, {}
        for i, sheet in enumerate(names, start=1):
            root=ET.fromstring(z.read(f'xl/worksheets/sheet{i}.xml'))
            f_by_cell, v_by_cell = {}, {}
            for cell in root.findall('.//m:sheetData/m:row/m:c', N):
                coord=cell.attrib['r']; f=cell.find('m:f',N); v=cell.find('m:v',N)
                if f is not None:f_by_cell[coord]=f.text
                if v is not None:v_by_cell[coord]=v.text
            formulas[sheet]=f_by_cell; values[sheet]=v_by_cell
        definitions=w.findall('m:definedNames/m:definedName',N)
        return names, definitions, formulas, values

class SubmissionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sheets,cls.names,cls.formulas,cls.values=workbook()

    def test_exact_report(self):
        self.assertEqual(hashlib.sha256(REPORT.read_bytes()).hexdigest(),EXPECTED_PDF_SHA256)

    def test_exact_workbook(self):
        self.assertEqual(hashlib.sha256(BOOK.read_bytes()).hexdigest(),EXPECTED_BOOK_SHA256)

    def test_six_final_worksheets(self):
        self.assertEqual(self.sheets,['Read Me','Summary','Inputs','Model','MREC Texas','Sources'])

    def test_48_defined_inputs(self):
        self.assertEqual(len(self.names),48)

    def test_final_economic_formulas_present(self):
        for coord in ('D16','E16','F16','D17','E17','F17'):
            self.assertIn(coord,self.formulas['Summary'])

    def test_normal_price_npvs(self):
        vals=self.values['Summary']
        for cell,expected in [('D16',19.0385879366303),('E16',-70.1301223261615),('F16',-73.6241593402984)]:
            self.assertAlmostEqual(float(vals[cell]),expected,places=8)

    def test_crisis_price_npvs(self):
        vals=self.values['Summary']
        for cell,expected in [('D17',-38.2401227306043),('E17',-119.698237326653),('F17',-130.902870007533)]:
            self.assertAlmostEqual(float(vals[cell]),expected,places=8)

    def test_orig_code_and_figures_available(self):
        required=['model/build/build_model.py','model/build/inputs.py','model/build/sources.py',
          'model/build/style.py','report/tiros_brownsville_report.tex',
          'report/figures/fig_pfd.tex','report/figures/fig_results.tex']
        for path in required:self.assertTrue((ROOT/path).is_file(),path)

if __name__=='__main__':unittest.main()
