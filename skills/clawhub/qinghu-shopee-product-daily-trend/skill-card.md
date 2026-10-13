## Description:

Queries daily price, sales, GMV, ratings, likes, and review trends for a Shopee product ID over up to 720 days.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Shopee sellers and analysts use this skill to inspect a product's daily historical sales and pricing trends by product ID, site, and date range.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad activation language may initiate a paid external data call for an unintended request.

Mitigation: Use only for explicit Shopee product daily-trend requests; disclose expected charges and obtain consent before paid calls.

Risk: Automatic setup can install Node and qhkit locally, and use requires a Qinghu API token.

Mitigation: Review setup first; prefer preinstalled, trusted, pinned dependencies and handle the token securely.

Risk: External Qinghu data requests may incur charges, including when a server call fails.

Mitigation: Confirm the site, product ID, and date range, check estimates, and avoid repeated speculative retries.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-shopee-product-daily-trend)
- [qhkit package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise trend summary with metrics and, for larger results, a table file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Daily observations may cover up to 720 days; results identify the Shopee site and date range, with credits used disclosed after paid calls.]

## Skill Version(s):

0.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
