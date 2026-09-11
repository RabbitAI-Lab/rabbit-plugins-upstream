---
name: ccs-receipt-verify
description: "Offline Ed25519 signature verification for AI-agent audit receipts. Verify that a CCS receipt was signed by a known signer and never tampered with: Ed25519 verification, RFC 8785 JCS canonicalization, SHA-256 content-hash recomputation and 22-field schema/tamper checks, using the vendored open-source CCS verification core. Zero network calls; only the receipt and the issuer public key are needed, private keys are never involved. Use when verifying a CCS receipt, verifying an Ed25519-signed agent decision receipt, or proving whether a signed agent-tool-call receipt was tampered after issuance."
version: 1.0.0
metadata:
  openclaw:
    requires:
      anyBins:
        - python3
        - python
    homepage: https://correctover.com/?utm_source=clawhub&utm_medium=skill&utm_campaign=ccs_verify
    emoji: "🔏"
    envVars:
      - name: CCS_API_TOKEN
        required: false
        description: Optional API key for Correctover's hosted online verification. Local mode needs no credentials at all.
---

# CCS Receipt Verify — Ed25519 local receipt verification

> **Don't trust the receipt. Verify it.**
>
> When you hold a CCS (Correctover Conformance Shape) AI-agent audit receipt
> and need to independently confirm "it was really signed by the issuer, and
> no field changed after signing", use this skill. Verification runs
> **locally by default** (vendored open-source CCS verification core, no
> network, receipt data stays on the machine). You only supply the **receipt
> itself** and the **issuer's public key**; the private key is never needed
> and never sent.
>
> 中文：本地验证单张 CCS AI Agent 审计收据——Ed25519 验签、RFC 8785 JCS
> 规范化、SHA-256 摘要重算、22 字段 schema 校验与篡改证据，默认零网络、
> 数据不出本机，只需收据和签发方公钥，私钥永不参与。

## What it does

A full verification pipeline on a single CCS receipt (local by default):

1. **RFC 8785 JCS canonicalization** — deterministic JSON serialization of
   the 20 fields excluding `signature`/`content_hash` (keys sorted by
   UTF-16, non-ASCII lowercased `\uXXXX`, ECMAScript shortest-number
   representation).
2. **SHA-256 content-hash recomputation** — recompute the digest and compare
   against the receipt's embedded `content_hash`.
3. **Ed25519 signature verification** — verify the canonical payload against
   the issuer public key you provide (PEM/DER/raw 32 bytes all accepted).
4. **22-field schema check** — field completeness, types, enums
   (`allow`/`block`), the 7 `checks` dimension statuses, base64 signature
   length.
5. **Tamper evidence** — on signature or hash failure, emit a cryptographic
   proof list, the signed field scope (20 field names), and internal
   consistency hints.

Stateless and idempotent: verifying the same receipt twice yields
byte-identical results.

## What it does NOT do

- It does not issue receipts and does not run the agent runtime 7-dimension
  checks (that is the CCS runtime's job).
- It makes no policy judgment: whether a receipt "should have allowed or
  blocked" is a policy question; this skill only answers "was it altered
  after signing / signed by the holder of the matching private key".
- It never needs or receives any private key.
- Local mode logs nothing remotely.

## Usage

```bash
# Verify a receipt (human-readable report)
python3 scripts/verify_receipt_online.py \
    -r examples/sample_receipt.json \
    -k examples/sample_pub.pem

# Machine-readable JSON
python3 scripts/verify_receipt_online.py \
    -r receipt.json -k pub.pem --json

# Read receipt from stdin
cat receipt.json | python3 scripts/verify_receipt_online.py -k pub.pem
```

**Exit codes**: `0` = receipt valid; `1` = invalid/tampered (report still
printed — this is a business result, not a crash); `2` = input error.

**Arguments**:

| Arg | Description |
|------|------|
| `-r/--receipt` | Receipt JSON file; omit or `-` for stdin |
| `-k/--public-key` | Issuer Ed25519 public key PEM file (required) |
| `--json` | Emit the full JSON report |
| `--online` | Explicitly use Correctover's hosted verification (default is local, offline) |
| `--endpoint` | Online mode: override the service endpoint (for self-hosted deployments) |

**Privacy boundary**: default verification is entirely local — the script
makes no network request, and neither the receipt nor the public key leaves
the machine. The verification core is the open-source CCS implementation
(same code as the official hosted service). Only with an explicit
`--online` flag are the receipt and the issuer **public key** sent over
HTTPS to the verification service; the private key is never needed, read,
or transmitted in any mode.

## Report fields

```json
{
  "valid": true,
  "errors": [],
  "evidence": {
    "schema": {"ok": true, "issues": []},
    "jcs": {"canonical_bytes": 1247, "digest_sha256": "9dff2be4…"},
    "content_hash": {"match": true, "claimed": "…", "recomputed": "…"},
    "ed25519": {"status": "valid", "verified": true}
  },
  "tamper": null,
  "receipt_ref": {"decision_id": "…", "agent_id": "…", "verdict": "allow"}
}
```

On tampering, `valid=false`, `tamper.detected=true`, `tamper.proof` lists
the cryptographic proofs (signature failure / digest mismatch), and
`tamper.signed_scope` lists the 20 signed fields for field-by-field
comparison.

## Example

```text
  [PASS] JCS canonicalization 1247 bytes, sha256=9dff2be41aa2d14c…
  [PASS] content_hash match
  [PASS] Ed25519 verification  status=valid
  [PASS] 22-field schema check
  RESULT: PASS: receipt authentic and valid  (4.1 ms)
```

Tampered sample (`examples/tampered_receipt.json` — `verdict` and
`checks.security.status` altered, signature unchanged):

```text
  [FAIL] content_hash match
  [FAIL] Ed25519 verification  status=invalid
  ⚠ Tamper evidence:
    - Ed25519 signature verification failed over the JCS canonical payload
    - content_hash does not match recomputed digest: signed fields changed after issuance
  RESULT: FAIL: receipt invalid / tampered
```

## Requirements

Python 3.7+, standard library only (`urllib`/`json`/`hashlib`). No
third-party packages required for local mode.

## About

By **Correctover** (Guigui Wang) — *Correctover = AI Reliability*. CCS
(Correctover Conformance Shape) is an open, vendor-neutral runtime
verification standard for AI agents: 7 dimensions (Structure/Schema/
Latency/Cost/Identity/Integrity/Security) with Ed25519-signed receipts that
turn "the agent did it" into auditable, tamper-evident evidence.
Homepage: <https://correctover.com/?utm_source=clawhub&utm_medium=skill&utm_campaign=ccs_verify>

## Disclaimer

Results are auto-generated and apply only to the submitted input. Automated
verification is an aid only and constitutes no security guarantee,
compliance conclusion, audit opinion, or legal opinion. No endorsement by
OWASP, IETF, or any standards body is claimed. The business impact of a
tampered receipt is outside the scope of automated checks; security
decisions must ultimately rely on qualified human review.

## License

MIT-0 for this ClawHub distribution. Anyone may use, modify, and
redistribute it, including commercially, with no attribution required.
