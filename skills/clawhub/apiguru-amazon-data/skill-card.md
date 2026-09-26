## Description:

Retrieves live product, price, review, search, offer, stock, deal, and seller data across 20 Amazon marketplaces through Apiguru.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apiguru-app](https://clawhub.ai/user/apiguru-app)

### License/Terms of Use:

MIT-0

## Use Case:

Agents serving shoppers, sellers, and developers use this skill to answer Amazon-specific product questions and monitor prices, reviews, offers, and stock with live marketplace data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Keyed API calls may incur charges.

Mitigation: Prefer free keyless calls; get explicit consent and set a task budget before billable requests.

Risk: API credentials could be exposed if handled carelessly.

Mitigation: Accept keys only when deliberately provided by the user and never disclose them in responses or logs.

Risk: Feedback posts may expose private information publicly.

Mitigation: Exclude secrets and personal data from feedback before posting.

## Reference(s):

- [Apiguru project homepage](https://github.com/apiguru-app/agent-kit)
- [Apiguru API documentation](https://agent.apiguru.app/llms.txt)
- [Endpoints and marketplaces](references/endpoints.md)
- [Errors and costs](references/errors-and-costs.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Markdown summaries or structured JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live, marketplace-specific data; paid queries require user consent.]

## Skill Version(s):

1.1.30 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
