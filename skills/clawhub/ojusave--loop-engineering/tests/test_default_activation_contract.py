from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = (ROOT / "SKILL.md").read_text()
OPENAI = (ROOT / "agents" / "openai.yaml").read_text()
ADAPTIVE = (ROOT / "references" / "adaptive-task-design.md").read_text()
EXAMPLES = (ROOT / "references" / "examples.md").read_text()
README = (ROOT / "README.md").read_text()
CASES = (ROOT / "tests" / "default_activation_cases.md").read_text()


class DefaultActivationContractTests(unittest.TestCase):
    def test_accepts_persistent_instructions_as_an_activation_source(self) -> None:
        self.assertIn(
            "active personal, workspace, or project instructions declare it the default",
            SKILL,
        )
        self.assertIn(
            "when an applicable personal, workspace, or project instruction says to use it by default",
            SKILL,
        )
        self.assertNotIn("only when the user explicitly invokes it", SKILL)

    def test_normative_sources_share_one_activation_contract(self) -> None:
        sources = {
            "skill": SKILL,
            "adaptive task design": ADAPTIVE,
            "routing examples": EXAMPLES,
            "readme": README,
        }
        forbidden = (
            "activate only when the user explicitly invokes",
            "only when the user explicitly invokes it",
            "designed for explicit invocation",
        )
        for name, source in sources.items():
            lowered = " ".join(source.lower().split())
            with self.subTest(source=name):
                for phrase in forbidden:
                    self.assertNotIn(phrase, lowered)

        normalized_sources = {
            name: " ".join(source.split()) for name, source in sources.items()
        }
        for phrase in (
            "personal, workspace, or project instruction",
            "substantive follow-ups",
            "clearly replaces the task",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, normalized_sources["adaptive task design"])
                self.assertIn(phrase, normalized_sources["readme"])
                self.assertIn(phrase, normalized_sources["routing examples"])

    def test_keeps_default_invocation_light_when_the_task_is_narrow(self) -> None:
        self.assertIn("When loop-by-default is active, match the loop to the work", SKILL)
        self.assertIn("Use Light for a narrow answer, clarification, or reversible edit", SKILL)

    def test_followups_are_deltas_and_replacements_reset(self) -> None:
        self.assertIn("Treat a follow-up in the same task as a delta", SKILL)
        self.assertIn("Start a new contract when the user clearly replaces the task", SKILL)
        self.assertEqual(CASES.count("## Case "), 3)
        self.assertIn("Additive follow-up preserves the main focus", CASES)
        self.assertIn("Explicit replacement resets the contract", CASES)

    def test_allows_implicit_skill_selection(self) -> None:
        self.assertIn("allow_implicit_invocation: true", OPENAI)


if __name__ == "__main__":
    unittest.main()
