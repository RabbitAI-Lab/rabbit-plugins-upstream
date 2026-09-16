
A WorkBuddy/CodeBuddy Skill implementing a multi-asset investment strategy framework. Covers US, A-share, and HK stocks with asset-class differentiated rules, portfolio-level risk controls, and disciplined execution protocols.

**Current version**: v2.3.15 (2026-09-16)

## What It Does

InvAssistant combines AI-driven strategy guidance with executable trading rules:

- **Asset Classification** — Three tiers (A: Platform Core / B: High-Beta Cyclical / C: Low-Volatility Income) with differentiated entry/exit logic
- **Portfolio Risk Controls** — 7 non-overridable red lines (single position ≤25%, sector ≤35%, AI narrative ≤50%, drawdown defense, VIX circuit breakers)
- **Multi-Market Coverage** — US stocks (A/B/C tiered), A-shares (3-condition engine), HK stocks (warning-line framework)
- **Entry Modes** — Mode A (panic mispricing), Mode B (trend confirmation), Mode C (rebalancing), Mode D (A-class candidate zone entry, v2.1.1)
- **QMS Scoring** — 4-factor quality rating (earnings trend, sector relative strength, EPS revision, price structure)

## Quick Start

```bash
cp -r invassistant-skill ~/.workbuddy/skills/invassistant
pip install -r requirements.txt
```

Then ask WorkBuddy: "检查持仓" or "portfolio check".

> ⚠️ **Data transmission notice**: the optional `scripts/send_*.py` helpers push report content to a webhook endpoint that you configure (WeCom / DingTalk / Feishu). They are inert until configured and never send anything else. Review your endpoint config before enabling.

> ⚠️ **Not financial advice**: this is a decision-support framework. All outputs require human review; the author assumes no liability for trading losses.

## Version History

| Version | Date | Key Changes |
|---------|------|-------------|
| v2.3.15 | 2026-09-16 | Fail-closed hardening (valuation + volume gates); Framework Scope section; data-transmission notices; pinned requirements |
| v2.3.14 | 2026-09-11 | Purge real tickers from sample config and inline examples (§13 D8 / P10) |
| v2.3.13 | 2026-09-11 | D7: every balance carries an as-of and a source; corrections ship with a cash rollforward |
| v2.3.1 | 2026-06-06 | Major cleanup: English SKILL.md, clean frontmatter, bilingual README, no personal scripts |
| v2.1.1 | 2026-06-04 | Mode D: A-class candidate zone entry (no observation delay) |
| v2.1 | 2026-05-18 | A/B/C asset classification; 7 red lines; 4-factor QMS; trailing stop removed for A-class |
| v2.0 | 2026-05-18 | Full rebuild: decision pyramid, 5-factor QMS, 10 red lines (replaced by v2.1) |
| v1.5.x | 2026 Q1-Q2 | 3-condition engine, dual-mode entry, trailing stops, behavioral patches |
| v1.0 | 2026-01 | Initial: 3 red lines entry + multi-layer exit engine |

## Architecture

```
invassistant/
├── SKILL.md                    # Core definition (triggers, workflow, strategy rules)
├── README.md                   # This file (English)
├── README_zh.md                # Chinese documentation
├── references/                 # Detailed strategy references
│   ├── us_stock_strategy.md    # US stock A/B/C rules + Mode D
│   ├── a_share_strategy.md     # A-share 3-condition engine
│   └── risk_control_and_overrides.md  # 7 red lines, QMS, override protocol
└── scripts/                    # Execution engine (Python, optional helpers)
    ├── portfolio_checker.py    # Main checker
    ├── redline_engine.py       # Entry filter engine (fail-closed gates)
    ├── exit_engine.py          # Exit engine (stop-loss, trend break, momentum)
    ├── init_config.py          # First-run config generator (generic sample tickers)
    ├── data_fetcher.py         # Market-data fetch helper
    └── send_*.py               # Opt-in push to WeCom/DingTalk/Feishu webhooks
```

## License

MIT License — see [LICENSE](LICENSE)
