#!/usr/bin/env python3
"""List every active GitLab issue and merge request assigned to this agent."""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
from urllib.parse import urlencode


PER_PAGE = 100
PRIORITY_ORDER = {
    "priority::blocker": 0,
    "priority::high": 1,
    "priority::medium": 2,
    "priority::low": 3,
}


def api_json(endpoint: str) -> object:
    result = subprocess.run(
        ["glab", "api", endpoint],
        check=True,
        text=True,
        stdout=subprocess.PIPE,
    )
    return json.loads(result.stdout)


def paginated(endpoint: str) -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    page = 1
    while True:
        separator = "&" if "?" in endpoint else "?"
        payload = api_json(
            f"{endpoint}{separator}{urlencode({'per_page': PER_PAGE, 'page': page})}"
        )
        if not isinstance(payload, list):
            raise ValueError(f"GitLab returned a non-list page for {endpoint}")
        for item in payload:
            if not isinstance(item, dict):
                raise ValueError(f"GitLab returned an invalid item for {endpoint}")
            records.append(item)
        if len(payload) < PER_PAGE:
            break
        page += 1
    return records


def normalized(item: dict[str, object], kind: str) -> dict[str, object]:
    assignees = item.get("assignees")
    if not isinstance(assignees, list):
        assignees = []
    labels = item.get("labels")
    if not isinstance(labels, list):
        labels = []
    updated_at = item.get("updated_at")
    user_notes_count = item.get("user_notes_count")
    if not isinstance(updated_at, str) or not updated_at:
        raise ValueError("GitLab item activity is missing updated_at")
    if (
        not isinstance(user_notes_count, int)
        or isinstance(user_notes_count, bool)
        or user_notes_count < 0
    ):
        raise ValueError("GitLab item activity has an invalid user_notes_count")
    return {
        "kind": kind,
        "project_id": item.get("project_id"),
        "iid": item.get("iid"),
        "title": item.get("title"),
        "web_url": item.get("web_url"),
        "labels": labels,
        "assignees": [
            assignee.get("username")
            for assignee in assignees
            if isinstance(assignee, dict)
        ],
        "activity_cursor": {
            "updated_at": updated_at,
            "user_notes_count": user_notes_count,
        },
    }


def issue_kind(item: dict[str, object]) -> str:
    """Keep incidents visible as incidents while treating other work items as issues."""
    return "incident" if item.get("issue_type") == "incident" else "issue"


def is_root_cause(item: dict[str, object]) -> bool:
    """Return whether an issue blocks at least one other open work item."""
    project_id = item.get("project_id")
    iid = item.get("iid")
    if (
        not isinstance(project_id, int)
        or isinstance(project_id, bool)
        or project_id <= 0
        or not isinstance(iid, int)
        or isinstance(iid, bool)
        or iid <= 0
    ):
        raise ValueError("GitLab issue identity is incomplete")
    links = paginated(f"projects/{project_id}/issues/{iid}/links")
    return any(
        link.get("link_type") == "blocks" and link.get("state") == "opened"
        for link in links
    )


def priority_rank(labels: object) -> int:
    if not isinstance(labels, list):
        raise ValueError("GitLab item labels are incomplete")
    return min(
        (PRIORITY_ORDER[label] for label in labels if label in PRIORITY_ORDER),
        default=len(PRIORITY_ORDER),
    )


def main() -> int:
    if shutil.which("glab") is None:
        print("glab is required", file=sys.stderr)
        return 69
    try:
        user = api_json("user")
        if not isinstance(user, dict) or not isinstance(user.get("username"), str):
            raise ValueError("GitLab user response is incomplete")
        username = user["username"]
        issue_items = paginated("issues?state=opened&scope=assigned_to_me")
        items = [
            *(normalized(item, issue_kind(item)) for item in issue_items),
            *(normalized(item, "merge_request") for item in paginated(
                "merge_requests?state=opened&scope=assigned_to_me"
            )),
        ]
    except (OSError, subprocess.SubprocessError, json.JSONDecodeError, ValueError) as error:
        print(f"unable to list active GitLab items: {error}", file=sys.stderr)
        return 69

    active = [
        item
        for item in items
        if "workflow::forbidden" not in item["labels"]
        and username in item["assignees"]
    ]
    try:
        root_causes = {
            (item["project_id"], item["iid"])
            for item in active
            if item["kind"] != "merge_request" and is_root_cause(item)
        }
        active.sort(
            key=lambda item: (
                priority_rank(item["labels"]),
                0 if (item["project_id"], item["iid"]) in root_causes else 1,
                str(item.get("web_url") or ""),
            )
        )
    except (OSError, subprocess.SubprocessError, json.JSONDecodeError, ValueError) as error:
        print(f"unable to order active GitLab items: {error}", file=sys.stderr)
        return 69
    json.dump(active, sys.stdout, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
