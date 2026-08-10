---
name: gdpr-check
description: |
  GDPR Compliance Check — General Data Protection Regulation (EU) 2016/679 (GDPR).

  Free to install; scoring runs on the CQDev cloud compliance engine
  (free API Key, 100 free calls). Covers 12 core items.
  Use when: the user asks to run the gdpr-check skill, or requests a
  GDPR 欧盟隐私合规检查 / General Data Protection Regulation (EU) 2016/679 (GDPR).
  Trigger: gdpr-check, run gdpr check, GDPR compliance check, EU privacy check, 欧盟隐私检查, GDPR 合规
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

# 🔒 GDPR 欧盟隐私合规检查 — Free 检查 (Cloud-Scored)

## Overview
GDPR 欧盟隐私合规检查 is a **free** 检查 based on 欧盟《通用数据保护条例》（GDPR, Regulation (EU) 2016/679）.
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
| 1 | Material & Territorial Scope | Art. 3 |
| 2 | Lawful Basis for Processing | Art. 6 |
| 3 | Valid Consent | Art. 7 |
| 4 | Transparency & Privacy Notice | Art. 13-14 |
| 5 | Data Subject Rights | Art. 15-17 |
| 6 | Automated Decision-Making | Art. 22 |
| 7 | Data Protection Impact Assessment | Art. 35 |
| 8 | Breach Notification | Art. 33-34 |
| 9 | International Transfers | Art. 44-49 |
| 10 | Security of Processing | Art. 32 |
| 11 | Processor Agreements | Art. 28 |
| 12 | Data Protection Officer | Art. 37-39 |

## Usage
### Free preview (no Key)
```bash
python3 scripts/gdpr-check.py --non-interactive
```
### Get a free API Key
```bash
python3 scripts/gdpr-check.py --login
# enter email + password → Key auto-written to ~/.config/compliancehub/gdpr-check.key (mode 0600)
```
Or open: https://compliancehub.cn/account.html?skill=gdpr-check

### Full 检查 + report
```bash
python3 scripts/gdpr-check.py --format html -o gdpr-check-report.html
```

## Agent guide
When a user asks for a GDPR 欧盟隐私合规检查:
1. Run `--non-interactive` to preview the 12 items (no Key needed).
2. If the user wants a scored report, prompt them to get a free Key (`--login` or the account page), then run the full 检查.

## Security & data handling
- **Account credentials (only on explicit `--login`):** When you run `--login`/`--auth`, the skill prompts for your email + password and POSTs them ONLY to compliancehub.cn's official auth endpoints (/api/v1/auth/register, /api/v1/auth/login) to create your account and issue the free API Key.
- **Where data goes:** Check items are fetched from, and your answers are scored by, the CQDev cloud at
  `https://compliancehub.cn` (the operator's official endpoint). Scoring transmits only your item answers and the free API Key (as a Bearer token).
- **API Key storage (user-initiated only):** written **only when you run `--login`** to
  `~/.config/compliancehub/gdpr-check.key` (0600), outside the skill folder. Or pass via `COMPLIANCEHUB_API_KEY`.
- **No shell execution:** stdlib only (`urllib`, `json`, `ssl`, `getpass`); no shell, no external binaries.
- **Not a rogue/autonomous agent:** Key persistence is ordinary API-key storage, not installation/auto-start.
- **Preview without cloud:** `--non-interactive` never contacts the cloud.
- Always confirm the destination is `compliancehub.cn` before running a scored check.

## Legal disclaimer
This tool provides general compliance guidance only and is **not legal advice**. Consult qualified counsel.

## License
MIT.
