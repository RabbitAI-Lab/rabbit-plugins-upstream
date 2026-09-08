## Description:

Live Amazon marketplace data from Apiguru for product details, prices, reviews, keyword search, best sellers, deals, offers, stock, and seller profiles across 20 Amazon marketplaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apiguru-app](https://clawhub.ai/user/apiguru-app)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill when a user explicitly asks for live Amazon marketplace data by ASIN, Amazon URL, product, seller, keyword, or for price, stock, and review monitoring. It helps select endpoints, run the bundled probe script, interpret billing and retry behavior, and avoid unsupported general shopping advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Billable API calls can occur after free probes are exhausted or when the user supplies an Apiguru API key.

Mitigation: Run the free capabilities check first, disclose planned calls and estimated costs, get explicit consent before any billable call, and stop when a 402 response is returned.

Risk: API keys can be exposed through shell history, process listings, logs, or unintended destinations.

Mitigation: Use the bundled probe script with an interactive prompt, stdin, or a user-named key file; never pass a key as a command-line value and send it only to dash.apiguru.app.

Risk: Feedback text and optional contact information are posted publicly.

Mitigation: Warn users before using feedback submission and avoid including secrets, private customer data, or sensitive contact details.

Risk: Optional MCP package examples are a separate integration with supply-chain and deployment risk.

Mitigation: Prefer the bundled probe script or hosted MCP endpoint; if local MCP is used, pin versions, verify artifacts, review dependencies, and run with least privilege.

Risk: Amazon marketplace data can be incomplete, marketplace-specific, or misleading for variants and shared review counts.

Mitigation: Choose the marketplace from the user's request, validate ASINs, use product details for exact variants, and avoid presenting listing-family review counts as variant-specific facts.

## Reference(s):

- [Apiguru endpoint reference](references/endpoints.md)
- [Costs, billing and retries](references/errors-and-costs.md)
- [Apiguru Agent Kit](https://github.com/apiguru-app/agent-kit)
- [ClawHub skill page](https://clawhub.ai/apiguru-app/skills/apiguru-amazon-data)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include live third-party API responses, pricing guidance, retry guidance, and optional public feedback submission results.]

## Skill Version(s):

1.1.22 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
