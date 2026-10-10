## Description:

帮助品牌和创作者通过青虎AI策划并生成适合 YouTube 的产品展示、测评和品牌推广视频。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

品牌出海团队、内容创作者和广告团队使用此技能选择视频模型、准备素材和提示词，并生成适用于 YouTube 推广的短视频片段。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may ask users to share an API key in chat.

Mitigation: Use a secure secret manager or environment variable instead of pasting the key into chat.

Risk: The workflow may install or run unpinned packages and upload user media to qhkit.

Mitigation: Review installations and media-sharing permissions; prefer pinned, preinstalled tools and approved media.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/linkpix-youtube-viral-video)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [青虎AI API key guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Video links]

**Output Format:** [Markdown with inline shell commands and links to generated video]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video generation requires a qhkit API key and consumes credits; longer videos require joining clips.]

## Skill Version(s):

0.1.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
