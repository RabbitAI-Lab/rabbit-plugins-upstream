## Description:

Use when building apps with HyperX Data API: Hyperliquid wallet analytics, market data, Twitter/news feeds.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hyperxtrade](https://clawhub.ai/user/hyperxtrade)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to build against the HyperX Data API for Hyperliquid wallet analytics, market analysis, Twitter streams, news feeds, and related trading data workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Some HyperX endpoints may require an API key or session cookie.

Mitigation: Use a secret manager or environment variables for credentials, and avoid pasting tokens or cookies into prompts, shared logs, or generated code.

Risk: Calling HyperX endpoints may expose wallet addresses or trading analytics queries to the HyperX service.

Mitigation: Review addresses and query payloads before API calls, and only send data that the user is authorized to share with HyperX.

## Reference(s):

- [HyperX Data API base URL](https://data-api.hyperx.trade)
- [HyperX API token settings](https://hyperx.trade/hyperliquid/settings)
- [HyperX skill page](https://clawhub.ai/hyperxtrade/skills/hyperx-data-api)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance]

**Output Format:** [Markdown guidance with endpoint tables and Python code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include REST and WebSocket endpoint guidance, authentication notes, request examples, and rate-limit details.]

## Skill Version(s):

1.1.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
