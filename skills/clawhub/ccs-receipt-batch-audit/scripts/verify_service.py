#!/usr/bin/env python3
"""verify_service.py — stateless online verification logic.

Wraps the offline CCS core (_ccs_core.py, copied verbatim from the published
ccs-receipt-verifier skill) with:

* single-receipt online verification report
* batch audit (<=200 receipts) with aggregate statistics
* optional hash-chain linkage check for ordered receipt batches

No state is kept between requests; no request content is logged.
"""
from __future__ import annotations

import time
from typing import Any

import core_ccs as core
import mcp_rules

BATCH_LIMIT = 200

# Fields cryptographically covered by the Ed25519 signature / content_hash.
SIGNED_SCOPE = [f for f in core.CCS_REQUIRED_FIELDS if f not in
                (core.SIGNATURE_FIELD, core.CONTENT_HASH_FIELD)]
# Fields NOT inside the signed pre-image (self-referential / derived).
UNSIGNED_FIELDS = [core.SIGNATURE_FIELD, core.CONTENT_HASH_FIELD]

# Audit-relevant fields to list when signed content has been altered after
# issuance (the signature proves *some* signed field changed; the content_hash
# mismatch confirms it — without an original copy no cryptographically sound
# field-level localization is possible).
AUDIT_SENSITIVE_FIELDS = [
    "verdict", "reason", "checks", "decision_id", "agent_id", "tool",
    "action", "request", "response", "policy_id", "policy_hash",
]


def _decode_public_key(public_key_pem: str | bytes | None):
    """Decode a PEM/DER/base64/raw public key; return None if absent/invalid."""
    if public_key_pem is None:
        return None
    if isinstance(public_key_pem, bytes):
        try:
            return core.load_public_key(public_key_pem)
        except Exception:
            return None
    if not isinstance(public_key_pem, str):
        return None
    s = public_key_pem.strip()
    if not s:
        return None
    # 1. PEM text
    if "BEGIN" in s:
        try:
            return core.load_public_key(s.encode("utf-8"))
        except Exception:
            pass
    # 2. base64-wrapped PEM (no PEM labels)
    import base64 as _b64
    try:
        raw = _b64.b64decode(s, validate=True)
        if b"BEGIN" in raw:
            return core.load_public_key(raw)
        return core.load_public_key(raw)  # DER / raw 32B
    except Exception:
        pass
    # 3. last resort: feed the string straight to the core loader
    try:
        return core.load_public_key(s)
    except Exception:
        return None


