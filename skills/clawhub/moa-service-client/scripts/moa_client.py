#!/usr/bin/env python3
"""Dependency-free client for the MOA Service Agent workflow."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import time
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode, urljoin, urlsplit
from urllib.request import Request, urlopen


DEFAULT_BASE_URL = "http://moa-service.ai.biwin.com:31080"
DEFAULT_WAIT_SECONDS = 4 * 60 * 60
DEFAULT_POLL_SECONDS = 20
TERMINAL_STATES = {"READY_FOR_REVIEW", "APPROVED", "FAILED"}
SHA_RE = re.compile(r"^[0-9a-f]{40}$")
PACKAGE_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CREDENTIALS = PACKAGE_ROOT / "credentials.local.env"


class MOAClientError(RuntimeError):
    def __init__(self, message: str, *, status: int | None = None) -> None:
        super().__init__(message)
        self.status = status


def _json_text(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2)


def _load_token(credentials: Path) -> str:
    token = os.environ.get("MOA_TOKEN", "").strip()
    if token:
        return token
    if credentials.is_file():
        for raw in credentials.read_text(encoding="utf-8").splitlines():
            line = raw.strip()
            if line.startswith("MOA_TOKEN="):
                return line.split("=", 1)[1].strip()
    return ""


class MOAClient:
    def __init__(self, base_url: str, token: str, actor: str) -> None:
        self.base_url = base_url.rstrip("/")
        self.token = token
        self.actor = actor

    def _headers(self, *, json_body: bool = False) -> dict[str, str]:
        headers = {"Accept": "application/json", "X-MOA-Actor": self.actor}
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        if json_body:
            headers["Content-Type"] = "application/json"
        return headers

    def request_json(
        self,
        method: str,
        path: str,
        body: dict[str, Any] | None = None,
        *,
        timeout: float = 60,
    ) -> dict[str, Any]:
        data = json.dumps(body, ensure_ascii=False).encode("utf-8") if body is not None else None
        request = Request(
            urljoin(f"{self.base_url}/", path.lstrip("/")),
            data=data,
            headers=self._headers(json_body=body is not None),
            method=method,
        )
        try:
            with urlopen(request, timeout=timeout) as response:
                payload = response.read()
        except HTTPError as exc:
            payload = exc.read()
            try:
                detail = json.loads(payload.decode("utf-8"))
                message = detail.get("message") or _json_text(detail)
            except (UnicodeDecodeError, json.JSONDecodeError):
                message = payload.decode("utf-8", errors="replace") or str(exc)
            raise MOAClientError(f"HTTP {exc.code}: {message}", status=exc.code) from None
        except URLError as exc:
            raise MOAClientError(f"request failed: {exc.reason}") from None
        try:
            value = json.loads(payload.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise MOAClientError(f"response is not valid JSON: {exc}") from None
        if not isinstance(value, dict):
            raise MOAClientError("response JSON must be an object")
        return value

    def request_bytes(self, path: str, *, timeout: float = 60) -> bytes:
        request = Request(
            urljoin(f"{self.base_url}/", path.lstrip("/")),
            headers=self._headers(),
            method="GET",
        )
        try:
            with urlopen(request, timeout=timeout) as response:
                return response.read()
        except HTTPError as exc:
            raise MOAClientError(f"artifact download failed: HTTP {exc.code}", status=exc.code) from None
        except URLError as exc:
            raise MOAClientError(f"artifact download failed: {exc.reason}") from None


def _parse_repo(value: str) -> dict[str, str]:
    try:
        name, remote_and_sha = value.split("=", 1)
        url, commit = remote_and_sha.rsplit("@", 1)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("repo must be name=http(s)://url.git@40-char-sha") from exc
    if not name.strip() or not SHA_RE.fullmatch(commit):
        raise argparse.ArgumentTypeError("repo must include a name and 40-character lowercase commit SHA")
    parsed = urlsplit(url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise argparse.ArgumentTypeError("repository URL must use HTTP(S)")
    if parsed.username or parsed.password:
        raise argparse.ArgumentTypeError("repository URL must not embed credentials")
    return {"name": name.strip(), "url": url, "commit": commit}


def _create_payload(args: argparse.Namespace) -> dict[str, Any]:
    prompt = Path(args.prompt_file).read_text(encoding="utf-8").strip()
    if not prompt:
        raise MOAClientError("prompt file is empty")
    payload: dict[str, Any] = {
        "requestId": args.request_id,
        "multicaTask": args.multica_task or args.request_id,
        "prompt": prompt,
        "repositories": args.repo,
    }
    if args.callback_url:
        payload["callbackUrl"] = args.callback_url
    return payload


def _wait_for(
    client: MOAClient,
    design_id: str,
    *,
    timeout_s: float,
    poll_s: float,
) -> dict[str, Any]:
    deadline = time.monotonic() + timeout_s
    last_status = ""
    consecutive_errors = 0
    while True:
        try:
            body = client.request_json("GET", f"/v1/designs/{design_id}", timeout=30)
            consecutive_errors = 0
        except MOAClientError as exc:
            consecutive_errors += 1
            if consecutive_errors >= 3:
                raise
            print(f"poll warning ({consecutive_errors}/3): {exc}", file=sys.stderr)
            time.sleep(poll_s)
            continue
        status = str(body.get("status", ""))
        if status != last_status:
            print(f"{design_id}: {status}", file=sys.stderr)
            last_status = status
        if status in TERMINAL_STATES:
            return body
        if time.monotonic() >= deadline:
            raise MOAClientError(
                f"client stopped waiting after {timeout_s:g}s; the server run was not cancelled"
            )
        time.sleep(poll_s)


def _result(
    client: MOAClient,
    design_id: str,
    *,
    version: int | None,
    out_dir: Path | None,
) -> dict[str, Any]:
    query = f"?{urlencode({'version': version})}" if version is not None else ""
    result = client.request_json("GET", f"/v1/designs/{design_id}/result{query}")
    if out_dir is None:
        return result
    out_dir.mkdir(parents=True, exist_ok=True)
    verified: list[dict[str, str]] = []
    artifacts = result.get("artifacts")
    if not isinstance(artifacts, list):
        raise MOAClientError("result response has no artifact list")
    for item in artifacts:
        if not isinstance(item, dict):
            raise MOAClientError("artifact record must be an object")
        name = str(item.get("name", ""))
        url = str(item.get("url", ""))
        expected = str(item.get("sha256", "")).lower()
        if not name or Path(name).name != name or not url or not re.fullmatch(r"[0-9a-f]{64}", expected):
            raise MOAClientError(f"invalid artifact record: {item!r}")
        data = client.request_bytes(url)
        actual = hashlib.sha256(data).hexdigest()
        if actual != expected:
            raise MOAClientError(f"SHA-256 mismatch for {name}: expected {expected}, got {actual}")
        destination = out_dir / name
        destination.write_bytes(data)
        verified.append({"name": name, "sha256": actual, "path": str(destination.resolve())})
    result["verifiedDownloads"] = verified
    return result


def _require_token(parser: argparse.ArgumentParser, args: argparse.Namespace, token: str) -> None:
    if args.command != "doctor" and not token:
        parser.error(
            "MOA_TOKEN is missing; configure it in the runtime environment or credentials.local.env"
        )


def _add_create_args(command: argparse.ArgumentParser) -> None:
    command.add_argument("--request-id", required=True, help="stable upstream correlation/idempotency ID")
    command.add_argument("--multica-task", help="defaults to request-id for non-Multica callers")
    command.add_argument("--prompt-file", required=True, type=Path)
    command.add_argument("--repo", required=True, action="append", type=_parse_repo)
    command.add_argument("--callback-url")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="MOA Service Agent client")
    parser.add_argument("--base-url", default=os.environ.get("MOA_BASE_URL", DEFAULT_BASE_URL))
    parser.add_argument("--credentials", type=Path, default=DEFAULT_CREDENTIALS)
    parser.add_argument("--actor", default=os.environ.get("MOA_ACTOR", "moa-service-client"))
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("doctor", help="check process and dependency readiness")
    models = sub.add_parser("models", help="show model catalog and seven-route snapshot")
    models.add_argument("--refresh", action="store_true", help="refresh in-memory model catalog first")
    fixed = sub.add_parser("fixed-test", help="run the bounded tool-free CC model test")
    fixed.add_argument("--model", required=True)

    create = sub.add_parser("create", help="create one asynchronous design run")
    _add_create_args(create)
    status = sub.add_parser("status", help="get current run status")
    status.add_argument("design_id")
    wait = sub.add_parser("wait", help="poll a run to a terminal state")
    wait.add_argument("design_id")
    wait.add_argument("--timeout", type=float, default=DEFAULT_WAIT_SECONDS)
    wait.add_argument("--poll", type=float, default=DEFAULT_POLL_SECONDS)
    runs = sub.add_parser("runs", help="get sanitized per-invocation records")
    runs.add_argument("design_id")
    runs.add_argument("--version", type=int)
    result = sub.add_parser("result", help="get and optionally download verified artifacts")
    result.add_argument("design_id")
    result.add_argument("--version", type=int)
    result.add_argument("--out", type=Path)

    run = sub.add_parser("run", help="create, wait, and optionally download in one command")
    _add_create_args(run)
    run.add_argument("--timeout", type=float, default=DEFAULT_WAIT_SECONDS)
    run.add_argument("--poll", type=float, default=DEFAULT_POLL_SECONDS)
    run.add_argument("--out", type=Path)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    token = _load_token(args.credentials)
    _require_token(parser, args, token)
    client = MOAClient(args.base_url, token, args.actor)

    try:
        if args.command == "doctor":
            health = client.request_json("GET", "/health", timeout=30)
            ready = client.request_json("GET", "/ready", timeout=30)
            print(_json_text({"health": health, "ready": ready}))
            return 0 if ready.get("ready") is True else 2
        if args.command == "models":
            if args.refresh:
                client.request_json("POST", "/v1/admin/model-center/models/refresh", timeout=60)
            print(_json_text(client.request_json("GET", "/v1/admin/model-center")))
            return 0
        if args.command == "fixed-test":
            body = client.request_json(
                "POST",
                "/v1/admin/diagnostics/claude-code/fixed-test",
                {"model": args.model},
                timeout=90,
            )
            print(_json_text(body))
            return 0 if body.get("status") == "NORMAL" else 2
        if args.command == "create":
            print(_json_text(client.request_json("POST", "/v1/designs", _create_payload(args))))
            return 0
        if args.command == "status":
            print(_json_text(client.request_json("GET", f"/v1/designs/{args.design_id}")))
            return 0
        if args.command == "wait":
            body = _wait_for(client, args.design_id, timeout_s=args.timeout, poll_s=args.poll)
            print(_json_text(body))
            return 3 if body.get("status") == "FAILED" else 0
        if args.command == "runs":
            query = f"?{urlencode({'version': args.version})}" if args.version is not None else ""
            print(
                _json_text(
                    client.request_json("GET", f"/v1/admin/designs/{args.design_id}/runs{query}")
                )
            )
            return 0
        if args.command == "result":
            print(_json_text(_result(client, args.design_id, version=args.version, out_dir=args.out)))
            return 0
        if args.command == "run":
            created = client.request_json("POST", "/v1/designs", _create_payload(args))
            design_id = str(created.get("designId", ""))
            if not design_id:
                raise MOAClientError("create response has no designId")
            print(_json_text(created), file=sys.stderr)
            terminal = _wait_for(client, design_id, timeout_s=args.timeout, poll_s=args.poll)
            if terminal.get("status") == "FAILED":
                print(_json_text(terminal))
                return 3
            version = terminal.get("currentVersion")
            print(
                _json_text(
                    _result(
                        client,
                        design_id,
                        version=version if isinstance(version, int) else None,
                        out_dir=args.out,
                    )
                )
            )
            return 0
    except (MOAClientError, OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    parser.error(f"unsupported command: {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
