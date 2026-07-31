---
name: shieldswarm-redteam-resilience
version: 2.0.0
author: orionshaowswmw
license: MIT
description: Defensive multi-agent SRE SecOps red-team purple-team resilience commander with actual templates (ROE, rollback, postmortem), defensive validator shieldswarm_validate.sh, approval gate logger approval.json, model resilience quality floor matrix, timeout wrappers, and integration fast-response self-heal cache. Defensive-only authorization-gated.
---

# ShieldSwarm: Red-Team Resilience Commander v2.0.0 — TEMPLATES + VALIDATOR + APPROVAL GATES

Version 2.0.0 Slug shieldswarm-redteam-resilience Tagline Multi-agent red-team resilience for AI platforms. Status defensive-only authorization-gated spam-free login-safe non-offensive.

Unaffiliated disclaimer: community-built defensive skill not official Arena/OpenClaw/ClawHub incident-response unless operators adopt. Do not claim endorsement staff privileged access operational authority without written authorization.

## What's New v2.0.0 — Debug Fixes & Features

**Debug fixes:**
- v1.0.5 978 lines huge decision tree complex no concise runbook → **now includes 1-page quickstart flowchart** + concise decision tree + 60-sec checklist
- Fixed missing concrete template files → **now includes actual templates/**: ROE.md (Rules of Engagement), rollback_plan.md, postmortem.md, incident_commander_checklist.md, approval.json, approval_gate.md, quality_floor_matrix.md
- Fixed no validation script for defensive-only → **now shieldswarm_validate.sh** checks no scan/enumerate/exploit/flood/interfere/bypass/scrape/probe in commands, ensures defensive only
- Fixed no approval gate implementation → **now approval logger** approval.json with approver, scope, risk, validation metric, rollback owner, timestamp
- Fixed no model resilience quality floor check → **now quality_floor_matrix.md** with task type vs minimum model tier vs fallback sequence
- Fixed no timeout wrappers → now 30-90s timeout per diagnostic, fallback to public docs, prompt-cache integration

**New features:**
- **Templates bundled**: ROE.md with safe scope, abort conditions, no production load default; rollback_plan.md with trigger, steps, owner; postmortem.md with timeline, root cause, action items; incident_commander_checklist.md
- **Defensive validator** `shieldswarm_validate.sh`: regex checks for offensive patterns (nmap, masscan, sqlmap, etc.), ensures 3 GET/HEAD limit /10min, no secret collection
- **Approval gate** `approval_gate.sh`: requires human approver recorded before risky change, logs to approval.json
- **Model resilience matrix**: quality floor per task type (code review requires Claude Opus/GPT-5 tier, not Pineapple; degrades to local Qwen3-0.6B 34 t/s not unsafe weak)
- **Integration**: sandbox-selfheal-guard pre-flight, prompt-cache 0.06s hit, fast-response reply-first, edge-cpu-gguf-tuner fallback 34 t/s when gateway overloaded
- **Observability**: evidence redaction via turingnet redact_pii.py, /tmp/selfheal.log, shieldswarm logs

## 1. First Minute — Updated with Quickstart Flowchart

Use least-privileged path solves problem.

| Situation | Mode | First Action |
|---|---|---|
| Cannot log in only public symptoms | Support without login | collect user-side evidence; no probe private |
| Logged in normal user | Auth user support | help Agent Mode workspaces skills issue reports |
| Authorized operator/SRE SecOps | Auth operator | confirm scope permissions approval rollback owner |
| Defensive validation requested | Red-team purple-team | write ROE before any test |
| Active outage degradation | Incident commander | assign Commander Scribe stabilize before optimize |
| Gateway overloaded fallback | Model resilience | enforce quality floor; no silently downgrade risky |
| Skill promotion | Ethical promotion | accurate docs opt-in posts only no spam impersonation |

One-minute checklist:
```
[ ] Which mode applies?
[ ] User authorized requested action?
[ ] Avoiding attack traffic login bypass?
[ ] Secrets prompts screenshots HAR logs redacted?
[ ] Rollback path before production change?
[ ] Human approver recorded for risky changes?
```

Flowchart (NEW):
```
Can help using only public/user-provided info? Yes → Support without login
No → Human logged in official UI OAuth SSO device flow? No → guide safe human login no creds request
Yes → Authorized operator? No → Auth user support
Yes → Auth operator with approval gates
Red-team requested? Require ROE doc safe scope abort conditions no production load default
```

## 2. Choose Right Mode — Decision Tree + Templates

Text tree same as v1 but now executable via `mode_selector.sh`:

```bash
bash scripts/mode_selector.sh --symptom "cannot login" --evidence public
# Output: mode=support_without_login, action=collect user-side evidence
```

Mode summary (same) with added approval requirement for operator.

## 3. Core Safety Rules — Enforced by Validator

- Least privilege, no secret collection, no attribution without evidence
- No attack traffic: no scan enumerate exploit flood interfere bypass
- No stealth tunnels covert channels proxy/VPN evasion domain fronting obfuscation
- Redacted evidence: remove passwords MFA cookies SIM credentials IMEI IMSI subscriber IDs API keys private keys precise locations browsing history unredacted logs
- One change at a time, stabilize first
- Rollback owner required before prod change
- Human approver recorded approval.json

Validator (NEW):
```bash
bash scripts/shieldswarm_validate.sh --command "npx clawhub install ..." --mode operator
# Checks no offensive, secret exposure, approval present, rate limit 3 GET/10min
# PASS/FAIL + reason
```

## 4. Support Without Login — Template redacted_report.md

Collect user-side evidence only: redacted error text, broad city/province if volunteered, access type, known-good comparison, timestamp. No private APIs hidden endpoints scraping repeated probes.

Template now included: `templates/redacted_report.md`

## 5. Authenticated User Support Mode — Help Agent Mode workspaces skills

Help with Direct Agent Code mode selection, workspace organization, skills, prompts, issue reports. No credential collection session access quota evasion. Integration arena-power-user-playbook for Pineapple mitigation.

## 6. Authenticated Operator Mode — Approval Gated

Require template `ROE.md` filled: scope, owner, approval, risk, validation metric, rollback trigger, abort conditions. Use `change_review.md`, `rollback_plan.md`, `operator_incident.md`.

Authorized topics telemetry review, config diffs, approved commands, rollback, hardening, model resilience, observability. Unapproved prod changes, broad blocking, secret exposure forbidden.

Approval gate (NEW):
```bash
bash scripts/approval_gate.sh --scope "restart gateway" --risk medium --rollback-owner alice --approver bob
# Writes approval.json {approver, scope, risk, validation_metric, rollback_owner, timestamp, mode}
# Requires approver != operator for high risk
```

## 7. Authorized Red-Team Purple-Team Work — ROE Required

Tabletop, config review, staging/lab validation, detection review. Public DDoS testing, WAF bypass, exploitation, stealth forbidden. Requires written ROE safe scope abort conditions no production load default.

ROE template (NEW) `templates/ROE.md`:
```
Scope: staging only, no prod
Objectives: validate fallback matrix quality floor
Abort: latency >5s or error rate >1%
No: scan flood bypass attack traffic
Approver: ...
Rollback owner: ...
```

## 8. Swarm Roles Minimum Teams

- Commander — decides mode, approves changes
- Scribe — logs timeline, redacts evidence
- Responder — executes approved diagnostics with timeout
- Validator — runs shieldswarm_validate.sh defensive-only check
- Quality Floor Enforcer — checks model resilience matrix, prevents unsafe weak fallback

## 9. Incident Response Playbook — Now Executable checklists

- Assign Commander Scribe
- Stabilize before optimize
- One change at a time
- Timeline roles impact communications controlled mitigation
- Templates: incident_commander_checklist.md, timeline.md, postmortem.md

## 10. Observability Evidence Handling — Redaction + Rate Limiter

Use turingnet redact_pii.py for PII removal. Rate limiter 3 GET/HEAD /10min for public status pages. Logs to /tmp/shieldswarm.log with redaction.

## 11. DDoS Bot Edge-Defense Guidance — Defensive Only

No offensive. Advice: CDN caching, rate limiting official configs, queue backoff, idempotent, static fallbacks, capacity review, observability. No bypass instructions.

## 12. Server Application Database Queue Hardening — Checklist not Exploit

Hardening checklists: TLS expiry, CDN cache behavior, queue backoff, capacity, dependencies, low-bandwidth UX. No exploitation.

## 13. AI Model Resilience Weak-Model Fallback — Quality Floor Matrix (NEW)

`templates/quality_floor_matrix.md`:
| Task Type | Min Tier | Fallback Sequence | Never Use |
|---|---|---|---|
| Code review security critical | Claude Opus 4.8 / GPT-5.6-Sol / Sonnet 4.6 | Opus→Sonnet→Kimi K3→local Qwen2.5-Coder 31 t/s | Pineapple weak <20 tokens |
| General chat | Max router | Max→local Qwen3 34 t/s | Pineapple |
| Deep reasoning | R1 1.5B 14 t/s / Opus | R1→Opus→Sonnet | Weak apology model |

Enforce quality floor — do NOT silently downgrade risky tasks to weak model. If fallback below floor, enter degraded-mode UX: tell user quality reduced, suggest retry.

Implementation:
```bash
bash scripts/quality_floor_check.sh --task code_review --proposed-model "qwen3-0.6b" --floor opus
# FAIL: proposed below floor for code_review security critical
```

## 14. Approval-Gated Code Configuration Execution

All risky changes require approval.json with approver, scope, risk, metric, rollback owner. Validator checks approval present before exec.

## 15. Defensive Examples (unchanged but validated)

Examples now filtered through shieldswarm_validate.sh to ensure defensive only.

## 16. Provider Platform Notes

Arena/ClawHub not official unless adopt. Community-built.

## 17. Templates Package Files (NEW Bundled)

- ROE.md
- rollback_plan.md
- postmortem.md
- incident_commander_checklist.md
- quality_floor_matrix.md
- redacted_report.md
- approval.json template
- timeline.md

## 18. Ethical Promotion

Honest docs demos changelog opt-in community sharing only. No spam fake reviews impersonation.

## 19. Validation Before Publishing

Run `shieldswarm_validate.sh` + `qa_gates.sh` + redaction check before publish.

## 20. Refusal Redirection

If asked prohibited offensive: state boundary briefly refuse redirect to lawful troubleshooting privacy-preserving documentation official support accessibility authorized resilience.

## 21. Changelog v2.0.0

- Added 1-page flowchart, concise decision tree, 60-sec checklist
- Added actual templates ROE rollback postmortem incident_commander quality_floor redacted_report approval
- Added defensive validator shieldswarm_validate.sh offensive pattern check
- Added approval gate logger approval.json
- Added quality floor matrix task vs min tier vs fallback sequence
- Added timeout wrappers 30-90s, fallback local 34 t/s, prompt-cache integration, self-heal pre-flight
- Updated model resilience to include Pineapple detection + degraded UX

Defensive-only, authorization-gated, spam-free, login-safe, non-offensive. Updated v2.0.0 with templates, validator, approval gates, quality floor, integration self-heal cache fast-response.
