#!/usr/bin/env python3
"""List active GitLab work assigned to the agent or submitted by collaborators."""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlencode


PER_PAGE = 100
PRIORITY_ORDER = {
    "priority::blocker": 0,
    "priority::high": 1,
    "priority::medium": 2,
    "priority::low": 3,
}
CONFIG_PATH_ENV = "OPENCLAW_CONFIG_PATH"


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


def configured_accept_entries() -> list[str]:
    """Read collaborator selectors from the active OpenClaw configuration."""
    configured_path = os.environ.get(CONFIG_PATH_ENV)
    config_path = (
        Path(configured_path).expanduser()
        if configured_path
        else Path.home() / ".openclaw" / "openclaw.json"
    )
    if not config_path.exists():
        return []
    payload = json.loads(config_path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError("OpenClaw configuration is not an object")
    skills = payload.get("skills", {})
    if not isinstance(skills, dict):
        raise ValueError("OpenClaw skills configuration is not an object")
    entries = skills.get("entries", {})
    if not isinstance(entries, dict):
        raise ValueError("OpenClaw skill entries configuration is not an object")
    agent = entries.get("gitlab-agent", {})
    if not isinstance(agent, dict):
        raise ValueError("gitlab-agent configuration is not an object")

    # OpenClaw currently reserves arbitrary skill settings below `config`, while
    # accepting the issue-requested direct spelling for forward compatibility.
    collaborators = agent.get("collaborators")
    if collaborators is None:
        skill_config = agent.get("config", {})
        if not isinstance(skill_config, dict):
            raise ValueError("gitlab-agent config is not an object")
        collaborators = skill_config.get("collaborators", {})
    if not isinstance(collaborators, dict):
        raise ValueError("gitlab-agent collaborators configuration is not an object")
    accept = collaborators.get("accept", [])
    if not isinstance(accept, list) or any(
        not isinstance(entry, str) or not entry.strip() for entry in accept
    ):
        raise ValueError("gitlab-agent collaborators.accept must be a list of strings")
    return [entry.strip() for entry in accept]


def user_matches_domain(user: dict[str, object], domain: str) -> bool:
    suffix = f"@{domain.lower()}"
    return any(
        isinstance(user.get(field), str)
        and str(user[field]).lower().endswith(suffix)
        for field in ("email", "public_email", "commit_email")
    )


def accepted_usernames(selectors: list[str]) -> set[str]:
    """Resolve username, group, and public-email-domain selectors."""
    usernames: set[str] = set()
    for selector in selectors:
        if selector.startswith("@"):
            domain = selector[1:].lower()
            if not domain or "." not in domain:
                raise ValueError(f"invalid collaborator email domain: {selector}")
            for user in paginated(f"users?{urlencode({'search': domain})}"):
                username = user.get("username")
                if isinstance(username, str) and user_matches_domain(user, domain):
                    usernames.add(username)
            continue

        matching_users = [
            user
            for user in paginated(f"users?{urlencode({'username': selector})}")
            if user.get("username") == selector
        ]
        usernames.update(
            user["username"]
            for user in matching_users
            if isinstance(user.get("username"), str)
        )

        groups = [
            group
            for group in paginated(f"groups?{urlencode({'search': selector})}")
            if group.get("full_path") == selector or group.get("path") == selector
        ]
        for group in groups:
            group_id = group.get("id")
            if not isinstance(group_id, int) or isinstance(group_id, bool):
                raise ValueError(f"GitLab group identity is incomplete: {selector}")
            for member in paginated(f"groups/{group_id}/members/all"):
                username = member.get("username")
                if isinstance(username, str):
                    usernames.add(username)

        if not matching_users and not groups:
            raise ValueError(f"unknown collaborator username or group: {selector}")
    return usernames


def unassigned_items_by(usernames: set[str]) -> list[dict[str, object]]:
    items: dict[tuple[object, object], dict[str, object]] = {}
    for username in sorted(usernames):
        endpoint = "issues?" + urlencode(
            {
                "state": "opened",
                "scope": "all",
                "assignee_id": "None",
                "author_username": username,
            }
        )
        for item in paginated(endpoint):
            author = item.get("author")
            if not isinstance(author, dict) or author.get("username") not in usernames:
                raise ValueError("GitLab collaborator item author is incomplete")
            items[(item.get("project_id"), item.get("iid"))] = item
    return list(items.values())


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
        collaborators = accepted_usernames(configured_accept_entries())
        assigned_issues = paginated("issues?state=opened&scope=assigned_to_me")
        collaborator_issues = unassigned_items_by(collaborators)
        collaborator_item_ids = {
            (item.get("project_id"), item.get("iid"))
            for item in collaborator_issues
        }
        issue_items = {
            (item.get("project_id"), item.get("iid")): item
            for item in [*assigned_issues, *collaborator_issues]
        }.values()
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
        and (
            username in item["assignees"]
            or (
                not item["assignees"]
                and (item["project_id"], item["iid"]) in collaborator_item_ids
            )
        )
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
