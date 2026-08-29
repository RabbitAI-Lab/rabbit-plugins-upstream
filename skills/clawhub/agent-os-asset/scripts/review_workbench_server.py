#!/usr/bin/env python3
"""Serve a review workbench with workspace-restricted local actions / 提供仅限 workspace 的本地 review workbench actions。"""

from __future__ import annotations

import argparse
import hmac
from http import HTTPStatus
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import hashlib
import ipaddress
import json
from pathlib import Path
import secrets
import subprocess
import sys
from typing import Type
from urllib import parse


SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_ADAPTER = SCRIPT_DIR / "mixed_folder_adapter.py"
DEFAULT_PIPELINE = SCRIPT_DIR / "asset_pipeline.py"


def inside(root: Path, target: Path) -> bool:
    try:
        target.resolve(strict=False).relative_to(root.resolve())
        return True
    except ValueError:
        return False


def resolve_review_path(root: Path, raw_path: str) -> Path:
    if not raw_path:
        raise ValueError("missing path")
    candidate = Path(raw_path)
    target = candidate.resolve(strict=False) if candidate.is_absolute() else (root / candidate).resolve(strict=False)
    if not inside(root, target):
        raise ValueError(f"path escapes workspace: {raw_path}")
    if not target.exists():
        raise FileNotFoundError(str(target))
    return target


def resolve_scope(root: Path, raw_scope: str) -> Path:
    scope = (root / raw_scope).resolve(strict=False) if raw_scope else root.resolve()
    if not inside(root, scope) or not scope.is_dir():
        raise ValueError(f"invalid scope: {raw_scope}")
    return scope


def imported_decision_path(root: Path, scope: str) -> Path:
    resolve_scope(root, scope)
    label = hashlib.sha256(scope.encode("utf-8")).hexdigest()[:12]
    return root / ".cleanup-extracted" / "imported-decisions" / f"{label}.json"


def pipeline_apply_result(stdout: str) -> dict[str, object]:
    """Extract stable apply/writeback details from pipeline JSON for the browser."""
    try:
        payload = json.loads(stdout)
    except json.JSONDecodeError:
        return {}
    results = payload.get("results", []) if isinstance(payload, dict) else []
    if not isinstance(results, list):
        return {}
    response: dict[str, object] = {}
    for item in results:
        if not isinstance(item, dict):
            continue
        stage = str(item.get("stage", ""))
        if stage == "apply":
            try:
                apply_payload = json.loads(str(item.get("stdout", "")))
            except json.JSONDecodeError:
                apply_payload = {}
            if isinstance(apply_payload, dict):
                for key in ("workbench", "report", "summary", "success"):
                    if key in apply_payload:
                        response[key] = apply_payload[key]
        elif stage == "post-apply-index":
            response["post_apply_index"] = {
                "status": item.get("status", ""),
                "blocked_reason": item.get("blocked_reason", ""),
            }
    return response


def is_loopback_host(host: str) -> bool:
    if host == "localhost":
        return True
    try:
        return ipaddress.ip_address(host).is_loopback
    except ValueError:
        return False


def valid_session_token(headers: object, expected: str) -> bool:
    getter = getattr(headers, "get", None)
    supplied = getter("X-Agent-Asset-Token", "") if getter else ""
    return bool(expected and supplied) and hmac.compare_digest(str(supplied), expected)


