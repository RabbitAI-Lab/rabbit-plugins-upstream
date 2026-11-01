## Description:

Retrieves live product, price, review, deal, offer, stock, and seller data from 23 Amazon marketplaces, with user approval required before billable lookups.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apiguru-app](https://clawhub.ai/user/apiguru-app)

### License/Terms of Use:

MIT

## Use Case:

External users use this skill when they ask an agent for current Amazon marketplace product, price, review, deal, offer, stock, or seller information by ASIN, Amazon URL, product, seller, or keyword. It covers Amazon marketplaces and is not intended for other stores or general shopping advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A request made with an API key is billed to the user's account, and lookup parameters are sent to Apiguru.

Mitigation: Get consent before any billable call, agree on a spending cap, and use only the parameters needed for the lookup.

Risk: Feedback submitted through the skill is posted publicly and could expose secrets or personal information.

Mitigation: Review the exact feedback text and remove secrets and personal information before submitting it.

Risk: Optional MCP packages and hosted services are separate from the bundled script and were not independently reviewed in this release evidence.

Mitigation: Use the bundled script by default; review and limit access for any MCP service before connecting it.

## Reference(s):

- [Project homepage (metadata)](https://github.com/apiguru-app/agent-kit)
- [API usage and payment documentation](https://agent.apiguru.app/llms-full.txt)
- [endpoints.md](references/endpoints.md)
- [errors-and-costs.md](references/errors-and-costs.md)

## Skill Output:

**Output Type(s):** [JSON, Text, Guidance]

**Output Format:** [Structured Amazon data in JSON with concise status or error messages and usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live results depend on the requested marketplace and endpoint; list responses may be limited or omit fields when requested.]

## Skill Version(s):

1.1.60 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
