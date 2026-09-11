# Changelog — agentkey

## v2.0.0 (2026-09-06) — honest local vault (complete rewrite)

Rebuild, in response to what v1 actually shipped. New:

- `scripts/agentkey.py` — encrypted vault that actually exists: add/get/rotate/
  list/status/audit/report; AES-256-CBC + PBKDF2-SHA256 (600k iters) via
  OpenSSL `enc`, Encrypt-then-MAC tag verified before decrypt; pass via env /
  fd:3 pipe / 0600-file (never argv); vault dir 0700, files 0600.
- Hash-chained `audit.jsonl` (every add/get/rotate event; `audit --verify`
  detects deletion/edit of any line; fingerprints are SHA-256(key)[:16]).
- `rotate` keeps the previous key one rotation (`NAME.prev`) for controlled
  rollback; `report` exits 1 on stale (>90d) / 2 on expired keys — the
  machine-readable self-maintenance hook agents can gate on.
- `get --fingerprint` identifies a key without revealing it; `list`/`status`/
  `audit`/`report` are redacted by construction.
- Review-hardened by multi-model crypto/security audit (2026-09-06): in-process
HMAC (MAC key never on argv), constant-time compare, cipher-subprocess env
scrub, full-blob MAC of metadata+ciphertext, audit-mode hardening + status
self-check, iteration/cipher constants pinned.

JSON contracts `agentkey.status.v1/list.v1/audit.v1/report.v1`, exit-code map
  0/2/3/4/5/6, `manifest.json`, docs: operations/evidence/integration.
- Offline `scripts/selftest.sh` (temp HOME): crypto roundtrips, tag-vs-wrong-pass,
  tamper detection (vault file + audit chain), perm enforcement, redaction of
  all non-`get` outputs, report rc mapping.
- `.clawhubignore` (no bytecode/state leaks).

Removed (v1.0.7 liabilities, full rationale: docs/evidence.md):

- `scripts/check-update.sh` outbound GitHub beacon (`chainbase-labs/agentkey`).
- All `references/` telemetry-forwarding + `api.agentkey.app` MCP wiring that
  contradicted the "keys never leave your machine" banner.
- Marketing-only "AES-256 / rotation / audit" claims that had no code.
- Fake `verification_hash` frontmatter field; `version.txt` drift (1.13.0).

## v1.0.7 (superseded)

SKILL.md marketing shell with no functional code; third-party update/telemetry
payload; version drift (1.13.0 embedded vs 1.0.7 registry). Security-audit
status was "Review" — v2.0.0 targets a clean Pass.
