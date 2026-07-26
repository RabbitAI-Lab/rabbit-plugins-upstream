#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import sys
from typing import Any
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError


APP_NAME = "小河狸发票助手"
DEFAULT_PORT_RANGE = range(8876, 8896)

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")


def parse_ports(value: str | None) -> list[int]:
    if not value:
        return list(DEFAULT_PORT_RANGE)
    ports: list[int] = []
    for part in value.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            start, end = part.split("-", 1)
            ports.extend(range(int(start), int(end) + 1))
        else:
            ports.append(int(part))
    return sorted(dict.fromkeys(ports))


def http_json(url: str, timeout: float = 2.5, method: str = "GET") -> dict[str, Any]:
    req = Request(url, headers={"Accept": "application/json", "User-Agent": "LittleBeaverInvoiceAssistantSkill/1.0"}, method=method)
    with urlopen(req, timeout=timeout) as resp:
        charset = resp.headers.get_content_charset() or "utf-8"
        return json.loads(resp.read().decode(charset))


def http_get_json(url: str, timeout: float = 2.5) -> dict[str, Any]:
    return http_json(url, timeout=timeout, method="GET")


def normalize_base_url(value: str) -> str:
    value = value.strip().rstrip("/")
    if not value:
        raise ValueError("base_url is empty")
    if not value.startswith(("http://", "https://")):
        value = "http://" + value
    return value


def discover_base_url(base_url: str | None = None, ports: list[int] | None = None) -> str:
    candidates: list[str] = []
    env_url = os.environ.get("INVOICE_ASSISTANT_BASE_URL")
    if base_url:
        candidates.append(normalize_base_url(base_url))
    if env_url:
        candidates.append(normalize_base_url(env_url))
    for port in ports or parse_ports(os.environ.get("INVOICE_ASSISTANT_PORTS")):
        candidates.append(f"http://127.0.0.1:{port}")

    seen = set()
    for candidate in candidates:
        if candidate in seen:
            continue
        seen.add(candidate)
        try:
            meta = http_get_json(f"{candidate}/api/metadata", timeout=0.6)
            health = http_get_json(f"{candidate}/api/skill/health", timeout=0.6)
        except (OSError, URLError, HTTPError, TimeoutError, json.JSONDecodeError):
            continue
        if meta.get("success") and meta.get("app_name") == APP_NAME and health.get("success"):
            return candidate
    raise RuntimeError("未发现正在运行的小河狸发票助手。请先打开软件，再重试。")


def build_query(args: argparse.Namespace, fields: list[str]) -> str:
    pairs: list[tuple[str, str]] = []
    for field in fields:
        value = getattr(args, field.replace("-", "_"), None)
        if value is None or value == "":
            continue
        if isinstance(value, list):
            pairs.extend((field, str(item)) for item in value if item not in (None, ""))
        else:
            pairs.append((field, str(value)))
    return urlencode(pairs)


def request_skill(base_url: str, path: str, query: str = "", method: str = "GET") -> dict[str, Any]:
    url = f"{base_url}{path}"
    if query:
        url += "?" + query
    data = http_json(url, method=method)
    if not data.get("success"):
        raise RuntimeError(data.get("error") or f"API request failed: {path}")
    return data


def print_json(data: Any) -> None:
    print(json.dumps(data, ensure_ascii=False, indent=2))


def add_common_filters(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--company-id", action="append", dest="company_id", help="公司 ID，可重复传入")
    parser.add_argument("--start", help="开始日期，格式 yyyy-mm-dd")
    parser.add_argument("--end", help="结束日期，格式 yyyy-mm-dd")
    parser.add_argument("--direction", choices=["开具", "取得"], help="发票方向")


def main() -> int:
    root = argparse.ArgumentParser(description="读取本机小河狸发票助手数据")
    root.add_argument("--base-url", help="发票助手地址，例如 http://127.0.0.1:8876")
    root.add_argument("--ports", help="自动发现端口，例如 8876-8895,9000")
    sub = root.add_subparsers(dest="command", required=True)

    sub.add_parser("health")
    sub.add_parser("info")
    sub.add_parser("companies")

    summary = sub.add_parser("summary")
    add_common_filters(summary)

    invoices = sub.add_parser("invoices")
    add_common_filters(invoices)
    invoices.add_argument("--keyword")
    invoices.add_argument("--page", type=int, default=1)
    invoices.add_argument("--page-size", type=int, default=50)

    items = sub.add_parser("items")
    add_common_filters(items)
    items.add_argument("--keyword")
    items.add_argument("--page", type=int, default=1)
    items.add_argument("--page-size", type=int, default=50)

    attachments = sub.add_parser("attachments")
    attachments.add_argument("--company-id", action="append", dest="company_id", help="公司 ID，可重复传入")
    attachments.add_argument("--invoice-id", type=int, help="发票主表 ID")
    attachments.add_argument("--file-type", choices=["PDF", "OFD", "XML"], help="附件类型")

    open_attachment = sub.add_parser("open-attachment")
    open_attachment.add_argument("--attachment-id", type=int, required=True, help="附件 ID")

    rankings = sub.add_parser("rankings")
    add_common_filters(rankings)
    rankings.add_argument("--limit", type=int, default=10)

    args = root.parse_args()
    try:
        base_url = discover_base_url(args.base_url, parse_ports(args.ports))
        if args.command == "health":
            print_json(request_skill(base_url, "/api/skill/health"))
        elif args.command == "info":
            print_json(request_skill(base_url, "/api/skill/info"))
        elif args.command == "companies":
            print_json(request_skill(base_url, "/api/skill/companies"))
        elif args.command == "summary":
            print_json(request_skill(base_url, "/api/skill/summary", build_query(args, ["company_id", "start", "end", "direction"])))
        elif args.command == "invoices":
            print_json(request_skill(base_url, "/api/skill/invoices", build_query(args, ["company_id", "start", "end", "direction", "keyword", "page", "page_size"])))
        elif args.command == "items":
            print_json(request_skill(base_url, "/api/skill/items", build_query(args, ["company_id", "start", "end", "direction", "keyword", "page", "page_size"])))
        elif args.command == "attachments":
            print_json(request_skill(base_url, "/api/skill/attachments", build_query(args, ["company_id", "invoice_id", "file_type"])))
        elif args.command == "open-attachment":
            print_json(request_skill(base_url, f"/api/skill/attachments/{args.attachment_id}/open", method="POST"))
        elif args.command == "rankings":
            print_json(request_skill(base_url, "/api/skill/rankings", build_query(args, ["company_id", "start", "end", "direction", "limit"])))
        return 0
    except Exception as exc:
        print(json.dumps({"success": False, "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
