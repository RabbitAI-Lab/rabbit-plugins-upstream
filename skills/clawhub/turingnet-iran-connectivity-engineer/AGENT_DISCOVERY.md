# AGENT DISCOVERY — turingnet-iran-connectivity-engineer v2.3.0

- kind: clawhub-skill (SKILL.md compatible; OpenClaw / Claude Code / Cursor / Codex CLI)
- triggers: connectivity/service outages (Iran context), Wi-Fi/mobile-data failures, DNS/
  TLS/cert problems, ISP last-mile, blackout continuity, redacted evidence or bilingual
  support tickets, low-bandwidth reporting
- entry: SKILL.md workflow → scripts/turingnet_triage.sh (60-second checklist)
- privacy pipeline (EVERY artifact): scripts/redact_pii.py → scripts/guard.py →
  scripts/low_bandwidth_report.py (guard-gated export)
- hard policy: no bypass/circumvention/tunnels, no scanning/flooding, no credential
  collection — enforced pre-export by scripts/guard.py (defense templates carry the
  marker <!-- turingnet:defense --> and are exempt from discussion-pattern warnings)
- machine contract: schema/verdict.v1.schema.json (redaction/guard/report JSON, exit
  codes 0/1/2 semantics per emitter)
- network: NONE by default; rate_limiter.sh get (explicit, 3/10min cap) and
  low_rate_diag.sh (explicit --owned attestation) are the only networked commands
- tests: bash scripts/selftest.sh → ALL PASS (10 stages, sandboxed, loopback-only)
- templates: 55 in templates/ (FA/EN intake, tickets, playbooks, timeline, change review)
- history: references/history.md · quality gate: README.md
