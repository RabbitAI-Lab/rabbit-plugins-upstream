## Description:

Guides creators and marketers through generating Xiaohongshu product-promotion videos with Qinghu AI and LinkPix.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Xiaohongshu creators, buyers, and marketers use this skill to plan and generate product showcases, unboxings, and short promotional videos from prompts and reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to share an API key in chat.

Mitigation: Configure the key in a secret manager or directly in the user's terminal; never paste it into chat.

Risk: Automatic installation or upgrades of unpinned packages can change local software and PATH settings.

Mitigation: Review installs and PATH changes before execution and prefer pinned package versions.

Risk: Reference media is uploaded to Qinghu/LinkPix services for video generation.

Mitigation: Upload only media the user is authorized and comfortable sharing with those services.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/linkpix-xiaohongshu-viral-video)
- [qhkit package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Text]

**Output Format:** [Markdown with command examples and video links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include model options, estimated and actual credits, task ID, and generated video URL.]

## Skill Version(s):

0.1.3 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
