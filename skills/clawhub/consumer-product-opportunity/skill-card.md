## Description:

Assess a physical consumer-product idea using public search-interest signals, marketplace listings, and sampled customer feedback in a specified market. Use for product-launch hypotheses, not one-off shopping, market-size estimates, or profit forecasts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Product teams and entrepreneurs use this skill to screen physical consumer-product launch or line-extension hypotheses with public search, marketplace, and sampled customer-feedback signals.

### Deployment Geography for Use:

Global; findings are market-specific and depend on the selected country and supported marketplace coverage.

## Known Risks and Mitigations:

Risk: Product phrases and launch details are sent to Crawlora and the queried public services.

Mitigation: Generalize confidential launch details and use only product phrases you are comfortable sharing with those services.

Risk: The workflow requires a Crawlora API key.

Mitigation: Provide the key securely through the expected environment variable and keep it out of shared commands and outputs.

Risk: Larger research sessions may consume more API credits.

Mitigation: Check API credit costs before running larger research sessions.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora service](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/consumer-product-opportunity)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Compact Markdown opportunity matrix with observed signals, launch hypothesis, evidence limits, and one next validation step.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes product attributes, market, query set, retrieval dates, sampled listings, price ranges and currencies, demand signals, and review themes; does not provide a numeric opportunity score, sales estimate, margin forecast, or launch recommendation.]

## Skill Version(s):

1.0.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
