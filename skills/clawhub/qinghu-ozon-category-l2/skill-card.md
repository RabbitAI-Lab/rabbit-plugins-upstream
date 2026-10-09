## Description:

按一级类目 ID 查询 Ozon 公共二级类目，并整理类目名称和 ID。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Ozon sellers and analysts use this skill to look up public second-level categories and their IDs under a specified first-level category.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill directs installation or upgrades of Node and qhkit, which can change the local environment.

Mitigation: Review before installing; install dependencies yourself and pin package versions where possible.

Risk: The skill requires a Qinghu API token and can make paid tool calls.

Mitigation: Configure the token deliberately and approve paid calls and expected credit usage before execution.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/qinghu-ozon-category-l2)
- [qhkit package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown table or concise text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Category names and IDs; reports credits used for paid calls.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
