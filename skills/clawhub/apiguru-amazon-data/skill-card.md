## Description:

Live Amazon marketplace data from Apiguru for product details, prices, reviews, keyword search, best-sellers, deals, offers and stock, and seller profiles across 20 Amazon marketplaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apiguru-app](https://clawhub.ai/user/apiguru-app)

### License/Terms of Use:

MIT

## Use Case:

Developers and agents use this skill when a user asks for Amazon marketplace data by ASIN, Amazon URL, product, seller, or keyword, or for Amazon price, stock, or review monitoring. It helps retrieve live structured Amazon data while requiring explicit consent before any billable call.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Amazon lookup queries are sent to Apiguru's service.

Mitigation: Use the skill only for user-requested Amazon data tasks and avoid sending unrelated personal or sensitive information in lookup terms.

Risk: Providing an Apiguru API key can bill the user's account.

Mitigation: Ask for explicit consent before billable calls, state the planned calls and cost, agree on a cap, and keep API keys private.

Risk: Feedback posts are public and may expose submitted text.

Mitigation: Do not include secrets, API keys, personal data, or private customer information in feedback messages.

Risk: Optional MCP server and package installation paths are separate from the reviewed script path.

Mitigation: Treat MCP use as a separate installation decision; prefer the reviewed script or hosted server, and review and pin any package before running it.

## Reference(s):

- [Apiguru endpoint reference](references/endpoints.md)
- [Costs, billing and retries](references/errors-and-costs.md)
- [Apiguru Agent Kit homepage](https://github.com/apiguru-app/agent-kit)
- [Apiguru x402 discovery document](https://agent.apiguru.app/.well-known/x402)
- [Apiguru paying documentation](https://agent.apiguru.app/llms.txt)
- [Apiguru feedback wall](https://dash.apiguru.app/feedback)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance, JSON API responses]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill returns live third-party API data and may include large JSON responses; list endpoints support compact projections and field selection.]

## Skill Version(s):

1.1.28 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
