## Description:

查询 Shopee 店铺最多 720 天的每日销量、销售额、商品数和评分趋势。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Shopee sellers and market analysts use this skill to inspect a shop's daily sales, revenue, product count, and rating trends by shop ID and marketplace.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid data requests can consume Qinghu credits, including some failed calls.

Mitigation: Check the quoted cost and obtain user approval before paid requests; report actual credits charged.

Risk: Using the skill requires an API token and network access to the Qinghu service.

Mitigation: Protect the token and install or connect to the service only if its package and service are trusted.

Risk: Setup instructions may install local software or change the user's shell environment.

Mitigation: Prefer a managed or preinstalled qhkit setup; get approval before global installs or shell-profile changes.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-shopee-shop-daily-trend)
- [Qinghu qhkit package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Markdown summary with optional tabular file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Daily shop metrics for up to 720 days; larger result sets may be delivered as a table file.]

## Skill Version(s):

0.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
