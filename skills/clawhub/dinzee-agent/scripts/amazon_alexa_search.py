#!/usr/bin/env python3
"""Amazon Alexa Shopping search through Dinzee Gateway.

Keeps the legacy local-script output envelope while routing the paid data call
through /v1/mcp/calls.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import time

from dinzee_wrapper import dinzee_call


SKILL_SLUG = "dinzee-amazon-alexa-for-shopping"
PROVIDER = "amazon_alexa"
TOOL = "alexa_search"


def _stable_key(arguments: dict, explicit: str | None) -> str:
    if explicit:
        return explicit
    encoded = json.dumps(arguments, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return "amazon_alexa:" + hashlib.sha256(encoded.encode("utf-8")).hexdigest()


def _legacy_envelope(gateway_response: dict, cost_ms: int) -> dict:
    result = gateway_response.get("result") if isinstance(gateway_response.get("result"), dict) else {}
    ok = gateway_response.get("ok") is True
    billing = gateway_response.get("billing") if isinstance(gateway_response.get("billing"), dict) else {}
    return {
        "stdout": result.get("stdout", ""),
        "data": result.get("data", result),
        "resultsNum": result.get("resultsNum", result.get("results_num", 0)),
        "code": result.get("code", 0 if ok else 1),
        "errcode": result.get("errcode", 0 if ok else 1),
        "msg": result.get("msg", "success" if ok else gateway_response.get("error", "failed")),
        "errmsg": result.get("errmsg", "" if ok else gateway_response.get("error", "failed")),
        "costTime": result.get("costTime", cost_ms),
        "taskId": result.get("taskId", gateway_response.get("request_id", "")),
        "request_id": gateway_response.get("request_id", ""),
        "billing": {
            "chargedPoints": billing.get("chargedPoints", 0),
            "chargeStatus": billing.get("chargeStatus", gateway_response.get("chargeStatus", "")),
            "ledgerId": billing.get("ledgerId"),
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Call Amazon Alexa shopping search via Dinzee Gateway")
    parser.add_argument("--prompts", required=True, help="JSON array or plain prompt string")
    parser.add_argument("--format", default="markdown")
    parser.add_argument("--url", default="")
    parser.add_argument("--idempotency-key", default="")
    parser.add_argument("--timeout", type=int, default=180)
    args = parser.parse_args()

    try:
        prompts = json.loads(args.prompts)
    except json.JSONDecodeError:
        prompts = [args.prompts]
    if not isinstance(prompts, list) or not prompts:
        print("Error: --prompts must be a non-empty JSON array or prompt string", file=sys.stderr)
        sys.exit(2)

    arguments = {"prompts": prompts, "format": args.format}
    if args.url:
        arguments["url"] = args.url

    started = time.time()
    response = dinzee_call(
        PROVIDER,
        TOOL,
        arguments,
        _stable_key(arguments, args.idempotency_key),
        skill_slug=SKILL_SLUG,
        timeout=max(60, args.timeout),
    )
    elapsed_ms = int((time.time() - started) * 1000)
    print(json.dumps(_legacy_envelope(response, elapsed_ms), ensure_ascii=False, indent=2))
    if response.get("ok") is not True:
        sys.exit(1)


if __name__ == "__main__":
    main()

