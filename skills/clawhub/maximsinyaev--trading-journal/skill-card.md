## Description:

Keep an exact trading journal for the user - record buys/sells, import broker exports (IBKR, Trading 212, Binance, any CSV/XLSX/JSON), show open positions and realized/unrealized P&L, stats (win rate, profit factor, R, drawdown), post-trade reviews, dividends and splits, and render an interactive HTML dashboard or Obsidian notes. Use whenever the user mentions their trades, positions, portfolio P&L, trading journal or trading performance. All numbers come from a deterministic local ledger, never from the model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maximsinyaev](https://clawhub.ai/user/maximsinyaev)

### License/Terms of Use:

MIT-0

## Use Case:

Traders use the skill to record or import transactions and review positions, profit and loss, performance statistics, and trade notes through a local trading ledger.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Trade and journal details returned by the CLI may be sent to the agent's model provider as part of the conversation context.

Mitigation: Treat journal output as sensitive and follow the data handling settings for the model provider in use.

Risk: Users may rely on recorded or imported ledger figures for investment or tax decisions.

Mitigation: Check results against broker statements and treat the skill as a record-keeping and research aid, not investment or tax advice.

## Reference(s):

- [Agent Trading Journal project](https://github.com/MaximSinyaev/agent-trading-journal)
- [Version 1.3.0 release notes](https://github.com/MaximSinyaev/agent-trading-journal/releases/tag/v1.3.0)
- [CLI reference](references/cli.md)
- [Import reference](references/import.md)
- [Metrics reference](references/metrics.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Files]

**Output Format:** [Text or Markdown summaries; optional offline HTML dashboard and Obsidian notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Trade figures are read from the local ledger; optional live quotes can be fetched through Yahoo Finance.]

## Skill Version(s):

1.3.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
