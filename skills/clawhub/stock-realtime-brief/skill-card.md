## Description: <br>
Stock Realtime Brief helps an agent generate China A-share portfolio briefings, single-stock analysis, multi-stock comparisons, screening, valuation, monitoring alerts, and trading-discipline checks from public market data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[michaelliugh](https://clawhub.ai/user/michaelliugh) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to support rule-based China A-share research workflows, including portfolio briefings, single-stock deep dives, multi-stock ranking, DCF valuation, sector rotation checks, real-time alerts, financial parsing, backtesting, and discipline reviews. The output is an analysis aid and does not replace licensed financial advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can produce finance-oriented operating guidance that users may mistake for investment advice. <br>
Mitigation: Treat outputs as decision-support analysis only, review all recommendations, and consult a qualified financial professional before trading. <br>
Risk: Market data, announcements, and alerts may be stale, incomplete, or wrong because the skill relies on third-party public data sources. <br>
Mitigation: Verify prices, filings, and material news with authoritative sources before acting on any generated report. <br>
Risk: The security review identifies under-scoped credential use, hard-coded portfolio paths, and QQ message sending to a fixed chat target. <br>
Mitigation: Configure or remove hard-coded chat IDs, watchlists, secret-file paths, and portfolio paths before running push or watch modes. <br>
Risk: Persistent monitoring and alerting can send portfolio or watchlist information outside the local environment. <br>
Mitigation: Run monitoring only after confirming where alerts are sent and what data leaves the machine. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/michaelliugh/skills/stock-realtime-brief) <br>
- [Publisher profile](https://clawhub.ai/user/michaelliugh) <br>
- [Project homepage](https://github.com/Michaelliugh/stock-realtime-brief) <br>
- [English README](README_EN.md) <br>
- [Methodology](docs/methodology.md) <br>
- [Data freshness principle](docs/principles/data-freshness.md) <br>
- [Trading discipline](docs/principles/trading-discipline.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports with tables, action lists, and optional shell commands or configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include market data summaries, stop-loss levels, alert setup guidance, portfolio paths, and risk notes.] <br>

## Skill Version(s): <br>
5.5.0 (source: frontmatter, pyproject.toml, CHANGELOG, server release) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
