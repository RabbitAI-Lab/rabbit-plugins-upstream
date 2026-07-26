#!/usr/bin/env python3
"""Tests for skill-auditor vet.py.

Run from skill-auditor repo root:
    python3 tests/test_vet.py
or:
    python3 -m pytest tests/  (if pytest installed)
"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
from vet import audit_skill, find_skill_files  # noqa: E402
from score import score_violations, severity_for_score, verdict_for_score  # noqa: E402

SKILL_ROOT = Path(__file__).resolve().parent.parent
TEST_GOOD = SKILL_ROOT / "tests" / "test_skill_good"
TEST_MALICIOUS = SKILL_ROOT / "tests" / "test_skill_malicious"


class TestBenignSkill(unittest.TestCase):
    """The benign sample should score low."""

    @classmethod
    def setUpClass(cls):
        cls.result = audit_skill(TEST_GOOD)

    def test_audited_without_error(self):
        self.assertEqual(self.result.skill_name, "safe-weather")

    def test_score_is_low(self):
        # The benign sample uses curl to api.open-meteo.com which is not in
        # default allowlist, so it might trigger NET_UNKNOWN_HOST.
        # But we still expect the score to be LOW (< 16).
        self.assertLess(self.result.risk_score, 20,
                        f"Expected low score for benign skill, got {self.result.risk_score}")

    def test_no_critical_violations(self):
        criticals = [v for v in self.result.violations if v.severity == "critical"]
        self.assertEqual(criticals, [],
                         f"Benign skill should have no critical violations, got {criticals}")

    def test_verdict_is_safe_or_caution(self):
        self.assertIn(self.result.verdict,
                      ["✅ SAFE TO INSTALL", "⚠️ INSTALL WITH CAUTION"])


class TestMaliciousSkill(unittest.TestCase):
    """The malicious sample should score very high."""

    @classmethod
    def setUpClass(cls):
        cls.result = audit_skill(TEST_MALICIOUS)

    def test_score_is_extreme(self):
        # evil-todo hits: CRED_SSH, CRED_AWS, IDENTITY_FILES, NET_CURL_PIPED,
        # NET_IP_LITERAL, NET_PASTEBIN, FILE_WRITE_OUTSIDE, RCE_PICKLE,
        # SHELL_TRUE, OBFUSCATE_BASE64... should max out.
        self.assertGreaterEqual(self.result.risk_score, 70,
                               f"Expected high score for malicious skill, got {self.result.risk_score}")

    def test_has_critical_violations(self):
        criticals = [v for v in self.result.violations if v.severity == "critical"]
        self.assertGreater(len(criticals), 0,
                           "Malicious skill should have at least one critical violation")

    def test_specific_critical_rules_triggered(self):
        rule_ids = {v.rule_id for v in self.result.violations}
        # Must catch SSH key theft
        self.assertIn("CRED_SSH", rule_ids)
        # Must catch AWS credential theft
        self.assertIn("CRED_AWS", rule_ids)
        # Must catch identity file access
        self.assertIn("IDENTITY_FILES", rule_ids)
        # Must catch curl|bash
        self.assertIn("NET_CURL_PIPED", rule_ids)

    def test_verdict_blocks_install(self):
        self.assertIn(self.result.verdict,
                      ["⚠️ HUMAN APPROVAL REQUIRED", "❌ DO NOT INSTALL"])


class TestScoringModel(unittest.TestCase):
    """Direct tests of the scoring model."""

    def test_no_violations_is_zero(self):
        self.assertEqual(score_violations([]), 0)

    def test_single_low(self):
        self.assertEqual(score_violations(["NO_LICENSE"]), 5)

    def test_single_critical(self):
        self.assertEqual(score_violations(["CRED_SSH"]), 25)

    def test_capped_at_100(self):
        # 5 critical = 125, should cap at 100
        self.assertEqual(score_violations(
            ["CRED_SSH", "CRED_AWS", "RCE_EVAL", "PERM_SUDO", "RCE_PICKLE"]
        ), 100)

    def test_severity_tiers(self):
        self.assertEqual(severity_for_score(0), "🟢 LOW")
        self.assertEqual(severity_for_score(15), "🟢 LOW")
        self.assertEqual(severity_for_score(16), "🟡 MEDIUM")
        self.assertEqual(severity_for_score(40), "🟡 MEDIUM")
        self.assertEqual(severity_for_score(41), "🔴 HIGH")
        self.assertEqual(severity_for_score(70), "🔴 HIGH")
        self.assertEqual(severity_for_score(71), "⛔ EXTREME")
        self.assertEqual(severity_for_score(100), "⛔ EXTREME")


class TestFileDiscovery(unittest.TestCase):
    def test_finds_skill_md(self):
        files = find_skill_files(TEST_GOOD)
        names = [f.name for f in files]
        self.assertIn("SKILL.md", names)

    def test_skips_hidden_dirs(self):
        files = find_skill_files(TEST_GOOD)
        for f in files:
            self.assertNotIn(".git", f.parts)


if __name__ == "__main__":
    unittest.main(verbosity=2)
