## Description:

三立期货AI交易助手 enables an agent to retrieve futures market data, account information, positions, orders, news, and leaderboard data, with simulated trading and live conditional order workflows when the user has authorized access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wyh431128](https://clawhub.ai/user/wyh431128)

### License/Terms of Use:

MIT-0

## Use Case:

External users and trading-support agents use this skill to connect OpenClaw conversations and MCP tools to the Sanli Zhiqi futures API for quotes, account review, simulated orders, live conditional orders, and company FAQ responses. It is not a source of investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence classifies the skill as suspicious because it can request financially sensitive authority for order placement, cancellation, and persistent live conditional orders.

Mitigation: Review the security warning before installation, start in simulated mode, and enable live trading only after understanding the permissions granted by the API key.

Risk: Stored API keys may authorize account access and trading actions until revoked.

Mitigation: Treat the API key as sensitive, verify the configured domain is the expected HTTPS endpoint, and revoke or rotate keys that are no longer needed.

Risk: Live conditional orders and stop-profit or stop-loss orders may persist after the conversation or client is closed.

Mitigation: Require explicit user confirmation of contract, direction, quantity, trigger price, and validity before creating or modifying live orders, and direct users to review or cancel active orders through the app when appropriate.

## Reference(s):

- [Usage Notes](references/usage-notes.md)
- [Company FAQ](references/company-faq.md)
- [OpenAPI Specification](references/openapi.yaml)
- [API Documentation Index](references/api.md)
- [Tool Schema Index](references/tools/index.json)
- [Publisher Profile](https://clawhub.ai/user/wyh431128)
- [Sanli Futures Website](https://www.sxslqh.com/)
- [Default API Domain](https://slzqapi.sxslqhsh.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and text responses with optional shell commands, API-oriented parameters, and MCP configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce trading workflow guidance and tool/API call parameters; live trading actions require user authorization and confirmation.]

## Skill Version(s):

1.5.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
