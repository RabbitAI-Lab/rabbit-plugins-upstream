---
name: ccpa-audit
description: |
  CCPA Compliance Audit — California Consumer Privacy Act (CCPA, Cal. Civ. Code §1798.100 et seq.) & CPRA amendment.

  Free to install; scoring runs on the CQDev cloud compliance engine
  (free API Key, 100 free calls). Covers 20 core items.
  Use when: the user explicitly asks to run the ccpa-audit skill (e.g. "run ccpa-audit",
  "use the ccpa-audit skill"). Do NOT activate on generic mentions of "CCPA" or "California privacy"
  in ordinary conversation — this skill transmits answers to a third-party cloud and must be
  opted into explicitly by name.
  Trigger (explicit opt-in only): ccpa-audit, run ccpa-audit, use ccpa-audit skill, run the ccpa-audit skill
  Pricing: Free skill; cloud scoring uses points (Check 1 / Audit 10 per run) from compliancehub.cn
  ⚠️ Cloud scoring sends your answers to compliancehub.cn. The free preview (--non-interactive) fetches the
  latest check items from the cloud rule library but transmits NO answers; if the network is unavailable it
  falls back to the bundled item set. Scored runs require a free API Key.
  🔐 Free API Key: registration happens in the **web account center** (https://compliancehub.cn/account.html),
  because it includes a human/captcha check the terminal cannot perform. This skill only CONSUMES the Key —
  supply it via the `COMPLIANCEHUB_API_KEY` environment variable or the
  `~/.config/compliancehub/ccpa-audit.key` file (0600). It never collects your email/password or registers accounts.
  🌐 Language: bilingual (中文/English). Guidance and recommendations default to Chinese for Chinese-speaking
  compliance teams; legal/regulatory terms keep English originals. Users may request English output at any time.

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

# 🔒 CCPA Compliance Audit (CCPA 合规深度审计) — Free, Cloud-Scored

## Overview
CCPA 合规深度审计 is a **free** 审计 based on 加州消费者隐私法案（CCPA）及 CPRA 修正案.
It covers 20 core items. Scoring runs on the CQDev cloud compliance engine.

## How it works (free + cloud)
> ⚠️ **Your answers leave this machine.** When you run a *scored* 审计, your responses are
> transmitted to the CQDev cloud at `compliancehub.cn` for scoring. The free `--non-interactive` preview
> fetches the latest check items from the cloud rule library but transmits NO answers; it falls back to the
> bundled item set if the network is unavailable.

- The skill is free to install.
- Check items are served from the cloud rule library (always current).
- Scoring + quota are computed in the cloud; you get a professional report locally.
- A free API Key (100 calls) is required for scoring. Get one in seconds at the web account center.

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
> 💡 交互提示：逐项作答时可直接输入中文（是 / 否 / 不适用），输入 `?` 可查看该项的合规建议；
> 作答进度自动存为草稿，中断后重新运行会提示「继续 / 重新开始」。

### Free preview (no Key)
```bash
python3 scripts/ccpa-audit.py --non-interactive
```
### Get a free API Key (web, then hand it to this skill)
1. Open the account center and register (human check is browser-only):
   https://compliancehub.cn/account.html?skill=ccpa-audit
2. Copy the Key, then give it to this skill (pick one):
```bash
export COMPLIANCEHUB_API_KEY=<网页显示的 Key>
# 或持久保存到本 skill 的密钥文件：
mkdir -p ~/.config/compliancehub && echo '<网页显示的 Key>' > ~/.config/compliancehub/ccpa-audit.key
```

### Full 审计 + report
```bash
python3 scripts/ccpa-audit.py --format html -o ccpa-audit-report.html
```

## Agent guide
When a user asks for a CCPA 合规深度审计:
1. Run `--non-interactive` to preview the 20 items (no Key needed).
2. If the user wants a scored report, point them to the web account center to get a free Key, then run the full 审计 (the Key is read from COMPLIANCEHUB_API_KEY or ~/.config/compliancehub/ccpa-audit.key).

## Security & data handling
- **No account creation / no credentials collected:** This skill never prompts for or transmits your email/password,
  and it never registers accounts. In preview mode (`--non-interactive`) it only reads the public rule library and
  sends NO answers; nothing about your compliance status persists across sessions.
- **Where data goes:** Check items are fetched from, and your answers are scored by, the CQDev cloud at
  `https://compliancehub.cn` (the operator's official endpoint). Scoring transmits only your item answers and the free API Key (as a Bearer token).
- **API Key (you provide it):** obtained from the web account center and supplied via the
  `COMPLIANCEHUB_API_KEY` environment variable or `~/.config/compliancehub/ccpa-audit.key` (0600, outside the skill
  folder). The skill reads the Key; it does not write accounts or collect credentials.
- **No shell execution:** stdlib only (`urllib`, `json`, `ssl`); no shell, no external binaries.
- **Not a rogue/autonomous agent:** The stored file is an ordinary API-key (0600), not an auto-start,
  session, or background process. No state is kept beyond that single key file.
- **Preview mode:** `--non-interactive` fetches the public check items from the cloud rule library but
  sends NO answers; it falls back to the bundled item set if the network is unavailable.
- Always confirm the destination is `compliancehub.cn` before running a scored check.

## Legal disclaimer
This tool provides general compliance guidance only and is **not legal advice**. Consult qualified counsel.

## License
MIT.
