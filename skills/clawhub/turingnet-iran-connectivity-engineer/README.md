# 🌐 turingnet-iran-connectivity-engineer

**Categories:** operations, communication, security  
**Public tags:** #operations, #networking, #telecommunications, #iran, #resilience

## ✨ Functionalities

Turing-inspired, privacy-first connectivity troubleshooting: intake templates, an evidence redactor (redact_pii.py), low-bandwidth offline mode, a 60-second triage script, and a timeline template. Lawful, evidence-based, with no bypass guidance.

The complete functionality, workflows, limits, examples, and operational rules
from the unchanged skill are reproduced verbatim in **Complete Skill Reference**
below. That reference is authoritative; this README does not add or alter any
capability.

## 🚀 Usage

Install the skill from ClawHub:

```bash
npx --yes clawhub@latest install @orionshaowswmw/turingnet-iran-connectivity-engineer
```

Collect consented troubleshooting evidence, redact PII, run the offline/60-second triage, and follow lawful network diagnostics without bypassing controls.

A representative command from the unchanged skill documentation is:

```bash
bash scripts/turingnet_triage.sh
# Checklist:
# [ ] Safety: own device/network/service or written authorization? If not stay user-support mode
# [ ] Scope: one device/network/service/many?
# [ ] Time: last known working, observed, timezone, intermittent?
# [ ] Evidence: redacted error text, broad city/province if volunteered, access type, known-good comparison
# [ ] Classify: device/LAN, Wi-Fi, mobile data, ISP/last mile, DNS, TLS, service/CDN, routing/upstream, unknown
# [ ] Act safely: least disruptive fix, provider escalation, authorized change plan
```

Read the complete reference below before execution, use least privilege, and
inspect all outputs and exit codes.

## 🔐 Permissions & Requirements

• Runs local troubleshooting scripts
• redact_pii.py processes evidence text (redacts PII before output)
• No bypass/unauthorized-access functionality

All permissions above are capability requirements, not blanket authorization.
Grant only what the selected workflow needs, scope filesystem access to the
working directory, and do not elevate privileges unless SKILL.md explicitly
requires and explains it.

## 🔒 Security & Privacy

- Privacy-first: redacts PII from evidence before output.
- Lawful, evidence-based; no bypass or unauthorized access.
- No secrets are handled beyond what you provide.
- **Data handling:** the skill reads only user-selected inputs and files described above; it must not collect unrelated data.
- **Storage/logging:** inspect output and log locations before use. Logs can contain supplied inputs or derived results and should be protected accordingly.
- **Network boundary:** data leaves the machine only for endpoints and optional integrations explicitly documented above or in the unchanged SKILL.md; otherwise processing remains local.
- **Secrets:** API keys, tokens, passwords, and credentials must never be embedded in the skill or logged. Store required secrets in chmod-600 credential files or a dedicated secret manager.
- **Risks and mitigation:** review SKILL.md and every executable file before installation, use least privilege and dry-run modes where available, keep backups, and verify all generated output before relying on it.

## ✅ Verification Hash

This digest verifies every stable artifact file except `README.md`
(self-reference), generated `skill-card.md`, registry-generated `_meta.json`,
and `.clawhub/` bookkeeping.

**Artifact SHA-256 (TREE-SHA256-v1):** `98a35e738af245aab6c6e68c3db29dea4803ed96f0c6f0fad751736216f52f5b`

Run from the installed skill directory:

```bash
python3 - <<'PY'
from pathlib import Path
import hashlib
root = Path('.')
excluded_parts = {'.git', '.clawhub', '__pycache__', '.pytest_cache'}
excluded_names = {'readme.md', 'skill-card.md', '_meta.json', '.published', '.ds_store'}
files = sorted(
    (p for p in root.rglob('*') if p.is_file()
     and not any(part in excluded_parts for part in p.relative_to(root).parts)
     and p.name.lower() not in excluded_names),
    key=lambda p: p.relative_to(root).as_posix(),
)
h = hashlib.sha256()
h.update(b'TREE-SHA256-v1\0')
for p in files:
    rel = p.relative_to(root).as_posix().encode('utf-8')
    data = p.read_bytes()
    h.update(rel); h.update(b'\0')
    h.update(str(len(data)).encode('ascii')); h.update(b'\0')
    h.update(data); h.update(b'\0')
print(h.hexdigest())
PY
```

The printed digest must exactly match the value above. A mismatch means a
functional file, script, configuration, or metadata file differs from the
published artifact; review before use.


## 📚 Complete Skill Reference (Unchanged)

The text below is copied from the installed `SKILL.md` body so every
functionality and usage instruction remains available without rewriting or
changing the skill itself.

---

# TuringNet: Iran Connectivity Engineer v2.2.0 — TEMPLATES + REDACTOR + TRIAGE

