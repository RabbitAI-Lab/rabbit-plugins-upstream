#!/usr/bin/env python3
"""Regression tests for the GitLab access gate and active-item listing."""

from __future__ import annotations

import importlib.util
import io
import json
import os
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest.mock import patch


SCRIPT_DIR = Path(__file__).resolve().parent


def load_script(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, SCRIPT_DIR / filename)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


access = load_script("check_project_access", "check-project-access.py")
active = load_script("list_active_items", "list-active-items.py")


USER = {"id": 33363466, "username": "eugene-harold-krabs"}
MEMBERSHIP = {
    "username": "eugene-harold-krabs",
    "access_level": 30,
    "membership_state": "active",
    "created_by": {"username": "xrow"},
}


class AccessGateTests(unittest.TestCase):
    @patch.object(access.shutil, "which", return_value="/usr/bin/glab")
    @patch.object(access, "update_labels")
    @patch.object(access, "api_json", side_effect=[USER, MEMBERSHIP])
    def test_allows_owner_created_membership(self, api_json, update_labels, _which):
        output = io.StringIO()
        with redirect_stdout(output):
            self.assertEqual(access.main(["xrow-public/ci-tools", "xrow"]), 0)
        update_labels.assert_not_called()
        self.assertIn("[allowed]", output.getvalue())
        self.assertEqual(api_json.call_count, 2)

    @patch.object(access.shutil, "which", return_value="/usr/bin/glab")
    @patch.object(access, "update_labels")
    @patch.object(access, "api_json", side_effect=[USER, MEMBERSHIP])
    def test_removes_forbidden_label_on_allowed_object(
        self, _api_json, update_labels, _which
    ):
        with redirect_stdout(io.StringIO()):
            self.assertEqual(
                access.main(
                    ["xrow-public/ci-tools", "xrow", "issue", "7"]
                ),
                0,
            )
        update_labels.assert_called_once_with(
            "projects/xrow-public%2Fci-tools/issues/7", allowed=True
        )

    @patch.object(access.shutil, "which", return_value="/usr/bin/glab")
    @patch.object(access, "update_labels")
    def test_creator_mismatch_sets_forbidden(self, update_labels, _which):
        membership = {**MEMBERSHIP, "created_by": {"username": "mallory"}}
        with patch.object(access, "api_json", side_effect=[USER, membership]):
            with redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as error:
                access.main(
                    ["xrow-public/ci-tools", "xrow", "merge_request", "8"]
                )
        self.assertEqual(error.exception.code, 77)
        update_labels.assert_called_once_with(
            "projects/xrow-public%2Fci-tools/merge_requests/8", allowed=False
        )

    @patch.object(access.shutil, "which", return_value="/usr/bin/glab")
    @patch.object(access, "update_labels")
    def test_incomplete_or_inactive_memberships_fail_closed(
        self, _update_labels, _which
    ):
        cases = [
            {key: value for key, value in MEMBERSHIP.items() if key != "created_by"},
            {**MEMBERSHIP, "membership_state": "blocked"},
        ]
        for membership in cases:
            with self.subTest(membership=membership):
                with patch.object(access, "api_json", side_effect=[USER, membership]):
                    with redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
                        access.main(["xrow-public/ci-tools", "xrow"])


