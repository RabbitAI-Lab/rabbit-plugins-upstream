---
name: ccpa-audit
description: |
  CCPA Compliance Audit — California Consumer Privacy Act (CCPA, Cal. Civ. Code §1798.100 et seq.) & CPRA amendment.

  Free to install; scoring runs on the CQDev cloud compliance engine
  (free API Key, 100 free calls). Covers 20 core items.
  Use when: the user asks to run the ccpa-audit skill, or requests a
  CCPA 合规深度审计 / California Consumer Privacy Act (CCPA, Cal. Civ. Code §1798.100 et seq.) & CPRA amendment.
  Trigger: ccpa-audit, CCPA 合规审计, 加州隐私审计, CCPA audit, 隐私合规报告
  Pricing: Free skill; cloud scoring uses points (Check 1 / Audit 10 per run) from compliancehub.cn
  ⚠️ Cloud scoring sends your answers to compliancehub.cn; use --non-interactive for a fully offline preview.
  🔐 Account provisioning: the optional `--login`/`--auth` command collects your email + password and transmits them ONLY to
  compliancehub.cn's official auth endpoints (/api/v1/auth/register, /api/v1/auth/login) to provision a free API Key.

  💡 Free preview: --non-interactive lists the 20 items without a Key
permissions:
  network:
    - "https://compliancehub.cn"
  filesystem:
    write:
      - "~/.config/compliancehub"
  env:
    - "COMPLIANCEHUB_API_KEY"
---

# 🔒 CCPA 合规深度审计 — Free 审计 (Cloud-Scored)

## Overview
CCPA 合规深度审计 is a **free** 审计 based on 加州消费者隐私法案（CCPA）及 CPRA 修正案.
It covers 20 core items. Scoring runs on the CQDev cloud compliance engine.

## How it works (free + cloud)
> ⚠️ **Your answers leave this machine.** When you run a *scored* 审计, your responses are
> transmitted to the CQDev cloud at `compliancehub.cn` for scoring. Run `--non-interactive` for a fully
> **offline** preview that never contacts the cloud.

- The skill is free to install.
- Check items are served from the cloud rule library (always current).
- Scoring + quota are computed in the cloud; you get a professional report locally.
- A free API Key (100 calls) is required for scoring. Register in seconds.

## What it checks (20 items)
| # | Check | Authority |
|---|-------|-----------|
| 1 | 知情权 | CCPA §1798.100 |
| 2 | 删除权 | CCPA §1798.105 |
| 3 | 选择退出权 | CCPA §1798.120 |
| 4 | 非歧视原则 | CCPA §1798.125 |
| 5 | 收集通知 | CCPA §1798.100(b) |
| 6 | 个人信息类别 | CCPA §1798.140 |
| 7 | 数据最小化 | CPRA §1798.100(b) |
| 8 | 服务提供商义务 | CCPA §1798.140(ag) |
| 9 | 第三方共享 | CCPA §1798.115 |
| 10 | 敏感个人信息(CPRA) | CPRA §1798.140(ae) |
| 11 | 更正权 | CPRA §1798.106 |
| 12 | 限制敏感PI使用 | CPRA §1798.121 |
| 13 | 自动化决策 | CPRA §1798.185(a)(16) |
| 14 | 隐私政策 | CCPA §1798.130 |
| 15 | 请求验证 | CCPA §1798.145(i) |
| 16 | 未成年人数据 | CCPA §1798.120(c) |
| 17 | 年度披露 | CCPA §1798.130(a)(5) |
| 18 | 合同审计权 | CCPA §1798.140(ag)(3) |
| 19 | 留存期限 | CPRA §1798.100(a)(3) |
| 20 | 安全义务 | CCPA §1798.150(a)(1) |

## Usage
### Free preview (no Key)
```bash
python3 scripts/ccpa-audit.py --non-interactive
```
### Get a free API Key
```bash
python3 scripts/ccpa-audit.py --login
# enter email + password → Key auto-written to ~/.config/compliancehub/ccpa-audit.key (mode 0600)
```
Or open: https://compliancehub.cn/account.html?skill=ccpa-audit

### Full 审计 + report
```bash
python3 scripts/ccpa-audit.py --format html -o ccpa-audit-report.html
```

## Agent guide
When a user asks for a CCPA 合规深度审计:
1. Run `--non-interactive` to preview the 20 items (no Key needed).
2. If the user wants a scored report, prompt them to get a free Key (`--login` or the account page), then run the full 审计.

## Security & data handling
- **Account credentials (only on explicit `--login`):** When you run `--login`/`--auth`, the skill prompts for your email + password and POSTs them ONLY to compliancehub.cn's official auth endpoints (/api/v1/auth/register, /api/v1/auth/login) to create your account and issue the free API Key.
- **Where data goes:** Check items are fetched from, and your answers are scored by, the CQDev cloud at
  `https://compliancehub.cn` (the operator's official endpoint). Scoring transmits only your item answers and the free API Key (as a Bearer token).
- **API Key storage (user-initiated only):** written **only when you run `--login`** to
  `~/.config/compliancehub/ccpa-audit.key` (0600), outside the skill folder. Or pass via `COMPLIANCEHUB_API_KEY`.
- **No shell execution:** stdlib only (`urllib`, `json`, `ssl`, `getpass`); no shell, no external binaries.
- **Not a rogue/autonomous agent:** Key persistence is ordinary API-key storage, not installation/auto-start.
- **Preview without cloud:** `--non-interactive` never contacts the cloud.
- Always confirm the destination is `compliancehub.cn` before running a scored check.

## Legal disclaimer
This tool provides general compliance guidance only and is **not legal advice**. Consult qualified counsel.

## License
MIT.
