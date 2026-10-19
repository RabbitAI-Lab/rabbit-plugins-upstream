## Description:

Helps users research trading ideas, backtest strategies, and request deployment of trading agents through Krexa with user approval for live deployment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[krexa](https://clawhub.ai/user/krexa)

### License/Terms of Use:

MIT-0

## Use Case:

Traders and other users can evaluate ideas for supported crypto and prediction markets, review backtests or paper trading, and request a live trading agent subject to their approval and limits in the Krexa app.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Exposure of the Krexa agent key could allow unauthorized research or deployment requests.

Mitigation: Keep KREXA_AGENT_KEY private, store it in an environment variable or secret store, and revoke it if exposed.

Risk: Live trading can lose money, especially if a strategy is deployed without a deep test or with unsuitable limits.

Mitigation: Review the venue, leverage, loss cap and other limits; consider a deep test and per-order approval; approve and fund live deployments only in the Krexa app.

## Reference(s):

- [Krexa skill on ClawHub](https://clawhub.ai/krexa/skills/krexa)
- [Krexa homepage](https://krexa.xyz)
- [Connection and key setup](artifact/references/setup.md)
- [Krexa tools](artifact/references/tools.md)
- [Trading and deployment limits](artifact/references/limits.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Text]

**Output Format:** [Markdown summaries of research, backtests, trading status, and deployment approval steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports trading limits and results returned by Krexa; provides approval links for user action.]

## Skill Version(s):

1.3.4 (source: skill metadata and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
