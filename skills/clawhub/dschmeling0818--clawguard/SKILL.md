---
name: clawguard
description: Use BEFORE installing, executing, or trusting any third-party OpenClaw / AgentSkills bundle. Returns a free security verdict (PASS, REVIEW, BLOCK) with a risk score; the full report with file, line and evidence is a paid x402 scan. Trigger whenever you are about to install, add, try, run, or evaluate a skill you did not write, or when asked whether a skill is safe.
version: 1.0.5
metadata:
  openclaw:
    requires:
      bins: [python3]
    homepage: https://clawguard.duckdns.org:8082
    permissions:
      network: [clawguard.duckdns.org]  # sends only a public source path to the fixed scan endpoint
      file_read: false              # reads no local files
      shell: false                  # runs no shell or subprocess commands
      env: false                    # reads no environment variables
allowed-tools: [python3]
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
python3 {baseDir}/scripts/clawguard.py preview <owner/repo/path>
```

Full report with every finding, file, line and evidence ($0.03 USDC per scan, paid automatically over x402 if this agent has a wallet configured):

```bash
python3 {baseDir}/scripts/clawguard.py scan <owner/repo/path>
```

The target is a public source path, for example `owner/repo` or `owner/repo/skills/weather-pro`. The client sends only that path. The ClawGuard service fetches the skill from its public source and scans it, so no local file is ever read or uploaded.

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

The client reads no local files. It sends only the public source path you give it, so it cannot disclose anything from your machine, and it runs no shell or subprocess commands.
