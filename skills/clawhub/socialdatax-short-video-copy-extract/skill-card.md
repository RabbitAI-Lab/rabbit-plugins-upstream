## Description:

从公开视频链接、分享文案、内容 ID 或现有任务 ID 提取短视频信息、简介和口播逐字稿，并整理为可复制文案。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

用户可将小红书、抖音、快手、微博或视频号的公开视频链接、分享文案、内容 ID 或已有任务 ID 交给此 Agent，以获取视频信息和口播转写，并整理成可复制文案。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The SocialDataX API key could be exposed or used unexpectedly.

Mitigation: Keep SOCIALDATAX_API_KEY private and provide only intended public-video links.

Risk: Calls may incur SocialDataX service charges, and the external package and publisher identity were not independently verified.

Mitigation: Check service charges and review a fixed CLI package version before use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-short-video-copy-extract)
- [SocialDataX API key and service information](https://socialdatax.com/ai?from=clawhub)
- [SocialDataX billing](https://socialdatax.com/dashboard/billing)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown with video details, transcript, copy-ready text, summary, or task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Transcript output is available only after a successful terminal task; returned video details depend on the source data.]

## Skill Version(s):

0.1.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
