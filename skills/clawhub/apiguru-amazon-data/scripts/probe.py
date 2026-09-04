#!/usr/bin/env python3
"""Call the Apiguru Amazon Data API from the command line.

Picks its access mode automatically:

  * APIGURU_API_KEY set  -> keyed API, billed to that account
  * otherwise            -> keyless agent gateway (free probes, then 402)

Only depends on the standard library, so it runs anywhere.

    python probe.py product-details --asin B09DJLW458 --geo US
    python probe.py product --asins B09DJLW458,B0BSHF7WHW
    python probe.py search --query "wireless earbuds" --geo UK
    python probe.py capabilities
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

KEYED_BASE = os.environ.get("APIGURU_BASE_URL", "https://dash.apiguru.app/api/v1")
KEYLESS_BASE = os.environ.get(
    "APIGURU_AGENT_BASE_URL", "https://agent.apiguru.app/agent/v1"
)

# command -> path. Mirrors the endpoint list; see references/endpoints.md.
COMMANDS = {
    "product-details": "/v2/product-details",
    "product-reviews": "/v2/product-reviews",
    "search": "/search",
    "product": "/product",
    "stock": "/stock",
    "best-sellers": "/v2/best-sellers",
    "deals": "/v2/deals",
    "seller-profile": "/seller-profile",
    "seller-products": "/v2/seller-products",
    "seller-reviews": "/v2/seller-reviews",
}

RETRYABLE = {429, 503}


def api_key() -> str | None:
    return os.environ.get("APIGURU_API_KEY") or None


def request(path: str, params: dict[str, str], retries: int = 3):
    """GET with backoff on the statuses that are transient AND unbilled."""
    key = api_key()
    base = KEYED_BASE if key else KEYLESS_BASE
    query = {k: v for k, v in params.items() if v is not None}
    url = f"{base}{path}?{urllib.parse.urlencode(query)}"

    headers = {"Accept": "application/json", "User-Agent": "apiguru-skill-probe/1.0"}
    if key:
        headers["X-API-KEY"] = key

    last_error = None
    for attempt in range(retries + 1):
        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=180) as response:
                return response.status, json.load(response), dict(response.headers)
        except urllib.error.HTTPError as exc:
            raw = exc.read().decode("utf-8", "replace")
            try:
                body = json.loads(raw)
            except ValueError:
                body = {"error": raw[:500]}

            if exc.code in RETRYABLE and attempt < retries:
                # Both of these are explicitly NOT billed, so retrying is free.
                delay = 2**attempt
                print(
                    f"  [{exc.code}] transient, retrying in {delay}s "
                    f"({attempt + 1}/{retries})",
                    file=sys.stderr,
                )
                time.sleep(delay)
                last_error = (exc.code, body, dict(exc.headers))
                continue
            return exc.code, body, dict(exc.headers)
        except urllib.error.URLError as exc:
            last_error = (0, {"error": f"connection failed: {exc.reason}"}, {})
            if attempt < retries:
                time.sleep(2**attempt)
                continue
    return last_error or (0, {"error": "request failed"}, {})


def explain(status: int, headers: dict) -> None:
    """Say what a status means for cost and for what to do next."""
    left = headers.get("X-Free-Probes-Remaining")
    if left is not None:
        note = headers.get("X-Price-Next-Call", "")
        print(
            f"  free probes remaining: {left}"
            + (f" (next call costs {note})" if note else ""),
            file=sys.stderr,
        )

    messages = {
        402: (
            "Payment required. Free probes are spent. Settle the "
            "PAYMENT-REQUIRED challenge with an x402 client, or set "
            "APIGURU_API_KEY."
        ),
        404: "Not found - BILLED. The ASIN is absent from this marketplace; try another geo.",
        400: "Bad input - not billed. ASINs must be 10 UPPERCASE alphanumeric chars.",
        503: "Upstream failure - not billed. Safe to retry.",
        429: "Rate limited. Back off and retry.",
    }
    if status in messages:
        print(f"  {messages[status]}", file=sys.stderr)


def cmd_capabilities() -> int:
    """Show prices and remaining free probes without spending one."""
    url = KEYLESS_BASE.rsplit("/agent/v1", 1)[0] + "/.well-known/x402"
    try:
        with urllib.request.urlopen(url, timeout=30) as response:
            data = json.load(response)
    except Exception as exc:
        print(f"Could not fetch capabilities: {exc}", file=sys.stderr)
        return 1

    print(f"{data['service']}")
    print(f"  rails: {', '.join(data['rails']) or 'none'}")
    print(
        f"  free probes: {data['freeProbesPerIp']} per IP "
        f"per {data['freeProbeWindowHours']}h"
    )
    print("  endpoints:")
    for resource in data["resources"]:
        print(f"    {resource['name']:24} {resource['price']:22} {resource['method']} "
              f"{resource['resource']}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Query the Apiguru Amazon Data API.")
    parser.add_argument("command", choices=[*COMMANDS, "capabilities"])
    for flag in (
        "asin", "asins", "geo", "query", "page", "sort_by", "seller_id",
        "seller_ids", "category", "subcategory_code", "offset", "categories",
        "brands", "brand", "min_price", "max_price", "condition",
        "offers_count", "from_rating", "to_rating",
    ):
        parser.add_argument(f"--{flag.replace('_', '-')}", dest=flag, default=None)
    parser.add_argument("--check-inventory", dest="check_inventory", action="store_true")
    parser.add_argument("--raw", action="store_true", help="Print raw JSON only.")

    args = parser.parse_args(argv)

    if args.command == "capabilities":
        return cmd_capabilities()

    params = {
        k: v
        for k, v in vars(args).items()
        if k not in ("command", "raw", "check_inventory") and v is not None
    }
    if args.check_inventory:
        params["check_inventory"] = "true"

    if not args.raw:
        mode = "keyed" if api_key() else "keyless"
        print(f"-> {args.command} ({mode})", file=sys.stderr)

    status, body, headers = request(COMMANDS[args.command], params)

    if not args.raw:
        explain(status, headers)

    print(json.dumps(body, indent=2, ensure_ascii=False))
    return 0 if status == 200 else 1


if __name__ == "__main__":
    sys.exit(main())