class ReviewHandler(SimpleHTTPRequestHandler):
    workspace_root: Path
    adapter_path: Path
    pipeline_path: Path
    allow_write = False
    allow_apply = False
    allow_file_open = False
    session_token = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(self.workspace_root), **kwargs)

    def do_OPTIONS(self) -> None:
        self.send_json(HTTPStatus.FORBIDDEN, {"error": "cross-origin actions disabled"})

    def do_GET(self) -> None:
        parsed = parse.urlparse(self.path)
        if parsed.path == "/__health":
            self.send_json(HTTPStatus.OK, {"status": "ok", "root": str(self.workspace_root)})
            return
        if parsed.path == "/__open":
            if not self.allow_file_open or not valid_session_token(self.headers, self.session_token):
                self.send_json(HTTPStatus.FORBIDDEN, {"error": "file opening is disabled or unauthorized"})
                return
            raw_path = parse.parse_qs(parsed.query).get("path", [""])[0]
            try:
                target = resolve_review_path(self.workspace_root, raw_path)
                subprocess.run(["open", str(target)], check=False)
                self.send_json(HTTPStatus.OK, {"status": "opened", "path": str(target)})
            except (ValueError, FileNotFoundError) as exc:
                self.send_json(HTTPStatus.BAD_REQUEST, {"error": str(exc)})
            return
        super().do_GET()

    def do_POST(self) -> None:
        parsed = parse.urlparse(self.path)
        if parsed.path not in {"/__save_decisions", "/__apply_decisions"}:
            self.send_json(HTTPStatus.NOT_FOUND, {"error": "unknown endpoint"})
            return
        if not valid_session_token(self.headers, self.session_token):
            self.send_json(HTTPStatus.FORBIDDEN, {"error": "invalid session token"})
            return
        if not self.allow_write:
            self.send_json(HTTPStatus.FORBIDDEN, {"error": "decision writes are disabled"})
            return
        if parsed.path == "/__apply_decisions" and not self.allow_apply:
            self.send_json(HTTPStatus.FORBIDDEN, {"error": "decision apply is disabled"})
            return
        try:
            payload = self.read_payload()
            decision_path = self.save_payload(payload)
        except (ValueError, FileNotFoundError, json.JSONDecodeError) as exc:
            self.send_json(HTTPStatus.BAD_REQUEST, {"error": str(exc)})
            return
        if parsed.path == "/__save_decisions":
            self.send_json(HTTPStatus.OK, {"status": "saved", "path": str(decision_path)})
            return
        scope = str(payload["scope"])
        result = subprocess.run(
            [
                sys.executable,
                str(self.pipeline_path),
                "--root",
                str(self.workspace_root),
                "--scope",
                scope,
                "--cleanup-tool",
                str(self.adapter_path),
                "--stage",
                "apply",
                "--decisions",
                str(decision_path),
                "--execute-decisions",
                "--after-apply-index",
                "auto",
                "--json",
            ],
            cwd=self.workspace_root,
            text=True,
            capture_output=True,
            check=False,
        )
        status = HTTPStatus.OK if result.returncode == 0 else HTTPStatus.INTERNAL_SERVER_ERROR
        self.send_json(
            status,
            {
                "status": "executed" if result.returncode == 0 else "failed",
                "path": str(decision_path),
                "apply": pipeline_apply_result(result.stdout),
                "stdout": result.stdout,
                "stderr": result.stderr,
            },
        )

    def read_payload(self) -> dict[str, object]:
        length = int(self.headers.get("Content-Length", "0"))
        if length <= 0 or length > 50 * 1024 * 1024:
            raise ValueError("invalid request body size")
        value = json.loads(self.rfile.read(length).decode("utf-8"))
        if not isinstance(value, dict) or not isinstance(value.get("scope"), str) or not isinstance(value.get("decisions"), list):
            raise ValueError("expected scope and decisions JSON payload")
        return value

    def save_payload(self, payload: dict[str, object]) -> Path:
        scope = str(payload["scope"])
        output = imported_decision_path(self.workspace_root, scope)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        return output

    def send_json(self, status: HTTPStatus, payload: dict[str, object]) -> None:
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def configured_handler(
    root: Path,
    adapter: Path,
    pipeline: Path,
    *,
    allow_write: bool = False,
    allow_apply: bool = False,
    allow_file_open: bool = False,
    session_token: str = "",
) -> Type[ReviewHandler]:
    class Handler(ReviewHandler):
        workspace_root = root.resolve()
        adapter_path = adapter.resolve()
        pipeline_path = pipeline.resolve()

    Handler.allow_write = allow_write
    Handler.allow_apply = allow_apply
    Handler.allow_file_open = allow_file_open
    Handler.session_token = session_token
    return Handler


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--scope", default=".")
    parser.add_argument("--adapter", type=Path, default=DEFAULT_ADAPTER)
    parser.add_argument("--pipeline", type=Path, default=DEFAULT_PIPELINE)
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8766)
    parser.add_argument("--open", action="store_true")
    parser.add_argument("--enable-write", action="store_true", help="Allow saving decisions through the local server / 允许通过本地 server 保存 decisions。")
    parser.add_argument("--enable-apply", action="store_true", help="Allow applying decisions and enable writes / 允许应用 decisions，并同时启用写入。")
    parser.add_argument("--enable-file-open", action="store_true", help="Allow opening reviewed files through the local server / 允许通过本地 server 打开已 review 的文件。")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    root = args.root.expanduser().resolve()
    scope = resolve_scope(root, args.scope)
    adapter = args.adapter.expanduser().resolve()
    pipeline = args.pipeline.expanduser().resolve()
    if not is_loopback_host(args.host):
        raise SystemExit("review server must bind to a loopback host / review server 必须绑定 loopback host")
    if not adapter.is_file():
        raise SystemExit(f"missing adapter / 缺少 adapter: {adapter}")
    if not pipeline.is_file():
        raise SystemExit(f"missing pipeline / 缺少 pipeline: {pipeline}")
    relative_workbench = (scope / "cleanup-asset-review-workbench.html").relative_to(root).as_posix()
    token = secrets.token_urlsafe(24)
    url = f"http://{args.host}:{args.port}/{parse.quote(relative_workbench)}?token={parse.quote(token)}"
    handler = configured_handler(
        root,
        adapter,
        pipeline,
        allow_write=args.enable_write or args.enable_apply,
        allow_apply=args.enable_apply,
        allow_file_open=args.enable_file_open,
        session_token=token,
    )
    server = ThreadingHTTPServer((args.host, args.port), handler)
    print(f"Serving review workbench / 正在提供 review workbench: {url}", flush=True)
    if args.open:
        subprocess.run(["open", url], check=False)
    server.serve_forever()


if __name__ == "__main__":
    main()
