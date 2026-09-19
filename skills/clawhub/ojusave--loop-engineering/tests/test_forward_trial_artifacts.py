from __future__ import annotations

import json
import hashlib
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TRIAL_DIR = ROOT / "tests" / "forward_trials"


class ForwardTrialArtifactTests(unittest.TestCase):
    def setUp(self) -> None:
        self.trials = [
            json.loads(path.read_text())
            for path in sorted(TRIAL_DIR.glob("prompt_compilation_*.json"))
        ]

    def test_trials_have_reproducible_inputs_outputs_and_candidate_ids(self) -> None:
        self.assertEqual(len(self.trials), 3)
        requests = {trial["user_request"] for trial in self.trials}
        self.assertEqual(len(requests), 1)

        for trial in self.trials:
            with self.subTest(trial=trial["id"]):
                self.assertTrue(trial["harness_instruction"])
                self.assertTrue(trial["response_lines"])
                self.assertRegex(
                    trial["candidate_identity"]["value"],
                    re.compile(r"^(?:[0-9a-f]{40}|[0-9a-f]{64})$"),
                )
                self.assertIn(
                    trial["candidate_identity"]["kind"],
                    {"git_commit", "git_tree", "behavior_manifest_sha256"},
                )

    def test_current_candidate_behavior_manifest_matches_trial(self) -> None:
        trial = next(
            trial
            for trial in self.trials
            if trial["id"] == "prompt-compilation-candidate-v2"
        )
        digest = hashlib.sha256()
        for relative in trial["candidate_identity"]["files"]:
            digest.update(relative.encode())
            digest.update(b"\0")
            digest.update((ROOT / relative).read_bytes())
            digest.update(b"\0")
        self.assertEqual(
            digest.hexdigest(),
            trial["candidate_identity"]["value"],
        )

    def test_recorded_evaluator_decisions_are_executable(self) -> None:
        for trial in self.trials:
            response = "\n".join(trial["response_lines"])
            passed = all(
                phrase in response for phrase in trial["pass_required"]
            ) and all(
                phrase not in response for phrase in trial["pass_forbidden"]
            )
            observed = "PASS" if passed else "REWORK_REQUIRED"
            with self.subTest(trial=trial["id"]):
                self.assertEqual(observed, trial["evaluator_decision"])
                self.assertTrue(trial["evaluator_reason"])

    def test_meta_change_shows_rework_then_recovery(self) -> None:
        decisions = {
            trial["id"]: trial["evaluator_decision"] for trial in self.trials
        }
        self.assertEqual(decisions["prompt-compilation-baseline"], "PASS")
        self.assertEqual(
            decisions["prompt-compilation-candidate-v1"],
            "REWORK_REQUIRED",
        )
        self.assertEqual(decisions["prompt-compilation-candidate-v2"], "PASS")


if __name__ == "__main__":
    unittest.main()
