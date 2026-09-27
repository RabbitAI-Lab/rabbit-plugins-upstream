## Description:

Retrieves live Amazon product, price, review, offer, stock, search, deal, and seller data through Apiguru across 20 marketplaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apiguru-app](https://clawhub.ai/user/apiguru-app)

### License/Terms of Use:

MIT

## Use Case:

Developers and other users request Amazon marketplace product and seller information by ASIN, URL, or keyword, or monitor prices, reviews, and availability through Apiguru.

### Deployment Geography for Use:

Global (20 supported Amazon marketplaces)

## Known Risks and Mitigations:

Risk: Keyed API calls may charge the user's Apiguru account.

Mitigation: Obtain explicit consent and agree on a spend cap before billable calls or batches.

Risk: An exposed API key could permit unwanted account usage.

Mitigation: Accept a key only when the user deliberately supplies it; keep it out of command lines and logs.

Risk: Feedback wall submissions are public and may expose sensitive details.

Mitigation: Submit feedback only at the user's request, omitting secrets, personal data, and sensitive request details.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/apiguru-app/skills/apiguru-amazon-data)
- [Project homepage (skill metadata)](https://github.com/apiguru-app/agent-kit)
- [Apiguru API guidance](https://agent.apiguru.app/llms.txt)
- [Endpoint reference](references/endpoints.md)
- [Costs, billing and retries](references/errors-and-costs.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands]

**Output Format:** [Markdown guidance and structured JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the selected Amazon marketplace and available Apiguru data.]

## Skill Version(s):

1.1.32 (source: server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
