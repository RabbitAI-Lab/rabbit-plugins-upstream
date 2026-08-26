#!/usr/bin/env python3
"""Slack API CLI — lightweight wrapper for agent tool use.

Expects SLACK_BOT_TOKEN env var. Outputs a single JSON object on stdout:
- Success: {"success": true, "data": {...}}
- Failure: {"success": false, "error": "..."}
"""

import argparse
import json
import os
import sys
import time

import httpx

API_BASE = "https://slack.com/api"
TIMEOUT = 30
MAX_RETRIES = 3


def _headers() -> dict:
    token = os.environ.get("SLACK_BOT_TOKEN")
    if not token:
        _out({"success": False, "error": "SLACK_BOT_TOKEN env var required"})
        sys.exit(1)
    return {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }


def _get(method: str, params: dict | None = None) -> dict:
    """GET a Slack Web API method, retrying on rate-limit (HTTP 429).

    Network errors and unexpected HTTP statuses are mapped to the
    ``_slack_error`` shape so the CLI's stdout JSON contract is preserved
    instead of letting an httpx exception crash the agent parser.
    """
    url = f"{API_BASE}/{method}"
    for attempt in range(MAX_RETRIES):
        try:
            with httpx.Client(timeout=TIMEOUT) as c:
                resp = c.get(url, params=params or {}, headers=_headers())
        except httpx.RequestError as e:
            return {"_slack_error": f"network_error: {e}"}
        if resp.status_code == 429:
            # Skip the sleep on the final attempt — we'd return rate_limited next.
            if attempt + 1 >= MAX_RETRIES:
                break
            wait = int(resp.headers.get("Retry-After", "5"))
            time.sleep(wait)
            continue
        if resp.status_code >= 400:
            return {"_slack_error": f"http_{resp.status_code}"}
        body = resp.json()
        # Slack always returns 200 with {"ok": false, "error": "..."} on failure.
        if not body.get("ok"):
            return {"_slack_error": body.get("error", "unknown_error"), **body}
        return body
    return {"_slack_error": "rate_limited"}


def _post(method: str, body: dict | None = None) -> dict:
    """POST a Slack Web API method (write actions: chat, reactions, …).

    Same error contract as ``_get``: never lets an httpx exception escape;
    always returns a dict — either Slack's response body or
    ``{"_slack_error": "..."}``.
    """
    url = f"{API_BASE}/{method}"
    headers = {**_headers(), "Content-Type": "application/json; charset=utf-8"}
    for attempt in range(MAX_RETRIES):
        try:
            with httpx.Client(timeout=TIMEOUT) as c:
                resp = c.post(url, json=body or {}, headers=headers)
        except httpx.RequestError as e:
            return {"_slack_error": f"network_error: {e}"}
        if resp.status_code == 429:
            if attempt + 1 >= MAX_RETRIES:
                break
            wait = int(resp.headers.get("Retry-After", "5"))
            time.sleep(wait)
            continue
        if resp.status_code >= 400:
            return {"_slack_error": f"http_{resp.status_code}"}
        data = resp.json()
        if not data.get("ok"):
            return {"_slack_error": data.get("error", "unknown_error"), **data}
        return data
    return {"_slack_error": "rate_limited"}


def _out(data) -> None:
    print(json.dumps(data, indent=2, default=str))


def _ok(data: dict) -> None:
    _out({"success": True, "data": data})


def _err(message: str) -> None:
    _out({"success": False, "error": message})


# ── Commands ──────────────────────────────────────────────────────────────


def cmd_whoami(_args) -> None:
    body = _get("auth.test")
    if "_slack_error" in body:
        _err(body["_slack_error"])
        return
    _ok(
        {
            "team": body.get("team"),
            "team_id": body.get("team_id"),
            "user": body.get("user"),
            "user_id": body.get("user_id"),
            "bot_id": body.get("bot_id"),
            "url": body.get("url"),
        }
    )


def cmd_list_channels(args) -> None:
    types = ["public_channel"]
    if args.include_private:
        types.append("private_channel")

    cursor: str | None = None
    channels: list[dict] = []
    limit_per_page = 200

    while True:
        params: dict = {
            "types": ",".join(types),
            "limit": limit_per_page,
            "exclude_archived": "true",
        }
        if cursor:
            params["cursor"] = cursor

        body = _get("conversations.list", params=params)
        if "_slack_error" in body:
            _err(body["_slack_error"])
            return

        for ch in body.get("channels", []):
            channels.append(
                {
                    "id": ch.get("id"),
                    "name": ch.get("name"),
                    "is_private": ch.get("is_private", False),
                    "is_member": ch.get("is_member", False),
                    "num_members": ch.get("num_members"),
                    "topic": (ch.get("topic") or {}).get("value", ""),
                }
            )
            if args.limit and len(channels) >= args.limit:
                _ok({"channels": channels[: args.limit]})
                return

        cursor = (body.get("response_metadata") or {}).get("next_cursor") or None
        if not cursor:
            break

    _ok({"channels": channels})


