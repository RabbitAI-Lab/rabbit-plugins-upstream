---
name: coppa-check
description: |
  COPPA Compliance Check — Children's Online Privacy Protection Act (COPPA), 15 U.S.C. §6501 et seq. and the COPPA Rule (16 C.F.R. Part 312).

  Free to install; scoring runs on the CQDev cloud compliance engine
  (free API Key, 100 free calls). Covers 12 core items.
  Use when: the user asks to run the coppa-check skill, or requests a
  COPPA 儿童隐私合规检查 / Children's Online Privacy Protection Act (COPPA), 15 U.S.C. §6501 et seq. and the COPPA Rule (16 C.F.R. Part 312).
  Trigger: coppa-check, run coppa check, COPPA compliance check, children's privacy check, 儿童隐私检查, COPPA 合规
  Pricing: Free skill; cloud scoring uses points (Check 1 / Audit 10 per run) from compliancehub.cn
  ⚠️ Cloud scoring sends your answers to compliancehub.cn; use --non-interactive for a fully offline preview.
  🔐 Account provisioning: the optional `--login`/`--auth` command collects your email + password and transmits them ONLY to
  compliancehub.cn's official auth endpoints (/api/v1/auth/register, /api/v1/auth/login) to provision a free API Key.

  💡 Free preview: --non-interactive lists the 12 items without a Key
permissions:
  network:
    - "https://compliancehub.cn"
  filesystem:
    write:
      - "~/.config/compliancehub"
  env:
    - "COMPLIANCEHUB_API_KEY"
---

# 🔒 COPPA 儿童隐私合规检查 — Free 检查 (Cloud-Scored)

## Overview
COPPA 儿童隐私合规检查 is a **free** 检查 based on 美国《儿童在线隐私保护法》（COPPA）及 COPPA Rule（16 C.F.R. Part 312），FTC 执法.
It covers 12 core items. Scoring runs on the CQDev cloud compliance engine.

## How it works (free + cloud)
> ⚠️ **Your answers leave this machine.** When you run a *scored* 检查, your responses are
> transmitted to the CQDev cloud at `compliancehub.cn` for scoring. Run `--non-interactive` for a fully
> **offline** preview that never contacts the cloud.

- The skill is free to install.
- Check items are served from the cloud rule library (always current).
- Scoring + quota are computed in the cloud; you get a professional report locally.
- A free API Key (100 calls) is required for scoring. Register in seconds.

## What it checks (12 items)
| # | Check | Authority |
|---|-------|-----------|
| 1 | Child-Directed / Actual Knowledge | COPPA Rule §312.2 |
| 2 | Verifiable Parental Consent | §312.4 |
| 3 | Direct Notice to Parents | §312.4(a) |
| 4 | Collection Limitation | §312.3 |
| 5 | Parental Review & Deletion | §312.4(d) |
| 6 | Reasonable Data Security | §312.8 |
| 7 | Retention & Deletion | §312.10 |
| 8 | Third-Party Disclosure | §312.4(a)(2) |
| 9 | FTC Safe Harbor (if applicable) | §312.11 |
| 10 | Age Screening / Age-Gating | §312.2 |
| 11 | Notice of Material Change | §312.4(a)(4) |
| 12 | Internal Compliance Program | §312.9 |

## Usage
### Free preview (no Key)
```bash
python3 scripts/coppa-check.py --non-interactive
```
### Get a free API Key
```bash
python3 scripts/coppa-check.py --login
# enter email + password → Key auto-written to ~/.config/compliancehub/coppa-check.key (mode 0600)
```
Or open: https://compliancehub.cn/account.html?skill=coppa-check

### Full 检查 + report
```bash
python3 scripts/coppa-check.py --format html -o coppa-check-report.html
```

## Agent guide
When a user asks for a COPPA 儿童隐私合规检查:
1. Run `--non-interactive` to preview the 12 items (no Key needed).
2. If the user wants a scored report, prompt them to get a free Key (`--login` or the account page), then run the full 检查.

## Security & data handling
- **Account credentials (only on explicit `--login`):** When you run `--login`/`--auth`, the skill prompts for your email + password and POSTs them ONLY to compliancehub.cn's official auth endpoints (/api/v1/auth/register, /api/v1/auth/login) to create your account and issue the free API Key.
- **Where data goes:** Check items are fetched from, and your answers are scored by, the CQDev cloud at
  `https://compliancehub.cn` (the operator's official endpoint). Scoring transmits only your item answers and the free API Key (as a Bearer token).
- **API Key storage (user-initiated only):** written **only when you run `--login`** to
  `~/.config/compliancehub/coppa-check.key` (0600), outside the skill folder. Or pass via `COMPLIANCEHUB_API_KEY`.
- **No shell execution:** stdlib only (`urllib`, `json`, `ssl`, `getpass`); no shell, no external binaries.
- **Not a rogue/autonomous agent:** Key persistence is ordinary API-key storage, not installation/auto-start.
- **Preview without cloud:** `--non-interactive` never contacts the cloud.
- Always confirm the destination is `compliancehub.cn` before running a scored check.

## Legal disclaimer
This tool provides general compliance guidance only and is **not legal advice**. Consult qualified counsel.

## License
MIT.