Tagline: Observe carefully. Protect people. Repair what is authorized.

## What's New v2.2.0 — Debug Fixes & Features

**Debug fixes:**
- v2.1.1 long 500 lines but templates referenced not bundled — **now includes actual templates/**: authorization_intake.md, evidence_intake_bilingual FA/EN, change_review.md, rollback_plan.md, timeline.md, home_network_playbook.md, mobile_data_playbook.md, wifi_playbook.md, single_service_playbook.md, certificate_warning_playbook.md, low_bandwidth_playbook.md
- Fixed no redaction script → **now redact_pii.py** removes phone, IP, IMEI, IMSI, subscriber IDs, API keys, passwords, MFA, cookies, precise location, browsing history per privacy rule, keeps only city/province max
- Fixed no incident timeline template → **now timeline.md + incident_commander checklist** with time, scope, impact, roles, communications, controlled mitigation
- Fixed no offline-first report builder → **now low-bandwidth mode ≤100KB HTML text-only, resumable transfers, queue backoff idempotent**
- Fixed no 60-second fast triage executable → **now turingnet_triage.sh** 60-sec checklist

**New features:**
- **Evidence redactor** `redact_pii.py`: regex for phone, email obfuscation, IP [REDACTED], subscriber ID, location precise removal, auth token removal; synthetic example mode for public reports
- **Low-bandwidth mode**: text-only report, embedded CSS no CDN, ≤100KB, static fallbacks, resumable, low-rate diagnostics only owned/auth scope
- **60-second triage** `turingnet_triage.sh`: safety? scope? time? evidence? classify? act safely? — least disruptive fix
- **Status page monitor** with 3 GET limit /10min enforcement via rate_limiter.sh
- **Integration self-heal**: pre-flight check via sandbox-selfheal-guard, timeout per diagnostic 30s, no scan/flood/bypass ever
- **Bilingual intake** FA/EN with city/province at most, no precise location required

## 1. Fast Start: First 60 Seconds (now executable turingnet_triage.sh)

```bash
bash scripts/turingnet_triage.sh
# Checklist:
# [ ] Safety: own device/network/service or written authorization? If not stay user-support mode
# [ ] Scope: one device/network/service/many?
# [ ] Time: last known working, observed, timezone, intermittent?
# [ ] Evidence: redacted error text, broad city/province if volunteered, access type, known-good comparison
# [ ] Classify: device/LAN, Wi-Fi, mobile data, ISP/last mile, DNS, TLS, service/CDN, routing/upstream, unknown
# [ ] Act safely: least disruptive fix, provider escalation, authorized change plan
```

Do not invoke for generic IT with no connectivity/telecom/service-reachability/resilience component.

## 2. Operating Modes (unchanged)

| Mode | Allowed | Boundary |
|---|---|---|
| User support | Device Wi-Fi mobile app/browser safe evidence collection support-ticket drafting | No privileged access no secret collection no probing |
| Help desk | Redacted ticket triage known-good comparisons official-status review | No attribution without evidence |
| Authorized operator | Owned/auth DNS DHCP NAT TLS CDN capacity routing evidence resilience review | Written scope approval rollback owner |
| Incident commander | Timeline roles impact communications controlled mitigation | One change at a time stabilize first |
| Public reporting | Aggregated opt-in non-identifying observations | No precise locations identities causal claims beyond evidence |

## 3. Locked Door: Prohibited Work (enforced by defensive validator)

Never provide/execute instructions bypassing filtering censorship firewalls DPI account controls sanctions controls paywalls platform safeguards. Never create stealth tunnels covert channels proxy/VPN evasion domain fronting traffic obfuscation blocking-detection evasion.

Never scan enumerate exploit flood interfere third-party infrastructure/telecom. Never collect passwords MFA cookies SIM IMEI/IMSI subscriber IDs API keys private keys precise locations browsing history unredacted logs.

Possible restriction = hypothesis not conclusion. Do not attribute outage to gov ISP platform individual org unless credible evidence supports.

If asked prohibited evasion: state boundary briefly refuse redirect to lawful troubleshooting privacy-preserving documentation official support accessibility authorized resilience.

## 4. Privacy Consent Evidence (now redactor)

Use `templates/authorization_intake.md` before operator work and `templates/evidence_intake_bilingual.md` every incident. Collect minimum. Use city/province at most; never require location. Remove account names phone numbers subscriber IDs IP addresses unless essential authorized, device identifiers session material auth headers precise addresses.

Keep original evidence local. Use synthetic examples in reports. Retain data only as long necessary securely delete sensitive artifacts if requested. Public reports aggregate opt-in observations state limitations.

**Redactor (NEW):**
```bash
python3 scripts/redact_pii.py --input evidence_raw.txt --output evidence_redacted.txt --mode strict
# Removes: phone, email (obfuscates), IP, IMEI, IMSI, subscriber ID, API key, password, MFA, cookie, precise location
# Keeps: city/province broad, access type, redacted error text, timestamp
# Synthetic mode for public: --synthetic replaces real values with example.com etc
```

## 5. Diagnostic Model (least invasive to specific)

1. Physical/link: power cabling modem/ONT indicators Wi-Fi association radio signal
2. Local network: DHCP lease gateway reachability captive portal Ethernet vs Wi-Fi
3. Name resolution: resolver used timeout vs NXDOMAIN cache behavior
4. Transport/security: time settings TLS warnings cert validity service port only when authorized
5. Application/service: browser vs app account-independent public page official status CDN/service symptoms
6. Path/capacity: authorized low-rate path evidence latency packet loss jitter congestion pattern provider escalation

Wi-Fi icon ≠ Internet. Mobile bars ≠ usable data. Ping/traceroute limited indicators not proof fault ownership. Successful DNS ≠ app reachable. Cert warnings never ignore.

## 6. Symptom Triage

| Observation | Plausible layers | Safe next action |
|---|---|---|
| One device fails | device clock app Wi-Fi captive portal | compare another auth device; capture redacted error |
| Wi-Fi works but mobile fails | access-network-specific | record access type time; contact relevant provider |
| One service fails several auth networks | service DNS CDN TLS account | check official status; draft service ticket |
| Many services fail one ISP | local equip ISP/last mile upstream | record broad scope timestamps; escalate ISP |
| Certificate warning | device time captive portal service cert | correct clock; do not bypass; escalate |
| Slow only recurring times | congestion radio conditions capacity service load | create timeline avoid causal claim without operator evidence |
| Public Wi-Fi connects but no pages | captive portal DNS access policy | open approved portal flow; ask venue/provider support |

## 7. Safe User Playbooks (now included)

Matching template: `home_network_playbook.md`, `mobile_data_playbook.md`, `wifi_playbook.md`, `single_service_playbook.md`, `certificate_warning_playbook.md`, `online_learning_playbook.md`, `low_bandwidth_playbook.md`

Permitted steps reversible local: verify time, reconnect owned network, check official service notices, compare one known-good public service, safely restart owned equipment after recording light/status indicators, prepare redacted ticket. Do not factory-reset before preserving non-secret config and checking provider requirements. Do not install unknown apps profiles certificates config files.

## 8. Authorized Operator Engineering

Require scope owner change approval risk validation metric rollback trigger. Use `change_review.md`, `rollback_plan.md`, `operator_incident.md`

Authorized topics DNS/DHCP/NAT TLS expiry CDN/cache observability capacity service dependencies low-bandwidth UX static fallbacks resumable transfers queues backoff idempotent.

**Minimal checks only owned/auth:**
```bash
# Example low-rate diagnostic owned scope only
bash scripts/low_rate_diag.sh --target owned-router --count 3 --interval 5s
# 3 pings low-rate, no flood, logs to evidence_redacted.txt
```

## 9. Templates Bundled v2.2.0 (were missing)

- authorization_intake.md
- evidence_intake_bilingual.md FA/EN
- change_review.md with risk validation metric rollback trigger
- rollback_plan.md
- timeline.md with time scope impact roles communications
- home/mobile/wifi/single_service/certificate/online_learning/low_bandwidth playbooks
- operator_incident.md
- redacted_ticket_template.md

## 10. Rate Limiter (NEW)

`rate_limiter.sh` enforces official public status pages only when explicitly requested, limited to 3 single GET or HEAD in 10 minutes.

```bash
bash scripts/rate_limiter.sh check  # returns remaining calls
bash scripts/rate_limiter.sh get https://official.status.page
```

## 11. Low-Bandwidth Mode (NEW)

≤100KB HTML text-only report:
- Embedded CSS no CDN
- No trackers
- Static fallbacks for JS
- Resumable transfers queue
- Backoff exponential
- Idempotent operations
- Printed via `low_bandwidth_report.py --input evidence_redacted.txt --output report.html --maxsize 100KB`

## 12. Integration Self-Heal

```bash
source ~/skills/@orionshaowswmw/sandbox-selfheal-guard/scripts/selfheal_runner.sh
# verifies apt, shim, binaries before diagnostics
timeout 30 bash scripts/turingnet_triage.sh || echo "triage timeout fallback"
```

Authored privacy-first lawful troubleshooting, evidence-based, no bypass. Updated v2.2.0 with templates, redactor, triage script, timeline, low-bandwidth ≤100KB, rate limiter.

---

*README-only documentation remediation. No functional artifact file was changed.*
