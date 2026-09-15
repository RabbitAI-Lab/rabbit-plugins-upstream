## Description:

Apiguru Amazon Data helps agents fetch live, structured Amazon marketplace data from Apiguru for product details, prices, reviews, search results, best-sellers, deals, offers, stock, and seller information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apiguru-app](https://clawhub.ai/user/apiguru-app)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill to retrieve current Amazon marketplace data by ASIN, Amazon URL, product keyword, seller, or marketplace query. It is intended for Amazon data lookup and monitoring workflows where the user consents before any billable API call.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Billable API usage can spend a user's Apiguru account balance after free probes are exhausted.

Mitigation: Run the free capabilities check before planning work, tell the user the calls and cost cap, and wait for explicit consent before using a paid API key or other paid path.

Risk: API keys can be exposed or sent to the wrong place if handled outside the documented workflow.

Mitigation: Use the bundled probe script's prompt, stdin, or user-named key file options; do not search for keys, echo keys, or send them anywhere except the documented Apiguru API host.

Risk: The optional MCP server is a separate component and can introduce supply-chain risk when fetched at launch.

Mitigation: Prefer the bundled probe script or hosted MCP endpoint; when running locally, pin the package version, verify the artifact, and review it before use.

Risk: Amazon data can vary by marketplace and listing variant, and some search-result fields can be misleading when treated as product-level facts.

Mitigation: Choose the marketplace from the user's request, validate ASIN and seller inputs before calling, and use product-details or best-sellers data for exact variant or rank claims.

## Reference(s):

- [Apiguru Agent Kit](https://github.com/apiguru-app/agent-kit)
- [ClawHub Skill Page](https://clawhub.ai/apiguru-app/skills/apiguru-amazon-data)
- [Endpoint Reference](references/endpoints.md)
- [Costs, Billing, and Retries](references/errors-and-costs.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include API response summaries, filtering guidance, cost notes, and consent prompts before billable calls.]

## Skill Version(s):

1.1.25 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
