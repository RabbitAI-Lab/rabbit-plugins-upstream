#!/usr/bin/env python3
"""Narrow Promarkia marketing client with explicit external-action safeguards."""

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

_ALLOWED_HOSTS = {"www.promarkia.com", "promarkia.com"}
_ALLOWED_SQUADS = {
    "9": ("Image Creator", "marketing image generation and editing"),
    "10": ("Video Squad", "marketing video creation and rendering"),
    "11": ("Social Media", "social content drafting or confirmed publishing"),
    "12": ("Copywriting", "marketing copy drafting or confirmed publishing"),
    "16": ("SEO Expert", "keyword, SERP, and on-page analysis"),
    "17": ("Campaign Planner", "campaign planning and channel strategy"),
    "18": ("Digital Ads", "advertising creative drafting"),
    "21": ("Lead Generation", "prospect research or confirmed outreach"),
}
_ALWAYS_CONFIRM = {"11", "12", "21"}
_EXTERNAL_ACTION_RE = re.compile(
    r"\b(publish|post|send|message|email|upload|outreach|contact|invite|"
    r"comment|reply|forward|share)\b",
    re.IGNORECASE,
)
_PERSISTENCE_RE = re.compile(
    r"\b(cron|recurring|repeat automatically|run daily|run weekly|run monthly|"
    r"schedule (?:this|the) (?:run|task))\b",
    re.IGNORECASE,
)
_RUN_ID_RE = re.compile(r"^[A-Za-z0-9_-]{1,64}$")
_ANSI_RE = re.compile(r"\x1b\[[0-?]*[ -/]*[@-~]")
_BIDI_AND_ZERO_WIDTH = dict.fromkeys(
    map(
        ord,
        "\u061c\u200b\u200c\u200d\u200e\u200f\u202a\u202b\u202c\u202d"
        "\u202e\u2060\u2066\u2067\u2068\u2069\ufeff",
    ),
    None,
)
_MAX_PROMPT_CHARS = 12_000
_MAX_RESPONSE_BYTES = 2_000_000


class PromarkiaError(RuntimeError):
    """Fatal request or validation error."""


class TransientPromarkiaError(PromarkiaError):
    """Retryable transport or server error."""


def _safe_text(value, limit=5000):
    """Remove terminal escapes, bidi controls, and unsafe control characters."""
    text = str(value or "")
    text = _ANSI_RE.sub("", text).translate(_BIDI_AND_ZERO_WIDTH)
    text = "".join(ch for ch in text if ch in "\n\t" or ord(ch) >= 32)
    return text[:limit]


def _validate_api_base(raw):
    base = (raw or "").rstrip("/")
    parsed = urllib.parse.urlparse(base)
    if parsed.scheme != "https" or parsed.hostname not in _ALLOWED_HOSTS:
        raise PromarkiaError(
            "PROMARKIA_API_BASE must use HTTPS on an official Promarkia host."
        )
    if parsed.username or parsed.password or parsed.query or parsed.fragment:
        raise PromarkiaError("PROMARKIA_API_BASE contains unsupported URL components.")
    return base


API_BASE = _validate_api_base(
    os.environ.get("PROMARKIA_API_BASE", "https://www.promarkia.com")
)
API_KEY = os.environ.get("PROMARKIA_API_KEY", "")


