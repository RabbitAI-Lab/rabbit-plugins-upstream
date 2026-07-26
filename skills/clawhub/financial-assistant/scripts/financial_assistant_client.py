#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.parse
import urllib.request


DEFAULT_PORTS = range(8765, 8785)
SERVICE_NAME = "financial-analysis-system"


def request_json(base_url: str, path: str, method: str = "GET", payload: dict | None = None, timeout: float = 5.0) -> dict:
    data = None
    headers = {"Accept": "application/json", "User-Agent": "LittleBeaverFinancialAssistantSkill/1.0"}
    if payload is not None:
        data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        headers["Content-Type"] = "application/json; charset=utf-8"
    request = urllib.request.Request(f"{base_url}{path}", data=data, headers=headers, method=method)
    with urllib.request.urlopen(request, timeout=timeout) as response:
        body = response.read().decode("utf-8")
    return json.loads(body) if body else {}


def discover_base_url(explicit: str | None = None) -> str:
    candidates = []
    if explicit:
        candidates.append(explicit.rstrip("/"))
    candidates.extend(f"http://127.0.0.1:{port}" for port in DEFAULT_PORTS)
    candidates.extend(f"http://localhost:{port}" for port in DEFAULT_PORTS)
    seen = set()
    for base_url in candidates:
        if base_url in seen:
            continue
        seen.add(base_url)
        try:
            data = request_json(base_url, "/api/local-agent/health", timeout=1.2)
        except Exception:
            continue
        if data.get("service") == SERVICE_NAME and data.get("success"):
            return base_url
    raise SystemExit("未找到正在运行的小河狸财报助手。请先打开软件后再试。")


def encode_query(params: dict[str, object]) -> str:
    filtered = {key: value for key, value in params.items() if value not in (None, "")}
    return urllib.parse.urlencode(filtered)


def print_json(data: dict) -> None:
    print(json.dumps(data, ensure_ascii=False, indent=2))


def main() -> None:
    parser = argparse.ArgumentParser(description="Query local Xiaoheli Financial Statement Assistant data.")
    parser.add_argument("--base-url", help="Override local app base URL, e.g. http://127.0.0.1:8765")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("health")
    sub.add_parser("companies")

    periods = sub.add_parser("periods")
    periods.add_argument("--company")
    periods.add_argument("--period-type", choices=["year", "quarter", "month"])

    metrics = sub.add_parser("metrics")
    metrics.add_argument("--period-id", type=int)
    metrics.add_argument("--company")
    metrics.add_argument("--period-type", choices=["year", "quarter", "month"])

    statement = sub.add_parser("statement")
    statement.add_argument("--period-id", type=int)
    statement.add_argument("--company")
    statement.add_argument("--period-type", choices=["year", "quarter", "month"])
    statement.add_argument("--statement", default="income_statement", choices=["balance_sheet", "income_statement", "cash_flow"])

    trend = sub.add_parser("trend")
    trend.add_argument("--company")
    trend.add_argument("--period-type", default="year", choices=["year", "quarter", "month"])
    trend.add_argument("--metric", default="revenue")

    ask = sub.add_parser("ask")
    ask.add_argument("message")
    ask.add_argument("--company")
    ask.add_argument("--period-type", default="year", choices=["year", "quarter", "month"])
    ask.add_argument("--period-id", type=int)

    args = parser.parse_args()
    base_url = discover_base_url(args.base_url)

    try:
        if args.command == "health":
            print_json(request_json(base_url, "/api/local-agent/health"))
        elif args.command == "companies":
            print_json(request_json(base_url, "/api/local-agent/companies"))
        elif args.command == "periods":
            query = encode_query({"company": args.company, "period_type": args.period_type})
            print_json(request_json(base_url, f"/api/local-agent/periods?{query}"))
        elif args.command == "metrics":
            query = encode_query({"period_id": args.period_id, "company": args.company, "period_type": args.period_type})
            print_json(request_json(base_url, f"/api/local-agent/metrics?{query}"))
        elif args.command == "statement":
            query = encode_query({"period_id": args.period_id, "company": args.company, "period_type": args.period_type, "statement": args.statement})
            print_json(request_json(base_url, f"/api/local-agent/statement?{query}"))
        elif args.command == "trend":
            query = encode_query({"company": args.company, "period_type": args.period_type, "metric": args.metric})
            print_json(request_json(base_url, f"/api/local-agent/trend?{query}"))
        elif args.command == "ask":
            payload = {"message": args.message, "company": args.company, "period_type": args.period_type, "period_id": args.period_id}
            print_json(request_json(base_url, "/api/local-agent/ask", method="POST", payload=payload, timeout=15))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise SystemExit(f"请求失败：HTTP {exc.code} {body}") from exc
    except urllib.error.URLError as exc:
        raise SystemExit(f"无法连接小河狸财报助手：{exc}") from exc


if __name__ == "__main__":
    main()
