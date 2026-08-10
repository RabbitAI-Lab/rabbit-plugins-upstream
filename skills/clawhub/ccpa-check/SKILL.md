---
name: ccpa-check
description: |
  CCPA/CPRA Compliance Check — based on the California Consumer Privacy Act (CCPA)
  and the CPRA amendment, covers 12 core compliance checks for businesses subject to
  California privacy law. Free to install; scoring runs on the CQDev cloud
  compliance engine (free API Key, 100 free calls).
  Use when: the user explicitly asks to run the CCPA Check skill, or asks for a
  CCPA/CPRA (California) compliance assessment / California consumer privacy review.
  Trigger: ccpa-check, run ccpa check, CCPA compliance check, California CCPA/CPRA assessment
  Pricing: Free skill; cloud scoring requires a free API Key (100 free calls) from compliancehub.cn
  ⚠️ Cloud scoring sends your 12 answers to compliancehub.cn; use --non-interactive for a fully offline preview that never contacts the cloud.
  💡 Free preview: --non-interactive lists the 12 check items without a Key
permissions:
  network:
    - "https://compliancehub.cn"
  filesystem:
    write:
      - "~/.config/compliancehub"
  env:
    - "COMPLIANCEHUB_API_KEY"
---

# 🔒 CCPA Check — Free Compliance Check (Cloud-Scored)

## Overview
CCPA Check is a **free** compliance self-check for businesses subject to the California
Consumer Privacy Act (CCPA) and the CPRA amendment. It covers 12 core checks across
applicability, consumer rights, opt-out, service providers, records, and security.
Scoring runs on the CQDev cloud compliance engine.

## How it works (free + cloud)
> ⚠️ **Your answers leave this machine.** When you run a *scored* check, your responses to the
> 12 compliance questions are transmitted to the CQDev cloud at `compliancehub.cn`
> for scoring. Those answers can cover sensitive details — consumer-data practices, service
> providers, security controls, and legal exposure. Only proceed if you are comfortable sending
> them to `compliancehub.cn`. Run `--non-interactive` for a fully **offline** preview that never
> contacts the cloud.

- The skill is free to install.
- Check items are served from the cloud rule library (always current).
- Scoring + quota are computed in the cloud; you get a professional report locally.
- A free API Key (100 calls) is required for scoring. Register in seconds.

## What it checks (12 items)
| # | Check | Authority |
|---|-------|-----------|
| 1 | Business Applicability | CCPA §1798.140(d) |
| 2 | Privacy Notice at Collection | CCPA §1798.100(b) |
| 3 | Consumer Rights Fulfillment | CCPA §1798.100/105/106 |
| 4 | Identity Verification | CCPA §1798.145(i) |
| 5 | Response Timeliness | CCPA §1798.130(a)(2) |
| 6 | Non-Discrimination | CCPA §1798.125 |
| 7 | Right to Opt-Out | CCPA §1798.120 |
| 8 | Sensitive PI Handling | CPRA §1798.121 |
| 9 | Sale/Sharing of PI | CCPA §1798.140(t)/115 |
| 10 | Service Provider Contracts | CCPA §1798.140(ag) |
| 11 | Record Keeping | CCPA §1798.130(a) |
| 12 | Reasonable Security | CCPA §1798.81.5 |

## Usage

### Free preview (no Key)
```bash
python3 scripts/ccpa-check.py --non-interactive
```

### Get a free API Key
```bash
python3 scripts/ccpa-check.py --login
# enter email + password → Key auto-written to ~/.config/compliancehub/ccpa-check.key (mode 0600)
```
Or open: https://compliancehub.cn/account.html?skill=ccpa-check

### Full check + report
```bash
python3 scripts/ccpa-check.py --format html -o ccpa-report.html
```
Answer 12 yes/no questions; the cloud scores and returns an HTML report.

## Agent guide
When a user asks for a CCPA/CPRA compliance check:
1. Run `--non-interactive` to preview the 12 items (no Key needed).
2. If the user wants a scored report, prompt them to get a free Key (`--login` or the
   account page), then run the full check.

## Security & data handling
- **Where data goes:** Check items are fetched from, and your yes/no answers are scored by,
  the CQDev cloud at `https://compliancehub.cn` (the operator's official endpoint,
  pinned in code and **not** overridable by environment variable). Scoring transmits only your
  item answers and the free API Key (as a Bearer token); no documents or other PII are sent.
- **API Key storage (user-initiated only):** The free Key is written **only when you run
  `--login`** (an explicit user action), to a private, per-user file
  `~/.config/compliancehub/ccpa-check.key` with `0600` permissions — **outside** this skill
  folder, so it is never committed to source control or shared with the workspace. You can also
  pass it via the `COMPLIANCEHUB_API_KEY` environment variable (recommended for CI/shared hosts).
- **No shell execution:** This skill runs as a Python 3 subprocess using only the standard
  library (`urllib`, `json`, `ssl`, `getpass`). It does **not** spawn a shell, does not run
  arbitrary OS commands, and does not execute external binaries.
- **Not a rogue/autonomous agent:** Writing the Key to `~/.config/compliancehub/` is ordinary
  API-key persistence for your convenience — not agent installation, not auto-start, and not
  self-modification. The skill does nothing unless you invoke it from the terminal.
- **Preview without cloud:** `--non-interactive` lists the 12 items and never contacts the cloud.
- Always confirm the destination is `compliancehub.cn` before running a scored check.

## Legal disclaimer
This tool provides general compliance guidance only and is **not legal advice**.
Consult qualified counsel for formal opinions. Laws change; verify against official sources.

## License
MIT.
