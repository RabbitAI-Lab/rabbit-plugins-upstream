# 🌐 turingnet-iran-connectivity-engineer

**v2.3.0 — everything the docs promise, now real scripts + tests.**
Privacy-first, lawful, no-bypass connectivity troubleshooting for the Iran context (FA/EN).
This README is the quality gate (functionality, permissions, security, verification hash);
`SKILL.md` is the operational instruction layer; `references/history.md` holds version history.

## ✨ Functionality

- **Evidence redactor** `scripts/redact_pii.py` — bilingual (normalizes Persian/Arabic
  digits), Iran-specific: phone numbers, کد ملی (checksum + context gated), IMEI / IMSI
  (432-MCC) / SIM ICCID / bank PAN (Luhn gated), IBAN/Sheba (mod-97), IPv4/IPv6, MAC,
  keyword-anchored GPS pairs, email obfuscation, bearer tokens / secrets / passwords.
  `--synthetic` mode for public reports; strict mode flags residual suspicion (exit 2).
- **Defensive guard** `scripts/guard.py` — makes the "enforced by defensive validator"
  promise real: BLOCKs drafts containing bypass/circumvention/tunnel-evasion/scanning/
  flooding/credential-harvesting/exploit instructions; ships defense templates marked
  `<!-- turingnet:defense -->` that legitimately discuss threats (SIM-jacking, DPI) and pass.
- **60-second triage** `scripts/turingnet_triage.sh` (+ `--collect` auto-redacted record).
- **Status-page rate limiter** `scripts/rate_limiter.sh` — 3 GET/HEAD per 10 min hard cap,
  offline `check`, one bounded curl per `get`.
- **Owned-scope diagnostics** `scripts/low_rate_diag.sh` — requires `--owned` attestation,
  clamps count 1–5 / interval ≥2 s, single stream, output auto-redacted.
- **Low-bandwidth report builder** `scripts/low_bandwidth_report.py` — guard-gated,
  ≤100 KB self-contained HTML (embedded CSS, no JS/CDN/trackers), size-cap split marker.
- **55 templates** incl. the previously-missing `timeline.md` and
  `redacted_ticket_template.md`; bilingual FA/EN intake and tickets.
- **Machine contract** `schema/verdict.v1.schema.json` for all `--json` outputs.
- **10-stage sandboxed selftest** `scripts/selftest.sh` (throwaway HOME, loopback-only).

## 🚀 Usage

```bash
openclaw skills install @orionshaowswmw/turingnet-iran-connectivity-engineer
# or: npx --yes clawhub@latest install turingnet-iran-connectivity-engineer
bash skills/turingnet-iran-connectivity-engineer/scripts/turingnet_triage.sh
python3 skills/turingnet-iran-connectivity-engineer/scripts/redact_pii.py \
  --input evidence_raw.txt --output evidence_redacted.txt --mode strict --json
```

## 🔐 Permissions & Requirements

- **Reads**: files you point it at (evidence, drafts). **Writes**: the `--output` path you
  give (or cwd for triage records / `--output` reports), plus its own state file
  `~/.cache/turingnet/rate.json` (rate-limiter budget only).
- **Network**: NONE by default. The only networked command is `rate_limiter.sh get <URL>`
  which you invoke explicitly, once per call, capped 3/10 min, 10 s timeout, http(s) only.
  `low_rate_diag.sh` sends `ping` (1 packet at a time, ≤5, ≥2 s apart) only with your
  `--owned` attestation. No telemetry, no reporting home.
- **Requires**: python3, bash, curl (`ping` optional for the diag script).
- **Never touches**: real user state outside the paths above; tests run in `mktemp` sandboxes.

## 🔒 Security & Privacy

- Redaction is checksum-gated (Melli, Luhn, mod-97) and context-anchored to avoid
  destroying evidence utility while catching real identifiers — bilingual, with
  zero-width-character and homoglyph normalization.
- The guard BLOCKs prohibited-instruction drafts before any report is built
  (`low_bandwidth_report.py` refuses on guard exit 2). Attack instructions block even
  inside defense-marked templates.
- Honest limitation: regex redaction is best-effort pattern detection — a PASS verdict
  means "no known pattern found", not proof of cleanliness. Human review before sharing
  remains mandatory; strict mode exists to surface suspicion, not to silence it.
- Keys/secrets never logged; nothing networks except the two explicitly invoked
  commands above. Review before install: everything is plain text (md/py/sh/json).

## ✅ Verification hash

sha256 of this release's `SKILL.md`:

```
ad5015cb88bd65221d6442d9c8960e18571c3e0e8660676eba3befc46e3c46de
```

Check: `sha256sum SKILL.md`

## Compatibility & license

Plain files + stdlib Python 3 / bash / curl. Works in any SKILL.md-compatible agent
(OpenClaw, Claude Code, Cursor, Codex CLI) and any model that can read files/JSON.
MIT-0.
