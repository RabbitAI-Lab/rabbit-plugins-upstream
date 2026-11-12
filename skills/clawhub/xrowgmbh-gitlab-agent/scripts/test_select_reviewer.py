#!/usr/bin/env python3
"""Regression tests for deterministic reviewer selection."""

from __future__ import annotations

import importlib.util
import io
import json
import os
import subprocess
import tempfile
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
    "target_branch": "main",
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
        agents_markdown="| reviewers | [xrow](https://gitlab.com/xrow) |\n",
        bot_ids=None,
        apply=False,
        changed=False,
        ignored=None,
        self_review=False,
        optional=False,
        approval_changed=False,
        approval_fails=False,
        can_merge=True,
        can_approve=True,
        mr_overrides=None,
        fresh_members=None,
        fresh_member=None,
        mr_change=None,
        commits=None,
        fresh_commits=None,
        user_emails=None,
    ):
        linked_items = [] if linked_items is None else linked_items
        members = MEMBERS if members is None else members
        selected_mr = {
            **MR,
            **({
                "reviewers": [],
                "draft": False,
                "merge_status": "can_be_merged",
                "detailed_merge_status": "mergeable",
                "blocking_discussions_resolved": True,
                "head_pipeline": {"status": "success", "sha": "abc"},
            } if self_review else {}),
        }
        selected_mr.update(mr_overrides or {})
        fresh_mr = {**selected_mr, "sha": "changed"} if changed else selected_mr
        fresh_mr = {**fresh_mr, **(mr_change or {})}
        bot_ids = set() if bot_ids is None else set(bot_ids)
        ignored = set() if ignored is None else set(ignored)
        commits = [{"id": "commit-one", "committer_email": "xrow@example.com"}] if commits is None else commits
        user_emails = {3: "xrow@example.com"} if user_emails is None else user_emails

        def object_for(endpoint, _description):
            if endpoint == "user":
                return ME
            if endpoint == "projects/example%2Fproject":
                return PROJECT
            if endpoint == "projects/example%2Fproject/merge_requests/7":
                return selected_mr
            if "/members/all/" in endpoint:
                return fresh_member or next(
                    member for member in members
                    if member["id"] == int(endpoint.rsplit("/", 1)[1])
                )
            if endpoint.startswith("users/"):
                user_id = int(endpoint.removeprefix("users/"))
                return {"id": user_id, "bot": user_id in bot_ids,
                        "public_email": user_emails.get(user_id, "")}
            raise AssertionError(endpoint)

        membership_calls = 0
        commit_calls = 0

        def pages(endpoint, _description):
            nonlocal membership_calls, commit_calls
            if endpoint.endswith("/commits"):
                commit_calls += 1
                return fresh_commits if commit_calls > 1 and fresh_commits is not None else commits
            if "/members/all" in endpoint:
                membership_calls += 1
                if membership_calls > 1 and fresh_members is not None:
                    return fresh_members
                return members
            if "/closes_issues" in endpoint:
                return linked_items
            if "/repository/tree" in endpoint:
                return [{"path": "AGENTS.md"}] if agents else []
            raise AssertionError(endpoint)

        object_calls = {"mr": 0}

        def objects(endpoint, description):
            if endpoint == "projects/example%2Fproject/merge_requests/7":
                object_calls["mr"] += 1
                return fresh_mr if apply and object_calls["mr"] > 1 else selected_mr
            return object_for(endpoint, description)

        approval_state_calls = 0

        def api_text(endpoint):
            nonlocal approval_state_calls
            if endpoint.endswith("/repository/branches/main"):
                return json.dumps({"name": "main", "protected": True})
            if endpoint.endswith("/protected_branches/main"):
                return json.dumps({"name": "main", "merge_access_levels": [
                    {"access_level": 30 if can_merge else 40}
                ]})
            if endpoint.endswith("/approvals"):
                return json.dumps({
                    "user_can_approve": can_approve,
                    "approvals_required": 0 if optional else 1,
                    "approvals_left": 0 if optional else 1,
                })
            if endpoint.endswith("/approval_state"):
                approval_state_calls += 1
                required = 0 if optional and not (
                    approval_changed and approval_state_calls > 1
                ) else 1
                return json.dumps({"rules": [{"approvals_required": required}]})
            return agents_markdown

        def run_command(args, **_kwargs):
            if approval_fails and any("/approve" in part for part in args):
                raise subprocess.CalledProcessError(403, args)
            return Mock(stdout='{"state":"merged"}')

        command = Mock(side_effect=run_command)
        self.last_command = command
        stdout = io.StringIO()
        with patch.object(reviewer, "ignored_reviewers", return_value=ignored), patch.object(
            reviewer.shutil, "which", return_value="/usr/bin/glab"
        ), patch.object(
            reviewer, "api_object", side_effect=objects
        ), patch.object(reviewer, "api_pages", side_effect=pages), patch.object(
            reviewer,
            "api_text",
            side_effect=api_text,
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

    def test_excludes_bots_and_service_accounts_from_every_rule(self):
        service_account = {
            "id": 4,
            "username": "sa-xrow-public",
            "access_level": 40,
            "state": "active",
            "locked": False,
        }
        result, _command = self.run_selection(
            members=[MEMBERS[0], service_account, MEMBERS[2]],
            linked_items=[linked(4, "sa-xrow-public")],
            agents=True,
            agents_markdown=(
                "| reviewers | [sa-xrow-public](https://gitlab.com/sa-xrow-public), "
                "[xrow](https://gitlab.com/xrow) |\n"
            ),
            bot_ids={4},
        )
        self.assertEqual(result["reviewer"]["username"], "xrow")
        self.assertEqual(result["rule"], "configured-reviewer")
        with redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
            self.run_selection(
                members=[MEMBERS[0], service_account],
                bot_ids={4},
            )

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

    def test_ignored_linked_author_uses_configured_reviewer(self):
        result, _command = self.run_selection(
            linked_items=[linked(2, "andyxrow")],
            agents=True,
            ignored={"andyxrow"},
        )
        self.assertEqual(result["reviewer"]["username"], "xrow")
        self.assertEqual(result["rule"], "configured-reviewer")

    def test_ignored_configured_reviewer_uses_fallback(self):
        result, _command = self.run_selection(agents=True, ignored={"xrow"})
        self.assertEqual(result["reviewer"]["username"], "andyxrow")
        self.assertEqual(result["rule"], "maintainer-fallback")

    def test_all_humans_ignored_fails_closed(self):
        with redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
            self.run_selection(ignored={"andyxrow", "xrow"})

    # Superseding owner contract: !200#note_4081781371. Only actual committers
    # qualify in the last tier, ordered Owner, Maintainer, then Developer.
    def test_committer_fallback_allows_author_assignee_without_approval(self):
        result, command = self.run_selection(
            members=[MEMBERS[0], MEMBERS[2]],
            mr_overrides={"author": {"id": 3, "username": "xrow"},
                          "assignees": [ME, MEMBERS[2]]}, apply=True,
        )
        self.assertEqual(result["reviewer"]["username"], "xrow")
        self.assertEqual(result["rule"], "merge-request-committer-fallback")
        self.assertTrue(result["committer_fallback"])
        self.assertFalse(result["self_merge"])
        self.assertFalse(result["merged"])
        self.assertIn("independent approval", result["approval_warning"])
        self.assertEqual(command.call_count, 1)
        self.assertEqual(json.loads(command.call_args.kwargs["input"]),
                         {"reviewer_ids": [3, 77]})

    def test_committer_need_not_be_the_mr_author(self):
        developer = {**MEMBERS[1], "access_level": 30}
        result, command = self.run_selection(
            members=[MEMBERS[0], developer],
            commits=[{"id": "one", "committer_email": "andy@example.com"}],
            user_emails={2: "andy@example.com"},
        )
        self.assertEqual(result["reviewer"]["id"], 2)
        self.assertTrue(result["committer_fallback"])
        self.assertTrue(result["dry_run"])
        command.assert_not_called()

    def test_author_without_a_matching_commit_is_not_a_fallback(self):
        with redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
            self.run_selection(members=[MEMBERS[0], MEMBERS[2]],
                mr_overrides={"author": MEMBERS[2]},
                commits=[{"id": "one", "committer_email": "someone-else@example.com"}])

    def test_committer_role_order_owner_then_maintainer_then_developer(self):
        developer = {**MEMBERS[1], "id": 4, "username": "developer", "access_level": 30}
        humans = [MEMBERS[1], MEMBERS[2], developer]
        commits = [{"id": str(m["id"]), "committer_email": m["username"] + "@example.com"}
                   for m in humans]
        emails = {m["id"]: m["username"] + "@example.com" for m in humans}
        for available, expected in ((humans, 3), ([humans[0], developer], 2), ([developer], 4)):
            with self.subTest(expected=expected):
                result, _ = self.run_selection(members=[MEMBERS[0], *available],
                    mr_overrides={"assignees": [ME, *available]},
                    commits=commits, user_emails=emails)
                self.assertEqual(result["reviewer"]["id"], expected)
                self.assertTrue(result["committer_fallback"])

    def test_preferred_reviewers_win_over_committer_fallback(self):
        for arguments in ({"linked_items": [linked(2, "andyxrow")]},
            {"agents": True, "agents_markdown": "| reviewers | [andyxrow](https://gitlab.com/andyxrow) |"}, {}):
            with self.subTest(arguments=arguments):
                result, _ = self.run_selection(
                    mr_overrides={"author": MEMBERS[2]}, **arguments)
                self.assertEqual(result["reviewer"]["id"], 2)
                self.assertFalse(result["committer_fallback"])

    def test_committer_fallback_keeps_account_membership_and_ignore_guards(self):
        for extra in ({"members": [MEMBERS[0]]},
            {"members": [MEMBERS[0], {**MEMBERS[2], "locked": True}]},
            {"members": [MEMBERS[0], {**MEMBERS[2], "state": "blocked"}]},
            {"members": [MEMBERS[0], {**MEMBERS[2], "access_level": 10}]},
            {"bot_ids": {3}}, {"ignored": {"xrow"}}, {"user_emails": {3: ""}}):
            arguments = {"members": [MEMBERS[0], MEMBERS[2]], "mr_overrides": {"author": MEMBERS[2]}, **extra}
            with self.subTest(arguments=arguments), redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
                self.run_selection(**arguments)
        with redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
            self.run_selection(members=[MEMBERS[0]], commits=[{"id": "one", "committer_email": "robot@example.com"}], user_emails={99: "robot@example.com"})

    def test_committer_fallback_revalidates_before_mutating(self):
        for fresh in ({"fresh_member": {**MEMBERS[2], "locked": True}},
            {"fresh_members": [MEMBERS[0]]}, {"fresh_members": MEMBERS},
            {"fresh_members": [MEMBERS[0], {"id": 3}]},
            {"fresh_commits": [{"id": "one", "committer_email": "different@example.com"}]},
            {"mr_change": {"author": MEMBERS[1]}}, {"changed": True}):
            with self.subTest(fresh=fresh), redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
                self.run_selection(members=[MEMBERS[0], MEMBERS[2]],
                    mr_overrides={"author": MEMBERS[2]}, apply=True, **fresh)
            self.last_command.assert_not_called()

    def test_invalid_or_ambiguous_committer_data_fails_closed(self):
        for commits, emails in (([{"id": "one"}], {3: "xrow@example.com"}),
            ([{"id": "one", "committer_email": "xrow@example.com"}], {2: "xrow@example.com", 3: "xrow@example.com"})):
            with self.subTest(commits=commits), redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
                self.run_selection(mr_overrides={"assignees": [ME, MEMBERS[1], MEMBERS[2]]}, commits=commits, user_emails=emails)

    def test_reads_nested_and_direct_reviewer_exclusions(self):
        for agent in (
            {"config": {"reviewer": {"ignore": ["xrow", "GitLabDuo"]}}},
            {"reviewer": {"ignore": ["xrow", "GitLabDuo"]}},
        ):
            with self.subTest(agent=agent), tempfile.TemporaryDirectory() as directory:
                config = Path(directory) / "openclaw.json"
                config.write_text(json.dumps({"skills": {"entries": {"gitlab-agent": agent}}}))
                with patch.dict(os.environ, {"OPENCLAW_CONFIG_PATH": str(config)}):
                    self.assertEqual(reviewer.ignored_reviewers(), {"xrow", "gitlabduo"})

    def test_rejects_malformed_reviewer_exclusions(self):
        with tempfile.TemporaryDirectory() as directory:
            config = Path(directory) / "openclaw.json"
            config.write_text(json.dumps({"skills": {"entries": {
                "gitlab-agent": {"config": {"reviewer": {"ignore": ["xrow", 7]}}}
            }}}))
            with patch.dict(os.environ, {"OPENCLAW_CONFIG_PATH": str(config)}):
                with redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
                    reviewer.ignored_reviewers()

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


    def test_optional_approval_self_review_merges(self):
        result, command = self.run_selection(
            self_review=True, optional=True, apply=True
        )
        self.assertEqual(result["rule"], "optional-approval-self-merge")
        self.assertEqual(result["reviewer"]["username"], "robot")
        self.assertTrue(result["merged"])
        calls = command.call_args_list
        self.assertEqual(len(calls), 3)
        self.assertEqual(json.loads(calls[0].kwargs["input"]), {"reviewer_ids": [99]})
        self.assertTrue(any("/approve" in part for part in calls[1].args[0]))
        self.assertTrue(any("/merge" in part for part in calls[2].args[0]))

    def test_failed_self_approval_never_attempts_merge(self):
        with redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
            self.run_selection(
                self_review=True, optional=True, approval_fails=True, apply=True
            )
        self.assertFalse(any(
            any(part.endswith("/merge") for part in call.args[0])
            for call in self.last_command.call_args_list
        ))

    def test_unavailable_self_approval_keeps_human_reviewer(self):
        result, _command = self.run_selection(
            self_review=True, optional=True, can_approve=False
        )
        self.assertFalse(result["self_merge"])
        self.assertEqual(result["reviewer"]["username"], "andyxrow")

    def test_insufficient_merge_access_keeps_human_reviewer(self):
        result, _command = self.run_selection(
            self_review=True, optional=True, can_merge=False
        )
        self.assertFalse(result["self_merge"])
        self.assertEqual(result["reviewer"]["username"], "andyxrow")

    def test_required_approval_keeps_human_reviewer(self):
        result, _command = self.run_selection(self_review=True, optional=False)
        self.assertFalse(result["self_merge"])
        self.assertEqual(result["reviewer"]["username"], "andyxrow")

    def test_changed_approval_rule_fails_before_writing(self):
        with redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
            self.run_selection(
                self_review=True, optional=True, approval_changed=True, apply=True
            )

    def test_draft_never_self_merges(self):
        self.assertFalse(reviewer.merge_ready({**MR, "draft": True}))

    def test_incomplete_approval_data_is_not_optional(self):
        with patch.object(reviewer, "api_text", side_effect=OSError):
            self.assertFalse(reviewer.optional_approval("projects/example/mr/7"))

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
