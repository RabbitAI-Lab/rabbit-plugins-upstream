## Description:

一键生成电商视频：商品展示视频、带货短视频、品牌宣传片、广告素材，支持 AI 脚本、分镜、多图一键成片，适配 TikTok、抖音、Amazon、Shopee 等平台。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to route e-commerce video requests to LinkPix/qhkit commands for product videos, short promotional clips, brand assets, scripts, storyboards, and multi-image video generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can ask users to provide API keys in chat.

Mitigation: Configure credentials locally through a secure path and avoid pasting API keys into chat.

Risk: The skill can install or upgrade global Node tooling.

Mitigation: Review and confirm global npm installs, Node installation, and upgrades before execution.

Risk: The skill can upload media and start paid video-generation actions.

Mitigation: Confirm uploads, model choices, durations, and estimated cost before running generation commands.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/autoagc/skills/linkpix-ecom-video)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu Console](https://www.iqinghu.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide media uploads, paid generation requests, task status polling, and credential configuration.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
