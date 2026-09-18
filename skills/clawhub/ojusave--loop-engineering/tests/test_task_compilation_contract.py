from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = (ROOT / "SKILL.md").read_text()
ORCHESTRATION = (ROOT / "references" / "orchestration.md").read_text()
PROMPT_GENERATION = (ROOT / "references" / "prompt-generation.md").read_text()
CASES = (ROOT / "tests" / "task_compilation_cases.md").read_text()


class TaskCompilationContractTests(unittest.TestCase):
    def test_understanding_precedes_mechanism_selection(self) -> None:
        understanding = SKILL.index("Understand the request before choosing research")
        outcome_contract = SKILL.index("## Start with a success card")
        topology = SKILL.index("declare an execution topology")
        self.assertGreater(understanding, outcome_contract)
        self.assertLess(understanding, topology)
        self.assertIn("Preserve the user's raw request as evidence", SKILL)
        self.assertIn("Treat proposed mechanisms as hypotheses", SKILL)

    def test_clear_requests_are_not_rewritten_into_large_prompts(self) -> None:
        self.assertIn(
            "For a narrow, clear request, do not rewrite it into a larger prompt",
            SKILL,
        )
        self.assertIn(
            "Do not begin by rewriting the user's request into a detailed multi-agent prompt",
            ORCHESTRATION,
        )
        self.assertIn(
            "When the user asks to rewrite a specific artifact but has not supplied it",
            SKILL,
        )
        self.assertIn(
            "Do not substitute a generic template unless the user explicitly asks for one",
            SKILL,
        )
        self.assertIn(
            "require that source before drafting",
            PROMPT_GENERATION,
        )
        self.assertIn(
            "Do not replace the requested rewrite with a generic placeholder template",
            PROMPT_GENERATION,
        )

    def test_execution_brief_is_compiled_after_the_outcome_contract(self) -> None:
        for field in (
            "Outcome and receiver",
            "Known facts and unknowns",
            "Boundaries",
            "Deliverables and proof",
            "Cut line",
            "Integration owner",
        ):
            with self.subTest(field=field):
                self.assertIn(field, ORCHESTRATION)
        self.assertIn(
            "compile one compact execution brief after the outcome contract",
            ORCHESTRATION,
        )

    def test_architecture_ladder_starts_simple(self) -> None:
        positions = [
            ORCHESTRATION.index("**Direct pass:**"),
            ORCHESTRATION.index("**Single adaptive loop:**"),
            ORCHESTRATION.index("**Fixed workflow:**"),
            ORCHESTRATION.index("**Graph-shaped execution:**"),
        ]
        self.assertEqual(positions, sorted(positions))
        self.assertIn("Do not promote work to a graph because the prompt is long", ORCHESTRATION)
        self.assertIn("A node is not automatically an agent", ORCHESTRATION)
        self.assertIn(
            "A fixed workflow may be drawn as a graph without becoming dynamic graph-shaped execution",
            ORCHESTRATION,
        )

    def test_research_and_specialist_briefs_are_bounded(self) -> None:
        self.assertIn(
            "Turn an unknown into a research question only when resolving it can change",
            ORCHESTRATION,
        )
        self.assertIn("source standard, bounded budget, and observable return", ORCHESTRATION)
        for phrase in (
            "goal",
            "necessary shared context",
            "inputs",
            "constraints and authority",
            "output contract",
            "budget",
            "dependencies",
            "return route",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, ORCHESTRATION)

    def test_cases_cover_direct_research_workflow_graph_and_false_success(self) -> None:
        self.assertEqual(CASES.count("## Case "), 6)
        for phrase in (
            "Clear narrow request is not inflated",
            "Proposed agents remain a hypothesis",
            "Unknown facts become bounded research",
            "Known sequence uses a workflow",
            "Independent branches earn a graph",
            "A polished prompt can still be false success",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, CASES)

    def test_forward_trials_record_observed_success_and_rework(self) -> None:
        self.assertIn("# Forward Trial Record: 2026-07-24", CASES)
        self.assertIn("did not invent an artifact, graph, or prompt", CASES)
        self.assertIn("before offering justified agent roles", CASES)
        self.assertIn("caused the contract to distinguish nodes from agents", CASES)
        self.assertIn("fixed sequential workflow drawn as a graph", CASES)
        self.assertIn("real operational safety remains unvalidated", CASES)


if __name__ == "__main__":
    unittest.main()
