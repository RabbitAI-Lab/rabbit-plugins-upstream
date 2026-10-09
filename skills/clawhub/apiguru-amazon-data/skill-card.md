## Description:

Helps agents retrieve live Amazon product, price, review, offer, stock, seller, and search data from Apiguru across supported marketplaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apiguru-app](https://clawhub.ai/user/apiguru-app)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agents use this skill to answer user-requested Amazon marketplace questions about products, prices, reviews, availability, and sellers, or to monitor these details across supported marketplaces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product queries contact Apiguru and can incur charges when a user supplies an API key or uses their own payment-capable client.

Mitigation: Check prices and free-call availability, obtain explicit consent before billable requests, and set a spending cap.

Risk: Optional feedback is posted publicly and could expose secrets or private user data.

Mitigation: Request consent before posting feedback and omit API keys, personal information, and private user content.

Risk: The optional MCP server or package installation is separate software not covered by this skill's review.

Mitigation: Review the MCP server or package separately before use; prefer the included script when that review is unavailable.

## Reference(s):

- [Apiguru endpoint reference](references/endpoints.md)
- [Apiguru costs, billing, and retries](references/errors-and-costs.md)
- [Apiguru agent-kit homepage (listed in release metadata)](https://github.com/apiguru-app/agent-kit)
- [Apiguru API endpoint and price catalog](https://agent.apiguru.app/.well-known/x402)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Natural-language answers or structured API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live data is limited to supported Amazon marketplaces; requests may consume free calls or incur charges with an explicitly supplied API key.]

## Skill Version(s):

1.1.51 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
