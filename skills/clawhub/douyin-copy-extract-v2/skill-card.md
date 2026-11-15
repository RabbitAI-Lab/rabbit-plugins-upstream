## Description:

粘贴抖音公开可访问的视频链接、分享文案或 aweme_id，一键提取视频标题/基础信息、原视频简介、口播逐字稿、可复制文案和精简版；适合内容创作、自媒体运营、短视频脚本整理、抖音文案提取、抖音视频转文字、抖音口播转文字、口播文案整理和逐字稿复盘。已有 job_id 时继续查询任务状态。来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators and social media operators can submit a publicly accessible Douyin video link, share text, aweme_id, or an existing job_id to retrieve video details, its description, a speech transcript, reusable copy, and a concise summary, or to check an existing task.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI is invoked through an unpinned @latest package, so the credential and request handling code can change between runs and has not been reviewed by the scanner.

Mitigation: Review and pin a specific CLI release before entering credentials or running requests; do not provide an API key until that release is trusted.

Risk: Video information supplied to the skill may be sent to SocialDataX for processing.

Mitigation: Submit only video links or information that you are comfortable sharing with SocialDataX.

Risk: The security analysis is incomplete because some local references could not be resolved.

Mitigation: Treat the scan as incomplete and review the unresolved references and CLI package before use.

## Reference(s):

- [SocialDataX AI](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/douyin-copy-extract-v2)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Service JSON summarized as Markdown with available video details, source description, transcript, reusable copy, concise summary, or task status and next steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports only fields returned by the service; transcript output is provided only after a successful terminal task.]

## Skill Version(s):

0.1.5 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
