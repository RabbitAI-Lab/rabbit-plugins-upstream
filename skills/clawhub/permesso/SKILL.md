---
name: permesso
description: Permission-gated security scans with fix-ready reports.
version: 1.0.0
author: funkysys-org
license: MIT
metadata:
  categories: [security, operations]
  topics: [vulnerability-scanning, hardening, reports, websites, servers]
---

# permesso — authorized scan + hardening reports

Authorized security scans of websites and servers that produce clear,
fix-oriented HTML reports. permesso is an installed CLI (PyPI package,
stdlib-only core, zero required API keys); this skill teaches the agent to
drive it safely and translate its findings for non-experts.

## Hard rules (non-negotiable)

1. **Never scan a target the user has not confirmed they own or are
   authorized to test.** Ask explicitly — "do you own or are you authorized
   to test `<target>`?" — and record the answer before any command.
2. Never suggest bypassing, editing, or weakening the authorization gate.
   An `UNAUTHORIZED` exit means re-run `permesso authorize`, nothing else.
3. Passive checks are still network activity: the gate applies to every
   command that touches the target, including `monitor`.

## Requirements

- Python ≥ 3.10. Install once (no root, no API keys, no env vars):
  ```bash
  pipx install permesso        # or: pip install permesso
  permesso doctor              # environment check + missing-tool recipes
  ```
- Optional deeper tools (permesso picks them up automatically, reports them
  as skipped when absent): `pipx install ssh-audit`; nuclei (release binary),
  testssl.sh, Lynis — exact commands in `permesso doctor`.
- Permissions: outbound HTTP/HTTPS to the authorized target only; optionally
  port 22 for ssh-audit. Nothing else.

## Workflow

1. **Confirm the target and authorization** (Hard rule 1). Completion
   criterion: explicit user confirmation recorded for that exact host.
2. **Gate setup** (once per machine, then per target):
   `permesso keygen` → `permesso authorize --target <host> --owner <email>`.
   Completion criterion: authorization file saved under `~/.permesso/`.
3. **Scan**:
   `permesso scan --target <host> --plain-language --lang en --out report.html --json scan.json`
   Completion criterion: `report.html` + `scan.json` written; read the JSON.
4. **Interpret for the customer**: every finding gets business impact + the
   concrete fix for their actual stack (nginx? WordPress? managed host?).
   The report's "what this means" text is the floor, not the ceiling.
5. **Deliver** `report.html` (self-contained, printable, brandable via
   `branding.json`). For recurring checks:
   `permesso monitor --target <host>` from cron/CI — history, drift, exit 10
   on new CRITICAL/HIGH findings.

## Pitfalls

- Missing optional tools are listed as **skipped** in the report. Tell the
  user what was *not* checked — never imply a clean bill of health.
- First nuclei run downloads its template database (a few minutes, once).
- The authorization file is HMAC-signed with scope and expiry: tampering,
  expiry or a different host aborts the scan with exit 2 before any packet.

## Verification

- `permesso doctor` lists every adapter's status on this machine.
- `scan.json` holds counts and the full findings; the HTML report is the
  customer-facing artifact and shows scope, owner and expiry of the
  authorization backing it.
