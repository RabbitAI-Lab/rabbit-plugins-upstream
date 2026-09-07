---
name: shieldswarm-redteam-resilience
version: 2.1.1
author: orionshaowswmw
license: MIT
categories: [security, operations, agents]
topics: [security, red-team, resilience, secops]
metadata: {"openclaw":{"emoji":"🛡️"}}
description: Defensive multi-agent SRE/SecOps red-team and purple-team resilience commander with working mode selection, command validation, approval gates, and a machine-readable model quality-floor matrix. Use when planning authorized incident response, defensive red-team/purple-team exercises, model-resilience fallbacks, rollback planning, or evidence handling. Defensive-only, authorization-gated, non-offensive; no attack traffic, no login bypass, no credential collection.
---

# ShieldSwarm: Red-Team Resilience Commander v2.1.1

Multi-agent red-team resilience for AI platforms. Status: **defensive-only, authorization-gated, non-offensive.** Community-built — not an official Arena/OpenClaw/ClawHub incident-response system; never claim endorsement, staff access, or operational authority without written authorization.

Every command below is real, shipped in this package, and has a fixed
machine-readable contract. If a file or command is not listed here, it does
not exist — do not invent paths.

## 0. Command contracts (read this first)

| Command | Purpose | Output (stdout) | Exit |
|---|---|---|---|
| `bash scripts/mode_selector.sh --symptom TEXT --evidence {public\|user\|operator}` | pick mode + first action | `mode=`, `action=`, `required=`, `next=` | 0 ok · 2 usage |
| `bash scripts/shieldswarm_validate.sh --command CMD [--mode M] [--roe FILE] [--max-len N]` | fail-closed command validation | `check=<name> status=<value>` lines, then `verdict=PASS\|FAIL` | 0 PASS · 1 FAIL · 2 usage |
| `bash scripts/approval_gate.sh --scope T --risk {low\|medium\|high} --rollback-owner N --approver N [--id ID] [--file P]` | record approval (JSONL, atomic) | `approval_id=`, `approval_file=` | 0 ok · 1 blocked · 2 usage |
| `bash scripts/approval_gate.sh --file P --check [--id ID] [--scope T]` | verify an approval exists | `approval_status=found\|missing` | 0 found · 1 missing · 2 usage |
| `bash scripts/quality_floor_check.sh --task T --proposed-model M [--matrix FILE]` | model quality-floor gate | `task_floor=`, `model_tier=`, `verdict=`, `below_floor=`, `policy=cloud_only` | 0 PASS · 1 FAIL · 2 usage |
| `python3 tools/self_improve.py log --event E [--area A] [--context C]` | append one feedback event | `logged=<event>` | 0 ok · 2 usage |
| `python3 tools/self_improve.py learn [--area A] [--limit N]` | read recent feedback | one `ts= area= event= context=` line per entry | 0 ok · 2 usage |
| `python3 tools/self_improve.py report [--out F]` | render improvement report | `report=<file> events=<n>` | 0 ok · 1 no template |
| `python3 tools/shieldswarm_selftest.py` | full offline package test | `PASS:` lines, ends `ALL CHECKS PASSED` | 0 pass · 1 fail |

All scripts: bash 3.2+ portable, coreutils only, **no network calls**,
deterministic, `--help` supported. Outputs are `key=value` — parse them, do
not re-derive.

## 1. First minute

1. Select the mode (least-privileged path that solves the problem):

```bash
bash scripts/mode_selector.sh --symptom "cannot login" --evidence public
# -> mode=support_without_login action=collect_user_side_evidence required=templates/no_login_diagnostic.md ...
```

2. Read the `required=` file. Do the `action=`. Nothing else until it is done.

3. Checklist (answer yes to all before any risky step): mode chosen? · user
   authorized this action? · no attack traffic / login bypass? · secrets,
   prompts, screenshots, HAR files, logs redacted? · rollback path exists
   before any production change? · human approver recorded in
   `approval.jsonl` for every risky change?

4. Escalation: public info sufficient → support w/o login · else guide the
   human through official UI/OAuth/SSO/device login (never request
   credentials) · authorized operator? no → auth-user support · yes →
   operator mode with approval gates · red-team requested → Rules of
   Engagement required before any test.

## 2. Hard safety rules (validator-enforced, fail-closed)

- Least privilege. No secret collection. No attribution without evidence.
- **No attack traffic:** no scan / enumerate / exploit / flood / interfere /
  bypass / scrape / probe. No stealth tunnels, covert channels,
  proxy/VPN evasion, domain fronting, obfuscation.
- **No login bypass.** Guide official login flows only; never collect
  passwords, sessions, or one-time codes.
- Redact evidence before handling: passwords, MFA, cookies, SIM
  credentials, IMEI/IMSI, subscriber IDs, API keys, private keys, precise
  locations, browsing history, unredacted logs (templates/redaction_checklist.md).
- One change at a time. Stabilize first. Rollback owner required before any
  production change. Human approver recorded in `approval.jsonl` for every
  risky change; for `risk=high` the approver must differ from the rollback
  owner and from the operator.
