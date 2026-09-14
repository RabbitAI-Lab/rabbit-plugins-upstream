#!/usr/bin/env python3
"""ccs_online_client.py — stdlib-only HTTP client for the CCS online API.

Shared by the three pay-skill CLI wrappers. No third-party dependency:
uses only urllib so it runs anywhere Python 3 runs.

Endpoint resolution (first hit wins):
  1. --endpoint argument
  2. CCS_API_ENDPOINT environment variable
  3. default public endpoint

A2M payment contract (Alipay 「AI 按量付费」, Agent-to-Merchant over HTTP 402):
  * First call without a valid payment proof -> the server returns
    HTTP 402 Payment Required with a `Payment-Needed` response header
    (and/or JSON body) carrying the bill and price.
  * The Agent performs checkout through the official Alipay payment skill
    (alipay-payment-skill / alipay-bot CLI): the user pays by Alipay.
    THIS script never implements payment itself and never touches any
    merchant key material.
  * After payment the Agent retries the same request carrying the
    `Payment-Proof` request header. Provide it via the CCS_PAYMENT_PROOF
    env var (the legacy CCS_PAY_TOKEN name is accepted as an alias and is
    sent the same way).
  * Server side (merchant): the proof is verified via Alipay OpenAPI
    alipay.aipay.agent.payment.verify before serving, and delivery is
    confirmed via alipay.aipay.agent.fulfillment.confirm afterwards
    (idempotent, retryable).

Self-managed auth (private/demo deployments without billing):
  * CCS_API_TOKEN env var -> sent as X-API-Key.
"""
from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request

DEFAULT_ENDPOINT = "https://ccs-verify-api-ccs-verify-juvxojspeq.cn-hongkong.fcapp.run"
MAX_BODY_BYTES = 2 * 1024 * 1024  # server-side cap


class CCSAPIError(Exception):
    def __init__(self, status: int, payload):
        self.status = status
        self.payload = payload
        super().__init__(f"CCS API HTTP {status}: {payload}")


class PaymentRequiredError(CCSAPIError):
    """HTTP 402: a bill was presented (Payment-Needed); pay and retry with
    a Payment-Proof header. The bill guidance is already printed to stderr
    by the client."""


def resolve_endpoint(cli_value: str | None = None) -> str:
    ep = cli_value or os.environ.get("CCS_API_ENDPOINT") or DEFAULT_ENDPOINT
    return ep.rstrip("/")


def _print_bill(payment_needed_header: str, payload) -> None:
    """Print the 402 bill and the checkout/retry guidance to stderr."""
    lines = ["=" * 64]
    lines.append("⚠️  需要付款：HTTP 402 Payment Required（A2M 支付宝「AI 按量付费」）")
    if payment_needed_header:
        lines.append(f"账单响应头 Payment-Needed: {payment_needed_header}")
    if isinstance(payload, dict) and payload:
        try:
            lines.append("账单响应体: " + json.dumps(payload, ensure_ascii=False))
        except Exception:
            lines.append(f"账单响应体: {payload}")
    lines.append("")
    lines.append("下一步（由 Agent 编排，本脚本不实现支付、不接触商户密钥）：")
    lines.append("  1. 通过支付宝官方支付技能（alipay-payment-skill / alipay-bot CLI）")
    lines.append("     发起收银，用户支付宝扫码/免密完成付款；")
    lines.append("  2. 付款后携带支付凭证重试原请求，例如：")
    lines.append("     CCS_PAYMENT_PROOF=<Payment-Proof 凭证> <原命令>")
    lines.append("=" * 64)
    print("\n".join(lines), file=sys.stderr)


def call(path: str, body: dict, endpoint: str | None = None,
         timeout: float = 30.0) -> dict:
    """POST JSON to the CCS API; return the parsed JSON response.

    Raises PaymentRequiredError on HTTP 402 (bill printed to stderr),
    CCSAPIError on other non-2xx. The request body is never logged.
    """
    ep = resolve_endpoint(endpoint)
    data = json.dumps(body, ensure_ascii=False).encode("utf-8")
    if len(data) > MAX_BODY_BYTES:
        raise CCSAPIError(413, {"error": f"请求体超过 {MAX_BODY_BYTES} 字节上限"})
    headers = {"Content-Type": "application/json; charset=utf-8",
               "User-Agent": "CCS-CLI/1.0 (channel=clawhub)"}
    api_key = os.environ.get("CCS_API_TOKEN")
    if api_key:
        headers["X-API-Key"] = api_key
    # A2M: payment proof from the Alipay checkout flow (official contract
    # header name is Payment-Proof). CCS_PAY_TOKEN kept as a legacy alias.
    proof = os.environ.get("CCS_PAYMENT_PROOF") or os.environ.get("CCS_PAY_TOKEN")
    if proof:
        headers["Payment-Proof"] = proof
    req = urllib.request.Request(ep + path, data=data, headers=headers,
                                 method="POST")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        try:
            payload = json.loads(e.read().decode("utf-8"))
        except Exception:
            payload = {"error": f"HTTP {e.code}"}
        if e.code == 402:
            pn = ""
            try:
                pn = e.headers.get("Payment-Needed", "") or ""
            except Exception:
                pn = ""
            _print_bill(pn, payload)
            raise PaymentRequiredError(402, payload)
        raise CCSAPIError(e.code, payload)
    except urllib.error.URLError as e:
        raise CCSAPIError(0, {"error": f"网络错误: {e.reason}"})


def print_disclaimer(report: dict):
    """Print the server-provided 5-paragraph disclaimer to stderr."""
    d = report.get("disclaimer")
    if d:
        print("---", file=sys.stderr)
        print("免责声明：", d, file=sys.stderr)
