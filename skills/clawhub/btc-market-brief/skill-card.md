## Description:

A short, data-backed Bitcoin market brief on demand or each morning, covering price and 24-hour change across exchanges, funding and basis, liquidations, notable signals, and unusual activity using AgentReeve's live multi-exchange data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shakeelamjid](https://clawhub.ai/user/shakeelamjid)

### License/Terms of Use:

MIT-0

## Use Case:

Bitcoin users can request a concise market snapshot on demand or each morning to review price changes, derivatives, liquidations, notable signals, and when the data was recorded.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may activate for unrelated status requests.

Mitigation: Review its activation rules before installing and limit use to Bitcoin market brief requests.

Risk: Small paid calls may be made without asking for approval each time.

Mitigation: Review the payment rules and set an acceptable spending limit; use the free preview when paid access is not desired.

## Reference(s):

- [Server-resolved source repository](https://github.com/shakeelamjid/agentreeve-skills/tree/main/btc-market-brief)
- [BTC Market Brief on ClawHub](https://clawhub.ai/shakeelamjid/skills/btc-market-brief)
- [AgentReeve BTC preview API](https://agentreeve.com/api/v1/btc/preview)
- [AgentReeve BTC brief API](https://agentreeve.com/api/v1/btc/brief)
- [AgentReeve BTC signals API](https://agentreeve.com/api/v1/btc/signals?days=30)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis]

**Output Format:** [Markdown in 4–6 concise lines]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a data timestamp; market information is observational, not financial advice.]

## Skill Version(s):

0.1.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
