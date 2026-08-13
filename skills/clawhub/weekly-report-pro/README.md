# Weekly Report Pro v1.1

Auto-collect Git commits + code stats → structured weekly/monthly reports. No fluff, results-oriented.

## Features

- 🔍 Auto-scans local Git repos for commits (weekly or monthly range)
- 📊 Optional code stats: lines added/deleted, files changed per repo
- 🔀 Supports merge commit inclusion for team-lead reporting
- 💬 Asks once for non-code work, metrics, blockers, and next-period plans
- 👤 Auto-detects role (Developer/Ops/Sales/Manager) from repo content
- 📄 4 role templates + 3 output styles (DingTalk/Feishu/Email)
- 📅 Dual mode: Weekly (`--mode weekly`) and Monthly (`--mode monthly`)
- 🔒 Privacy-first: all data stays local, nothing uploaded

> **v1.1** — Added monthly mode, code line stats, merge commit support, and smart role detection.

## Quick Start

1. Say "Write my weekly report" or "生成周报" or "写月报"
2. Point to your code directories when asked
3. Answer a few quick questions about your week/month
4. Get a polished, results-oriented report

## Requirements

- Python 3.8+
- Git (for commit collection)

## CLI Options

```
python3 collect_git.py --dirs ~/code --days 7 --with-stats
                       --mode monthly | --include-merges | --author <name>
```

## Who Is This For?

- Developers who want Git commits auto-summarized with line stats
- Tech leads who need merge-aware team progress reports
- Anyone who hates writing weekly/monthly reports from scratch
