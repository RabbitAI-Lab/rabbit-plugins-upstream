## Description:

按 Ozon 商品 ID 查询近 7 天、近 28 天、自然月、季度或年度的销售趋势快照。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Ozon sellers and analysts use this skill to inspect a product's sales history by reporting period and assess whether sales are rising or falling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing external tooling or changing the runtime environment without review.

Mitigation: Approve npm, Node, and qhkit installation before execution; avoid persistent PATH changes unless needed.

Risk: Exposing an API token or incurring charges for paid Ozon queries.

Mitigation: Use a secure secret store or temporary environment variable for the token, and confirm estimated credits before paid calls.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-ozon-product-trend)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Markdown summary or spreadsheet file for larger result sets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Labels results by platform, reporting period, and sample size.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
