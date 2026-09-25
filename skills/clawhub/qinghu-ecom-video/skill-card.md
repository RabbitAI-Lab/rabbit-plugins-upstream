## Description:

一键生成电商视频，包括商品展示、带货短视频、品牌宣传片和广告素材，支持 AI 脚本、分镜、多图一键成片，并适配 TikTok、抖音、Amazon、Shopee 等平台。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to route e-commerce video requests into qhkit commands for generated product videos, quick multi-image videos, storyboards, pricing estimates, task polling, and delivery guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can automatically install or upgrade qhkit and related Node tooling and may alter the user's shell environment.

Mitigation: Approve installs manually, prefer pinned known-good package versions, avoid shell profile changes unless needed, and confirm where the qhkit token is stored before using private product media.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-ecom-video)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides qhkit command selection, configuration, estimation, polling, and delivery of generated video URLs.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