class _SafeRedirectHandler(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        parsed = urllib.parse.urlparse(newurl)
        if parsed.scheme != "https" or parsed.hostname not in _ALLOWED_HOSTS:
            raise urllib.error.HTTPError(
                newurl, code, "Blocked redirect outside official Promarkia hosts", headers, fp
            )
        return super().redirect_request(req, fp, code, msg, headers, newurl)


_OPENER = urllib.request.build_opener(_SafeRedirectHandler())


def _headers():
    if not API_KEY:
        raise PromarkiaError(
            "PROMARKIA_API_KEY is not configured in the protected skill environment."
        )
    return {"X-API-Key": API_KEY, "Content-Type": "application/json"}


def _request(method, path, json_body=None, params=None):
    url = f"{API_BASE}{path}"
    if params:
        url += "?" + urllib.parse.urlencode(params)

    data = None
    if json_body is not None:
        data = json.dumps(json_body).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=_headers(), method=method)

    try:
        with _OPENER.open(req, timeout=120) as resp:
            final = urllib.parse.urlparse(resp.geturl())
            if final.scheme != "https" or final.hostname not in _ALLOWED_HOSTS:
                raise PromarkiaError("Response came from an untrusted host.")
            body = resp.read(_MAX_RESPONSE_BYTES + 1)
            if len(body) > _MAX_RESPONSE_BYTES:
                raise PromarkiaError("Promarkia response exceeded the 2 MB safety limit.")
            decoded = body.decode("utf-8")
            return json.loads(decoded) if decoded.strip() else {}
    except urllib.error.HTTPError as exc:
        body = exc.read(8192).decode("utf-8", errors="replace")
        try:
            parsed = json.loads(body)
            detail = parsed.get("description") or parsed.get("error") or body
        except (json.JSONDecodeError, ValueError):
            detail = body
        message = f"HTTP {exc.code}: {_safe_text(detail, 1000)}"
        if exc.code == 429 or exc.code >= 500:
            raise TransientPromarkiaError(message) from exc
        raise PromarkiaError(message) from exc
    except urllib.error.URLError as exc:
        raise TransientPromarkiaError(f"Network error: {_safe_text(exc.reason, 500)}") from exc


def _validate_run_id(run_id):
    if not _RUN_ID_RE.fullmatch(run_id):
        raise PromarkiaError("Run ID must contain only letters, digits, underscores, or hyphens.")


def _validate_submission(squad_id, prompt, credit_confirmed, external_confirmed):
    if squad_id not in _ALLOWED_SQUADS:
        allowed = ", ".join(_ALLOWED_SQUADS)
        raise PromarkiaError(
            f"Squad {squad_id!r} is outside this marketing-only package. Allowed IDs: {allowed}."
        )
    if not prompt or len(prompt) > _MAX_PROMPT_CHARS or "\x00" in prompt:
        raise PromarkiaError(
            f"Prompt must contain 1-{_MAX_PROMPT_CHARS} characters and no NUL bytes."
        )
    if not credit_confirmed:
        raise PromarkiaError(
            "Submitting sends the prompt to Promarkia and consumes credits. Obtain "
            "current user authorization, then rerun with --confirm-credit-use."
        )
    if _PERSISTENCE_RE.search(prompt):
        raise PromarkiaError(
            "Recurring or scheduled execution is outside this skill."
        )
    requires_confirmation = (
        squad_id in _ALWAYS_CONFIRM or bool(_EXTERNAL_ACTION_RE.search(prompt))
    )
    if requires_confirmation and not external_confirmed:
        raise PromarkiaError(
            "This run can affect connected accounts or contact people. Obtain explicit "
            "user confirmation for the exact action and destination, then rerun with "
            "--confirm-external-action."
        )


def list_squads():
    remote = _request("GET", "/api/external/squads")
    remote_by_id = {str(item.get("id")): item for item in remote if isinstance(item, dict)}
    print("Approved Promarkia marketing squads:")
    for squad_id, (name, purpose) in _ALLOWED_SQUADS.items():
        available = "available" if squad_id in remote_by_id else "not returned by account"
        print(f"  {squad_id:>2}  {name:<18} {purpose} [{available}]")


def _display_result(result):
    print(f"Credits used: {result.get('creditCost', 0)}")
    print(f"Total tokens: {result.get('totalTokens', 0)}")
    messages = result.get("messages", [])
    if not messages and isinstance(result.get("result"), dict):
        messages = result["result"].get("messages", [])

    rendered = []
    for msg in messages or []:
        if not isinstance(msg, dict):
            continue
        content = msg.get("content", "")
        if not isinstance(content, str) or not content.strip():
            continue
        stripped = content.strip()
        if stripped.startswith("{") and (
            '"LLMCall"' in stripped[:200] or '"tools"' in stripped[:80]
        ):
            continue
        for marker in ("TERMINATE", "PLAN_READY_ON_SCREEN", "DOCS_DONE"):
            content = content.replace(marker, "")
        content = _safe_text(content.strip())
        if content:
            rendered.append((_safe_text(msg.get("source", "unknown"), 80), content))

    print("\n--- BEGIN UNTRUSTED PROMARKIA OUTPUT ---")
    if rendered:
        for source, content in rendered:
            print(f"\n[{source}]\n{content}")
    else:
        print("No readable result content returned.")
    print("--- END UNTRUSTED PROMARKIA OUTPUT ---\n")