def verify_one(receipt: Any, public_key_pem: str | bytes | None) -> dict:
    """Verify one receipt. Returns a structured online report dict."""
    t0 = time.perf_counter()
    errors: list[str] = []
    evidence: dict[str, Any] = {}
    tamper: dict[str, Any] | None = None

    if not isinstance(receipt, dict):
        return {
            "valid": False,
            "errors": ["receipt 不是 JSON 对象"],
            "evidence": {},
            "tamper": None,
            "duration_ms": round((time.perf_counter() - t0) * 1000, 3),
        }

    pub = _decode_public_key(public_key_pem)

    # --- 1. schema ---
    schema_errors = core.validate_schema(receipt)
    evidence["schema"] = {"ok": not schema_errors, "issues": schema_errors[:10]}
    errors.extend(schema_errors)

    # --- 2. canonicalization + digest ---
    try:
        payload = core.signing_payload(receipt)
        digest = core.sha256_hex(payload)
        evidence["jcs"] = {
            "canonical_bytes": len(payload),
            "digest_sha256": digest,
        }
    except Exception as e:
        payload = b""
        digest = ""
        errors.append(f"JCS 规范化失败: {e}")
        evidence["jcs"] = {"ok": False, "error": str(e)}

    # --- 3. content_hash comparison ---
    claimed_hash = receipt.get("content_hash")
    hash_ok = isinstance(claimed_hash, str) and claimed_hash == digest and bool(payload)
    evidence["content_hash"] = {
        "claimed": claimed_hash if isinstance(claimed_hash, str) else None,
        "recomputed": digest or None,
        "match": hash_ok,
    }
    if payload and isinstance(claimed_hash, str) and not hash_ok:
        errors.append("content_hash 与重算的 SHA-256(JCS payload) 不一致")

    # --- 4. Ed25519 signature ---
    sig_ok = False
    sig_status = "missing"
    if pub is None:
        sig_status = "no_public_key"
        errors.append("未提供可用的 Ed25519 公钥，无法验签（可在请求中传 public_key_pem）")
    else:
        sig_b64 = receipt.get("signature")
        if isinstance(sig_b64, str) and payload:
            try:
                sig_raw = core.b64d(sig_b64)
                try:
                    pub.verify(sig_raw, payload)
                    sig_ok = True
                    sig_status = "valid"
                except Exception:
                    sig_ok = False
                    sig_status = "invalid"
            except Exception:
                sig_status = "malformed"
        if not sig_ok and sig_status != "no_public_key":
            errors.append("Ed25519 签名验证失败（签名与规范化载荷不匹配）")
    evidence["ed25519"] = {"status": sig_status, "verified": sig_ok}

    # --- 5. tamper evidence ---
    content_altered = payload and isinstance(claimed_hash, str) and not hash_ok
    sig_failed = not sig_ok and sig_status in ("invalid", "malformed")
    if content_altered or sig_failed:
        tamper = {
            "detected": True,
            "proof": [],
            "note": ("密码学证明：该收据在签发后被改动，或被非签发方密钥签名。"
                     "单条收据无原始副本时，密码学可证明内容被篡改，但无法定位具体字段；"
                     "以下字段属于签名覆盖范围，建议逐一比对原始收据。"),
            "signed_scope": SIGNED_SCOPE,
            "unsigned_fields": UNSIGNED_FIELDS,
            "audit_sensitive_fields": AUDIT_SENSITIVE_FIELDS,
        }
        if sig_failed:
            tamper["proof"].append("Ed25519 签名对 JCS 规范化载荷验签失败")
        if content_altered:
            tamper["proof"].append("content_hash 与重算摘要不一致：签名覆盖字段在签发后被修改")
        # light internal-consistency hints (not cryptographic localization)
        hints = _consistency_hints(receipt)
        if hints:
            tamper["consistency_hints"] = hints

    valid = not errors
    return {
        "valid": valid,
        "errors": errors,
        "evidence": evidence,
        "tamper": tamper,
        "receipt_ref": {
            k: receipt.get(k) for k in
            ("decision_id", "agent_id", "tool", "action", "verdict",
             "timestamp", "issuer", "public_key_id", "previous_receipt_hash")
            if isinstance(receipt, dict) and k in receipt
        },
        "duration_ms": round((time.perf_counter() - t0) * 1000, 3),
    }


def _consistency_hints(receipt: dict) -> list[str]:
    """Non-cryptographic internal-consistency observations (hints only)."""
    hints: list[str] = []
    verdict = receipt.get("verdict")
    checks = receipt.get("checks")
    if isinstance(checks, dict):
        statuses = [v.get("status") for v in checks.values() if isinstance(v, dict)]
        fails = [k for k, v in checks.items() if isinstance(v, dict) and v.get("status") == "fail"]
        if verdict == "allow" and fails:
            hints.append(f"verdict=allow 但 checks.{fails[0]}.status=fail（逻辑矛盾，人工复核）")
        if verdict == "block" and statuses and all(s == "pass" for s in statuses):
            hints.append("verdict=block 但 7 项 checks 全部 pass（逻辑矛盾，人工复核）")
    return hints


