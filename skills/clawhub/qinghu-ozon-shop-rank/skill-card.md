## Description:

按账期、类目、店铺类型、销量、销售额及评分等条件查询 Ozon 热销店铺榜单。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

电商运营人员和市场分析师使用此技能筛选 Ozon 热销店铺，识别头部店铺与对标对象。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or updating external Node/qhkit tooling may change the user's environment.

Mitigation: Review installation steps first and install a pinned qhkit version in a managed environment.

Risk: The skill requires qhkit credentials and can issue paid data queries.

Mitigation: Configure credentials deliberately; check the estimated credit cost and obtain approval before paid calls.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-ozon-shop-rank)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise ranking summary with optional tabular file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the selected Ozon category, reporting period, and filters.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
