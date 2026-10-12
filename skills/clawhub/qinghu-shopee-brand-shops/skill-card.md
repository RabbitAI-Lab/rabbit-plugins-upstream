## Description:

按品牌名称查询 Shopee 上销售该品牌的热销店铺列表。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

商家及市场分析人员按品牌、Shopee 站点和榜单周期查找热销店铺，并查看相关店铺数据。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or update local software and change the shell environment.

Mitigation: Review and explicitly approve npm, npx, Node, PATH and shell-profile changes; prefer a managed or pinned qhkit installation.

Risk: Configuring the Qinghu API token may store a secret locally.

Mitigation: Check where qhkit stores credentials before configuring a token; use an environment variable where appropriate.

Risk: Queries may consume paid Qinghu credits.

Mitigation: Check the estimate and obtain user approval before paid calls.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/qinghu-shopee-brand-shops)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise prose with an optional Markdown preview or exported table file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Identifies the site, period and sample size; reports credits spent on paid calls.]

## Skill Version(s):

0.1.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
