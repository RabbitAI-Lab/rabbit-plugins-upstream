## Description:

Fetches live Amazon marketplace product, pricing, review, offer, search, deal, best-seller, stock, and seller data across 20 countries for research, monitoring, catalog enrichment, sourcing, and review analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apiguru-app](https://clawhub.ai/user/apiguru-app)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query live Amazon marketplace data for product research, price and buy-box monitoring, catalog enrichment, product sourcing, and review sentiment analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API requests can consume free probes, trigger paid API-key billing, or require x402 payment handling.

Mitigation: Check pricing and remaining free probes before large jobs, batch requests where supported, and use an API key only for accounts intended to be billed.

Risk: Changing APIGURU_BASE_URL or APIGURU_AGENT_BASE_URL can route requests and credentials to an untrusted host.

Mitigation: Leave the default service URLs in place unless the replacement endpoint is trusted and expected for the deployment.

Risk: Invalid marketplace, ASIN, seller, or retry choices can waste calls or produce misleading results.

Mitigation: Validate inputs, choose the intended marketplace, retry only transient 429 or 503 responses, and avoid retrying final 400 or billed 404 responses.

## Reference(s):

- [Apiguru Amazon Data on ClawHub](https://clawhub.ai/apiguru-app/skills/apiguru-amazon-data)
- [Apiguru endpoint reference](references/endpoints.md)
- [Costs, billing and retries](references/errors-and-costs.md)
- [x402 endpoint capabilities](https://agent.apiguru.app/.well-known/x402)
- [Hosted Apiguru MCP server](https://mcp.apiguru.app/mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with command examples, JSON snippets, and API call parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide live network API calls through keyless x402 access or an optional APIGURU_API_KEY.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
