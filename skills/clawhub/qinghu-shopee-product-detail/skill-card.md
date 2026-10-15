## Description:

Looks up Shopee product sales, revenue, product type, and shop type for up to 10 product IDs per request through Qinghu AI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Sellers and analysts use this skill to retrieve and compare Shopee product metrics by product ID and marketplace, with user approval before paid queries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade qhkit and Node tooling on the local machine.

Mitigation: Review the tooling first and prefer a preinstalled, reviewed qhkit version in a controlled environment; avoid automatic latest-version upgrades when reproducibility matters.

Risk: A Qinghu API token must be configured for queries.

Mitigation: Configure the token only in a trusted environment and do not disclose it in responses.

Risk: Product-detail calls spend Qinghu credits.

Mitigation: Check the current credit estimate and obtain user approval before making paid calls.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/qinghu-shopee-product-detail)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise Markdown summary, with a table file for larger result sets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Up to 10 product IDs per query; identifies site and reporting period, and reports credits charged.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
