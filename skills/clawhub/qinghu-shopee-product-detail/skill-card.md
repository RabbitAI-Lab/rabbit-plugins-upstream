## Description:

Looks up Shopee product sales, revenue, product type, and shop type for up to 10 product IDs per request using Qinghu data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Shopee sellers and analysts use this skill to retrieve product-level sales, revenue, and classification data by product ID for a selected site and date.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or upgrading the required CLI can change the host environment.

Mitigation: Review or perform installation yourself and prefer a pinned package version over automatic latest upgrades.

Risk: Configuring API credentials can leave a token in local settings.

Mitigation: Provide the token through a managed secret or temporary environment variable rather than persisting it in local config.

Risk: Product queries consume paid Qinghu credits, and failed service calls may still incur charges.

Mitigation: Check the current price and obtain user approval before paid calls; limit retries and report actual credits consumed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-shopee-product-detail)
- [Qinghu qhkit package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands, Configuration guidance]

**Output Format:** [Concise prose with product statistics and optional tabular file for larger results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Queries require a Shopee site, date, and up to 10 product IDs; paid calls consume Qinghu credits.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
