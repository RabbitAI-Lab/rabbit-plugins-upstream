#!/usr/bin/env python3
"""Plan and claim the next continuation from live GitLab facts; never write GitLab."""

from __future__ import annotations

import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
import fcntl
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile


ACTIVE = ("created", "waiting_for_resource", "preparing", "pending", "running")
TERMINAL = ("success", "failed", "canceled", "skipped")
PRIORITY = ("blocker", "high", "medium", "low")
KINDS = ("assess", "prepare", "investigate", "verify", "dispatch_ci")
GUARDS = ("issue_closed", "mr_merged", "pipeline_terminal", "project_ci_idle",
          "agent_capacity", "activity_changed")


def timestamp(value):
    result = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if result.tzinfo is None:
        raise ValueError("timestamps must include a time zone")
    return result


def positive(value):
    if type(value) is not int or value <= 0:
        raise ValueError("expected a positive integer")
    return value


def read_api(endpoint):
    response = subprocess.run(["glab", "api", endpoint], check=True, text=True,
                              capture_output=True, timeout=25)
    return json.loads(response.stdout)


class LiveGitLab:
    def __init__(self, api=read_api):
        self.request = api
        self.cache = {}
        self.user = self.object("user")
        positive(self.user["id"])
        if not isinstance(self.user.get("username"), str):
            raise ValueError("incomplete current user")
        spec = importlib.util.spec_from_file_location(
            "resume_discovery", Path(__file__).with_name("list-active-items.py"))
        self.discovery = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.discovery)
        self.discovery.api_json = self.get
        self.owner = self.discovery.configured_owner()
        self.projects = {}

    def get(self, endpoint):
        if endpoint not in self.cache:
            response = self.request(endpoint)
            if not isinstance(response, (dict, list)):
                raise ValueError("API response is not an object or array")
            self.cache[endpoint] = response
        return self.cache[endpoint]

    def object(self, endpoint):
        response = self.get(endpoint)
        if not isinstance(response, dict):
            raise ValueError("API object response is incomplete")
        return response

    def pages(self, endpoint):
        result = []
        separator = "&" if "?" in endpoint else "?"
        for page in range(1, 101):
            batch = self.get(f"{endpoint}{separator}per_page=100&page={page}")
            if not isinstance(batch, list) or any(not isinstance(x, dict) for x in batch):
                raise ValueError("incomplete paginated response")
            result.extend(batch)
            if len(batch) < 100:
                return result
        raise ValueError("pagination exceeded its bound")

    def authorized(self, project_id):
        positive(project_id)
        if project_id not in self.projects:
            project = self.object(f"projects/{project_id}")
            if type(project.get("archived")) is not bool:
                raise ValueError("project metadata is incomplete")
            self.projects[project_id] = (
                project.get("archived") is False
                and not project.get("marked_for_deletion_at")
                and not project.get("forked_from_project")
                and (self.user["username"] == self.owner
                     or self.discovery.owner_created_membership(
                         str(project_id), self.user["id"], self.user["username"], self.owner))
            )
        return self.projects[project_id]

    def refresh(self, row):
        project_id, iid = positive(row["project_id"]), positive(row["iid"])
        if not self.authorized(project_id):
            return None
        collection = "merge_requests" if row["kind"] == "merge_request" else "issues"
        detail = self.object(f"projects/{project_id}/{collection}/{iid}")
        labels = detail.get("labels")
        if not isinstance(labels, list) or any(not isinstance(x, str) for x in labels):
            raise ValueError("incomplete labels")
        if detail.get("state") not in ("opened", "closed", "merged", "locked"):
            raise ValueError("item state is incomplete")
        assignees = detail.get("assignees")
        if not isinstance(assignees, list) or any(not isinstance(a, dict) or type(a.get("id")) is not int for a in assignees):
            raise ValueError("assignees are incomplete")
        if (detail["state"] != "opened" or "workflow::forbidden" in labels
                or not any(a["id"] == self.user["id"] for a in assignees)):
            return None
        if row["kind"] == "merge_request" and not detail.get("source_branch"):
            raise ValueError("source branch is missing")
        normalized = self.discovery.normalized(detail, row["kind"])
        if normalized["web_url"] != row["web_url"]:
            raise ValueError("item identity changed")
        return {**normalized, "source_branch": detail.get("source_branch"),
                "head_pipeline": detail.get("head_pipeline")}

    def active_pipelines(self, project_id):
        pipelines = [pipeline for status in ACTIVE for pipeline in self.pages(
            f"projects/{project_id}/pipelines?status={status}")]
        for pipeline in pipelines:
            positive(pipeline.get("id"))
            if (not isinstance(pipeline.get("ref"), str) or not pipeline["ref"]
                    or not isinstance(pipeline.get("source"), str) or not pipeline["source"]
                    or pipeline.get("status") not in ACTIVE):
                raise ValueError("active pipeline metadata is incomplete")
        return pipelines

    def terminal_tree(self, project_id, pipeline_id, seen=None):
        seen = set() if seen is None else seen
        key = (project_id, pipeline_id)
        if key in seen:
            return True
        if len(seen) >= 200:
            raise ValueError("pipeline tree exceeded its bound")
        seen.add(key)
        status = self.object(f"projects/{project_id}/pipelines/{pipeline_id}").get("status")
        if status not in (*ACTIVE, *TERMINAL, "manual", "scheduled"):
            raise ValueError("unknown pipeline status")
        if status not in TERMINAL:
            return False
        for bridge in self.pages(f"projects/{project_id}/pipelines/{pipeline_id}/bridges"):
            child = bridge.get("downstream_pipeline")
            if child:
                child_project = positive(child["project_id"])
                if not self.authorized(child_project):
                    raise ValueError("downstream project is not authorized")
                if not self.terminal_tree(child_project, positive(child["id"]), seen):
                    return False
        return True

    def guard(self, condition, row, items, coverage_complete):
        kind = condition["kind"]
        if kind == "activity_changed":
            baseline = condition.get("baseline_cursor")
            if not isinstance(baseline, dict) or set(baseline) != {"updated_at", "user_notes_count"}:
                raise ValueError("activity guard needs an audited baseline cursor")
            return row["activity_cursor"] != baseline
        if kind == "agent_capacity":
            if not coverage_complete:
                raise ValueError("unknown items prevent a complete capacity check")
            limit = positive(condition.get("limit"))
            active = set()
            # A targeted input file must not hide another assigned work root.
            assigned = []
            for candidate in self.pages("merge_requests?state=opened&scope=assigned_to_me"):
                current = self.refresh({**candidate, "kind": "merge_request"})
                if current is not None:
                    assigned.append(current)
            projects = {i["project_id"] for i in assigned}
            for project in projects:
                mrs = [i for i in assigned if i["project_id"] == project]
                for pipeline in self.active_pipelines(project):
                    if "source" not in pipeline:
                        raise ValueError("pipeline source is missing")
                    if pipeline["source"] == "parent_pipeline":
                        continue
                    if any(pipeline["id"] == (i.get("head_pipeline") or {}).get("id")
                           or pipeline.get("ref") in (i.get("source_branch"),
                                                      f"refs/merge-requests/{i['iid']}/head",
                                                      f"refs/merge-requests/{i['iid']}/merge") for i in mrs):
                        active.add((project, pipeline["id"]))
            return len(active) < limit
        project = positive(condition.get("project_id"))
        if not self.authorized(project):
            raise ValueError("guard project is not authorized")
        if kind == "project_ci_idle":
            refs = condition.get("refs")
            if not isinstance(refs, list) or not refs or any(not isinstance(x, str) or not x for x in refs):
                raise ValueError("CI guard requires explicit branch names")
            return not any(p.get("ref") in refs for p in self.active_pipelines(project))
        if kind == "pipeline_terminal":
            return self.terminal_tree(project, positive(condition.get("pipeline_id")))
        collection, expected = ("issues", "closed") if kind == "issue_closed" else ("merge_requests", "merged")
        state = self.object(f"projects/{project}/{collection}/{positive(condition.get('iid'))}").get("state")
        if state not in ("opened", "closed", "merged", "locked"):
            raise ValueError("unknown dependency state")
        return state == expected


