## Description:

粘贴抖音公开可访问的视频链接、分享文案或 aweme_id，一键提取视频标题/基础信息、原视频简介、口播逐字稿、可复制文案和精简版；适合内容创作、自媒体运营、短视频脚本整理、抖音文案提取、抖音视频转文字、抖音口播转文字、口播文案整理和逐字稿复盘。已有 job_id 时继续查询任务状态。来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

内容创作者和自媒体运营者可使用此 skill 处理用户提供的抖音公开视频链接、分享文案、aweme_id 或已有任务 ID，获取视频基础信息、简介与口播逐字稿，并整理为可复制文案和精简版。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: SocialDataX receives the submitted video link or ID and uses the service key; processing may consume credits.

Mitigation: Run only for explicitly requested public videos, keep SOCIALDATAX_API_KEY in the environment and separate from unrelated credentials, and consider expected credit use.

Risk: Long-running jobs can lead to excessive polling.

Mitigation: Set a polling time limit and continue checking only the same returned job ID.

Risk: Unreviewed or changing CLI dependencies can create avoidable execution risk.

Mitigation: Prefer a reviewed, pinned CLI version.

## Reference(s):

- [SocialDataX API Key and service page](https://socialdatax.com/ai?from=clawhub)
- [ClawHub release page](https://clawhub.ai/devinchen2014/skills/douyin-copy-extract-v2)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured JSON results organized as Markdown with video details, original description, transcript, copy-ready text, concise summary, or task status.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Deliver a transcript only after the task is terminal and successful; otherwise provide status and continue with the same job ID.]

## Skill Version(s):

0.1.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
