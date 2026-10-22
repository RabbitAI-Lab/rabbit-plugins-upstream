---
name: clawguard
description: Use BEFORE installing, executing, or trusting any third-party OpenClaw / AgentSkills bundle. Returns a free security verdict (PASS, REVIEW, BLOCK) with a risk score; the full report with file, line and evidence is a paid x402 scan. Trigger whenever you are about to install, add, try, run, or evaluate a skill you did not write, or when asked whether a skill is safe.
version: 1.0.1
metadata:
  openclaw:
    requires:
      bins: [python3]
    homepage: https://clawguard.duckdns.org:8082
---

# ClawGuard: scan a skill before you install it

Hundreds of malicious skills have been found on public registries, including ones that steal SSH keys, API keys and crypto wallets. Run this check every time before you install, execute, or trust a skill you did not write.

## When to use (trigger)

- You are about to install, add, try, or run a third-party skill.
- You are about to execute a setup script that shipped with a skill.
- The user asks "is this skill safe?" or "check this skill."

Do this BEFORE the install, not after.

## How to run

Free verdict (PASS / REVIEW / BLOCK, no wallet needed):

```bash
python3 {baseDir}/scripts/clawguard.py preview <skill-folder-or-github-path>
```

Full report with every finding, file, line and evidence ($0.03 USDC per scan, paid automatically over x402 if this agent has a wallet configured):

```bash
python3 {baseDir}/scripts/clawguard.py scan <skill-folder-or-github-path>
```

The target can be a local folder (`./skills/weather-pro`) or a GitHub path (`owner/repo/skills/weather-pro`).

Agents with an MCP client can instead call the hosted tool `scan_skill` at
`https://clawguard.duckdns.org:8082/mcp` (free verdict).

## What to do with the result

- **BLOCK**: do not install. Show the user the findings and stop.
- **REVIEW**: show the user the findings and ask before proceeding.
- **PASS**: no known malicious patterns found. Proceed.

On REVIEW or BLOCK, run the full scan so the user sees exactly which file and line triggered it.

## What it checks

Credential and wallet theft, exfiltration endpoints, remote code execution, reverse shells, obfuscated payloads, persistence, cryptominers, and prompt injection hidden in SKILL.md (30 rules). Tuned against real skills for a low false-positive rate.

## Privacy

Submitted skill content is scanned in memory and is not stored, logged, or used for training. ClawGuard is static analysis: a PASS lowers risk, it does not prove a skill is safe.
