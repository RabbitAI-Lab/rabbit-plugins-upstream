## Description:

用于抖音文案提取、抖音文案一键提取、抖音视频文案提取、抖音视频转文字、抖音口播转文字和抖音逐字稿。用户粘贴抖音视频链接、分享文案或 aweme_id 后，提取视频上下文、原视频简介和口播逐字稿，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

People who need a Douyin video's description and spoken content transcribed can submit a video link, share text, or aweme_id, then retrieve the transcript or check an existing transcription job.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI package is changeable and installs automatically, creating a supply-chain and credential exposure risk.

Mitigation: Review the package and its version before running it; use only the official SocialDataX access page, and keep API credentials in the private local credential store or a protected environment variable rather than in chat, logs, or project files.

Risk: The available security analysis is incomplete because it scanned one Markdown file and could not resolve several local references.

Mitigation: Resolve and review the referenced package behavior and dependencies, then complete a security review before deployment.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/douyin-video-copy-extract)
- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Files]

**Output Format:** [Structured Markdown transcript and job status; optional UTF-8 SRT subtitle file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Transcript results depend on the submitted video and job status. SRT export requires valid time segments and writes to a new user-selected file.]

## Skill Version(s):

0.1.13 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
