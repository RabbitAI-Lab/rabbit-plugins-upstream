## Description:

该技能帮助代理使用 qhkit 将商品图片背景替换为指定营销场景，并引导安装、配置、积分估算和生成图片交付。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

电商运营人员、设计协作者和代理开发者可用该技能把商品图放入大理石台面、户外、节日等营销场景，并在用户需要多个场景版本时组织重复生成。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup and upgrade flow can make broad local software changes by installing or updating qhkit and Node tooling.

Mitigation: Require explicit user confirmation before installs or upgrades, and prefer a pinned, reviewed @iqinghu/qhkit package version.

Risk: External CLI messages could suggest dynamic upgrade commands.

Mitigation: Do not execute commands copied from CLI output automatically; inspect them and use known package-manager commands only after confirmation.

Risk: The skill requires service credentials for qhkit access.

Mitigation: Use a narrowly scoped token, avoid exposing it in logs or files, and run generation from a limited working directory.

Risk: Generated background replacement can subtly change product details such as text, logos, or structure.

Mitigation: Review generated images before delivery or publication, especially product identifiers and structural details.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-background-swap)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu AI API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON parameter examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides qhkit image generation and returns generated image URLs with actual credit usage when available.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
