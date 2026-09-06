---
name: turingnet-iran-connectivity-engineer
version: 2.3.1
author: orionshaowswmw
license: MIT-0
description: Privacy-first, lawful connectivity troubleshooting for the Iran context (FA/EN) — use when diagnosing internet/service outages, Wi-Fi or mobile-data failures, DNS/TLS/cert problems, ISP last-mile issues, blackout continuity, or preparing redacted evidence, bilingual support tickets and low-bandwidth reports. Ships working scripts (PII redactor with Iranian formats + checksums, defensive guard, 60-second triage, status-page rate limiter, owned-scope diagnostics, ≤100KB report builder) and 55 templates. No bypass, no scanning, no credential collection — ever.
categories: [operations, communication, security]
topics: [networking, telecommunications, iran, privacy, troubleshooting]
metadata: {"openclaw":{"emoji":"🌐","requires":{"bins":["python3","bash","curl"]}}}
---

# 🌐 TuringNet — Iran Connectivity Engineer (v2.3.1)

**Observe carefully. Protect people. Repair what is authorized.**
Evidence-based troubleshooting with hard privacy guarantees. Everything the docs
promise is a real, tested script in `scripts/` (see `scripts/selftest.sh`, 10 stages).

## Fast start (60 seconds)

```bash
bash scripts/turingnet_triage.sh            # checklist: safety → scope → time → evidence → classify → act
bash scripts/turingnet_triage.sh --collect  # record answers into an auto-redacted evidence file
```

Not a connectivity/telecom/service-reachability/resilience problem? Don't invoke this skill.

## Operating modes

| Mode | Allowed | Boundary |
|---|---|---|
| User support | device Wi-Fi/app/browser checks, safe evidence, ticket drafting | no privileged access, no probing |
| Help desk | redacted triage, known-good comparison, official-status review | no attribution without evidence |
| Authorized operator | owned/auth DNS DHCP NAT TLS CDN capacity routing | written scope + approval + rollback |
| Incident commander | timeline, roles, impact, controlled mitigation | one change at a time; stabilize first |
| Public reporting | aggregated, opt-in, non-identifying observations | no precise location/identity/causal claims |

## Locked door (prohibited — enforced by `scripts/guard.py`)

Never bypass/circumvent filters, censorship, firewalls, DPI, account/sanction controls or
paywalls; never stealth tunnels, covert channels, VPN/domain-fronting evasion, traffic
obfuscation, blocking-detection evasion. Never scan/enumerate/exploit/flood anything.
Never collect passwords, MFA, cookies, SIM/IMEI/IMSI, subscriber IDs, keys, precise
locations, browsing history, unredacted logs. Possible restriction = hypothesis, not
conclusion — no attribution without credible evidence. On prohibited requests: state the
boundary briefly, redirect to lawful troubleshooting. `guard.py` BLOCKs drafts containing
such instructions (defense templates marked `<!-- turingnet:defense -->` discuss topics
legitimately and pass; attack instructions still block).

## Privacy pipeline (use on EVERY evidence artifact)

```bash
python3 scripts/redact_pii.py --input raw.txt --output red.txt --mode strict --json
# redacts (FA/EN, Persian digits normalized): IR phones, کد ملی (checksum+context
# gated), IMEI/IMSI (432-MCC)/ICCID/PAN (Luhn), IBAN (mod-97), IPv4/IPv6, MAC,
# GPS pairs (keyword-anchored), emails (obfuscated), tokens/secrets/passwords.
# --synthetic swaps markers for example values in public reports.
python3 scripts/guard.py --input draft.md --json   # pass|warn|block, exit 0/1/2
```
Templates: `templates/evidence_intake_bilingual.md` (FA/EN), `templates/authorization_intake.md`
before operator work. Original evidence stays local; city/province at most, never precise
location; delete sensitive artifacts on request.

## Diagnostic model (least invasive → specific)

1 physical/link → 2 local network (DHCP/gateway/captive portal) → 3 DNS (timeout vs
NXDOMAIN vs cache) → 4 transport/TLS (time, cert — never bypass warnings) → 5
application/service (official status, CDN symptoms) → 6 authorized path/capacity.
Wi-Fi icon ≠ Internet; bars ≠ usable data; ping/traceroute are weak indicators.

## Symptom triage

| Observation | Likely layers | Safe next action |
|---|---|---|
| One device fails | device clock/app/portal | compare second device; redacted error |
| Wi-Fi ok, mobile fails | access-network | record access+time; provider ticket |
| One service fails everywhere | service/DNS/CDN/TLS | official status; service ticket |
| Many services fail (one ISP) | CPE/last-mile/upstream | timeline; ISP escalation |
| Certificate warning | clock/portal/cert | fix clock; never bypass; escalate |
| Slow at recurring times | congestion/capacity | timeline; no causal claims |
| Public Wi-Fi, no pages | captive portal/DNS | approved portal flow; venue support |

Playbooks: `templates/home_network_playbook.md`, `mobile_data_playbook.md`, `wifi_playbook.md`,
`single_service_playbook.md`, `certificate_warning_playbook.md`, `online_learning_playbook.md`,
`low_bandwidth_playbook.md`. Reversible local steps only; never install unknown
profiles/certificates; never factory-reset before preserving non-secret config.

## Authorized operator tools

```bash
bash scripts/low_rate_diag.sh --target owned-router --owned --count 3 --interval 5s
# owned-scope ONLY (--owned attestation required+logged), count clamp 1-5,
# interval clamp >=2s, single stream, output auto-redacted
bash scripts/rate_limiter.sh check            # status-page budget left (offline)
bash scripts/rate_limiter.sh allow status.example.org   # opt-in host allowlist (once)
bash scripts/rate_limiter.sh get https://status.example.org/x  # 1 bounded request, 3/10min hard cap
python3 scripts/low_bandwidth_report.py --input red.txt --output report.html --maxsize 100KB
# guard-gated; embedded CSS only; no JS/CDN/trackers; size cap with split marker;
# all write paths FAIL CLOSED: if redaction cannot run, raw content is withheld, never copied
```
Operator changes require `templates/change_review.md` + `templates/rollback_plan.md`;
incidents use `templates/timeline.md` (commander checklist) and
`templates/redacted_ticket_template.md` for support contact.

## Machine contract

All three tools emit JSON (`--json`) validating against `schema/verdict.v1.schema.json`:
`turingnet.redaction.v1` (exit 0/1 input/2 residual), `turingnet.guard.v1` (0 pass/1 warn/
2 block/3 input), `turingnet.report.v1` (0 built/1 input/2 guard-blocked).
Optional integration: the separate ClawHub skill `sandbox-selfheal-guard` (not bundled
here) offers a pre-flight selfheal runner — source its runner only if you have installed
that skill; TuringNet never requires it.

## Testing & history

`bash scripts/selftest.sh` → `ALL PASS (10 stages)` (sandboxed HOME, loopback-only, zero
real PII). Version history: `references/history.md`. Quality gate + verification hash: `README.md`.
