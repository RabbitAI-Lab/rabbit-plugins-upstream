## Description:

查询 Shopee 类目的月度、季度或年度长期趋势，支持多站点比较及产品类型和商品所在地筛选。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Sellers and market analysts use this skill to compare Shopee category growth across sites and time periods using Qinghu trend data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the required CLI can change the local toolchain.

Mitigation: Install only if you trust the qhkit provider; prefer a sandbox or pre-provisioned CLI and pin its package version when possible.

Risk: Token configuration and paid queries can expose credentials or incur charges.

Mitigation: Protect the token, review estimated credits, and approve the scope of each paid query before use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-shopee-category-trend)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Files]

**Output Format:** [Concise written conclusions with supporting data and a table file for larger results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports site, period and sample size; paid queries report credits consumed.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
