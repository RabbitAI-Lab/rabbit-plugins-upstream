## Description:

Fetches live Amazon product, price, review, search, deal, stock and seller data through Apiguru across 20 marketplaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apiguru-app](https://clawhub.ai/user/apiguru-app)

### License/Terms of Use:

MIT-0

## Use Case:

Agents serving shoppers, researchers and developers use this skill when a user requests current Amazon marketplace details by ASIN, product, seller or keyword, or asks to monitor price, stock or reviews. It is not intended for other stores or general shopping advice.

### Deployment Geography for Use:

Global (Amazon data for 20 supported marketplaces)

## Known Risks and Mitigations:

Risk: Keyed API requests may charge the user's account, including unsuccessful marketplace lookups.

Mitigation: Confirm the calls, item count and spending cap before billable use; stop at the cap and never search for or expose an API key.

Risk: Feedback is posted publicly and may expose sensitive information.

Mitigation: Send feedback only at the user's request and exclude secrets and personal information.

Risk: The optional MCP package is separate from this skill and has not been reviewed as part of it.

Mitigation: Review the package and its dependencies independently before installing or running it.

## Reference(s):

- [Apiguru endpoint reference](references/endpoints.md)
- [Costs, billing and retries](references/errors-and-costs.md)
- [Apiguru agent kit (homepage linked in skill metadata)](https://github.com/apiguru-app/agent-kit)
- [Apiguru API capabilities and pricing](https://agent.apiguru.app/.well-known/x402)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Natural-language answers informed by structured API responses, with optional command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Answers depend on the requested Amazon marketplace and available API data; responses may omit or truncate fields.]

## Skill Version(s):

1.1.42 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
