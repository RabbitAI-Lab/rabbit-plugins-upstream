## Description:

查询 Ozon 三级类目的市场销售详情，帮助用户了解细分类目的市场规模和销量。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Ozon sellers and market analysts use this skill to retrieve sales and market-size details for a specified third-level product category and category type.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions can install or upgrade npm packages, download Node, and change PATH or shell startup files.

Mitigation: Prefer a pre-provisioned qhkit installation and obtain explicit approval before any host setup or upgrade.

Risk: Configuring qhkit requires a Qinghu API token that may be stored on the host.

Mitigation: Obtain approval before credential configuration; handle the token as a secret and avoid displaying it in output.

Risk: Market-data calls consume Qinghu credits, and larger results may cost more.

Mitigation: Estimate charges and confirm the planned paid calls with the user before executing them.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/qinghu-ozon-category-sales)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise sales summary with optional table file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Identifies platform, period, and sample size; paid queries consume Qinghu credits.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
