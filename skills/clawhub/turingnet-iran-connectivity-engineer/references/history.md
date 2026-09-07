# Version history

## v2.3.0 — everything promised, shipped and tested

- **Six real scripts now ship** (previously referenced but absent from the artifact):
  `redact_pii.py` (bilingual PII redactor with Iranian formats: phones incl. Persian digits,
  کد ملی checksum+context gated, IMEI/IMSI(432)/ICCID/PAN Luhn-gated, IBAN mod-97, IPv4/6,
  MAC, keyword-anchored GPS, email obfuscation, token/secret stripping, synthetic mode),
  `guard.py` (the defensive validator §3 always claimed: prohibited-instruction BLOCKs,
  defense-marker exemption, residual-PII warnings), `turingnet_triage.sh` (+`--collect`),
  `rate_limiter.sh` (3 GET/HEAD per 10 min, offline `check`), `low_rate_diag.sh`
  (--owned attestation, clamps, auto-redacted output), `low_bandwidth_report.py`
  (guard-gated, ≤100KB, embedded CSS only).
- **Added the two missing templates** referenced since v2.2.0: `timeline.md` (with incident-
  commander checklist), `redacted_ticket_template.md`.
- **§12 integration made optional** (guarded existence check; previously a hard dangling
  path into another skill).
- **Machine contract**: `schema/verdict.v1.schema.json` covering all three JSON emitters.
- **10-stage sandboxed selftest** (`scripts/selftest.sh`) — no real PII, loopback only.
- **Lean SKILL.md** (~95 lines) with trigger-shaped description, categories/topics,
  `requires.bins`; frontmatter license normalized to MIT-0 (registry value).
- Debug findings fixed during this build: redactor overlap resolution now keeps the
  LONGEST span (a shorter overlapping match could previously leave a token tail exposed);
  landline phones require an explicit prefix (bare 10-digit timestamps were swallowed);
  national-ID redaction is context-anchored (1725552000 and 1000000001 are checksum-valid
  Melli codes by chance — unlabeled valid candidates now raise residual warnings instead
  of silent redaction); replacement counts reflect final kept spans, not candidates.

## v2.2.0 (documented features — scripts existed only as references until v2.3.0)

Templates bundled (55), redactor/triage/timeline/low-bandwidth/rate-limiter documented,
bilingual intake FA/EN.

## v2.1.x and earlier

Progressive privacy hardening, template library growth, operating-mode definitions,
prohibited-work policy. See the registry changelog for per-patch details.
