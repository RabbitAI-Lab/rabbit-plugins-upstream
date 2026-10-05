## Description:

Retrieves live Amazon product, pricing, review, search, stock, deal, and seller data across 23 marketplaces through Apiguru's API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apiguru-app](https://clawhub.ai/user/apiguru-app)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve current Amazon listing, price, review, offer, stock, search, deal, and seller information for user-requested marketplaces. It is not intended for other stores or general shopping advice.

### Deployment Geography for Use:

Global (23 supported Amazon marketplaces)

## Known Risks and Mitigations:

Risk: Amazon product, seller, or keyword queries are sent to Apiguru.

Mitigation: Use only for user-requested Amazon lookups and disclose the external service before sending sensitive queries.

Risk: API-key or wallet-backed requests can incur charges.

Mitigation: Check remaining free calls and current prices, obtain explicit approval before billable calls, and agree a spending cap.

Risk: Feedback posts may expose secrets or private information on a public wall.

Mitigation: Send feedback only with user consent; exclude API keys, personal information, and private prompts or results.

Risk: Optional MCP integration introduces a separate package or server trust boundary.

Mitigation: Prefer the included probe script for direct use; review MCP server and package setup separately before enabling it.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/apiguru-app/skills/apiguru-amazon-data)
- [Project homepage (skill metadata)](https://github.com/apiguru-app/agent-kit)
- [Apiguru API documentation](https://agent.apiguru.app/llms-full.txt)
- [Endpoint reference](artifact/references/endpoints.md)
- [Costs, billing and retries](artifact/references/errors-and-costs.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown, Shell commands, Guidance]

**Output Format:** [JSON API results with text or Markdown explanations and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the selected marketplace, available API data, and free or approved paid access.]

## Skill Version(s):

1.1.50 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
