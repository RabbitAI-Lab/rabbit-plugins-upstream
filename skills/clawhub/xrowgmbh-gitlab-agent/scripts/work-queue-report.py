#!/usr/bin/env python3
"""Read-only Control UI report using the installed agent's gates and ordering."""

from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent


def load_helper(name):
    spec = importlib.util.spec_from_file_location(name.replace("-", "_"), SCRIPT_DIR / name)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


active = load_helper("list-active-items.py")


def read_api(endpoint):
    # No shell, supplied command, write method, or unbounded network read.
    result = subprocess.run(
        ["glab", "api", endpoint], check=True, text=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=25,
    )
    return json.loads(result.stdout)


def report():
    active.api_json = read_api
    user = read_api("user")
    if type(user.get("id")) is not int or not isinstance(user.get("username"), str):
        raise ValueError("Incomplete GitLab identity")
    owner = active.configured_owner()
    projects = {}
    access = {}
    records = []
    for collection in ("issues", "merge_requests"):
        for candidate in active.paginated(f"{collection}?state=opened&scope=assigned_to_me"):
            if not active.project_is_active(candidate.get("project_id"), projects):
                continue
            kind = "merge_request" if collection == "merge_requests" else active.issue_kind(candidate)
            project, endpoint = active.object_endpoint(candidate, kind)
            if project not in access:
                access[project] = user["username"] == owner or active.owner_created_membership(
                    project, user["id"], user["username"], owner,
                )
            if not access[project]:
                continue
            current = read_api(endpoint)
            labels = current.get("labels")
            if (current.get("state") != "opened"
                    or not any(a.get("username") == user["username"] for a in current.get("assignees", []))
                    or not isinstance(labels, list) or any(not isinstance(s, str) for s in labels)):
                continue
            row = active.normalized(current, kind)
            row.update(
                created_at=current.get("created_at"),
                time_spent=current.get("time_stats", {}).get("total_time_spent", 0),
                item_type=current.get("issue_type", kind),
            )
            records.append(row)

    records = active.order_items(records)
    todos = []
    # All pending to-dos are visible, not only owner mentions used by automation.
    for todo in active.paginated("todos?state=pending"):
        if todo.get("state") != "pending":
            continue
        target = todo.get("target") or {}
        author = todo.get("author") or {}
        todos.append({
            "id": todo["id"], "title": target.get("title") or todo.get("body") or "GitLab to-do",
            "web_url": todo.get("target_url"), "created_at": todo.get("created_at"),
            "labels": target.get("labels", []), "item_type": todo.get("target_type", "To-do"),
            "time_spent": target.get("time_stats", {}).get("total_time_spent", 0),
            "author": author.get("username"), "action": todo.get("action_name"),
            "owner_addressed": author.get("username") == owner and todo.get("action_name") == "directly_addressed",
        })
    sources = []
    for name, description in (
        ("list-active-items.py", "Assigned work, owner membership checks, incident adoption and priority ordering."),
        ("list-directly-addressed-todos.py", "Pending direct mentions from the configured owner, in GitLab order."),
        ("work-queue-report.py", "This read-only report; reuses the discovery gates and ordering without adopting or updating items."),
    ):
        source_prefix = "skills/gitlab-agent/scripts" if "skills" in SCRIPT_DIR.parts else "gitlab-agent/scripts"
        sources.append({"name": name, "path": f"{source_prefix}/{name}",
                        "description": description, "source": (SCRIPT_DIR / name).read_text(encoding="utf-8")})
    return {"user": {"username": user["username"], "name": user.get("name")}, "owner": owner,
            "generated_at": datetime.now(timezone.utc).isoformat(), "items": records,
            "todos": todos, "scripts": sources}


if __name__ == "__main__":
    try:
        print(json.dumps(report()))
    except (OSError, subprocess.SubprocessError, ValueError, KeyError, TypeError):
        print("Work Queue could not read GitLab. Check the server's GitLab authentication and agent profile.", file=sys.stderr)
        sys.exit(1)
