## Description:

用于抖音文案提取、抖音文案一键提取、抖音视频文案提取、抖音视频转文字、抖音口播转文字和抖音逐字稿。用户粘贴抖音视频链接、分享文案或 aweme_id 后，提取视频上下文、原视频简介和口播逐字稿，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

面向希望整理抖音视频内容的用户或智能体：提交抖音视频链接、分享文案或 aweme_id，以获取视频上下文、原视频简介和口播逐字稿。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected video links or share text are processed by SocialDataX, and service-credit charges may apply.

Mitigation: Submit only content the user intends to process and check service-credit costs before starting a job.

Risk: The CLI uses an API key and third-party dependencies at runtime.

Mitigation: Prefer a reviewed, fixed CLI version and restrict the API key's access to the necessary service and local resources.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/devinchen2014/skills/douyin-video-copy-extract)
- [SocialDataX](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Structured text with video details, description, transcript, copy-ready text, concise version, and job status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [If a transcript job is still running, the response includes its job ID, current status, and a continuation command.]

## Skill Version(s):

0.1.9 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
