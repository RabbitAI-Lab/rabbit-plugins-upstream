## Description:

Stock Screener is an MCP skill for A-share market screening, quote diagnostics, strategy backtesting, market review, portfolio and alert management, AI research reports, and five-day ML direction forecasts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[frontier-ai-vl](https://clawhub.ai/user/frontier-ai-vl)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze A-share markets, screen candidates, monitor watchlists and positions, run simple backtests, and request stock research outputs through an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Backtest accounting can materially misstate results.

Mitigation: Treat backtest output as decision support only until the sell-accounting issue is fixed and tested.

Risk: DSA credentials can be sent to an unconstrained configured URL.

Mitigation: Set DSA_BASE_URL only to trusted local or internal endpoints.

Risk: The MCP server makes market-data network requests and stores watchlist and portfolio records locally.

Mitigation: Review data flows before installation and avoid entering sensitive personal or trading data unless local storage and upstream market-data access are acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/frontier-ai-vl/skills/stock-screener-pro)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown and structured text returned by MCP tool calls]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update local SQLite portfolio, watchlist, and alert records; ML predictions may use cached in-memory results.]

## Skill Version(s):

3.1.1 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
