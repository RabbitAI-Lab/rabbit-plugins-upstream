## Description:

Retrieves live Amazon product, pricing, review, search, offer, stock, and seller data through Apiguru across supported marketplaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apiguru-app](https://clawhub.ai/user/apiguru-app)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users request current Amazon marketplace information by ASIN, product, seller, or keyword, including price, stock, and review monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using an API key can incur per-call charges.

Mitigation: Obtain explicit approval before paid calls, agree on a spending cap, and do not provide an API key without authorization.

Risk: Feedback submissions appear on a public feedback wall.

Mitigation: Post only with the user's approval and exclude sensitive information.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/apiguru-app/skills/apiguru-amazon-data)
- [Declared skill homepage](https://github.com/apiguru-app/agent-kit)
- [Apiguru endpoint reference](references/endpoints.md)
- [Costs, billing, and retries](references/errors-and-costs.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [JSON API responses and Markdown explanations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses reflect live API data and may be subject to quotas or per-call charges.]

## Skill Version(s):

1.1.54 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
