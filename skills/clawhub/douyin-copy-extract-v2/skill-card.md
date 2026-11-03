## Description:

粘贴抖音公开可访问的视频链接、分享文案或 aweme_id，一键提取视频标题/基础信息、原视频简介、口播逐字稿、可复制文案和精简版；适合内容创作、自媒体运营、短视频脚本整理、抖音文案提取、抖音视频转文字、抖音口播转文字、口播文案整理和逐字稿复盘。已有 job_id 时继续查询任务状态。来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

内容创作者和自媒体运营者可提交抖音公开视频链接、分享文案或 aweme_id，获取视频基础信息、简介和口播逐字稿，并整理成可复制文案与精简版；也可用已有 job_id 查询任务状态。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted video references or share text are sent to SocialDataX for processing.

Mitigation: Submit public video references and exclude unrelated private information.

Risk: The API key and external CLI or hosted service introduce credential and dependency risks.

Mitigation: Keep the API key in client-managed secret storage and out of chat and version control; prefer a reviewed fixed CLI version with limited permissions.

## Reference(s):

- [SocialDataX service and API key information](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/douyin-copy-extract-v2)

## Skill Output:

**Output Type(s):** [Text, Markdown, Task status guidance]

**Output Format:** [Markdown with video details, description, transcript, copy-ready text, concise summary, and status details when applicable]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses fields returned by the service; pending or failed tasks include status and next-step information.]

## Skill Version(s):

0.1.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