def audit_batch(payload: dict) -> dict:
    """Verify a batch of receipts.

    payload: {"receipts": [...], "public_key_pem"?: str, "check_chain"?: bool}
    """
    t0 = time.perf_counter()
    receipts = payload.get("receipts")
    if not isinstance(receipts, list):
        return {"error": "receipts 必须是数组", "ok": False}
    if len(receipts) == 0:
        return {"error": "receipts 为空", "ok": False}
    if len(receipts) > BATCH_LIMIT:
        return {"error": f"每批最多 {BATCH_LIMIT} 条，收到 {len(receipts)} 条",
                "ok": False}

    pub_pem = payload.get("public_key_pem")
    check_chain = bool(payload.get("check_chain", False))

    results = []
    fail_reasons: dict[str, int] = {}
    tampered_indexes: list[int] = []
    valid_count = 0
    for i, r in enumerate(receipts):
        rep = verify_one(r, pub_pem)
        if rep["valid"]:
            valid_count += 1
        else:
            if rep.get("tamper"):
                tampered_indexes.append(i)
            for e in rep["errors"]:
                key = e.split("（")[0].split(":")[0][:40]
                fail_reasons[key] = fail_reasons.get(key, 0) + 1
        results.append({
            "index": i,
            "valid": rep["valid"],
            "decision_id": rep["receipt_ref"].get("decision_id"),
            "verdict": rep["receipt_ref"].get("verdict"),
            "errors": rep["errors"][:5],
            "tamper_detected": bool(rep.get("tamper")),
            "duration_ms": rep["duration_ms"],
        })

    chain_report = None
    if check_chain:
        chain_report = _check_chain(receipts)

    total = len(receipts)
    return {
        "ok": True,
        "total": total,
        "valid": valid_count,
        "invalid": total - valid_count,
        "pass_rate": round(valid_count / total, 4),
        "fail_reason_distribution": fail_reasons,
        "tampered_indexes": tampered_indexes,
        "chain": chain_report,
        "results": results,
        "duration_ms": round((time.perf_counter() - t0) * 1000, 3),
    }


def _check_chain(receipts: list[dict]) -> dict:
    """Optional linkage check: previous_receipt_hash[i] == content_hash[i-1]."""
    breaks = []
    prev_digest = None
    for i, r in enumerate(receipts):
        if not isinstance(r, dict):
            breaks.append({"index": i, "issue": "非对象收据"})
            continue
        link = r.get("previous_receipt_hash")
        try:
            digest = core.sha256_hex(core.signing_payload(r))
        except Exception:
            digest = None
        if i == 0:
            if link not in (None, core.GENESIS_HASH):
                breaks.append({"index": i, "issue": "首条收据 previous_receipt_hash 非 null/genesis"})
        else:
            if prev_digest is not None and link != prev_digest:
                breaks.append({
                    "index": i,
                    "issue": "哈希链断裂：previous_receipt_hash 与前一条 content_hash 不匹配",
                    "expected": prev_digest,
                    "claimed": link,
                })
        prev_digest = r.get("content_hash") if digest else prev_digest
        # Use recomputed digest as the true link target when available
        if digest:
            prev_digest = digest
    return {"linked": not breaks, "breaks": breaks[:20], "checked": len(receipts)}


def checkup_mcp(payload: dict) -> dict:
    """Static MCP/Agent security checkup.

    payload: {"config": <parsed MCP config object> | "<json string>",
              "endpoint_url"?: str}
    """
    t0 = time.perf_counter()
    config = payload.get("config")
    if isinstance(config, str):
        import json as _json
        try:
            config = _json.loads(config)
        except Exception as e:
            return {"error": f"config 不是合法 JSON: {e}", "ok": False}

    # If an endpoint URL is supplied, treat it as a single-server remote
    # config for static checks (NO network connection is made).
    endpoint = payload.get("endpoint_url")
    if config is None and isinstance(endpoint, str) and endpoint:
        config = {"mcpServers": {"remote": {"url": endpoint, "type": "http"}}}

    if config is None:
        return {"error": "需要 config（MCP 配置 JSON 对象/字符串）或 endpoint_url", "ok": False}

    report = mcp_rules.check_config(config)
    report["ok"] = True
    report["duration_ms"] = round((time.perf_counter() - t0) * 1000, 3)
    report["manual_audit_note"] = (
        "以上为 14 项自动化静态检查结果，仅为初筛。远程端点的实时行为、工具实现代码、"
        "权限边界与数据流需人工深度审计确认，详见报告免责声明。"
    )
    return report
