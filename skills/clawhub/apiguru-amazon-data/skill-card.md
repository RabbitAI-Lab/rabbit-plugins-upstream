## Description:

Fetches live Amazon marketplace product details, prices, reviews, keyword search results, best-sellers, deals, offers, stock, and seller profiles through Apiguru.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apiguru-app](https://clawhub.ai/user/apiguru-app)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use this skill to retrieve live Amazon marketplace product, pricing, review, inventory, deal, and seller data for Amazon-specific lookup and monitoring requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connection failures can trigger additional paid requests without renewed approval.

Mitigation: Prefer free keyless access; before using an API key, require user approval before retrying any uncertain connection failure.

Risk: Feedback submissions are public and may include contact details.

Mitigation: Treat feedback as public; omit personal or contact information unless the user intends to publish it.

## Reference(s):

- [Apiguru endpoint reference](references/endpoints.md)
- [Costs, billing and retries](references/errors-and-costs.md)
- [Apiguru API documentation](https://agent.apiguru.app/llms-full.txt)

## Skill Output:

**Output Type(s):** [JSON, Text]

**Output Format:** [Structured Amazon marketplace data returned as JSON, with concise textual summaries as needed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returned fields vary by endpoint and requested data.]

## Skill Version(s):

1.1.56 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