class LabelSyncTests(unittest.TestCase):
    endpoint = "projects/xrow-public%2Fci-tools/issues/7"

    def sync(self, labels, allowed):
        with patch.object(access, "api_json", return_value={"labels": labels}), patch.object(
            access.subprocess, "run"
        ) as write:
            access.update_labels(self.endpoint, allowed=allowed)
        return write

    def test_repeated_allowed_checks_send_no_write(self):
        for _ in range(2):
            self.sync(["size::small", "type::bug", "workflow::review"], True).assert_not_called()

    def test_repeated_denied_checks_send_no_write(self):
        for _ in range(2):
            self.sync(["type::bug", "workflow::forbidden"], False).assert_not_called()

    def test_allowed_check_removes_only_present_forbidden(self):
        write = self.sync(["type::bug", "workflow::forbidden"], True)
        self.assertEqual(write.call_args.args[0], [
            "glab", "api", "-X", "PUT", self.endpoint,
            "-f", "remove_labels=workflow::forbidden",
        ])
        write.assert_called_once()

    def test_denied_check_sends_only_real_delta(self):
        write = self.sync(["type::bug", "workflow::review"], False)
        self.assertEqual(write.call_args.args[0], [
            "glab", "api", "-X", "PUT", self.endpoint,
            "-f", "add_labels=workflow::forbidden", "-f", "remove_labels=workflow::review",
        ])
        write.assert_called_once()

    def test_denied_check_cleans_other_workflows_without_readding_forbidden(self):
        write = self.sync(["workflow::forbidden", "workflow::custom", "type::bug"], False)
        self.assertEqual(write.call_args.args[0], [
            "glab", "api", "-X", "PUT", self.endpoint,
            "-f", "remove_labels=workflow::custom",
        ])

    def test_empty_labels_add_only_when_denied(self):
        self.sync([], True).assert_not_called()
        write = self.sync([], False)
        self.assertEqual(write.call_args.args[0], [
            "glab", "api", "-X", "PUT", self.endpoint,
            "-f", "add_labels=workflow::forbidden",
        ])

    def test_incomplete_label_reads_never_write(self):
        for payload in ({}, {"labels": None}, {"labels": "workflow::review"}, {"labels": [None]}, []):
            for allowed in (True, False):
                with self.subTest(payload=payload, allowed=allowed):
                    with patch.object(access, "api_json", return_value=payload), patch.object(
                        access.subprocess, "run"
                    ) as write, self.assertRaises(ValueError):
                        access.update_labels(self.endpoint, allowed=allowed)
                    write.assert_not_called()

    @patch.object(access.shutil, "which", return_value="/usr/bin/glab")
    def test_denied_gate_still_exits_forbidden_when_label_is_unchanged(self, _which):
        membership = {**MEMBERSHIP, "created_by": {"username": "mallory"}}
        with patch.object(access, "api_json", side_effect=[USER, membership, {"labels": ["workflow::forbidden"]}]):
            with patch.object(access.subprocess, "run") as write, redirect_stderr(io.StringIO()):
                with self.assertRaises(SystemExit) as error:
                    access.main(["xrow-public/ci-tools", "xrow", "issue", "7"])
            self.assertEqual(error.exception.code, 77)
            write.assert_not_called()

    @patch.object(access.shutil, "which", return_value="/usr/bin/glab")
    def test_missing_labels_fail_closed_without_writes(self, _which):
        with patch.object(access, "api_json", side_effect=[USER, MEMBERSHIP, {}, {}]):
            with patch.object(access.subprocess, "run") as write, redirect_stderr(io.StringIO()):
                with self.assertRaises(SystemExit) as error:
                    access.main(["xrow-public/ci-tools", "xrow", "issue", "7"])
            self.assertEqual(error.exception.code, 77)
            write.assert_not_called()

    @patch.object(access.shutil, "which", return_value="/usr/bin/glab")
    def test_unreadable_labels_fail_closed_without_writes(self, _which):
        errors = (
            access.subprocess.CalledProcessError(1, ["glab", "api"]),
            json.JSONDecodeError("invalid response", "", 0),
        )
        for failure in errors:
            with self.subTest(failure=type(failure).__name__):
                with patch.object(
                    access, "api_json", side_effect=[USER, MEMBERSHIP, failure, failure]
                ), patch.object(access.subprocess, "run") as write:
                    with redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as error:
                        access.main(["xrow-public/ci-tools", "xrow", "issue", "7"])
                    self.assertEqual(error.exception.code, 77)
                    write.assert_not_called()

    def test_state_transitions_then_repeated_checks_write_once(self):
        labels = {"type::bug", "team::platform", "workflow::custom"}
        commands = []

        def read(_endpoint):
            return {"labels": list(labels)}

        def write(command, **_kwargs):
            commands.append(command)
            for field in command[5:]:
                if field.startswith("add_labels="):
                    labels.update(field.split("=", 1)[1].split(","))
                if field.startswith("remove_labels="):
                    labels.difference_update(field.split("=", 1)[1].split(","))

        with patch.object(access, "api_json", side_effect=read), patch.object(
            access.subprocess, "run", side_effect=write
        ):
            access.update_labels(self.endpoint, allowed=False)
            access.update_labels(self.endpoint, allowed=False)
            self.assertEqual(len(commands), 1)
            self.assertEqual(labels, {"type::bug", "team::platform", "workflow::forbidden"})
            access.update_labels(self.endpoint, allowed=True)
            access.update_labels(self.endpoint, allowed=True)
            self.assertEqual(len(commands), 2)
            self.assertEqual(labels, {"type::bug", "team::platform"})


