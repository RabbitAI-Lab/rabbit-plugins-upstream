from __future__ import annotations

import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = (ROOT / "SKILL.md").read_text()
ORCHESTRATION = (ROOT / "references" / "orchestration.md").read_text()
INIT_STATE = (ROOT / "scripts" / "init_loop_state.py").read_text()
CREATE_HANDOFF = ROOT / "scripts" / "create_handoff.py"
INIT_LOOP_STATE = ROOT / "scripts" / "init_loop_state.py"
CASES = (ROOT / "tests" / "execution_topology_cases.md").read_text()


class ExecutionTopologyContractTests(unittest.TestCase):
    def test_keeps_single_loop_as_the_default(self) -> None:
        self.assertIn("Deep is not automatically graph-shaped", SKILL)
        self.assertIn("Default to one adaptive parent loop", ORCHESTRATION)
        self.assertIn("Do not create an explicit graph merely because the task is Deep", ORCHESTRATION)

    def test_routes_only_material_deep_topologies(self) -> None:
        for phrase in (
            "genuinely independent workstreams",
            "distinct tools, permissions, failure boundaries, or approval gates",
            "converge through a verified integration or decision",
            "resume without restarting completed work",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, ORCHESTRATION)
        self.assertIn("declare an execution topology before creating handoffs", SKILL)

    def test_topology_records_execution_contract(self) -> None:
        for field in (
            "Node or check owner",
            "Depends on",
            "Input and artifact",
            "Output contract",
            "Status and budget",
            "Failure route",
            "Merge owner",
            "Approval gate",
        ):
            with self.subTest(field=field):
                self.assertIn(field, ORCHESTRATION)
        self.assertIn("## Execution topology (Deep only)", INIT_STATE)
        self.assertIn("Topology declaration:", INIT_STATE)

    def test_parallel_merge_recovery_and_resume_are_bounded(self) -> None:
        for phrase in (
            "dependencies are satisfied",
            "Parallelize only nodes that do not require one another's unfinished work",
            "Before fan-in",
            "Retry only the failed or invalidated branch",
            "Propagate invalidation to dependent nodes",
            "On resume",
            "verify external state before repeating actions",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, ORCHESTRATION)

    def test_adhd_companion_is_active_but_optional(self) -> None:
        self.assertIn("When the user activates `i-have-adhd`", SKILL)
        self.assertIn("use its loaded contract for progress and final responses", SKILL)
        self.assertIn("Do not make the optional companion skill a prerequisite", SKILL)

    def test_cases_cover_simple_parallel_dependent_and_false_success_paths(self) -> None:
        self.assertEqual(CASES.count("## Case "), 5)
        for title in (
            "Narrow fix stays in one loop",
            "Sequential checks do not require a graph",
            "Independent research branches converge",
            "Dependent delivery resumes safely",
            "Passing branches with an incomplete merge",
        ):
            with self.subTest(title=title):
                self.assertIn(title, CASES)

    def test_forward_trials_record_routing_without_overclaiming(self) -> None:
        self.assertIn("# Forward Trial Record: 2026-07-24", CASES)
        for phrase in (
            "created no graph, state, handoff, or specialist ceremony",
            "bounded branch effort",
            "invalidated affected downstream evidence",
            "verify routing and instruction behavior, not production outcomes",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, CASES)

    def _state(self, mode: str, declaration: str = "") -> str:
        return f"""# Loop state

- **mode:** {mode}

## Starting point

Baseline

## Target

Target

## Measure and threshold

Measure

## Proof required

ARTIFACT VERIFIED

## Guardrails and exclusions

Guardrails

## Next use or decision

Decision

## Execution topology (Deep only)

Topology declaration: {declaration}

For each node record: stable identifier and check owner; dependencies; required input and durable artifact; output contract; status and budget; failure route; merge owner; approval gate.
"""

    def _create_handoff(self, mode: str, declaration: str = "") -> subprocess.CompletedProcess[str]:
        with tempfile.TemporaryDirectory() as temp:
            state_dir = Path(temp)
            (state_dir / "state.md").write_text(self._state(mode, declaration))
            return subprocess.run(
                [
                    "python3",
                    str(CREATE_HANDOFF),
                    "--from-loop",
                    "parent",
                    "--to-loop",
                    "reviewer",
                    "--objective",
                    "Review",
                    "--artifact",
                    "artifact",
                    "--uncertainty",
                    "uncertainty",
                    "--acceptance",
                    "checks",
                    "--state-dir",
                    str(state_dir),
                ],
                capture_output=True,
                text=True,
                check=False,
            )

    def test_deep_handoff_rejects_blank_topology_declaration(self) -> None:
        result = self._create_handoff("deep")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("complete the Topology declaration", result.stderr)

    def test_generated_deep_template_rejects_blank_topology_declaration(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            initialized = subprocess.run(
                [
                    "python3",
                    str(INIT_LOOP_STATE),
                    "--task",
                    "generated template gate",
                    "--mode",
                    "deep",
                    "--root",
                    temp,
                ],
                capture_output=True,
                text=True,
                check=True,
            )
            state_dir = Path(initialized.stdout.strip())
            state_path = state_dir / "state.md"
            state = state_path.read_text()
            for heading, value in (
                ("Starting point", "Baseline"),
                ("Target", "Target"),
                ("Measure and threshold", "Measure"),
                ("Proof required", "ARTIFACT VERIFIED"),
                ("Guardrails and exclusions", "Guardrails"),
                ("Next use or decision", "Decision"),
            ):
                state = state.replace(
                    f"## {heading}\n\n",
                    f"## {heading}\n\n{value}\n\n",
                    1,
                )
            state_path.write_text(state)
            result = subprocess.run(
                [
                    "python3",
                    str(CREATE_HANDOFF),
                    "--from-loop",
                    "parent",
                    "--to-loop",
                    "reviewer",
                    "--objective",
                    "Review",
                    "--artifact",
                    "artifact",
                    "--uncertainty",
                    "uncertainty",
                    "--acceptance",
                    "checks",
                    "--state-dir",
                    str(state_dir),
                ],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("complete the Topology declaration", result.stderr)

    def test_deep_handoff_accepts_declared_single_parent_loop(self) -> None:
        result = self._create_handoff(
            "deep",
            "Single parent loop; no explicit topology required.",
        )
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_standard_handoff_does_not_require_topology_declaration(self) -> None:
        result = self._create_handoff("standard")
        self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == "__main__":
    unittest.main()