- Public endpoints: maximum **three single GET or HEAD requests in 10 minutes**.

Validate any proposed command before running it:

```bash
bash scripts/shieldswarm_validate.sh --command "npx clawhub install <slug>" --mode operator
```

## 3. Model resilience — quality floor

Single source of truth: `templates/quality_floor_matrix.yaml` (flat,
machine-readable; cloud-only policy). Gate every model selection:

```bash
bash scripts/quality_floor_check.sh --task "security code review" --proposed-model "claude-opus-5"
bash scripts/quality_floor_check.sh --task "status update" --proposed-model "gemini-3-flash"
```

- Tiers: tier1 frontier · tier2 strong-fast · tier3 everything else
  (unknown model names = tier3).
- Floors: red-team / security / incident / production work = tier1 · code
  review, rollback, postmortems, updates = tier2 · triage = tier3.
- **Never silently downgrade** a task below its floor. Below floor → degraded
  mode: tell the user quality is reduced and suggest a retry.
- **cloud_only:** local/offline models (gguf/ollama/llama.cpp/onnx) are
  rejected by the script. Never route ShieldSwarm tasks to local models.
- Speed: use the fastest model that passes the floor (see
  references/model_resilience.md for sequences and degraded-mode UX).

## 4. Modes (one line each — load the reference when the mode is active)

- **support_without_login** — redacted user-side evidence only; no private
  probing. → `templates/no_login_diagnostic.md`
- **auth_user_support** — workspaces, skills, prompts, issue reports; no
  credential/session/quota access. → `templates/support_ticket.md`
- **auth_operator** — approval-gated; authorization template first, then
  validated, approved, one-at-a-time changes. → `templates/operator_authorization.yaml`
- **incident_commander** — Commander + Scribe; stabilize before optimize.
  → `references/incident.md`
- **model_resilience** — enforce the quality floor; degraded-mode UX.
  → `references/model_resilience.md`
- **red_team** — Rules of Engagement **before any test**; tabletop, config
  review, staging/lab validation, detection review only. The validator
  rejects an empty or unfilled ROE (requires the keys `scope:`,
  `abort_conditions:`, `rollback_owner:`, `authorized_by:`, and non-empty
  `exercise_name` / `authorized_by` / `rollback_owner`). Emergency
  abort: say **STOP SHIELDSWARM EXERCISE NOW**. → `templates/red_team_roe.yaml`
- **ethical_promotion** — honest docs, opt-in sharing only. → `references/promotion.md`

Full playbooks: `references/modes.md`.

## 5. Swarm roles (minimum team)

Commander (mode + change approval) · Scribe (timeline, redaction, feedback
log) · Responder (approved diagnostics, 30–90 s timeouts) · Validator
(`shieldswarm_validate.sh`) · Quality-Floor Enforcer (`quality_floor_check.sh`).

## 6. Self-improvement loop (durable skill memory)

After every failed gate, blocked approval, below-floor event, or aborted
exercise, the Scribe logs one redacted line:

```bash
python3 tools/self_improve.py log --event below_floor --area floor --context "task=code_review model=qwen3-0.6b floor=tier1"
python3 tools/self_improve.py learn --area floor        # before retrying
python3 tools/self_improve.py report                    # at exercise end
```

Feedback lives in local `feedback.jsonl` (never uploaded). At the next
version bump, apply the top actionable report items and record them in
`CHANGELOG.md` — the changelog is the long-term memory. Protocol:
`references/self_improvement.md`.

## 7. Publishing, promotion, refusal

Pre-publish gate: selftest `ALL CHECKS PASSED` + validator over every command
example + redaction pass. This skill is defensive-only and authorization-gated
by design; promotion is opt-in, honest, and spam-free. If asked for
prohibited offensive work: refuse in one short sentence and redirect to
lawful troubleshooting, privacy-preserving documentation, official support,
or authorized resilience work under a written ROE. Details:
`references/promotion.md`.

## 8. Load map (progressive disclosure — read only what the mode needs)

| Load when | File |
|---|---|
| always (this file) | `SKILL.md` |
| mode selected | the `required=` file from mode_selector |
| any mode details | `references/modes.md` |
| incident_commander active | `references/incident.md` |
| model_resilience active | `references/model_resilience.md` |
| ethical_promotion active | `references/promotion.md` |
| feedback/retry after failure | `references/self_improvement.md` |
| templates | `templates/` (25 files; `ls templates/` for the list) |
| verification | `python3 tools/shieldswarm_selftest.py` |

## 9. Verification

```bash
python3 tools/shieldswarm_selftest.py   # full offline package test
```

Covers: package hygiene, frontmatter, reference integrity, YAML parsing,
script syntax, functional PASS/FAIL paths for all four scripts, matrix
semantics, safety phrases, secret/dangerous-pattern scans, changelog/version
consistency.

## 10. Versioning

`CHANGELOG.md` is authoritative. Registry note: earlier registry versions
served newer content under old tags — always publish with an explicit
`--version` and read `CHANGELOG.md` before trusting a cached copy.
