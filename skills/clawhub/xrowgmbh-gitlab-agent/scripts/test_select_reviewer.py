#!/usr/bin/env python3
"""Regression tests for deterministic reviewer selection."""

from __future__ import annotations

import importlib.util
import io
import json
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest.mock import Mock, patch


SCRIPT = Path(__file__).resolve().parent / "select-reviewer.py"
SPEC = importlib.util.spec_from_file_location("select_reviewer", SCRIPT)
assert SPEC and SPEC.loader
reviewer = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(reviewer)


ME = {"id": 99, "username": "robot"}
PROJECT = {"id": 1, "default_branch": "main"}
MR = {
    "iid": 7,
    "state": "opened",
    "sha": "abc",
    "author": {"id": 99, "username": "robot"},
    "assignees": [{"id": 99, "username": "robot"}],
    "reviewers": [{"id": 77, "username": "existing"}],
}
MEMBERS = [
    {
        "id": 99,
        "username": "robot",
        "access_level": 30,
        "state": "active",
        "locked": False,
    },
    {
        "id": 2,
        "username": "andyxrow",
        "access_level": 40,
        "state": "active",
        "locked": False,
    },
    {
        "id": 3,
        "username": "xrow",
        "access_level": 50,
        "state": "active",
        "locked": False,
    },
]


def linked(author_id: int, username: str, iid: int = 19) -> dict[str, object]:
    return {"id": iid, "iid": iid, "author": {"id": author_id, "username": username}}


class ReviewerSelectionTests(unittest.TestCase):
    def run_selection(
        self,
        *,
        linked_items=None,
        members=None,
        agents=False,
        apply=False,
        changed=False,
    ):
        linked_items = [] if linked_items is None else linked_items
        members = MEMBERS if members is None else members
        fresh_mr = {**MR, "sha": "changed"} if changed else MR
        objects = [ME, PROJECT, MR]
        if apply:
            objects.extend([MEMBERS[1], fresh_mr])

        def pages(endpoint, _description):
            if "/members/all" in endpoint:
                return members
            if "/closes_issues" in endpoint:
                return linked_items
            if "/repository/tree" in endpoint:
                return [{"path": "AGENTS.md"}] if agents else []
            raise AssertionError(endpoint)

        command = Mock()
        stdout = io.StringIO()
        with patch.object(reviewer.shutil, "which", return_value="/usr/bin/glab"), patch.object(
            reviewer, "api_object", side_effect=objects
        ), patch.object(reviewer, "api_pages", side_effect=pages), patch.object(
            reviewer,
            "api_text",
            return_value="| reviewers | [xrow](https://gitlab.com/xrow) |\n",
        ), patch.object(reviewer.subprocess, "run", command), redirect_stdout(stdout):
            reviewer.main(
                [*( ["--apply"] if apply else []), "example/project", "7"]
            )
        return json.loads(stdout.getvalue()), command

    def test_prefers_unique_linked_work_item_author(self):
        result, _command = self.run_selection(
            linked_items=[linked(2, "andyxrow")], agents=True
        )
        self.assertEqual(result["reviewer"]["username"], "andyxrow")
        self.assertEqual(result["rule"], "linked-work-item-author")

    def test_prefers_configured_reviewer_without_linked_author(self):
        result, _command = self.run_selection(agents=True)
        self.assertEqual(result["reviewer"]["username"], "xrow")
        self.assertEqual(result["rule"], "configured-reviewer")

    def test_falls_back_to_maintainer_then_owner(self):
        result, _command = self.run_selection()
        self.assertEqual(result["reviewer"]["username"], "andyxrow")
        self.assertEqual(result["rule"], "maintainer-fallback")
        owner_only = [MEMBERS[0], MEMBERS[2]]
        result, _command = self.run_selection(members=owner_only)
        self.assertEqual(result["reviewer"]["username"], "xrow")
        self.assertEqual(result["rule"], "owner-fallback")

    def test_fails_on_ambiguous_authors_or_incomplete_membership(self):
        cases = [
            {
                "linked_items": [linked(2, "andyxrow"), linked(3, "xrow", 20)],
            },
            {
                "members": [
                    {
                        "id": 2,
                        "username": "andyxrow",
                        "access_level": 40,
                        "state": "active",
                    }
                ]
            },
        ]
        for arguments in cases:
            with (
                self.subTest(arguments=arguments),
                redirect_stderr(io.StringIO()),
                self.assertRaises(SystemExit),
            ):
                self.run_selection(**arguments)

    def test_apply_preserves_existing_reviewer(self):
        result, command = self.run_selection(
            linked_items=[linked(2, "andyxrow")], apply=True
        )
        self.assertTrue(result["applied"])
        body = json.loads(command.call_args.kwargs["input"])
        self.assertEqual(body["reviewer_ids"], [2, 77])

    def test_apply_fails_if_merge_request_changed(self):
        with redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
            self.run_selection(
                linked_items=[linked(2, "andyxrow")], apply=True, changed=True
            )

    def test_pagination_loops_until_a_short_page(self):
        first_page = [{"id": value} for value in range(100)]
        with patch.object(
            reviewer, "api_text", side_effect=[json.dumps(first_page), '[{"id":100}]']
        ) as api_text:
            records = reviewer.api_pages("projects/example/members", "members")
        self.assertEqual(len(records), 101)
        self.assertIn("page=1", api_text.call_args_list[0].args[0])
        self.assertIn("page=2", api_text.call_args_list[1].args[0])


if __name__ == "__main__":
    unittest.main()