class ActiveItemTests(unittest.TestCase):
    @patch.object(active.shutil, "which", return_value="/usr/bin/glab")
    def test_filters_forbidden_and_other_assignees_without_argument_limits(
        self, _which
    ):
        large_title = "x" * (os.sysconf("SC_ARG_MAX") + 8192)
        issue = {
            "project_id": 1,
            "iid": 1,
            "title": large_title,
            "web_url": "https://gitlab.example/a/-/issues/1",
            "labels": ["workflow::backlog"],
            "assignees": [{"username": "eugene-harold-krabs"}],
            "updated_at": "2026-09-16T10:00:00.000Z",
            "user_notes_count": 7,
        }
        forbidden = {
            **issue,
            "iid": 2,
            "web_url": "https://gitlab.example/b/-/issues/2",
            "labels": ["workflow::forbidden"],
        }
        merge_request = {
            "project_id": 3,
            "iid": 3,
            "title": "active MR",
            "web_url": "https://gitlab.example/c/-/merge_requests/3",
            "labels": [],
            "assignees": [{"username": "eugene-harold-krabs"}],
            "updated_at": "2026-09-16T10:01:00.000Z",
            "user_notes_count": 2,
        }
        other = {
            **merge_request,
            "iid": 4,
            "web_url": "https://gitlab.example/d/-/merge_requests/4",
            "assignees": [{"username": "someone-else"}],
        }
        with patch.object(active, "api_json", return_value=USER), patch.object(
            active,
            "paginated",
            side_effect=[[issue, forbidden], [merge_request, other]],
        ):
            output = io.StringIO()
            with redirect_stdout(output):
                self.assertEqual(active.main(), 0)
        payload = json.loads(output.getvalue())
        self.assertEqual([item["iid"] for item in payload], [1, 3])
        self.assertEqual(len(payload[0]["title"]), len(large_title))
        self.assertEqual(
            payload[0]["activity_cursor"],
            {
                "updated_at": "2026-09-16T10:00:00.000Z",
                "user_notes_count": 7,
            },
        )

    def test_incomplete_activity_metadata_fails_closed(self):
        item = {
            "project_id": 1,
            "iid": 1,
            "title": "missing activity",
            "web_url": "https://gitlab.example/a/-/issues/1",
            "labels": [],
            "assignees": [{"username": "eugene-harold-krabs"}],
        }
        invalid_activity = (
            item,
            {**item, "updated_at": "2026-09-16T10:00:00.000Z"},
            {
                **item,
                "updated_at": "2026-09-16T10:00:00.000Z",
                "user_notes_count": -1,
            },
            {
                **item,
                "updated_at": "2026-09-16T10:00:00.000Z",
                "user_notes_count": True,
            },
        )
        for payload in invalid_activity:
            with self.subTest(payload=payload):
                with self.assertRaises(ValueError):
                    active.normalized(payload, "issue")

    @patch.object(active.shutil, "which", return_value="/usr/bin/glab")
    def test_main_emits_no_partial_queue_when_activity_is_incomplete(self, _which):
        incomplete = {
            "project_id": 1,
            "iid": 1,
            "title": "missing activity",
            "web_url": "https://gitlab.example/a/-/issues/1",
            "labels": [],
            "assignees": [{"username": "eugene-harold-krabs"}],
        }
        output = io.StringIO()
        with patch.object(active, "api_json", return_value=USER), patch.object(
            active, "paginated", side_effect=[[incomplete], []]
        ), redirect_stdout(output), redirect_stderr(io.StringIO()):
            self.assertEqual(active.main(), 69)
        self.assertEqual(output.getvalue(), "")

    def test_pagination_loops_until_a_short_page(self):
        first_page = [{"iid": value} for value in range(100)]
        with patch.object(
            active, "api_json", side_effect=[first_page, [{"iid": 100}]]
        ) as api_json:
            records = active.paginated("issues?state=opened")
        self.assertEqual(len(records), 101)
        self.assertIn("page=1", api_json.call_args_list[0].args[0])
        self.assertIn("page=2", api_json.call_args_list[1].args[0])


if __name__ == "__main__":
    unittest.main()
