---
name: shieldswarm-redteam-resilience
version: 2.0.1
author: orionshaowswmw
license: MIT
categories: [security, operations, agents]
topics: [security, red-team, resilience, secops]
metadata: {"openclaw":{"emoji":"🛡️"}}
description: Defensive multi-agent SRE/SecOps red-team purple-team resilience commander — mode selector, defensive-only validator (shieldswarm_validate.sh), approval gates (approval.json), ROE/rollback/postmortem templates, model quality-floor matrix, evidence redaction, timeout wrappers. Defensive-only, authorization-gated, non-offensive.
---

# ShieldSwarm: Red-Team Resilience Commander v2.0.1

Tagline: multi-agent red-team resilience for AI platforms. Status: **defensive-only, authorization-gated, spam-free, login-safe, non-offensive.** Community-built — NOT official Arena/OpenClaw/ClawHub incident-response unless operators adopt; never claim endorsement, staff access, privileged access, or operational authority without written authorization.

## First minute

1. Pick the mode (least-privileged path that solves the problem):

| Situation | Mode | First action |
|---|---|---|
| Cannot log in, public symptoms only | Support w/o login | collect user-side evidence; never probe private |
| Logged-in normal user | Auth user support | help with Agent Mode workspaces/skills/issue reports |
| Authorized operator / SRE / SecOps | Auth operator | confirm scope, permissions, approval, rollback owner |
| Defensive validation requested | Red/purple team | write ROE **before** any test |
| Active outage / degradation | Incident commander | assign Commander+Scribe; stabilize before optimize |
| Gateway overloaded / fallback | Model resilience | enforce quality floor; never silently downgrade risky tasks |
| Skill promotion | Ethical promotion | accurate docs, opt-in posts only, no spam/impersonation |

```bash
bash scripts/mode_selector.sh --symptom "cannot login" --evidence public   # -> mode=…, action=…
```

2. Checklist: mode chosen? · user authorized this action? · no attack traffic / login bypass? · secrets, prompts, screenshots, HAR files, logs redacted? · rollback path before any production change? · human approver recorded for risky changes?
3. Flow: public/user-provided info enough → support w/o login · else human login via official UI/OAuth/SSO/device flow (guide them; never request credentials) → authorized operator? no → auth-user support · yes → operator mode with approval gates · red-team requested → ROE required (safe scope, abort conditions, no production load by default).

## Hard safety rules (validator-enforced)

- Least privilege; no secret collection; no attribution without evidence.
- No attack traffic: no scan / enumerate / exploit / flood / interfere / bypass / scrape / probe. No stealth tunnels, covert channels, proxy/VPN evasion, domain fronting, obfuscation.
- Redact evidence before handling: passwords, MFA, cookies, SIM credentials, IMEI/IMSI, subscriber IDs, API keys, private keys, precise locations, browsing history, unredacted logs.
- One change at a time; stabilize first; rollback owner required before prod change; human approver recorded in `approval.json` for every risky change.

```bash
bash scripts/shieldswarm_validate.sh --command "npx clawhub install ..." --mode operator   # PASS/FAIL: offensive patterns (nmap/masscan/sqlmap/...), secret exposure, approval present, rate limit
bash scripts/approval_gate.sh --scope "restart gateway" --risk medium --rollback-owner alice --approver bob   # writes approval.json; approver != operator for high risk
bash scripts/quality_floor_check.sh --task code_review --proposed-model "qwen3-0.6b" --floor opus   # FAIL: below floor
bash tools/shieldswarm_selftest.py
```

## Modes

- **Support w/o login** — user-side evidence only (redacted error text, broad location if volunteered, access type, known-good comparison, timestamp); no private APIs/hidden endpoints/scraping/repeated probes. Template `redacted_report.md`.
- **Auth user support** — Agent Mode / direct-agent-code mode selection, workspaces, skills, prompts, issue reports; no credential collection, session access, quota evasion. Integrates arena-power-user-playbook (Pineapple mitigation).
- **Auth operator (approval-gated)** — fill `templates/ROE.md` first (scope, owner, approval, risk, validation metric, rollback trigger, abort conditions); use `change_review.md` / `rollback_plan.md` / `operator_incident.md`. Authorized: telemetry, config diffs, approved commands, rollback, hardening, model resilience, observability. Forbidden: unapproved prod changes, broad blocking, secret exposure.
- **Red/purple team (ROE REQUIRED)** — tabletop, config review, staging/lab validation, detection review ONLY; public DDoS testing, WAF bypass, exploitation, stealth forbidden. ROE sketch: Scope "staging only" · Abort "latency >5 s or err >1 %" · No "scan/flood/bypass" · Approver · Rollback owner.
- **Incident response** — Commander+Scribe; stabilize before optimize; one change at a time; timeline/roles/impact/communications; templates `incident_commander_checklist.md` / `timeline.md` / `postmortem.md`.

## Swarm roles (minimum team)

Commander (mode + change approval) · Scribe (timeline, redaction) · Responder (approved diagnostics with 30–90 s timeouts) · Validator (`shieldswarm_validate.sh` defensive-only check) · Quality-Floor Enforcer (matrix; blocks unsafe weak fallback).

## Model resilience — quality floor (`templates/quality_floor_matrix.md`)

| Task type | Min tier | Fallback sequence | Never use |
|---|---|---|---|
| Code review (security-critical) | Claude Opus 4.8 / GPT-5.6-Sol / Sonnet 4.6 | Opus→Sonnet→Kimi K3→local Qwen2.5-Coder 31 t/s | Pineapple (weak, <20 tok) |
| General chat | Max router | Max→local Qwen3 34 t/s | Pineapple |
| Deep reasoning | R1 1.5B 14 t/s / Opus | R1→Opus→Sonnet | Weak apology model |

Never silently downgrade a risky task below its floor; if fallback lands below floor → degraded-mode UX: tell the user quality is reduced and suggest retry. Integration: sandbox-selfheal-guard pre-flight · prompt-cache (0.06 s hits) · fast-response reply-first · edge-cpu-gguf-tuner local fallback (34 t/s) when the gateway is overloaded.

## Ops hardening & observability (defensive only)

- **DDoS edge defense (no bypass instructions):** CDN caching, official-config rate limiting, queue backoff, idempotency, static fallbacks, capacity review, observability. **Hardening checklists (no exploitation):** TLS expiry, CDN behavior, queue backoff, capacity, dependencies, low-bandwidth UX.
- **Evidence:** `turingnet redact_pii.py` for PII; rate limiter 3 GET/HEAD per 10 min on public status pages; logs to `/tmp/shieldswarm.log` (redacted) + `/tmp/selfheal.log`.
- **Templates:** `ls templates/` (30+: ROE, rollback_plan, postmortem, incident_commander_checklist, quality_floor_matrix, redacted_report, approval.json, timeline, …).

## Publishing, promotion, refusal

Pre-publish gate: `shieldswarm_validate.sh` + `qa_gates.sh` + redaction check. Ethical promotion: honest docs/demos/changelog, opt-in community sharing only — no spam, fake reviews, impersonation. If asked for prohibited offensive work: state the boundary briefly, refuse, redirect to lawful troubleshooting, privacy-preserving documentation, official support, accessibility, or authorized resilience work.

Version history: registry version list (registry currently serves the v2.x content as v1.0.12 — publish with an explicit `--version`).
