## Description:

粘贴抖音公开可访问的视频链接、分享文案或 aweme_id，一键提取视频标题/基础信息、原视频简介、口播逐字稿、可复制文案和精简版；适合内容创作、自媒体运营、短视频脚本整理、抖音文案提取、抖音视频转文字、抖音口播转文字、口播文案整理和逐字稿复盘。已有 job_id 时继续查询任务状态。来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

内容创作者和自媒体运营者可提交公开可访问的抖音视频链接、分享文案或内容 ID，获取视频信息、原简介和口播逐字稿，并整理成可复制文案与精简版；已有任务也可继续查询状态。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted video links, share text, and video IDs are sent to SocialDataX for processing.

Mitigation: Use only public video material suitable for submission and exclude sensitive content.

Risk: Transcription requests may incur service charges.

Mitigation: Check applicable service charges or account balance before submitting a task.

Risk: The npm CLI is not bundled or verified by this review.

Mitigation: Review the CLI and use a fixed version before running it.

Risk: An unfinished task can continue polling until completion unless stopped.

Mitigation: Stop polling when the task reaches a terminal state or when the user asks to stop.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/douyin-copy-extract-v2)
- [SocialDataX AI and API key information](https://socialdatax.com/ai?from=clawhub)
- [SocialDataX billing](https://socialdatax.com/dashboard/billing)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Markdown transcript and video details, with structured task status when a job is still running or fails]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Depending on returned data, includes video details, original description, transcript, copy-ready text, concise summary, or job status.]

## Skill Version(s):

0.1.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