def validate_action(action):
    if (not isinstance(action, dict) or action.get("kind") not in KINDS
            or not isinstance(action.get("id"), str) or not action["id"]
            or not isinstance(action.get("guards"), list)):
        raise ValueError("invalid pending action")
    kinds = set()
    for guard in action["guards"]:
        if not isinstance(guard, dict) or guard.get("kind") not in GUARDS:
            raise ValueError("unknown guard; action must be reassessed")
        kinds.add(guard["kind"])
    if action["kind"] == "dispatch_ci" and not {"project_ci_idle", "agent_capacity"} <= kinds:
        raise ValueError("CI dispatch requires both default-branch and work-capacity guards")


def plan(rows, state, live, now, updates=None, preempt=()):
    if state.get("version", 1) != 1 or not isinstance(state.get("items", {}), dict):
        raise ValueError("unsupported execution-state schema")
    timestamp(now)
    result = {"runnable": [], "waiting": [], "needs_recheck": [], "excluded": []}
    items = []
    seen = set()
    for row in rows:
        url = row["web_url"]
        if url in seen:
            raise ValueError("duplicate queue item")
        seen.add(url)
        try:
            current = live.refresh(row)
            if current is None:
                result["excluded"].append(url)
            else:
                items.append(current)
        except (OSError, subprocess.SubprocessError, ValueError, KeyError, TypeError):
            result["needs_recheck"].append({"url": url, "reason": "live item/access check failed"})
    coverage_complete = not result["needs_recheck"]
    eligible = {i["web_url"] for i in items}
    if set(updates or {}) - eligible:
        raise ValueError("action update target is not currently eligible")
    result["ineligible_preemptions"] = sorted(set(preempt) - eligible)
    # Discovery, not a saved record, grants candidacy. Keep history when an item
    # disappears or fails a live check, so a later valid assignment can resume it.
    records = json.loads(json.dumps(state.get("items", {})))
    for position, row in enumerate(items):
        url = row["web_url"]
        record = dict(state.get("items", {}).get(url, {}))
        record.setdefault("first_pending_at", now)
        if url in (updates or {}):
            actions = updates[url]
            if not isinstance(actions, list) or not actions:
                raise ValueError("an open item requires a pending action or explicit wait guard")
            for action in actions:
                validate_action(action)
            record["actions"] = actions
            record["audited_cursor"] = row["activity_cursor"]
        record.setdefault("actions", [{"id": "assess-next-action", "kind": "assess", "guards": []}])
        records[url] = record
        try:
            if not isinstance(record["actions"], list) or not record["actions"]:
                raise ValueError("open item has no next action or wait guard")
            age = record.get("last_attempt_at") or record["first_pending_at"]
            if any(timestamp(value) > timestamp(now) for value in
                   (record["first_pending_at"], age)):
                raise ValueError("execution state contains a future timestamp")
            ready, blocked, unknown = [], [], []
            actions = record["actions"]
            if record.get("audited_cursor") != row["activity_cursor"]:
                # Changed instructions invalidate execution authority, not the
                # durable continuation. Unchanged cursors still refresh guards.
                actions = [{"id": "audit-current-activity", "kind": "assess", "guards": []}]
            for action in actions:
                try:
                    validate_action(action)
                    if action["kind"] == "dispatch_ci" and not any(
                            g["kind"] == "project_ci_idle" and g.get("project_id") == row["project_id"]
                            for g in action["guards"]):
                        raise ValueError("CI idle guard must cover the item's own project")
                    checks = [live.guard(g, row, items, coverage_complete) for g in action["guards"]]
                    if any(type(c) is not bool for c in checks):
                        raise ValueError("guard did not return a boolean")
                    (ready if all(checks) else blocked).append(action)
                except (OSError, subprocess.SubprocessError, ValueError, KeyError, TypeError):
                    unknown.append(action.get("id", "invalid-action"))
            if unknown:
                result["needs_recheck"].append({"url": url, "reason": "guard check failed", "actions": unknown})
            if ready:
                priority = min((PRIORITY.index(label[10:]) for label in row["labels"]
                                if label.startswith("priority::") and label[10:] in PRIORITY), default=4)
                result["runnable"].append({"url": url, "action": ready[0],
                    "sort": [0 if url in preempt else 1, priority, timestamp(age).timestamp(), position]})
            elif blocked:
                result["waiting"].append({"url": url, "actions": blocked})
        except (ValueError, KeyError, TypeError):
            result["needs_recheck"].append({"url": url, "reason": "execution state needs repair"})
    result["runnable"].sort(key=lambda i: i["sort"])
    for row in result["runnable"]:
        row.pop("sort")
    result["next"] = result["runnable"][0] if result["runnable"] else None
    result["no_runnable_work"] = not result["runnable"] and not result["needs_recheck"]
    result["state"] = {"version": 1, "items": records}
    return result


