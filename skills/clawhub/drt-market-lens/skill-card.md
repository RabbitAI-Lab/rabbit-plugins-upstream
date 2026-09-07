## Description:

DRT Market Lens guides local DRT/ICT market analysis with 1h klines, premium/discount zones, SMA trend filters, and daily bias for 17 indices, forex, metals, and crypto instruments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[northcap-group](https://clawhub.ai/user/northcap-group)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to frame local market-analysis workflows for selected indices, forex pairs, metals, and crypto assets. It helps compare daily bias, premium/discount context, DRT zones, and SMA trend filters without placing trades.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Market-analysis guidance may be mistaken for financial advice or trade execution support.

Mitigation: Treat outputs as analytical context only; review decisions independently and do not use the skill as an automated trading system.

Risk: The artifact references a market_lens.py script, but that script is not included in the submitted artifact.

Mitigation: Review and scan any script, broker data source, or CSV ingestion workflow added later before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/northcap-group/skills/drt-market-lens)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown guidance with bash command examples and tabular analysis expectations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local-only guidance; any market data source or script added later should be reviewed separately.]

## Skill Version(s):

1.0.12 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
