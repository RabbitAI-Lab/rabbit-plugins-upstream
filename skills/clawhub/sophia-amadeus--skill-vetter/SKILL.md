---
name: skill-vetter
description: Security-first skill vetting for AI agents. Use before installing any skill from ClawHub, GitHub, or other sources. Triggers on: 'install skill', 'check skill', 'review skill', 'vet skill', 'skill security', 'skill audit', 'is this skill safe', 'clawhub inspect', 'check this skill', 'security check'. Checks for red flags, permission scope, suspicious patterns, credential storage, and network access before installation.
---

# Skill Vetter

Security-first vetting before skill installation. Every skill gets audited — no exceptions.

## Quick Start

```bash
# Inspect and vet a ClawHub skill
clawhub inspect <slug> --files
clawhub inspect <slug> --file SKILL.md
clawhub inspect <slug> --file scripts/*.sh
clawhub inspect <slug> --file hooks/**/*.js
```

## Output Format

```
=== Security Vet: <slug> ===
Version: x.x.x | Updated: YYYY-MM-DD
Version count: N (community traction)
Security: CLEAN / CAUTION / FLAG

Credential storage: CLEAN / FLAG
Network access: CLEAN / FLAG
File system: CLEAN / FLAG
Permissions: CLEAR / VAGUE
Patterns: CLEAN / SUSPICIOUS

SCORE: N/5
VERDICT: Install / Caution / Reject / Dangerous
REASON: <one-line explanation>
```

## Security Checks (in order)

### 1. ClawHub Official Scan
Always check ClawHub's own security status first:
```bash
clawhub inspect <slug>
```
Look for: `Security: CLEAN` or `Security: FLAG`. ClawHub runs automated scans — trust them.

### 2. Credential Storage
Check for plaintext credential patterns:
```bash
clawhub inspect <slug> --file <script.sh> | grep -i "API_KEY\|PASSWORD\|SECRET\|TOKEN"
```
**Red flags:** Hardcoded keys, plaintext passwords, placeholder keys that look real.

### 3. Network Access
Inspect all scripts for outbound calls:
```bash
clawhub inspect <slug> --files | grep scripts
# Then inspect each script:
clawhub inspect <slug> --file scripts/<name.sh>
```
**Red flags:** Phone-home patterns, data exfil, calls to unknown servers without documentation.

### 4. File System Operations
Check scripts for destructive operations:
```bash
clawhub inspect <slug> --file scripts/<name.sh> | grep -E "rm -rf|sudo |eval |exec "
```
**Red flags:** Recursive delete, shell evaluation, world-writable permissions.

### 5. Permission Documentation
Review SKILL.md metadata:
```bash
clawhub inspect <slug> --file SKILL.md
```
**Red flags:** Missing `requires` field, vague tool descriptions, no documentation.

## Scoring

| Signal | Score |
|--------|-------|
| ClawHub Security: CLEAN | +2 |
| No credential storage | +1 |
| No outbound exfil | +1 |
| No destructive operations | +1 |
| Clear permission documentation | +1 |
| Credential in plaintext | -2 |
| Exfil to unknown server | -2 |
| Destructive operations | -2 |
| ClawHub Security: FLAG | -3 |

**Verdict thresholds:**
- **Install** (6-5): Clear, safe to install
- **Caution** (4-3): Review scripts before install
- **Reject** (2-1): Do not install — review source
- **Dangerous** (0 or below): Security risk — do not install

## Real Example: self-improving-agent

```bash
clawhub inspect self-improving-agent
# Output:
# Security: CLEAN
# Updated: 2026-05-01
# License: MIT-0
# Version count: 31

clawhub inspect self-improving-agent --file SKILL.md
# Clean: no credentials, no destructive ops, well-documented

clawhub inspect self-improving-agent --file scripts/activator.sh
# Clean: text output only, no network, no credentials

clawhub inspect self-improving-agent --file hooks/openclaw/handler.js
# Clean: simple reminder injection, no exfil

# VERDICT: Install (6/6 — ClawHub clean, MIT-0, no red flags)
```

## When to Use

Always vet before:
- `clawhub install <slug>`
- Downloading skills from GitHub
- Accepting skill files from third parties
- Running any skill for the first time

## References

- Credential patterns: `references/credential-patterns.md`
- Safe coding patterns: `references/safe-patterns.md`
- Flagged skills: `references/flagged-skills.md`