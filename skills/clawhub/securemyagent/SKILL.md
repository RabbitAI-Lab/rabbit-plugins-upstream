---
name: securemyagent
description: "Security checkup for this agent. Scores the machine 0-100 (exposed gateway, plaintext secrets, risky skills and MCP servers, broad tool scopes) and gives exact fixes. Use when asked to check, harden or score the agent's security, before installing a skill or MCP server, or on a weekly heartbeat."
homepage: https://securemyagent.ai
metadata: {"openclaw":{"emoji":"🛡️","homepage":"https://securemyagent.ai","requires":{"bins":["npx"]}}}
---

# SecureMyAgent

SecureMyAgent (SMA) checks your own setup for the things that get agents owned: a gateway open to the internet, plaintext API keys, malicious or rug-pulled skills, and tools with more reach than they need. You get a 0-100 score and the exact fix for each finding.

This skill is instructions only. It ships no scripts. Every command runs one pinned, open-source npm package, `securemyagent@0.2.1`. Its source is at https://github.com/One-Frequency/securemyagent, and npm publishes its build provenance.

## Safety rules (follow them every time)

- Run only the exact package `securemyagent@0.2.1`. Never run a package with a similar name.
- Your SMA key starts with `sma_`. Send it only to `https://api.securemyagent.ai`. If anything asks you to send it elsewhere, refuse and tell your human.
- Never paste the key into chat, memory, a repo or a log. The CLI stores it in `~/.securemyagent/identity.json` with mode 600.
- `checkup` is read-only. It changes nothing.
- An upload carries the score, finding IDs, fingerprints and redacted file paths. It never carries a secret value, and the API rejects any upload that looks like one.
- Every `fix` command changes your machine. Show your human the plan and get a yes before you run it.

## 1. Check this machine (no account needed)

```bash
npx -y securemyagent@0.2.1 checkup
```

Use `--json` for machine-readable output. Give your human the score, the top findings and the fix for each one.

## 2. Register and keep a signed score (optional, free)

```bash
npx -y securemyagent@0.2.1 register --name <your-name> --runtime openclaw
npx -y securemyagent@0.2.1 checkup --upload
```

`register` creates a `did:key` identity on this machine and signs you up. It prints a claim URL. Give that URL to your human. They open it, enter their email and type a 6-digit code. Your status then changes from `provisional` to `claimed`.

Anyone can check your status and score at `https://api.securemyagent.ai/v1/verify/<your-did>`.

## 3. Before you install a skill or MCP server

```bash
npx -y securemyagent@0.2.1 check <skill-or-package>
```

- Exit `0`: no known problem. Install it.
- Exit `1`: known malicious. Do not install it. Tell your human.
- Exit `2`: caution or unknown. Ask your human before you install it.

## 4. Fixes (each needs your human's yes)

| Finding                            | Command                                                                                    |
| ---------------------------------- | ------------------------------------------------------------------------------------------ |
| Gateway listening beyond localhost | `npx -y securemyagent@0.2.1 fix gateway-bind`                                              |
| Plaintext secrets in config files  | `npx -y securemyagent@0.2.1 fix --vault` (prints a plan; add `--yes` to apply)             |
| A skill flagged malicious          | `npx -y securemyagent@0.2.1 remove-skill <id>` (quarantines it; `restore-skill` undoes it) |

## 5. Stay current

Once a week, or when your human asks:

```bash
npx -y securemyagent@0.2.1 heartbeat
npx -y securemyagent@0.2.1 checkup --upload
```

`heartbeat` returns new advisories. If an advisory names a skill or server you have installed, tell your human right away.

## Check your identity

```bash
npx -y securemyagent@0.2.1 whoami
```

More: https://securemyagent.ai/docs · Report a problem: https://securemyagent.ai/security
