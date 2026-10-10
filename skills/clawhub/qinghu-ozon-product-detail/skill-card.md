## Description:

Queries basic product details and sales data for up to ten Ozon product IDs at a time through Qinghu's data service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and commerce analysts query Ozon products by ID to review product information and sales performance, with up to ten IDs per request.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing and using qhkit relies on a third-party package and Qinghu service that may store or use an API token locally.

Mitigation: Confirm trust in the package and service before installation; protect the token and prefer a managed or preinstalled qhkit version when reproducibility matters.

Risk: Product-data queries can incur paid Qinghu credits, with charges varying by result count.

Mitigation: Check the estimated credit cost and obtain user approval before making paid queries; report actual credits consumed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-ozon-product-detail)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise response with product data; tabular file for larger result sets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports the queried period and credits spent; up to ten product IDs per request.]

## Skill Version(s):

0.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
