"""Live-fact continuation regressions: external changes need no MR activity change."""

from copy import deepcopy
import importlib.util
import json
import os
from pathlib import Path
import subprocess
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch
from urllib.parse import parse_qs, urlsplit


spec = importlib.util.spec_from_file_location("resume_work", Path(__file__).with_name("resume-work.py"))
resume = importlib.util.module_from_spec(spec)
spec.loader.exec_module(resume)
NOW = "2026-10-29T16:00:00Z"
EARLIER = "2026-10-28T10:00:00Z"


def item(iid=588, workflow="paused", priority=None):
    return {"kind": "merge_request", "project_id": 42, "iid": iid,
            "web_url": f"https://gitlab.com/team/project/-/merge_requests/{iid}",
            "title": f"Task {iid}", "state": "opened", "created_at": EARLIER,
            "updated_at": EARLIER, "user_notes_count": 0,
            "activity_cursor": {"updated_at": EARLIER, "user_notes_count": 0},
            "labels": [f"workflow::{workflow}"] + ([f"priority::{priority}"] if priority else []),
            "assignees": [{"id": 7, "username": "robot"}],
            "source_branch": f"fix/{iid}", "head_pipeline": {"id": iid + 1000, "status": "skipped"}}


def action(kind="prepare", guards=(), name="continue"):
    return {"id": name, "kind": kind, "guards": list(guards)}


def dispatch():
    return action("dispatch_ci", [
        {"kind": "project_ci_idle", "project_id": 42, "refs": ["main", "dev"]},
        {"kind": "agent_capacity", "limit": 2},
        {"kind": "pipeline_terminal", "project_id": 42, "pipeline_id": 9}])


def state(rows, actions=None):
    return {"version": 1, "items": {r["web_url"]: {
        "first_pending_at": EARLIER, "audited_cursor": r["activity_cursor"],
        "actions": actions or [action()]} for r in rows}}


def owner_config(directory):
    path = Path(directory) / "openclaw.json"
    path.write_text(json.dumps({"skills": {"entries": {"gitlab-agent": {"config": {"owner": "robot"}}}}}))
    return str(path)


class Fixture:
    def __init__(self, rows):
        self.rows = {r["iid"]: deepcopy(r) for r in rows}
        self.calls = []
        self.pipelines = []
        self.child_status = "success"
        self.dependency_state = "closed"
        self.fail = None

    def api(self, endpoint):
        self.calls.append(endpoint)
        if self.fail and self.fail in endpoint:
            raise subprocess.TimeoutExpired(["glab", "api"], 25)
        if endpoint == "user":
            return {"id": 7, "username": "robot"}
        if endpoint == "projects/42":
            return {"archived": False}
        if endpoint.startswith("merge_requests?state=opened&scope=assigned_to_me"):
            return list(self.rows.values())
        if endpoint.startswith("projects/42/merge_requests/"):
            return deepcopy(self.rows[int(endpoint.rsplit("/", 1)[-1])])
        if endpoint == "projects/42/issues/447":
            return {"state": self.dependency_state}
        if endpoint == "projects/42/pipelines/9":
            return {"status": "failed"}
        if endpoint == "projects/42/pipelines/10":
            return {"status": self.child_status}
        if "/pipelines/9/bridges?" in endpoint:
            return [{"downstream_pipeline": {"project_id": 42, "id": 10}}]
        if "/pipelines/10/bridges?" in endpoint:
            return []
        if endpoint.startswith("projects/42/pipelines?"):
            status = parse_qs(urlsplit(endpoint).query)["status"][0]
            return [p for p in self.pipelines if p["status"] == status]
        raise AssertionError(endpoint)

    def live(self):
        with TemporaryDirectory() as directory, patch.dict(os.environ, OPENCLAW_CONFIG_PATH=owner_config(directory)):
            return resume.LiveGitLab(self.api)


