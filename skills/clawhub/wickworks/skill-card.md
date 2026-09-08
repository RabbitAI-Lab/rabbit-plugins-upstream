## Description:

wickworks lets an agent compute stateless technical indicators and Smart-Money-Concepts objects from caller-supplied OHLC candlestick bars through REST or MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use wickworks when an agent needs technical indicators, Smart-Money-Concepts structure, or compact market-data summaries computed from OHLC bars supplied by the caller. It is useful for enriching trading or market datasets without asking the skill to fetch data, forecast prices, or produce buy/sell opinions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup uses a mutable third-party container image.

Mitigation: Run only a trusted instance and prefer a pinned image digest or locally audited build.

Risk: The service is unauthenticated by default and can be called by anyone who can reach its port.

Mitigation: Bind it to 127.0.0.1 by default, or expose it only behind authenticated reverse-proxy or VPN controls.

Risk: Caller-supplied OHLC data may be proprietary or sensitive.

Mitigation: Send bars only to an endpoint you operate or otherwise trust.

Risk: The skill returns market-analysis primitives, not forecasts or trading recommendations.

Mitigation: Treat outputs as computed indicators for analysis and avoid presenting them as buy, sell, or price-prediction advice.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/wickworks)
- [wickworks setup](references/setup.md)
- [Project homepage](https://github.com/psyb0t/docker-wickworks)
- [Model Context Protocol](https://modelcontextprotocol.io)
- [OpenClaw MCP bridge plugin](https://github.com/psyb0t/docker-wickworks/tree/main/.agents/plugins/wickworks)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON examples and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides an agent to call a stateless JSON service that returns NaN-safe indicator series, structured indicator objects, metadata, health results, or MCP tool results.]

## Skill Version(s):

0.7.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