@contextmanager
def state_lock(path):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.with_suffix(path.suffix + ".lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        yield


def save_state(path, state):
    name = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", dir=path.parent, delete=False) as output:
            name = output.name
            json.dump(state, output, indent=2)
            output.write("\n")
            output.flush()
            os.fsync(output.fileno())
        os.replace(name, path)
        directory = os.open(path.parent, os.O_RDONLY | os.O_DIRECTORY)
        try:
            os.fsync(directory)
        finally:
            os.close(directory)
    finally:
        if name and os.path.exists(name):
            os.unlink(name)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--items", type=Path, required=True, help="fresh gated discovery JSON array")
    parser.add_argument("--state", type=Path, required=True, help="separate durable execution state")
    parser.add_argument("--actions", type=Path, help="URL-to-pending-actions JSON map")
    parser.add_argument("--preempt", action="append", default=[], help="freshly audited owner/Maintainer instruction URL")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--claim", action="store_true", help="atomically persist state and next selection attempt")
    mode.add_argument("--check-idle", action="store_true", help="return exit 3 if runnable work remains")
    args = parser.parse_args()
    try:
        with state_lock(args.state):
            state = json.loads(args.state.read_text()) if args.state.exists() else {}
            rows = json.loads(args.items.read_text())
            updates = json.loads(args.actions.read_text()) if args.actions else None
            now = datetime.now(timezone.utc).isoformat()
            result = plan(rows, state, LiveGitLab(), now, updates, args.preempt)
            if args.claim:
                if result["next"]:
                    result["state"]["items"][result["next"]["url"]]["last_attempt_at"] = now
                save_state(args.state, result["state"])
            print(json.dumps(result))
            if result["needs_recheck"]:
                return 2
            return 3 if args.check_idle and result["next"] else 0
    except (OSError, subprocess.SubprocessError, ValueError, KeyError, TypeError):
        print("Continuation planning failed closed; preserve existing state and recheck live inputs.", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
