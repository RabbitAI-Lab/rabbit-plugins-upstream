## Description:

用于抖音文案提取、抖音文案一键提取、抖音视频文案提取、抖音视频转文字、抖音口播转文字和抖音逐字稿。用户粘贴抖音视频链接、分享文案或 aweme_id 后，提取视频上下文、原视频简介和口播逐字稿，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use this skill to help users submit or continue bounded Douyin speech-to-text transcript jobs from a Douyin URL, share text, aweme_id, or job_id. It returns visible video context, the original description, transcript text, copy-ready prose, a concise version, and task status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Douyin content submitted for transcription is sent to SocialDataX.

Mitigation: Use the skill only with Douyin content the user intends to send to SocialDataX.

Risk: Duplicate submissions while a transcript job is pending can create redundant work.

Mitigation: Keep the returned job_id and continue polling that same job instead of submitting the same video again.

Risk: The workflow requires a SocialDataX API key in the runtime environment.

Mitigation: Confirm the user is comfortable providing SOCIALDATAX_API_KEY before installing or running the CLI.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/douyin-video-copy-extract)
- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown sections with inline shell commands; transcript job responses may include JSON-like status fields.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SOCIALDATAX_API_KEY and node/npm for the preferred direct CLI workflow.]

## Skill Version(s):

0.1.6 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