class ContinuationTests(unittest.TestCase):
    def test_unchanged_paused_mr_resumes_when_main_and_old_child_finish(self):
        row = item()
        fixture = Fixture([row])
        fixture.pipelines = [{"id": 1, "ref": "main", "status": "running", "source": "push"}]
        fixture.child_status = "running"
        pending = state([row], [dispatch()])
        blocked = resume.plan([row], pending, fixture.live(), NOW)
        self.assertIsNone(blocked["next"])
        fixture.pipelines = []
        # A failed root is not terminal lifecycle evidence while its child runs.
        child_running = resume.plan([row], blocked["state"], fixture.live(), NOW)
        self.assertIsNone(child_running["next"])
        fixture.child_status = "success"
        resumed = resume.plan([row], child_running["state"], fixture.live(), NOW)
        self.assertEqual(resumed["next"]["url"], row["web_url"])
        self.assertEqual(fixture.rows[588]["activity_cursor"], row["activity_cursor"])
        self.assertEqual(resumed["state"]["items"][row["web_url"]]["first_pending_at"], EARLIER)

    def test_every_eligible_open_workflow_state_is_reassessed(self):
        guard = {"kind": "issue_closed", "project_id": 42, "iid": 447}
        for workflow in ("blocked", "paused", "in-progress", "backlog", "review", "need-human", "stale"):
            with self.subTest(workflow=workflow):
                row = item(workflow=workflow)
                fixture = Fixture([row]);fixture.dependency_state = "opened"
                pending = state([row], [action(guards=[guard])])
                self.assertIsNone(resume.plan([row], pending, fixture.live(), NOW)["next"])
                fixture.dependency_state = "closed"
                self.assertIsNotNone(resume.plan([row], pending, fixture.live(), NOW)["next"])

    def test_blocked_dispatch_does_not_block_independent_source_work(self):
        row = item();fixture = Fixture([row])
        fixture.pipelines = [{"id": 1, "ref": "main", "status": "pending", "source": "push"}]
        result = resume.plan([row], state([row], [dispatch(), action(name="prepare-source")]), fixture.live(), NOW)
        self.assertEqual(result["next"]["action"]["id"], "prepare-source")

    def test_waiting_high_priority_item_does_not_starve_next_runnable_item(self):
        rows = [item(602, priority="blocker"), item(588)]
        fixture = Fixture(rows);fixture.dependency_state = "opened"
        pending = state(rows)
        pending["items"][rows[0]["web_url"]]["actions"] = [action(guards=[
            {"kind": "issue_closed", "project_id": 42, "iid": 447}])]
        result = resume.plan(rows, pending, fixture.live(), NOW)
        self.assertEqual(result["next"]["url"], rows[1]["web_url"])

    def test_old_continuation_precedes_recently_served_peer_after_restart(self):
        rows = [item(611), item(588)]  # Keep the existing newest-first UI/discovery order.
        fixture = Fixture(rows);pending = state(rows)
        pending["items"][rows[0]["web_url"]]["last_attempt_at"] = "2026-10-29T15:00:00Z"
        restarted = json.loads(json.dumps(pending))
        result = resume.plan(rows, restarted, fixture.live(), NOW)
        self.assertEqual(result["next"]["url"], rows[1]["web_url"])
        # Planning/activity inspection alone never resets scheduling age.
        self.assertEqual(result["state"], restarted)

    def test_priority_and_audited_owner_preemption_remain_authoritative(self):
        rows = [item(588), item(602, priority="blocker")]
        fixture = Fixture(rows);pending = state(rows)
        self.assertEqual(resume.plan(rows, pending, fixture.live(), NOW)["next"]["url"], rows[1]["web_url"])
        chosen = resume.plan(rows, pending, fixture.live(), NOW, preempt=[rows[0]["web_url"]])
        self.assertEqual(chosen["next"]["url"], rows[0]["web_url"])

    def test_closed_unassigned_forbidden_and_denied_items_cannot_be_selected(self):
        for change in ({"state": "closed"}, {"assignees": []}, {"labels": ["workflow::forbidden"]}):
            row = item();fixture = Fixture([row]);fixture.rows[588].update(change)
            self.assertEqual(resume.plan([row], state([row]), fixture.live(), NOW)["excluded"], [row["web_url"]])
        row = item();fixture = Fixture([row]);live = fixture.live()
        with patch.object(live, "authorized", return_value=False):
            result = resume.plan([row], state([row]), live, NOW)
        self.assertIsNone(result["next"])
        self.assertFalse(any("merge_requests" in c for c in fixture.calls))

    def test_changed_human_feedback_triggers_assessment_not_an_approval(self):
        row = item(workflow="need-human");fixture = Fixture([row])
        pending = state([row], [action("assess", [
            {"kind": "activity_changed", "baseline_cursor": row["activity_cursor"]}])])
        self.assertIsNone(resume.plan([row], pending, fixture.live(), NOW)["next"])
        fixture.rows[588]["user_notes_count"] = 1
        result = resume.plan([row], pending, fixture.live(), NOW)
        self.assertEqual(result["next"]["action"]["kind"], "assess")

    def test_unknown_or_failed_live_checks_are_not_ready_or_exhausted(self):
        row = item();fixture = Fixture([row]);fixture.fail = "/pipelines?"
        result = resume.plan([row], state([row], [dispatch()]), fixture.live(), NOW)
        self.assertIsNone(result["next"])
        self.assertTrue(result["needs_recheck"])
        self.assertFalse(result["no_runnable_work"])

    def test_unknown_item_does_not_suppress_other_independent_work(self):
        rows = [item(602), item(588)];fixture = Fixture(rows);fixture.fail = "merge_requests/602"
        pending = state(rows)
        result = resume.plan(rows, pending, fixture.live(), NOW)
        self.assertEqual(result["next"]["url"], rows[1]["web_url"])
        self.assertEqual(result["state"]["items"][rows[0]["web_url"]], pending["items"][rows[0]["web_url"]])

    def test_capacity_counts_work_roots_not_children_or_unassigned_mrs(self):
        rows = [item(588), item(611)];fixture = Fixture(rows)
        fixture.pipelines = [
            {"id": 11, "ref": "refs/merge-requests/611/head", "status": "running", "source": "merge_request_event"},
            {"id": 12, "ref": "refs/merge-requests/611/head", "status": "running", "source": "parent_pipeline"},
            {"id": 13, "ref": "refs/merge-requests/900/head", "status": "running", "source": "merge_request_event"}]
        guard = {"kind": "agent_capacity", "limit": 2}
        self.assertTrue(fixture.live().guard(guard, rows[0], rows, True))
        fixture.pipelines.append({"id": 14, "ref": "fix/588", "status": "pending", "source": "push"})
        self.assertFalse(fixture.live().guard(guard, rows[0], rows, True))

    def test_targeted_queue_cannot_hide_other_assigned_work_from_capacity(self):
        rows = [item(588), item(611)];fixture = Fixture(rows)
        fixture.pipelines = [{"id": 11, "ref": "fix/611", "status": "running", "source": "push"}]
        guard = {"kind": "agent_capacity", "limit": 1}
        self.assertFalse(fixture.live().guard(guard, rows[0], [rows[0]], True))

    def test_changed_activity_requires_audit_before_old_action_can_execute(self):
        row = item();fixture = Fixture([row]);pending = state([row], [dispatch()])
        fixture.rows[588]["user_notes_count"] = 1
        result = resume.plan([row], pending, fixture.live(), NOW)
        self.assertEqual(result["next"]["action"]["kind"], "assess")
        updated = resume.plan([row], result["state"], fixture.live(), NOW,
                              updates={row["web_url"]: [dispatch()]})
        self.assertEqual(updated["next"]["action"]["kind"], "dispatch_ci")

    def test_pipeline_guard_paginates_before_declaring_a_branch_idle(self):
        row = item();fixture = Fixture([row]);api = fixture.api
        def paginated(endpoint):
            if endpoint.startswith("projects/42/pipelines?status=running"):
                if "page=2" in endpoint:
                    return [{"id": 999, "ref": "main", "status": "running", "source": "push"}]
                return [{"id": i + 1, "ref": "other", "status": "running", "source": "push"} for i in range(100)]
            return api(endpoint)
        with TemporaryDirectory() as directory, patch.dict(os.environ, OPENCLAW_CONFIG_PATH=owner_config(directory)):
            live = resume.LiveGitLab(paginated)
        result = resume.plan([row], state([row], [dispatch()]), live, NOW)
        self.assertIsNone(result["next"])

    def test_dependency_mr_must_be_merged_not_closed(self):
        row = item();dependency = item(600);fixture = Fixture([row, dependency])
        guard = {"kind": "mr_merged", "project_id": 42, "iid": 600}
        pending = state([row], [action(guards=[guard])])
        fixture.rows[600]["state"] = "closed"
        self.assertIsNone(resume.plan([row], pending, fixture.live(), NOW)["next"])
        fixture.rows[600]["state"] = "merged"
        self.assertIsNotNone(resume.plan([row], pending, fixture.live(), NOW)["next"])

    def test_missing_or_unsupported_guards_cannot_enable_dispatch(self):
        row = item();fixture = Fixture([row])
        for a in (action("dispatch_ci"), action(guards=[{"kind": "trust-old-checkpoint"}])):
            with self.subTest(action=a):
                result = resume.plan([row], state([row], [a]), fixture.live(), NOW)
                self.assertIsNone(result["next"])
                self.assertTrue(result["needs_recheck"])

    def test_new_or_legacy_items_get_an_explicit_next_action_assessment(self):
        row = item(workflow="blocked");fixture = Fixture([row])
        result = resume.plan([row], {}, fixture.live(), NOW)
        self.assertEqual(result["next"]["action"]["kind"], "assess")

    def test_same_snapshot_produces_identical_plan(self):
        rows = [item(611), item(588)];fixture = Fixture(rows)
        self.assertEqual(resume.plan(rows, state(rows), fixture.live(), NOW),
                         resume.plan(rows, state(rows), fixture.live(), NOW))

    def test_preemption_cannot_reintroduce_a_forbidden_target(self):
        row = item(workflow="forbidden");other = item(611);fixture = Fixture([row, other])
        result = resume.plan([row, other], state([row, other]), fixture.live(), NOW, preempt=[row["web_url"]])
        self.assertEqual(result["next"]["url"], other["web_url"])
        self.assertEqual(result["ineligible_preemptions"], [row["web_url"]])

    def test_incomplete_pipeline_metadata_does_not_mean_idle(self):
        row = item();fixture = Fixture([row])
        fixture.pipelines = [{"id": 1, "status": "running", "source": "push"}]
        result = resume.plan([row], state([row], [dispatch()]), fixture.live(), NOW)
        self.assertIsNone(result["next"])
        self.assertTrue(result["needs_recheck"])

    def test_empty_legacy_action_list_cannot_make_an_open_item_disappear(self):
        row = item();fixture = Fixture([row]);pending = state([row])
        pending["items"][row["web_url"]]["actions"] = []
        result = resume.plan([row], pending, fixture.live(), NOW)
        self.assertTrue(result["needs_recheck"])
        self.assertFalse(result["no_runnable_work"])

    def test_malformed_live_metadata_is_unknown_not_an_empty_queue(self):
        for change in ({"state": None}, {"assignees": None}, {"labels": None}, {"source_branch": None}):
            with self.subTest(change=change):
                row = item();fixture = Fixture([row]);fixture.rows[588].update(change)
                result = resume.plan([row], state([row]), fixture.live(), NOW)
                self.assertTrue(result["needs_recheck"])
                self.assertFalse(result["no_runnable_work"])

    def test_excluded_and_temporarily_missing_items_keep_resume_history(self):
        row = item();pending = state([row], [dispatch()]);fixture = Fixture([row])
        fixture.rows[588]["assignees"] = []
        result = resume.plan([row], pending, fixture.live(), NOW)
        self.assertEqual(result["state"], pending)
        self.assertIsNone(result["next"])
        missing = resume.plan([], pending, fixture.live(), NOW)
        self.assertEqual(missing["state"], pending)
        self.assertIsNone(missing["next"])

    def test_atomic_replace_failure_preserves_previous_checkpoint(self):
        with TemporaryDirectory() as directory:
            path = Path(directory) / "state.json";path.write_text('{"previous":true}')
            with patch.object(resume.os, "replace", side_effect=OSError("disk failure")):
                with self.assertRaises(OSError):
                    resume.save_state(path, {"new": True})
            self.assertEqual(json.loads(path.read_text()), {"previous": True})
            self.assertEqual(list(Path(directory).iterdir()), [path])

    def test_api_transport_is_bounded_and_read_only(self):
        with patch.object(resume.subprocess, "run") as run:
            run.return_value.stdout = "{}"
            resume.read_api("projects/42")
        self.assertEqual(run.call_args.args[0], ["glab", "api", "projects/42"])
        self.assertEqual(run.call_args.kwargs["timeout"], 25)
        self.assertNotIn("shell", run.call_args.kwargs)

    def test_cli_persists_fair_selection_across_processes_without_gitlab_writes(self):
        with TemporaryDirectory() as directory:
            root = Path(directory);binary = root / "bin";binary.mkdir()
            rows = [item(611), item(588)];pending = state(rows)
            for record in pending["items"].values():
                record["first_pending_at"] = "2000-01-01T00:00:00Z"
            pending["items"][rows[0]["web_url"]]["last_attempt_at"] = "2001-01-01T00:00:00Z"
            fixture = {"user": {"id": 7, "username": "robot"}, "projects/42": {"archived": False},
                       **{f"projects/42/merge_requests/{r['iid']}": r for r in rows}}
            (root / "fixture.json").write_text(json.dumps(fixture))
            (root / "items.json").write_text(json.dumps(rows))
            (root / "state.json").write_text(json.dumps(pending))
            executable = binary / "glab"
            executable.write_text(
                "#!/usr/bin/env python3\nimport json,os,sys\nfrom pathlib import Path\n"
                "assert len(sys.argv)==3 and sys.argv[1]=='api', sys.argv\n"
                "with open(os.environ['TASK_API_LOG'],'a') as f: f.write(json.dumps(sys.argv[1:])+'\\n')\n"
                "print(json.dumps(json.loads(Path(os.environ['TASK_FIXTURE']).read_text())[sys.argv[2]]))\n")
            executable.chmod(0o755)
            env = {**os.environ, "PATH": f"{binary}{os.pathsep}{os.environ['PATH']}",
                   "OPENCLAW_CONFIG_PATH": owner_config(root), "TASK_FIXTURE": str(root / "fixture.json"),
                   "TASK_API_LOG": str(root / "api.log"), "PYTHONDONTWRITEBYTECODE": "1"}
            command = ["python3", str(Path(resume.__file__)), "--items", str(root / "items.json"),
                       "--state", str(root / "state.json"), "--claim"]
            first = subprocess.run(command, env=env, text=True, capture_output=True, check=True)
            second = subprocess.run(command, env=env, text=True, capture_output=True, check=True)
            self.assertEqual(json.loads(first.stdout)["next"]["url"], rows[1]["web_url"])
            self.assertEqual(json.loads(second.stdout)["next"]["url"], rows[0]["web_url"])
            persisted = json.loads((root / "state.json").read_text())
            self.assertEqual(persisted["items"][rows[1]["web_url"]]["first_pending_at"], "2000-01-01T00:00:00Z")
            before = (root / "state.json").read_bytes()
            (root / "bad-actions.json").write_text(json.dumps({rows[0]["web_url"]: [action("dispatch_ci")]}))
            failed = subprocess.run(command + ["--actions", str(root / "bad-actions.json")],
                                    env=env, text=True, capture_output=True)
            self.assertEqual(failed.returncode, 1)
            self.assertEqual((root / "state.json").read_bytes(), before)
            check_idle = subprocess.run(command[:-1] + ["--check-idle"],
                                        env=env, text=True, capture_output=True)
            self.assertEqual(check_idle.returncode, 3)
            self.assertFalse(json.loads(check_idle.stdout)["no_runnable_work"])
            self.assertEqual((root / "state.json").read_bytes(), before)
            del fixture["projects/42/merge_requests/588"]
            (root / "fixture.json").write_text(json.dumps(fixture))
            partial = subprocess.run(command[:-1] + ["--check-idle"],
                                     env=env, text=True, capture_output=True)
            self.assertEqual(partial.returncode, 2)
            self.assertTrue(json.loads(partial.stdout)["needs_recheck"])
            self.assertEqual((root / "state.json").read_bytes(), before)
            self.assertTrue(all(json.loads(line)[0] == "api" for line in (root / "api.log").read_text().splitlines()))


if __name__ == "__main__":
    unittest.main()
