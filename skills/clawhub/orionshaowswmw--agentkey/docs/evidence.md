# Evidence — agentkey v2.0.0

Every security-relevant mechanism, and why. Verified 2026-09-06.

## Encryption at rest

- **AES-256-CBC + PBKDF2 via system OpenSSL CLI**, fresh per-write `-salt`,
  `-pbkdf2 -iter 600000`. OWASP Password Storage Cheat Sheet recommends
  ~600,000 PBKDF2-HMAC-SHA256 iterations; `enc`'s PBKDF2 uses SHA-256 by
  default. OpenSSL `enc` does NOT support AEAD (GCM/EAX) — see OpenSSL wiki/
  r/cryptography consensus — so **encrypt-then-MAC** is required instead:
- **`tag = HMAC-SHA256(SHA256(b"agentkey-mac-v1||" ‖ pass), b"agentkey-v1" ‖ v ‖ cipher ‖ iter ‖ ct)`**
  — full-blob ciphertext+metadata authentication (mutating cipher/iter/v is a
  tag violation → exit 4), domain-separated raw-32-byte MAC key, tag verified
  BEFORE any decrypt. Additionally (v2.0.0 review-driven):
- **MAC computed in-process** via stdlib `hmac` — never `openssl dgst -hmac <key>`
  on argv (a key on argv is readable in /proc/ps/auditd); constant-time compare
  via `hmac.compare_digest`.
- **Cipher subprocess env is scrubbed** of `AGENTKEY_PASS` (children never
  inherit the passphrase: `ps -efww` exposes env blocks on Linux).
- **Audit log mode hardened** (0600 even under odd umasks; `status` checks and
  repairs + reports `audit_mode_hardened`).
  — key separation for the MAC (independent derivation label), tag verified
  BEFORE any decrypt attempt, so modified vault bytes never reach the cipher
  (classic decrypt-of-forged-ciphertext attack class; "validate MAC first"
  guidance in Ferguson/Schneier/Kohno, Cryptography Engineering).
- **Passphrase delivery** via `-pass fd:3` over an inherited pipe —
  never on the openssl argv (ps/eavesdrop), never an env of a child process.

## Why keys arrive on stdin / 0600 files only

Process argv is world-readable in `/proc`, captured by `ps`, `top`, auditd and
most shells' history. The 0600 file check exists because mode-600-by-default
masked-env aversion (corp env logs) makes argv unrecoverable; stdin is not
logged by the process table. Evidence: every documented "API key leaked via
command line" postmortem class.

## Hash-chained audit log (`audit.jsonl`)

Each entry: `{ts, action, name, provider, fp, actor, detail, prev, hash}` where
`hash = SHA256(JSON-without-hash)` and `prev = previous entry's hash` (genesis
=`"0"*64`). `audit --verify` recomputes and compares chains → deleting or
editing a middle entry is detectable (tamper-evident logging, Küçük et al./
Sarbanes style constructs). Fingerprints are SHA-256(key) truncated to 16 hex
chars — non-reversible*, stable identification without disclosure
(*computationally; trivially brute-forceable only for low-entropy keys, which
API keys are not).

## Staleness policy

`report` flags: `expired` = `expires` ISO date in the past (rc 2);
`stale` = age since last rotation > 90 days (rc 1). The 90-day cadence is
widely documented best practice for long-lived API tokens (NIST SP 800-57 §5.3
key-lifetime guidance; major cloud provider rotation docs).

## What the v1.0.7 artifact got wrong (recorded for buyers)

- Claimed "AES-256" with **no code at all** in the bundle.
- Embedded a third-party update beacon (`check-update.sh` → GitHub releases of
  `chainbase-labs/agentkey`) and telemetry forwarding to `api.agentkey.app`
  via MCP — contradicting its "keys NEVER leave your machine" banner.
- `version.txt = 1.13.0` vs published 1.0.7; bogus frontmatter `verification_hash`.
v2.0.0 deletes all of it. Zero outbound: no update check, no telemetry, no MCP.
