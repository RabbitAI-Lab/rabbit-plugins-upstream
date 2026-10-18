## Description:

Retrieves live Amazon product, pricing, review, offer, stock, seller, and search data through Apiguru across 23 marketplaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apiguru-app](https://clawhub.ai/user/apiguru-app)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use this skill to answer user-requested Amazon marketplace questions about products, prices, reviews, availability, sellers, and keyword results, or to monitor Amazon listings. It is not intended for other stores or general shopping advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product, seller, keyword, and optional feedback details are sent to Apiguru.

Mitigation: Share only necessary query details; obtain user consent before submitting feedback, and omit personal or confidential data.

Risk: API-key calls and broad or batched requests may incur charges.

Mitigation: Check current prices and remaining free calls, agree on the scope and spending cap, and obtain approval before any billable call.

Risk: The optional MCP package or server is separate software beyond this skill's review.

Mitigation: Review it separately before use; pin and verify packages if installing locally.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/apiguru-app/skills/apiguru-amazon-data)
- [Skill homepage (listed in metadata)](https://github.com/apiguru-app/agent-kit)
- [Endpoint and marketplace reference](references/endpoints.md)
- [Costs, billing, and errors](references/errors-and-costs.md)
- [Apiguru agent API and payment documentation](https://agent.apiguru.app/llms-full.txt)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [JSON API data and Markdown guidance with CLI examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the selected Amazon marketplace; billable calls require user approval.]

## Skill Version(s):

1.1.55 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
