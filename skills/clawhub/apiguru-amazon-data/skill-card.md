## Description:

Retrieves live Amazon product, price, review, search, deal, stock, and seller data from Apiguru across 23 marketplaces on request.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apiguru-app](https://clawhub.ai/user/apiguru-app)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve current Amazon marketplace data by ASIN, product URL, keyword, or seller, and to monitor prices, stock, and reviews. Billable calls require explicit user consent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Some references were unresolved, leaving the security analysis incomplete at medium confidence.

Mitigation: Review relevant references before installation or relying on results; a clean scan is not a guarantee.

Risk: Calls after the free quota, or calls using an API key, can incur charges.

Mitigation: Before billable calls or batch and broad searches, explain the call count and cost, get explicit user consent, and agree on a spend cap.

Risk: The feedback command posts the submitted text to Apiguru's public feedback wall.

Mitigation: Review feedback text before submitting it and remove private or sensitive information.

## Reference(s):

- [Project homepage (Clawdis metadata)](https://github.com/apiguru-app/agent-kit)
- [Apiguru API pricing and endpoint schemas](https://agent.apiguru.app/.well-known/x402)
- [Apiguru API usage and payment guide](https://agent.apiguru.app/llms-full.txt)
- [Endpoint reference](artifact/references/endpoints.md)
- [Errors and costs reference](artifact/references/errors-and-costs.md)

## Skill Output:

**Output Type(s):** [JSON, Text]

**Output Format:** [Structured marketplace data returned as JSON and summarized as text when useful]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live results vary by marketplace; free quota and paid-call costs apply.]

## Skill Version(s):

1.1.61 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
