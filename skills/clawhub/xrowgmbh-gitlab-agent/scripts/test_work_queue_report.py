"""#144 requirements: ordered read-only work, metadata, scripts and to-dos."""

import importlib.util
import unittest
from pathlib import Path
from unittest.mock import patch

spec = importlib.util.spec_from_file_location("queue_report", Path(__file__).with_name("work-queue-report.py"))
queue = importlib.util.module_from_spec(spec)
spec.loader.exec_module(queue)


def item(iid, *, kind="issue", labels=None):
    return {
        "project_id": 42, "iid": iid, "title": f"Item {iid}", "state": "opened",
        "issue_type": "incident" if kind == "incident" else "issue",
        "web_url": f"https://gitlab.com/team/project/-/{'merge_requests' if kind == 'merge_request' else 'issues'}/{iid}",
        "assignees": [{"username": "robot"}], "labels": labels or [],
        "updated_at": "2026-10-01T12:00:00Z", "user_notes_count": 0,
        "created_at": "2026-09-01T12:00:00Z", "time_stats": {"total_time_spent": 5400},
    }


class QueueReportTests(unittest.TestCase):
    def run_report(self, issues=(), mrs=(), todos=(), current=None, member=True):
        candidates = [*issues, *mrs]

        def api(endpoint):
            if endpoint == "user":
                return {"id": 7, "username": "robot", "name": "Robot"}
            for row in candidates:
                if endpoint == queue.active.object_endpoint(row, "merge_request" if row in mrs else "issue")[1]:
                    return current if current is not None else row
            raise AssertionError(endpoint)

        def pages(endpoint):
            if endpoint.startswith("issues?state"):
                return list(issues)
            if endpoint.startswith("merge_requests?state"):
                return list(mrs)
            if endpoint == "todos?state=pending":
                return list(todos)
            return []

        with patch.object(queue, "read_api", side_effect=api), \
                patch.object(queue.active, "paginated", side_effect=pages), \
                patch.object(queue.active, "configured_owner", return_value="owner"), \
                patch.object(queue.active, "project_is_active", return_value=True), \
                patch.object(queue.active, "owner_created_membership", return_value=member), \
                patch.object(queue.active, "synchronize_forbidden") as labels, \
                patch.object(queue.active, "assign_unassigned_items") as assign, \
                patch.object(queue.active, "adopt_incident") as adopt:
            result = queue.report()
            # Opening a report must not perform scheduled agent mutations.
            labels.assert_not_called()
            assign.assert_not_called()
            adopt.assert_not_called()
            return result

    def test_created_kind_labels_and_total_time_are_visible(self):
        incident = item(1, kind="incident", labels=["priority::high", "size::small", "type::support"])
        mr = item(2, kind="merge_request")
        result = self.run_report([incident], [mr])
        self.assertEqual(result["items"][0]["kind"], "incident")
        self.assertEqual(result["items"][0]["created_at"], incident["created_at"])
        self.assertEqual(result["items"][0]["labels"], incident["labels"])
        self.assertEqual(result["items"][0]["time_spent"], 5400)
        self.assertEqual(result["items"][1]["kind"], "merge_request")

    def test_reuses_discovery_priority_and_blocking_order(self):
        low, high, blocker, root = [item(i, labels=[priority]) for i, priority in (
            (1, "priority::low"), (2, "priority::high"), (3, "priority::blocker"), (4, "priority::high"))]
        with patch.object(queue.active, "is_root_cause", side_effect=lambda row: row["iid"] == 4):
            result = self.run_report([low, high, blocker, root])
        self.assertEqual([row["iid"] for row in result["items"]], [3, 4, 2, 1])

    def test_denied_unassigned_closed_and_unreadable_labels_are_omitted(self):
        row = item(1)
        self.assertEqual(self.run_report([row], member=False)["items"], [])
        for change in ({"assignees": []}, {"state": "closed"}, {"labels": None}):
            with self.subTest(change=change):
                self.assertEqual(self.run_report([row], current={**row, **change})["items"], [])

    def test_pending_todos_include_other_actions_and_preserve_api_order(self):
        todos = [{"id": n, "state": "pending", "target": {"title": str(n), "labels": []},
                  "author": {"username": "owner"}, "action_name": action,
                  "target_url": "https://gitlab.com/team/project/-/issues/1#note_2"}
                 for n, action in [(9, "directly_addressed"), (3, "assigned")]]
        result = self.run_report(todos=todos + [{"state": "done"}])
        self.assertEqual([todo["id"] for todo in result["todos"]], [9, 3])
        self.assertEqual([todo["owner_addressed"] for todo in result["todos"]], [True, False])

    def test_shows_actual_existing_script_sources(self):
        sources = self.run_report()["scripts"]
        by_name = {entry["name"]: entry for entry in sources}
        for name in ("list-active-items.py", "list-directly-addressed-todos.py"):
            self.assertEqual(by_name[name]["source"], (queue.SCRIPT_DIR / name).read_text())

    def test_api_uses_only_bounded_read_command(self):
        with patch.object(queue.subprocess, "run") as run:
            run.return_value.stdout = "[]"
            self.assertEqual(queue.read_api("todos?state=pending"), [])
        self.assertEqual(run.call_args.args[0], ["glab", "api", "todos?state=pending"])
        self.assertEqual(run.call_args.kwargs["timeout"], 25)
        self.assertNotIn("shell", run.call_args.kwargs)


if __name__ == "__main__":
    unittest.main()
