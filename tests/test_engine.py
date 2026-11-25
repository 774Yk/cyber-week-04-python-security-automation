"""Tests for offline Python security automation.

Author: Y_774 | Telegram: @Y_774 | Instagram: @Y.77.4 | GitHub: 774Yk
Contact: yassenalhajere@gmail.com
"""
import json
import tempfile
import unittest
from pathlib import Path
from secauto.engine import inventory, report, scan_file

class EngineTests(unittest.TestCase):
    def test_secret_pattern_is_detected(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "config.txt"
            path.write_text("api_key = 'training-secret-value'\n")
            self.assertEqual(scan_file(path)[0].rule_id, "SEC-001")

    def test_debug_json_is_detected(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "settings.json"
            path.write_text(json.dumps({"debug": True}))
            self.assertEqual(scan_file(path)[0].rule_id, "CFG-001")

    def test_report_has_hash_inventory_and_clean_sample(self):
        root = Path("sample-data")
        result = report(root)
        self.assertTrue(result["files"])
        self.assertTrue(all(len(item["sha256"]) == 64 for item in result["files"]))
        self.assertEqual(result["findings"], [])

    def test_inventory_is_deterministic(self):
        self.assertEqual(inventory(Path("sample-data")), inventory(Path("sample-data")))

if __name__ == "__main__":
    unittest.main()
