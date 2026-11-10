## Description:

为商品口播种草视频编写脚本和分镜，并生成带有日常自拍质感的 UGC 视频。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

电商营销人员和内容创作者可用它为商品设计口播脚本、交替呈现人物与商品特写的分镜，并制作适合社交平台的 UGC 风格视频素材。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release scan is rated benign with medium confidence, but coverage is partial and some components were not fully inspected.

Mitigation: Review the skill and its permissions before installation, especially any components or tool access not covered by the scan.

Risk: The security guidance notes undeclared tool scope and calls to external generation providers, which may receive prompts or supplied images.

Mitigation: Check the requested permissions and each provider's data handling before use; send only content approved for that provider.

Risk: The security guidance notes an unpinned package reference.

Mitigation: Review the package source and pin an approved version before relying on it in a production workflow.

Risk: Generated testimonial-style content could be mistaken for a real customer's endorsement.

Mitigation: Present scenarios as AI-generated demonstrations, do not invent real buyer identities or reviews, substantiate product claims, and follow the destination platform's disclosure rules.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/ugc-testimonial)
- [Video backend configuration](references/video-backends.md)
- [Provider CLI reference](references/provider-cli.md)
- [Brand kit model reference guidance](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/brand-kit/skill.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Video files, Subtitle files, Shell commands]

**Output Format:** [Markdown guidance, spoken scripts, JSON storyboards, generated video files, and SRT subtitles]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Storyboard length, shot selection, captions, and video output depend on the product brief and configured video model.]

## Skill Version(s):

1.0.27 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