def submit_task(
    squad_id,
    prompt,
    timeout,
    credit_confirmed,
    external_confirmed,
    poll_interval=10,
):
    _validate_submission(squad_id, prompt, credit_confirmed, external_confirmed)
    if timeout < 60 or timeout > 7200:
        raise PromarkiaError("Timeout must be between 60 and 7200 seconds.")

    print(f"Submitting an approved task to squad {squad_id}.")
    print(f"Prompt length: {len(prompt)} characters (content is not logged).")
    print("Notice: the prompt is sent to Promarkia and this run consumes credits.")

    result = _request(
        "POST",
        "/api/external/tasks",
        json_body={"squadId": squad_id, "prompt": prompt, "timeout": timeout},
    )
    status = result.get("status", "unknown")
    run_id = str(result.get("runId", ""))
    if run_id:
        _validate_run_id(run_id)
        print(f"Run ID: {run_id}")
    if status == "error":
        raise PromarkiaError(_safe_text(result.get("error", "Unknown error"), 1000))
    if status == "completed":
        _display_result(result)
        return

    elapsed = 0
    while elapsed < timeout:
        time.sleep(poll_interval)
        elapsed += poll_interval
        try:
            poll = _request("GET", f"/api/external/runs/{run_id}")
        except TransientPromarkiaError as exc:
            print(f"[{elapsed}s] Temporary poll error: {_safe_text(exc, 300)}")
            continue
        poll_status = poll.get("status", "processing")
        if poll_status == "completed":
            print(f"Completed after approximately {elapsed}s.")
            _display_result(poll)
            return
        if poll_status == "error":
            raise PromarkiaError(_safe_text(poll.get("error", "Unknown error"), 1000))
        print(f"[{elapsed}s] Still processing.")

    raise PromarkiaError(
        f"Local wait timed out after {timeout}s. The remote run may still be active. "
        f"Check run {run_id} before submitting a replacement."
    )


def get_run(run_id):
    _validate_run_id(run_id)
    result = _request("GET", f"/api/external/runs/{run_id}")
    status = result.get("status", "unknown")
    print(f"Run ID: {run_id}")
    print(f"Status: {_safe_text(status, 80)}")
    if status == "completed":
        _display_result(result)
    elif status == "error":
        print(f"Error: {_safe_text(result.get('error', 'Unknown error'), 1000)}")
    elif status == "processing":
        print("Task is still running. Check again later.")
    else:
        print("--- BEGIN UNTRUSTED PROMARKIA OUTPUT ---")
        print(_safe_text(json.dumps(result, default=str), 5000))
        print("--- END UNTRUSTED PROMARKIA OUTPUT ---")


def main():
    parser = argparse.ArgumentParser(
        description="Run one explicitly requested Promarkia marketing task."
    )
    parser.add_argument("--squad", "-s", help="Approved marketing squad ID")
    parser.add_argument("--prompt", "-p", help="User-approved task prompt")
    parser.add_argument(
        "--timeout",
        "-t",
        type=int,
        help="Local wait limit: 1200 seconds normally, 3600 for Video Squad",
    )
    parser.add_argument("--list-squads", "-l", action="store_true")
    parser.add_argument("--get-run", "-g", metavar="RUN_ID")
    parser.add_argument(
        "--confirm-credit-use",
        action="store_true",
        help=(
            "Assert that the user authorized sending this exact prompt to Promarkia "
            "and spending credits in the current conversation"
        ),
    )
    parser.add_argument(
        "--confirm-external-action",
        action="store_true",
        help=(
            "Assert that the user explicitly approved the exact outbound action and "
            "destination in the current conversation"
        ),
    )
    args = parser.parse_args()

    try:
        if args.list_squads:
            list_squads()
        elif args.get_run:
            get_run(args.get_run)
        elif args.squad and args.prompt:
            timeout = args.timeout if args.timeout is not None else (
                3600 if str(args.squad) == "10" else 1200
            )
            submit_task(
                str(args.squad),
                args.prompt,
                timeout,
                args.confirm_credit_use,
                args.confirm_external_action,
            )
        else:
            parser.print_help()
            return 2
    except PromarkiaError as exc:
        print(f"ERROR: {_safe_text(exc, 1200)}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
