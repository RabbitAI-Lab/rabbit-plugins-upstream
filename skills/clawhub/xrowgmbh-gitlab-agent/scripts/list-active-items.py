#!/usr/bin/env python3
"""List every active GitLab issue and merge request assigned to this agent."""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
from urllib.parse import urlencode


PER_PAGE = 100


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
    }


def main() -> int:
    if shutil.which("glab") is None:
        print("glab is required", file=sys.stderr)
        return 69
    try:
        user = api_json("user")
        if not isinstance(user, dict) or not isinstance(user.get("username"), str):
            raise ValueError("GitLab user response is incomplete")
        username = user["username"]
        items = [
            *(normalized(item, "issue") for item in paginated(
                "issues?state=opened&scope=assigned_to_me"
            )),
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
    active.sort(key=lambda item: str(item.get("web_url") or ""))
    json.dump(active, sys.stdout, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
