## Description:

Use Krexa to research and backtest trading ideas, decode strategy material, run paper agents, and request user-approved live deployments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[krexa](https://clawhub.ai/user/krexa)

### License/Terms of Use:

MIT-0

## Use Case:

External traders use the skill to evaluate trading strategies with research and backtests, monitor paper agents, and manage approval requests for live trading.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Krexa receives submitted strategy material, and connected-account balances may be visible to the agent.

Mitigation: Submit only material intended for Krexa and review which exchange accounts are connected.

Risk: Exposure can vary by venue, and some venues lack per-trade and daily dollar caps.

Mitigation: Before approving a live deployment, review the strategy, funding, leverage, and venue-specific limits; use per-order approval to review each trade.

Risk: The Krexa key can access trading-related functions, and exchange credentials should remain private.

Mitigation: Protect the Krexa key and keep exchange credentials out of chat.

## Reference(s):

- [Krexa homepage](https://krexa.xyz)
- [Krexa MCP setup and key management](https://krexa.xyz/mcp/link)
- [Krexa MCP endpoint](https://www.krexa.xyz/mcp)
- [ClawHub skill listing](https://clawhub.ai/krexa/skills/krexa)

## Skill Output:

**Output Type(s):** [Text, Analysis, Guidance, JSON]

**Output Format:** [Structured tool results summarized in text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Trading research, backtest results, agent status, and deployment approval requests; no files are required.]

## Skill Version(s):

1.5.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
