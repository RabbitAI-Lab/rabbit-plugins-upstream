#!/usr/bin/env python3
"""batch_audit.py — batch-audit up to 200 CCS receipts.

Default mode is FULLY LOCAL verification (no network, no data leaves the
machine): the same Correctover CCS verification core runs in-process.

    * verifies every receipt (JCS canonicalization, SHA-256 content_hash,
      Ed25519 signature against ONE issuer public key you supply, schema)
    * aggregate statistics: total / valid / invalid / pass_rate
    * tamper detection per receipt with tampered-index list
    * optional hash-chain linkage check (--check-chain):
      previous_receipt_hash[i] must equal the recomputed content_hash[i-1]

Use --online ONLY if you explicitly want the Correctover hosted service
(e.g. self-hosted deployments with --endpoint); then receipts and the
issuer's PUBLIC key are sent over HTTPS. No private keys are ever sent.

Input formats (--file or stdin):
  * {"receipts": [ ... ], "public_key_pem": "-----BEGIN PUBLIC KEY-----..."}
  * a bare JSON array of receipts (public key then taken from -k/--public-key)

Exit codes: 0 = all receipts valid; 1 = one or more invalid; 2 = usage/network;
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

MAX_BATCH = 200


def _load_doc(args):
    if args.file and args.file != "-":
        try:
            with open(args.file, encoding="utf-8") as f:
                return json.load(f), None
        except Exception as e:
            return None, f"输入错误: 无法读取批次文件: {e}"
    try:
        return json.load(sys.stdin), None
    except Exception as e:
        return None, f"输入错误: stdin 不是合法 JSON: {e}"


def _pubkey(body, args):
    if body.get("public_key_pem"):
        return body["public_key_pem"], None
    if not args.public_key:
        return None, "输入错误: 批次未内嵌 public_key_pem，需要 -k/--public-key 指定公钥文件"
    try:
        with open(args.public_key, encoding="utf-8") as f:
            return f.read(), None
    except Exception as e:
        return None, f"输入错误: 无法读取公钥文件: {e}"


def _render(rep):
    print("=" * 64)
    print("  CCS 收据批量审计报告（本地验签）")
    print("=" * 64)
    print(f"  总数 total   : {rep.get('total')}")
    print(f"  有效 valid   : {rep.get('valid')}")
    print(f"  无效 invalid : {rep.get('invalid')}")
    print(f"  通过率 pass  : {rep.get('pass_rate')}")
    print(f"  篡改索引     : {rep.get('tampered_indexes')}")
    frd = rep.get("fail_reason_distribution", {})
    if frd:
        print("  失败原因分布 :")
        for k, v in sorted(frd.items(), key=lambda kv: -kv[1]):
            print(f"    - {k}: {v}")
    chain = rep.get("chain")
    if chain is not None:
        print(f"  哈希链检查   : {'链接完整 linked=True' if chain.get('linked') else '存在断裂 breaks'}")
        for b in chain.get("breaks", [])[:10]:
            print(f"    - index {b.get('index')}: {b.get('issue')}")
    print("-" * 64)
    print("  逐条结果 (仅列出无效项，完整明细用 --json):")
    shown = 0
    for r in rep.get("results", []):
        if not r.get("valid"):
            print(f"    [#{r.get('index')}] {r.get('decision_id')} "
                  f"verdict={r.get('verdict')} tamper={r.get('tamper_detected')}")
            for e in r.get("errors", [])[:3]:
                print(f"        {e}")
            shown += 1
    if shown == 0:
        print("    （全部有效）")
    print("-" * 64)
    print(f"  耗时: {rep.get('duration_ms')} ms")
    print("=" * 64)
    print()
    print(DISCLAIMER)


def main() -> int:
    ap = argparse.ArgumentParser(
        description="CCS 收据批量审计（单批最多 200 条；默认本地验签，零外传）")
    ap.add_argument("-f", "--file",
                    help="批量 JSON 文件（{'receipts':[...]} 或纯数组；省略或 '-' 从 stdin）")
    ap.add_argument("-k", "--public-key",
                    help="签发方 Ed25519 公钥 PEM 文件（文件内未内嵌公钥时必填）")
    ap.add_argument("--check-chain", action="store_true",
                    help="额外检查收据间 previous_receipt_hash 哈希链链接")
    ap.add_argument("--online", action="store_true",
                    help="显式使用 Correctover 在线服务验证（默认本地，不联网）")
    ap.add_argument("--endpoint", help="在线模式：覆盖 CCS 服务端点")
    ap.add_argument("--json", action="store_true", help="输出完整机器可读 JSON")
    args = ap.parse_args()

    doc, err = _load_doc(args)
    if err:
        print(err, file=sys.stderr)
        return 2

    if isinstance(doc, list):
        body = {"receipts": doc}
    elif isinstance(doc, dict) and isinstance(doc.get("receipts"), list):
        body = dict(doc)
    else:
        print("输入错误: 需要 {'receipts': [...]} 或收据数组", file=sys.stderr)
        return 2

    if len(body["receipts"]) > MAX_BATCH:
        print(f"输入错误: 单批最多 {MAX_BATCH} 条，收到 {len(body['receipts'])} 条",
              file=sys.stderr)
        return 2

    pub_pem, err = _pubkey(body, args)
    if err:
        print(err, file=sys.stderr)
        return 2
    body["public_key_pem"] = pub_pem
    body["check_chain"] = bool(args.check_chain) or bool(body.get("check_chain"))

    if args.online:
        import ccs_online_client as client  # noqa: E402
        try:
            rep = client.call("/v1/audit/batch", body, endpoint=args.endpoint,
                              timeout=90)
        except client.PaymentRequiredError:
            return 3
        except client.CCSAPIError as e:
            print(f"服务错误: HTTP {e.status} {e.payload}", file=sys.stderr)
            return 2
        if rep.get("ok") is False:
            print(f"服务返回错误: {rep.get('error')}", file=sys.stderr)
            return 2
    else:
        import verify_service as vs  # noqa: E402
        rep = vs.audit_batch(body)
        rep.setdefault("disclaimer", DISCLAIMER)

    if args.json:
        print(json.dumps(rep, ensure_ascii=False, indent=2))
    else:
        _render(rep)
    return 0 if rep.get("invalid", 1) == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
