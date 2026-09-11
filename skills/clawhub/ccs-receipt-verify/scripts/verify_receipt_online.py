#!/usr/bin/env python3
"""verify_receipt_online.py — verify ONE CCS receipt.

Default mode is FULLY LOCAL verification (no network, no data leaves the
machine): the same Correctover CCS verification core runs in-process.

    * RFC 8785 JCS canonicalization + SHA-256 content_hash recomputation
    * Ed25519 signature verification against the issuer public key you supply
    * 22-field schema validation
    * tamper evidence (proof list + signed-scope field inventory)

Use --online ONLY if you explicitly want the Correctover hosted service
(e.g. self-hosted deployments with --endpoint); then the receipt and the
issuer's PUBLIC key are sent over HTTPS. No private keys are ever sent in
any mode.

Usage:
    python verify_receipt_online.py -r receipt.json -k pub.pem
    python verify_receipt_online.py -r receipt.json -k pub.pem --json
    cat receipt.json | python verify_receipt_online.py -k pub.pem

Exit codes: 0 = receipt valid; 1 = invalid/tampered; 2 = usage/network error;
            3 = online mode returned HTTP 402 (payment required).
"""
from __future__ import annotations

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

DISCLAIMER = (
    "免责声明： 本结果由 Correctover CCS 收据验证工具自动生成，仅对本次提交的输入数据负责。 "
    "自动化检查仅为辅助手段，不构成安全保证、合规结论、审计意见或法律意见。 "
    "本工具不声称获得 OWASP、IETF 等任何标准组织的背书或认证；报告中引用的标准名称仅用于说明检查依据。 "
    "收据对应的业务影响超出自动检查范围，需人工深度复核。 "
    "任何安全决策与合规判定，应以具备资质的人工审计/复核结论为最终依据。"
)


def _load_inputs(args):
    if not args.receipt or args.receipt == "-":
        try:
            receipt = json.load(sys.stdin)
        except Exception as e:
            print(f"输入错误: stdin 不是合法 JSON: {e}", file=sys.stderr)
            return None, None, 2
    else:
        try:
            with open(args.receipt, encoding="utf-8") as f:
                receipt = json.load(f)
        except Exception as e:
            print(f"输入错误: 无法读取收据文件: {e}", file=sys.stderr)
            return None, None, 2
    try:
        with open(args.public_key, encoding="utf-8") as f:
            pub_pem = f.read()
    except Exception as e:
        print(f"输入错误: 无法读取公钥文件: {e}", file=sys.stderr)
        return None, None, 2
    return receipt, pub_pem, 0


def _render(rep):
    ref = rep.get("receipt_ref", {})
    print("=" * 60)
    print("  CCS 收据验证 — 单收据报告（本地验签）")
    print("=" * 60)
    for k in ("decision_id", "agent_id", "tool", "action", "verdict",
              "timestamp", "issuer"):
        if k in ref:
            print(f"  {k:12s}: {ref[k]}")
    ev = rep.get("evidence", {})
    print("-" * 60)
    jcs = ev.get("jcs", {})
    print(f"  [{'PASS' if jcs.get('canonical_bytes') else 'FAIL'}] JCS 规范化 "
          f"{jcs.get('canonical_bytes', '-')} bytes, "
          f"sha256={str(jcs.get('digest_sha256', ''))[:16]}…")
    ch = ev.get("content_hash", {})
    print(f"  [{'PASS' if ch.get('match') else 'FAIL'}] content_hash 比对")
    sig = ev.get("ed25519", {})
    ok = sig.get("status") == "valid"
    print(f"  [{'PASS' if ok else 'FAIL'}] Ed25519 验签  status={sig.get('status')}")
    sc = ev.get("schema", {})
    print(f"  [{'PASS' if sc.get('ok') else 'FAIL'}] 22 字段 schema 校验 "
          f"{('（' + str(len(sc.get('issues', []))) + ' 个问题）') if sc.get('issues') else ''}")
    print("-" * 60)
    if rep.get("tamper"):
        t = rep["tamper"]
        print("  ⚠ 篡改证据 (tamper detected):")
        for p in t.get("proof", []):
            print(f"    - {p}")
        print(f"  说明: {t.get('note', '')}")
        print("-" * 60)
    if rep.get("errors"):
        print("  errors:")
        for e in rep["errors"]:
            print(f"    - {e}")
        print("-" * 60)
    verdict = "PASS: 收据真实有效" if rep.get("valid") else "FAIL: 收据无效/被篡改"
    print(f"  RESULT: {verdict}  ({rep.get('duration_ms')} ms)")
    print("=" * 60)
    print()
    print(DISCLAIMER)


def main() -> int:
    ap = argparse.ArgumentParser(
        description="验证单张 CCS Ed25519 签名收据（默认本地验签，零外传）")
    ap.add_argument("-r", "--receipt",
                    help="收据 JSON 文件路径（省略或 '-' 从 stdin 读取）")
    ap.add_argument("-k", "--public-key", required=True,
                    help="签发方 Ed25519 公钥（PEM 文件，也可用 DER/原始32字节）")
    ap.add_argument("--online", action="store_true",
                    help="显式使用 Correctover 在线服务验证（默认本地，不联网）")
    ap.add_argument("--endpoint", help="在线模式：覆盖服务端点")
    ap.add_argument("--json", action="store_true", help="输出完整机器可读 JSON")
    args = ap.parse_args()

    receipt, pub_pem, code = _load_inputs(args)
    if code:
        return code

    if args.online:
        import ccs_online_client as client  # noqa: E402
        try:
            rep = client.call("/v1/verify/receipt",
                              {"receipt": receipt, "public_key_pem": pub_pem},
                              endpoint=args.endpoint)
        except client.PaymentRequiredError:
            return 3
        except client.CCSAPIError as e:
            print(f"服务错误: HTTP {e.status} {e.payload}", file=sys.stderr)
            return 2
    else:
        import verify_service as vs  # noqa: E402
        rep = vs.verify_one(receipt, pub_pem)
        rep.setdefault("disclaimer", DISCLAIMER)

    if args.json:
        print(json.dumps(rep, ensure_ascii=False, indent=2))
    else:
        _render(rep)
    return 0 if rep.get("valid") else 1


if __name__ == "__main__":
    sys.exit(main())
