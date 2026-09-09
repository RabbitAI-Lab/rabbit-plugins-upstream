## Description:

A deterministic A-share paper-trading skill for limit-order simulation, five-level order book matching, T+1 settlement, portfolio valuation, and auditable SQLite ledgers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fize](https://clawhub.ai/user/fize)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate a local A-share paper-trading workflow, including account creation, quotes, limit orders, order processing, portfolio review, trade history, and audit checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Market-data provider responses, including the unauthenticated Sina fallback path, may affect simulated fills and portfolio history.

Mitigation: Treat simulation results as advisory and review quote sources, timestamps, and stored snapshots before relying on fills or valuation.

Risk: The skill writes simulated account, order, fill, and quote data to a local SQLite ledger.

Mitigation: Use an appropriate local database path, protect ledger files, and confirm destructive account or order actions before execution.

Risk: Order placement, account reset, and batch processing can materially change the simulated ledger state.

Mitigation: Require explicit user confirmation before account resets, order placement, cancellation, or batch order processing.

## Reference(s):

- [Command reference](references/command_reference.md)
- [Market data contract](references/data_contract.md)
- [Trading rules](references/trading_rules.md)
- [Shanghai Stock Exchange trading rules](https://www.sse.com.cn/lawandrules/sselawsrules2025/stocks/exchange/c/c_20260424_10816482.shtml)
- [Shenzhen Stock Exchange trading rules](https://www.szse.cn/lawrules/rule/trade/current/t20260424_620190.html)
- [Ministry of Finance stamp-tax reduction](https://xj.mof.gov.cn/zcfagui/202311/t20231108_3915476.htm)
- [ChinaClear transfer fees](https://www.chinaclear.cn/zdjs/editor_file/20220701154723234.pdf)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with CLI commands and optional JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local SQLite trading records and may contact market-data providers for quotes and trading calendars.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
