## Description:

Helps agents retrieve live Amazon product, price, review, search, deal, stock, and seller data from Apiguru across 20 marketplaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apiguru-app](https://clawhub.ai/user/apiguru-app)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use this skill to answer user-requested Amazon marketplace questions about products, prices, reviews, offers, availability, and sellers. It is not intended for other retailers or general shopping advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Amazon queries and optional feedback text are sent to Apiguru; feedback may be public.

Mitigation: Send only user-approved requests and omit secrets or private request payloads from feedback.

Risk: Calls made with an Apiguru API key can incur charges after free usage.

Mitigation: Check pricing and remaining free calls, agree a spending cap, and obtain explicit approval before keyed or batch calls.

Risk: Optional MCP or package installation uses a separate artifact outside this skill's review.

Mitigation: Review and approve that artifact independently before installing or running it.

## Reference(s):

- [Apiguru project homepage (listed in skill metadata)](https://github.com/apiguru-app/agent-kit)
- [Apiguru agent API documentation](https://agent.apiguru.app/llms.txt)
- [Endpoint and marketplace reference](artifact/references/endpoints.md)
- [Costs, billing, and retries](artifact/references/errors-and-costs.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands]

**Output Format:** [Markdown guidance and structured API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses depend on the selected Amazon marketplace and Apiguru availability.]

## Skill Version(s):

1.1.40 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
