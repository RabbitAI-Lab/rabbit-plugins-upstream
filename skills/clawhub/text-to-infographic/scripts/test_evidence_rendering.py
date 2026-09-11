from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

from render_infographic_html import (  # noqa: E402
    EVIDENCE_CSS,
    build_evidence_payload,
    build_html,
    has_evidence,
)
from validate_infographic_plan import apply_defaults, load_json  # noqa: E402


class EvidenceRenderingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.evidence_path = ROOT / "examples" / "infographic-data-story-demo.json"
        cls.legacy_path = ROOT / "examples" / "infographic-flywheel-demo.json"
        cls.evidence_plan = apply_defaults(load_json(cls.evidence_path))
        cls.legacy_plan = apply_defaults(load_json(cls.legacy_path))

    def test_evidence_html_contains_auditable_summary(self) -> None:
        rendered = build_html(self.evidence_plan)
        self.assertIn('class="ig-evidence-summary"', rendered)
        self.assertIn("证据摘要", rendered)
        self.assertIn("[1]", rendered)
        self.assertIn("8.9 分钟", rendered)
        self.assertIn("观察期: 2026 Q2", rendered)
        self.assertIn("基期: 12.9 minute · 2026 Q1", rendered)
        self.assertIn(">comparison<", rendered)
        self.assertIn("限定语:", rendered)
        self.assertIn("证据绑定:", rendered)
        self.assertIn(">caveat<", rendered)
        self.assertIn("@media print", rendered)

    def test_evidence_payload_numbers_sources_and_resolves_bindings(self) -> None:
        payload = build_evidence_payload(self.evidence_plan)
        self.assertIsNotNone(payload)
        assert payload is not None
        self.assertEqual([1, 2], [source["number"] for source in payload["sources"]])
        self.assertEqual([1], payload["metrics"][0]["source_numbers"])
        self.assertEqual([1], payload["claims"][0]["evidence_binding"]["source_numbers"])
        self.assertEqual("0.5.0", payload["version"])
        self.assertEqual("c_risk", payload["annotations"][1]["target_id"])

    def test_legacy_html_has_no_evidence_changes(self) -> None:
        rendered = build_html(self.legacy_plan)
        self.assertFalse(has_evidence(self.legacy_plan))
        self.assertNotIn('class="ig-evidence-summary"', rendered)
        self.assertNotIn(EVIDENCE_CSS.strip(), rendered)

    def test_html_cli_writes_sidecar_only_for_evidence_plan(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            subprocess.run([sys.executable, str(SCRIPTS / "render_infographic_html.py"), str(self.evidence_path), str(self.legacy_path), "--out", temp_dir], check=True, capture_output=True, text=True)
            output = Path(temp_dir)
            evidence_id = self.evidence_plan["infographic_id"]
            legacy_id = self.legacy_plan["infographic_id"]
            self.assertTrue((output / f"{evidence_id}.html").exists())
            self.assertTrue((output / f"{evidence_id}.evidence.json").exists())
            self.assertTrue((output / f"{legacy_id}.html").exists())
            self.assertFalse((output / f"{legacy_id}.evidence.json").exists())
            sidecar = json.loads((output / f"{evidence_id}.evidence.json").read_text(encoding="utf-8"))
            self.assertEqual(evidence_id, sidecar["infographic_id"])


if __name__ == "__main__":
    unittest.main()
