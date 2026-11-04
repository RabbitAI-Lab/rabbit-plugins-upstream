## Description:

从小红书、抖音、快手、微博和视频号的公开视频链接、分享文案、内容 ID 或已有任务 ID 中提取视频信息、简介和口播逐字稿。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

面向需要整理公开视频内容的用户，用于获取视频基础信息、原简介和口播逐字稿，并生成便于复制的文案及精简版。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted video inputs are processed by SocialDataX, and requests may use paid credits.

Mitigation: Use public-video inputs, remove unrelated personal information and sensitive URL parameters, and check account costs.

Risk: The downloaded package behavior and hosted-service data handling have not been verified.

Mitigation: Prefer a reviewed, fixed CLI version and check the provider's data-handling terms before submitting sensitive material.

Risk: An API key is required for direct CLI use.

Mitigation: Keep the key in supported secret storage and never include it in chat, logs, screenshots, or skill files.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/devinchen2014/skills/socialdatax-short-video-copy-extract)
- [SocialDataX skill and API information](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with video details, transcript, copy-ready text, summary, or task status as available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses only information returned for the video or transcription task; unavailable fields are identified rather than filled in.]

## Skill Version(s):

0.1.3 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
