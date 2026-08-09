## Description:

多参考图生视频工具，根据多张参考图和提示词生成视频，支持 KLING、SEED、SEED_FAST 和 HAPPY_HORSE 模型，并可控制时长、Pro 模式、声音、宽高比和分辨率。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate short videos from one or more reference image URLs plus optional prompt guidance through LinkFox-hosted video generation models. It is suited for multi-image video creation workflows that need asynchronous task creation, polling, and local video-file delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends user-provided image URLs and prompts to LinkFox services for video generation.

Mitigation: Use only image URLs and prompts that are appropriate to share with LinkFox, and avoid submitting confidential or regulated content unless separately approved.

Risk: The bundled onboarding flow can perform SMS login, expose API keys, and create payment orders for credits.

Mitigation: Use onboarding commands only when intentional account setup or credit purchase is needed, and keep returned API keys and payment QR files out of shared logs and workspaces.

Risk: Generated media and raw API responses are stored in local workspace directories.

Mitigation: Review local output locations before sharing the workspace, and share only the final local video paths or files intended for the user.

## Reference(s):

- [多参考图生视频 API 参考](references/api.md)
- [解决认证和积分问题](references/onboarding.md)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-aigc-videogen-multi)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with shell commands and local generated video file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated videos are downloaded to a local media directory; raw API responses are stored locally and temporary signed source URLs should not be shown to users.]

## Skill Version(s):

1.2.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
