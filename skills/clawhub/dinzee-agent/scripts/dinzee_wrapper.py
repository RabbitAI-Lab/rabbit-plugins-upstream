#!/usr/bin/env python3
"""Shared Dinzee Gateway wrapper for local Hermes/OpenClaw skills."""

from __future__ import annotations

import json
import os
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen


DEFAULT_GATEWAY_BASE = "https://gateway.dinzee.ai"
DEFAULT_TIMEOUT = 180


def load_dinzee_token() -> str:
    token = (os.environ.get("DINZEE_USER_TOKEN") or os.environ.get("DINZEEAGENT_API_KEY") or "").strip()
    if token:
        return token

    cred = Path.home() / ".dinzee" / "credentials.json"
    if cred.exists():
        data = json.loads(cred.read_text(encoding="utf-8"))
        token = str(data.get("user_token") or data.get("token") or "").strip()
        if token:
            return token

    raise RuntimeError("找不到 Dinzee 用户接入 token，请设置 DINZEE_USER_TOKEN 或运行 dinzee.py login")


def gateway_base() -> str:
    raw = (
        os.environ.get("DINZEE_GATEWAY_BASE")
        or os.environ.get("DINZEE_GATEWAY_BASE_URL")
        or DEFAULT_GATEWAY_BASE
    ).strip() or DEFAULT_GATEWAY_BASE
    return raw.rstrip("/")


def dinzee_call(
    provider: str,
    tool: str,
    arguments: dict,
    idempotency_key: str,
    *,
    skill_slug: str = "",
    skill_run_id: str | None = None,
    timeout: int = DEFAULT_TIMEOUT,
) -> dict:
    token = load_dinzee_token()
    enriched = dict(arguments)
    if skill_slug:
        enriched.setdefault("_dinzee_skill_slug", skill_slug)
    run_id = skill_run_id if skill_run_id is not None else os.environ.get("DINZEE_SKILL_RUN_ID", "")
    if run_id:
        enriched.setdefault("_dinzee_skill_run_id", run_id)

    payload = {
        "provider": provider,
        "tool": tool,
        "idempotencyKey": idempotency_key,
        "arguments": enriched,
    }
    req = Request(
        f"{gateway_base()}/v1/mcp/calls",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "DinzeeLocalSkill/1.0",
        },
        method="POST",
    )
    try:
        with urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except HTTPError as exc:
        raw = exc.read().decode("utf-8") if exc.fp else ""
        try:
            body = json.loads(raw) if raw else {}
        except json.JSONDecodeError:
            body = {"error_body": raw}
        body.setdefault("ok", False)
        body.setdefault("http_status", exc.code)
        return body

def finalize_skill_run(
    skill_slug: str,
    skill_run_id: str,
    idempotency_key: str,
    *,
    timeout: int = DEFAULT_TIMEOUT,
) -> dict:
    token = load_dinzee_token()
    payload = {
        "skill_slug": skill_slug,
        "skill_run_id": skill_run_id,
        "idempotencyKey": idempotency_key,
    }
    req = Request(
        f"{gateway_base()}/v1/skill-runs/finalize",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "DinzeeLocalSkill/1.0",
        },
        method="POST",
    )
    try:
        with urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except HTTPError as exc:
        raw = exc.read().decode("utf-8") if exc.fp else ""
        try:
            body = json.loads(raw) if raw else {}
        except json.JSONDecodeError:
            body = {"error_body": raw}
        body.setdefault("ok", False)
        body.setdefault("http_status", exc.code)
        return body