def cmd_channel_history(args) -> None:
    """Fetch channel history with optional time-window filtering.

    Slack returns messages newest-first by default; we keep that ordering
    so the agent sees recent context first.
    """
    cursor: str | None = None
    messages: list[dict] = []
    limit_per_page = 200

    while True:
        params: dict = {
            "channel": args.channel,
            "limit": limit_per_page,
        }
        if args.oldest:
            params["oldest"] = args.oldest
        if args.latest:
            params["latest"] = args.latest
        if cursor:
            params["cursor"] = cursor

        body = _get("conversations.history", params=params)
        if "_slack_error" in body:
            _err(body["_slack_error"])
            return

        for m in body.get("messages", []):
            messages.append(
                {
                    "ts": m.get("ts"),
                    "user": m.get("user"),
                    "text": m.get("text"),
                    "thread_ts": m.get("thread_ts"),
                    "reply_count": m.get("reply_count", 0),
                    "subtype": m.get("subtype"),
                }
            )
            if args.limit and len(messages) >= args.limit:
                _ok({"channel": args.channel, "messages": messages[: args.limit]})
                return

        cursor = (body.get("response_metadata") or {}).get("next_cursor") or None
        if not cursor:
            break

    _ok({"channel": args.channel, "messages": messages})


def cmd_send_message(args) -> None:
    payload: dict = {"channel": args.channel, "text": args.text}
    if args.thread_ts:
        payload["thread_ts"] = args.thread_ts
    body = _post("chat.postMessage", body=payload)
    if "_slack_error" in body:
        _err(body["_slack_error"])
        return
    _ok({"channel": body.get("channel"), "ts": body.get("ts")})


def cmd_lookup_user(args) -> None:
    body = _get("users.info", params={"user": args.user})
    if "_slack_error" in body:
        _err(body["_slack_error"])
        return
    user = body.get("user") or {}
    _ok(
        {
            "id": user.get("id"),
            "name": user.get("name"),
            "real_name": user.get("real_name"),
            "display_name": (user.get("profile") or {}).get("display_name"),
            "is_bot": user.get("is_bot", False),
        }
    )


def cmd_reactions_add(args) -> None:
    body = _post(
        "reactions.add",
        body={"channel": args.channel, "timestamp": args.timestamp, "name": args.emoji},
    )
    if "_slack_error" in body:
        _err(body["_slack_error"])
        return
    _ok({"added": True})


def cmd_reactions_remove(args) -> None:
    body = _post(
        "reactions.remove",
        body={"channel": args.channel, "timestamp": args.timestamp, "name": args.emoji},
    )
    if "_slack_error" in body:
        _err(body["_slack_error"])
        return
    _ok({"removed": True})


# ── Entrypoint ────────────────────────────────────────────────────────────


def main() -> None:
    parser = argparse.ArgumentParser(description="Slack API CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("whoami", help="Verify the bot token and print workspace info.")

    p_list = sub.add_parser(
        "list-channels", help="List channels visible to the bot."
    )
    p_list.add_argument(
        "--include-private",
        action="store_true",
        help="Also list private channels the bot has been invited to.",
    )
    p_list.add_argument(
        "--limit",
        type=int,
        default=0,
        help="Maximum number of channels to return (0 = no limit).",
    )

    p_hist = sub.add_parser(
        "channel-history",
        help="Fetch messages from a channel (newest-first).",
    )
    p_hist.add_argument("--channel", required=True, help="Channel ID, e.g. C0123ABCD.")
    p_hist.add_argument(
        "--oldest", help="Unix ts (or Slack ts) — only return messages after this."
    )
    p_hist.add_argument(
        "--latest", help="Unix ts (or Slack ts) — only return messages before this."
    )
    p_hist.add_argument(
        "--limit",
        type=int,
        default=0,
        help="Max messages to return (0 = no limit, paginate fully).",
    )

    p_send = sub.add_parser("send-message", help="Post a message to a channel.")
    p_send.add_argument("--channel", required=True, help="Channel ID.")
    p_send.add_argument("--text", required=True, help="Message text.")
    p_send.add_argument(
        "--thread-ts",
        dest="thread_ts",
        help="Reply in this thread (the parent message's ts).",
    )

    p_user = sub.add_parser("lookup-user", help="Resolve a Slack user ID.")
    p_user.add_argument("--user", required=True, help="User ID, e.g. U0123ABCD.")

    p_react_add = sub.add_parser("reactions-add", help="Add an emoji reaction.")
    p_react_add.add_argument("--channel", required=True)
    p_react_add.add_argument("--timestamp", required=True, help="Target message ts.")
    p_react_add.add_argument(
        "--emoji", required=True, help="Emoji name, no colons (e.g. 'eyes')."
    )

    p_react_rm = sub.add_parser("reactions-remove", help="Remove an emoji reaction.")
    p_react_rm.add_argument("--channel", required=True)
    p_react_rm.add_argument("--timestamp", required=True)
    p_react_rm.add_argument("--emoji", required=True)

    args = parser.parse_args()
    handlers = {
        "whoami": cmd_whoami,
        "list-channels": cmd_list_channels,
        "channel-history": cmd_channel_history,
        "send-message": cmd_send_message,
        "lookup-user": cmd_lookup_user,
        "reactions-add": cmd_reactions_add,
        "reactions-remove": cmd_reactions_remove,
    }
    handlers[args.command](args)


if __name__ == "__main__":
    main()
