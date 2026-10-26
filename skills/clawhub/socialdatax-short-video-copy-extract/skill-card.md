## Description:

面向短视频文案提取、短视频文案一键提取、视频文案提取、视频链接转文案、短视频转文字、视频转文字、口播转文字、视频逐字稿和逐字稿整理。用户粘贴小红书、抖音、快手、微博和视频号公开视频链接、分享文案、内容 ID 或已有 job_id 后，获取视频基础信息、原视频简介、口播逐字稿、可复制文案和精简版，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents can submit public short-video links, share text, content IDs, or existing job IDs to retrieve video details, descriptions, and speech transcripts for transcript review and copy-ready text preparation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Video processing uses the configured SocialDataX API key and may consume service credits.

Mitigation: Keep the API key private and submit only videos within the user's intended scope.

Risk: An unpinned CLI package may change between releases.

Mitigation: Prefer a reviewed fixed CLI version when relying on repeatable behavior.

Risk: Polling an unfinished task may continue longer than intended.

Mitigation: Set a practical polling time limit and continue querying only the existing job ID.

## Reference(s):

- [SocialDataX AI service](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-short-video-copy-extract)
- [Publisher profile](https://clawhub.ai/user/devinchen2014)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Structured video details, source description, transcript, copy-ready text, and a concise version; task status and errors when processing is incomplete or unsuccessful.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Only report fields present in returned results; provide a transcript only after a successful terminal result.]

## Skill Version(s):

0.1.1 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
