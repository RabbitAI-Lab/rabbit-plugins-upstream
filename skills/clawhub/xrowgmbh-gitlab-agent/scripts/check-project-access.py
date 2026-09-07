#!/usr/bin/env python3
"""Fail closed unless the agent's project membership was created by its owner."""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
from typing import NoReturn
from urllib.parse import quote


USAGE = (
    "Usage: check-project-access.py <project-path> <owner-username> "
    "[<issue|merge_request> <iid>]"
)
OTHER_WORKFLOWS = ",".join(
    (
        "workflow::backlog",
        "workflow::in-progress",
        "workflow::paused",
        "workflow::blocked",
        "workflow::need-human",
        "workflow::review",
        "workflow::stale",
        "workflow::done",
    )
)


def api_json(endpoint: str) -> object:
    result = subprocess.run(
        ["glab", "api", endpoint],
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
    )
    return json.loads(result.stdout)


def update_labels(endpoint: str, *, allowed: bool) -> None:
    command = ["glab", "api", "-X", "PUT", endpoint]
    if allowed:
        command.extend(("-f", "remove_labels=workflow::forbidden"))
    else:
        command.extend(
            (
                "-f",
                "add_labels=workflow::forbidden",
                "-f",
                f"remove_labels={OTHER_WORKFLOWS}",
            )
        )
    subprocess.run(
        command,
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def forbidden(message: str, object_endpoint: str | None) -> NoReturn:
    if object_endpoint:
        try:
            update_labels(object_endpoint, allowed=False)
        except (OSError, subprocess.SubprocessError):
            print("[warning] unable to set workflow::forbidden", file=sys.stderr)
    print(f"[forbidden] {message}", file=sys.stderr)
    raise SystemExit(77)


def require_string(payload: dict[str, object], key: str, message: str) -> str:
    value = payload.get(key)
    if not isinstance(value, str) or not value:
        raise ValueError(message)
    return value


def main(argv: list[str]) -> int:
    if len(argv) not in (2, 4):
        print(USAGE, file=sys.stderr)
        return 64

    project_path, owner_username = argv[:2]
    object_endpoint: str | None = None
    if len(argv) == 4:
        object_kind, object_iid = argv[2:]
        collection = {"issue": "issues", "merge_request": "merge_requests"}.get(
            object_kind
        )
        if collection is None or not object_iid.isdecimal():
            print(USAGE, file=sys.stderr)
            return 64
        object_endpoint = (
            f"projects/{quote(project_path, safe='')}/{collection}/{object_iid}"
        )

    if shutil.which("glab") is None:
        forbidden("glab is required", object_endpoint)

    try:
        user = api_json("user")
        if not isinstance(user, dict):
            raise ValueError("GitLab user response is incomplete")
        agent_id = user.get("id")
        if type(agent_id) is not int:
            raise ValueError("GitLab user id is missing")
        agent_username = require_string(user, "username", "GitLab username is missing")
    except (OSError, subprocess.SubprocessError, json.JSONDecodeError, ValueError):
        forbidden("unable to resolve the authenticated GitLab user", object_endpoint)

    try:
        membership = api_json(
            f"projects/{quote(project_path, safe='')}/members/all/{agent_id}"
        )
    except (OSError, subprocess.SubprocessError, json.JSONDecodeError):
        forbidden(
            f"{agent_username} is not a project member of {project_path}",
            object_endpoint,
        )
    if not isinstance(membership, dict):
        forbidden("project membership response is incomplete", object_endpoint)

    try:
        membership_state = require_string(
            membership, "membership_state", "membership state is missing"
        )
        access_level = membership.get("access_level")
        if type(access_level) is not int:
            raise ValueError("membership access level is missing")
        member_username = require_string(
            membership, "username", "membership username is missing"
        )
        created_by = membership.get("created_by")
        if not isinstance(created_by, dict):
            raise ValueError("membership creator is missing")
        creator_username = require_string(
            created_by, "username", "membership creator is missing"
        )
    except ValueError as error:
        forbidden(str(error), object_endpoint)

    if member_username != agent_username:
        forbidden(
            "membership identity does not match the authenticated user", object_endpoint
        )
    if membership_state != "active":
        forbidden("membership is not active", object_endpoint)
    if access_level < 10:
        forbidden("membership does not grant project access", object_endpoint)
    if creator_username != owner_username:
        forbidden(
            f"membership was created by {creator_username}, not {owner_username}",
            object_endpoint,
        )

    if object_endpoint:
        try:
            update_labels(object_endpoint, allowed=True)
        except (OSError, subprocess.SubprocessError):
            forbidden("unable to remove workflow::forbidden", object_endpoint)
    print(
        f"[allowed] {agent_username} was added to {project_path} by {owner_username}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
