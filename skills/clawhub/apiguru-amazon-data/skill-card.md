## Description:

Retrieves live product, price, review, stock, deal, best-seller, and seller data from 23 Amazon marketplaces through Apiguru when users request Amazon-specific lookups; billable calls require user approval.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apiguru-app](https://clawhub.ai/user/apiguru-app)

### License/Terms of Use:

MIT

## Use Case:

External users and developers can retrieve current product, price, review, stock, deal, best-seller, and seller information from supported Amazon marketplaces when an Amazon data lookup is requested.

### Deployment Geography for Use:

23 Amazon marketplaces across the Americas, Europe, the Middle East, Africa, and Asia-Pacific; availability varies by marketplace.

## Known Risks and Mitigations:

Risk: API calls can become billable after the free daily quota.

Mitigation: Check live pricing and remaining free calls, get approval before billable calls, and agree on a spending cap.

Risk: Feedback is posted to a public wall and may expose sensitive information.

Mitigation: Review the feedback text and remove sensitive information before submitting it.

Risk: Optional MCP packages are outside this skill's security review.

Mitigation: Review optional MCP packages separately before installing or using them.

## Reference(s):

- [Endpoint reference](references/endpoints.md)
- [Errors and costs](references/errors-and-costs.md)
- [Apiguru API documentation](https://agent.apiguru.app/llms-full.txt)
- [Apiguru API pricing and schemas](https://agent.apiguru.app/.well-known/x402)
- [Apiguru agent-kit project](https://github.com/apiguru-app/agent-kit)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands]

**Output Format:** [Structured JSON results with concise text summaries; shell commands for requests]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live marketplace data; available fields and results vary by endpoint and marketplace.]

## Skill Version(s):

1.1.58 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
