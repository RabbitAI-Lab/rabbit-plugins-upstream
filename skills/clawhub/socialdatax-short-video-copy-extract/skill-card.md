## Description:

接收小红书、抖音、快手、微博或视频号的公开视频链接、内容 ID 或任务 ID，提取视频信息、简介和口播逐字稿，并整理为可复制文案。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

公开视频内容的使用者可提取五个平台视频的基础信息、简介和口播转写，并整理成逐字稿、可复制文案和精简版。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment flags repeated use of a mutable `@latest` CLI as a supply-chain risk.

Mitigation: Use a specifically reviewed CLI version and check its dependencies and package integrity before installation.

Risk: Video links or IDs are sent to SocialDataX for processing.

Mitigation: Before submitting a video, confirm that sharing its link or ID with SocialDataX is appropriate.

Risk: The scanner's verdict is incomplete because some local references could not be resolved.

Mitigation: Review the unresolved references and treat the current security assessment as partial.

## Reference(s):

- [SocialDataX AI and API key information](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-short-video-copy-extract)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration instructions, Files]

**Output Format:** [Markdown transcript and copy-ready text; CLI results are JSON, with optional SRT subtitle output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns video details, description, transcript, and a concise rewrite when available; optional SRT export.]

## Skill Version(s):

0.1.5 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
