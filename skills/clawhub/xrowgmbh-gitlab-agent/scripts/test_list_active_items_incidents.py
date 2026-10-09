"""Regression tests for incident adoption during active-work discovery."""

from __future__ import annotations

import importlib.util
import json
import subprocess
import unittest
from pathlib import Path
from unittest.mock import patch


MODULE_PATH = Path(__file__).with_name("list-active-items.py")
SPEC = importlib.util.spec_from_file_location("list_active_items", MODULE_PATH)
assert SPEC and SPEC.loader
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)


class IncidentDiscoveryTests(unittest.TestCase):
    def test_lists_unassigned_incidents_across_member_projects(self):
        incident = {"iid": 2, "issue_type": "incident", "assignees": []}

        def pages(endpoint):
            if endpoint == "projects?membership=true&simple=true":
                return [{"id": 7}, {"id": 8}]
            if endpoint.startswith("projects/7/"):
                return [incident]
            return []

        with patch.object(module, "paginated", side_effect=pages) as paginated:
            self.assertEqual(module.unassigned_incidents(), [incident])
        self.assertEqual(paginated.call_count, 3)

    def test_adopts_critical_incident_after_membership_gate(self):
        item = {"project_id": 7, "iid": 2, "web_url": "https://gitlab.com/team/project/-/issues/2"}
        current = {
            "issue_type": "incident", "state": "opened", "assignees": [],
            "labels": ["priority::low", "workflow::backlog", "keep"], "severity": "CRITICAL",
        }
        adopted = {**current, "assignees": [{"username": "agent"}]}
        with patch.object(module, "owner_created_membership", return_value=True) as member, patch.object(
            module, "api_json", side_effect=[current, current]
        ) as api, patch.object(
            module.subprocess, "run", return_value=subprocess.CompletedProcess([], 0, json.dumps(adopted))
        ) as run:
            self.assertEqual(module.adopt_incident(item, "agent", 12, "owner"), adopted)
        member.assert_called_once_with("team/project", 12, "agent", "owner")
        self.assertEqual(api.call_count, 2)
        command = run.call_args.args[0]
        self.assertIn("assignee_ids=12", command)
        self.assertIn("add_labels=priority::blocker,type::support,workflow::in-progress", command)
        self.assertIn("remove_labels=priority::low,workflow::backlog", command)

    def test_denied_gate_only_replaces_workflow_label(self):
        item = {"project_id": 7, "iid": 2, "web_url": "https://gitlab.com/team/project/-/issues/2"}
        with patch.object(module, "owner_created_membership", return_value=False), patch.object(
            module, "api_json", return_value={"labels": ["workflow::backlog", "keep"]}
        ) as api, patch.object(module.subprocess, "run") as run:
            self.assertIsNone(module.adopt_incident(item, "agent", 12, "owner"))
        api.assert_called_once_with("projects/team%2Fproject/issues/2")
        command = run.call_args.args[0]
        self.assertIn("add_labels=workflow::forbidden", command)
        self.assertIn("remove_labels=workflow::backlog", command)
        self.assertFalse(any(arg.startswith("assignee_ids=") for arg in command))

    def test_assigned_incident_is_not_overwritten(self):
        item = {"project_id": 7, "iid": 2, "web_url": "https://gitlab.com/team/project/-/issues/2"}
        current = {
            "issue_type": "incident", "state": "opened",
            "assignees": [{"username": "human"}], "labels": [],
        }
        with patch.object(module, "owner_created_membership", return_value=True), patch.object(
            module, "api_json", return_value=current
        ), patch.object(module.subprocess, "run") as run:
            self.assertIsNone(module.adopt_incident(item, "agent", 12, "owner"))
        run.assert_not_called()


if __name__ == "__main__":
    unittest.main()
