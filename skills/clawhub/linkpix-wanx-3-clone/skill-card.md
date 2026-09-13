## Description:

帮助电商短视频团队通过青虎AI识别电商爆款视频的展示节奏、卖点文案和脚本结构，并生成适配淘宝、天猫及相关内容流量场景的同类型短视频。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce marketers, merchants, and video production teams use this skill to analyze a reference short video, adapt its structure to their own product, and guide generation of a similar ecommerce video through qhkit and LinkPix workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may expose API keys if users paste tokens into chat.

Mitigation: Configure qhkit tokens through local secret storage or environment variables and avoid sharing credentials in conversation.

Risk: Runtime installation of mutable third-party packages can change behavior between runs.

Mitigation: Review the skill before installation, use an isolated environment, and prefer pinned or preinstalled qhkit dependencies.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/linkpix-wanx-3-clone)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides video analysis, script rewriting, task polling, result download, and user confirmation before paid generation.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
