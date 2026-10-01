## Description:

Helps agents retrieve live Amazon product, price, review, search, deal, stock, and seller data across 23 marketplaces through Apiguru.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apiguru-app](https://clawhub.ai/user/apiguru-app)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use this skill to answer user-requested Amazon marketplace lookups and monitor prices, availability, and reviews. It is not intended for other stores or general shopping recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Amazon lookup parameters are sent to Apiguru's third-party service.

Mitigation: Use the skill only for requested Amazon data, and avoid including sensitive information in lookup parameters.

Risk: Keyed requests and batch lookups can incur charges, including when a timed-out request completes.

Mitigation: Prefer keyless calls; obtain approval and agree a spending cap before billable or batch requests, and confirm before repeating timed-out keyed calls.

Risk: Feedback submissions are posted publicly and may expose secrets or personal data.

Mitigation: Review feedback before sending it and omit API keys, personal information, and other sensitive content.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/apiguru-app/skills/apiguru-amazon-data)
- [Project homepage (skill metadata)](https://github.com/apiguru-app/agent-kit)
- [Endpoint and marketplace reference](references/endpoints.md)
- [Costs, billing, and retries](references/errors-and-costs.md)
- [Apiguru API pricing and schemas](https://agent.apiguru.app/.well-known/x402)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands]

**Output Format:** [Markdown summaries of JSON API responses, with optional Python command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live Amazon marketplace data; calls may be rate-limited or billable.]

## Skill Version(s):

1.1.48 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
