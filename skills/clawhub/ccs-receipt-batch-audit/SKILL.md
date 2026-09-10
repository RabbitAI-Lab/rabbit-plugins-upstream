---
name: ccs-receipt-batch-audit
description: "Batch Ed25519 signature verification for up to 200 AI-agent audit receipts, fully offline. Every receipt is checked against one issuer public key with Ed25519 verification plus RFC 8785 JCS/SHA-256 integrity checks; outputs aggregate valid/invalid statistics, pass rate, tampered-index list with per-receipt failure reasons, and optional hash-chain linkage, using the vendored open-source CCS verification core. Zero network calls. Use when batch-verifying CCS receipts, auditing a batch of signed agent decision receipts, or verifying a receipt chain."
version: 1.0.0
metadata:
  openclaw:
    requires:
      anyBins:
        - python3
        - python
    homepage: https://correctover.com/?utm_source=clawhub&utm_medium=skill&utm_campaign=ccs_batch
    emoji: "🗂️"
    envVars:
      - name: CCS_API_TOKEN
        required: false
        description: Optional API key for Correctover's hosted online audit. Local mode needs no credentials at all.
---

# CCS Receipt Batch Audit — bulk verification & tamper stats (local)

> When you hold an entire batch of CCS AI-agent audit receipts — pipeline
> outputs, log archives, evidence sets handed across systems — and need to
> know in one shot which are authentic and which were tampered with or
> carry invalid signatures, use this skill. Verification runs **locally by
> default** (vendored open-source CCS core, no network, receipts stay on the
> machine). Up to 200 receipts per batch, verified against one issuer public
> key.
>
> 中文：本地批量审计最多 200 张 CCS 审计收据——逐张 Ed25519 验签 + JCS/SHA-256
> 完整性校验，输出有效/无效统计、通过率、篡改索引和逐条失败原因，可选哈希链
> 链接检查；默认零网络、数据不出本机。

## What it does

Every receipt in the batch runs the same full pipeline as single-receipt
verification:

1. **RFC 8785 JCS canonicalization** + **SHA-256 content-hash recompute
   and comparison**;
2. **Ed25519 verification** (one issuer public key for the whole batch;
   PEM/DER/raw 32 bytes accepted);
3. **22-field schema check**;
4. Aggregate output: `total / valid / invalid / pass_rate`, failure-reason
   distribution, the tampered-index list (`tampered_indexes`), and
   per-receipt results (index, decision_id, verdict, error summary, tamper
   flag, duration).
5. **Optional hash-chain check** (`--check-chain`): for ordered batches,
   verify that `previous_receipt_hash[i]` equals the recomputed content
   hash of the prior receipt; reports the first break point (index + reason).

Stateless and idempotent: re-auditing the same batch gives identical
statistics.

## What it does NOT do

- It does not issue receipts and does not judge whether any individual
  business decision "should have allowed or blocked".
- It never receives a private key; the public-key trust anchor is managed by
  the user.
- Batch cap is 200 receipts (the service returns 400 beyond that); split
  larger sets.
- Local mode logs nothing remotely.

## Usage

```bash
# Batch audit (public key embedded in the file, or supplied via -k)
python3 scripts/batch_audit.py -f examples/batch_mixed.json

# Separate public key + hash-chain check
python3 scripts/batch_audit.py -f receipts.json -k pub.pem --check-chain

# Machine-readable JSON (full per-receipt detail)
python3 scripts/batch_audit.py -f receipts.json -k pub.pem --json

# Read from stdin ({"receipts":[...]} or a bare receipt array)
cat receipts.json | python3 scripts/batch_audit.py -k pub.pem
```

**Exit codes**: `0` = all valid; `1` = at least one invalid/tampered receipt
(report still printed); `2` = input error.

**Arguments**:

| Arg | Description |
|------|------|
| `-f/--file` | Batch JSON file (`{"receipts":[...]}` or a bare array); omit or `-` for stdin |
| `-k/--public-key` | Issuer public key PEM file (required unless the file embeds `public_key_pem`) |
| `--check-chain` | Also verify hash-chain linkage between receipts |
| `--json` | Emit the full JSON report (per-item detail) |
| `--online` | Explicitly use Correctover's hosted audit (default is local, offline) |
| `--endpoint` | Online mode: override the service endpoint (self-hosted) |

**Privacy boundary**: default batch verification is entirely local — no
network request, receipts and public keys stay on the machine. The core is
the open-source CCS implementation (same code as the official hosted
service). Only with an explicit `--online` flag are receipts and the issuer
**public key** sent over HTTPS; private keys are never needed, read, or
transmitted.

## Report fields

```json
{
  "total": 5, "valid": 4, "invalid": 1, "pass_rate": 0.8,
  "fail_reason_distribution": {"Ed25519 signature verification failed": 1},
  "tampered_indexes": [4],
  "chain": null,
  "results": [
    {"index": 0, "valid": true, "decision_id": "dec-batch-000",
     "verdict": "allow", "errors": [], "tamper_detected": false,
     "duration_ms": 1.8}
  ]
}
```

## Example

`examples/batch_mixed.json` holds 5 receipts (4 genuinely signed; the 5th
tampered — `verdict` flipped to `block`, `checks.security.status` flipped to
`fail`, signature unchanged):

```text
  total   : 5
  valid   : 4
  invalid : 1
  pass    : 0.8
  tampered: [4]
  Per-receipt (invalid only; use --json for full detail):
    [#4] dec-batch-004 verdict=block tamper=True
        content_hash does not match recomputed SHA-256(JCS payload)
        Ed25519 signature verification failed (signature vs canonical payload mismatch)
```

A 5-receipt batch takes about 4–5 ms locally (measured; varies by machine).

## Requirements

Python 3.7+, standard library only (`urllib`/`json`/`hashlib`). No
third-party packages required for local mode.

## About

By **Correctover** (Guigui Wang) — *Correctover = AI Reliability*. CCS
(Correctover Conformance Shape) is an open, vendor-neutral runtime
verification standard for AI agents: 7 dimensions with Ed25519-signed
receipts that make agent tool calls auditable and tamper-evident — signed
evidence you can hand across teams, pipelines, and systems.
Homepage: <https://correctover.com/?utm_source=clawhub&utm_medium=skill&utm_campaign=ccs_batch>

## Disclaimer

Results are auto-generated and apply only to the submitted data. Automated
checks are an aid only and constitute no security guarantee, compliance
conclusion, audit opinion, or legal opinion. No endorsement by OWASP, IETF,
or any standards body is claimed. The business impact of tampered receipts
is outside the scope of automated checks and requires manual review; any
security or compliance decision must ultimately rely on qualified human
review.

## License

MIT-0 for this ClawHub distribution. Anyone may use, modify, and
redistribute it, including commercially, with no attribution required.
