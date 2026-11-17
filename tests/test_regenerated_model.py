"""Source reproducibility checks against the exact final team submission.

Rebuild happens only in a temporary directory, not in model/.
"""
import sys
from pathlib import Path
import unittest

TOOLS = Path(__file__).resolve().parents[1] / "tools"
sys.path.insert(0, str(TOOLS))
from rebuild_and_verify import (  # noqa: E402
    ROOT, SOURCE, SUBMITTED, SHA256_FINAL, safe_rebuild, workbook_cells
)


class SourceRebuildTests(unittest.TestCase):
    def test_original_source_rebuild_matches_submitted_formulas_and_inputs(self):
        result = safe_rebuild()
        self.assertEqual(result["sheets"], 6)
        self.assertEqual(result["named_inputs"], 48)
        self.assertEqual(result["formulas"], 271)
        self.assertTrue(result["submitted_sha256_unchanged"])

    def test_required_original_mrec_source_is_present(self):
        self.assertTrue((SOURCE / "mrec_block.py").is_file())

    def test_normal_and_crisis_prices_use_separate_formulas(self):
        _, defs, contents = workbook_cells(SUBMITTED)
        forms = contents["Model"][0]
        self.assertEqual(defs["P_acid_BR"], "Inputs!$C$27")
        self.assertEqual(defs["P_acid_TX"], "Inputs!$C$28")
        self.assertIn("P_acid_TX_26", forms["D61"])
        self.assertIn("P_acid_BR_26", forms["D61"])
        self.assertEqual(forms["D62"], "D60-(D61-D32)*D59/1000000")


if __name__ == "__main__":
    unittest.main()
