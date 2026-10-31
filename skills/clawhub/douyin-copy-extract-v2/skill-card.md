## Description:

粘贴抖音公开可访问的视频链接、分享文案或 aweme_id，一键提取视频标题/基础信息、原视频简介、口播逐字稿、可复制文案和精简版；适合内容创作、自媒体运营、短视频脚本整理、抖音文案提取、抖音视频转文字、抖音口播转文字、口播文案整理和逐字稿复盘。已有 job_id 时继续查询任务状态。来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

面向内容创作者和自媒体运营者，用于从公开可访问的抖音视频提取视频信息、简介和口播逐字稿，并整理为可复制文案或精简版。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Video inputs and job IDs are sent to SocialDataX using the configured API key; service credits may be required.

Mitigation: Account for the external processing and possible credit use before submitting a video, and protect SOCIALDATAX_API_KEY.

Risk: The downloaded CLI implementation is outside the bundled artifact reviewed for this release.

Mitigation: Consider pinning a reviewed package version.

Risk: A transcription job may take longer than expected.

Mitigation: Stop polling if a job takes too long.

## Reference(s):

- [SocialDataX API Key and service information](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/douyin-copy-extract-v2)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown with video details, description, transcript, copy-ready and concise text, or task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Only include fields returned by the service; provide the transcript only after a task succeeds.]

## Skill Version(s):

0.1.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
