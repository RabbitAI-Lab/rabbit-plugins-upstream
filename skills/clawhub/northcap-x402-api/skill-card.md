## Description:

Provides pay-per-call crypto trading signals with entry, stop-loss and take-profit via the x402 standard (USDC on Ethereum). Live DRT/ICT signals for agents and traders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[northcap-group](https://clawhub.ai/user/northcap-group)

### License/Terms of Use:

MIT-0

## Use Case:

External agents and traders use this skill to discover, purchase, and call Northcap's paid x402 crypto-signal API for LONG/SHORT signals with entry, stop-loss, take-profit, and risk-reward values. It is intended for users who explicitly accept paid API calls and the financial risk of using trading signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can lead an agent toward paid API calls and USDC payments.

Mitigation: Require explicit user approval before payment, confirm pricing and wallet details, and limit calls to intentional use.

Risk: Crypto trading signals may be wrong or unsuitable for real trading decisions.

Mitigation: Treat signals as advisory data, require human review before trades, and do not rely on past backtest claims as a profit guarantee.

Risk: Authenticated calls send the X402_API_KEY and request details to an external service.

Mitigation: Use a dedicated API key, store it in the environment only, and restrict network access to the documented API host.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/northcap-group/skills/northcap-x402-api)
- [Northcap API base URL](https://api.northcapgroup.com)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API request and response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access to https://api.northcapgroup.com and the X402_API_KEY environment variable for authenticated signal calls.]

## Skill Version(s):

1.0.15 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
