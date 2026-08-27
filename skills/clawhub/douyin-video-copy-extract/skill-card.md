## Description:

用于抖音文案提取、抖音文案一键提取、抖音视频文案提取、抖音视频转文字、抖音口播转文字和抖音逐字稿；用户粘贴抖音视频链接、分享文案或 aweme_id 后，可提取视频上下文、原视频简介和口播逐字稿。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to submit or check Douyin video speech-to-text transcript jobs from a video URL, share text, aweme_id, or job_id. The skill helps return visible video context, the original description, spoken transcript, copy-ready text, a concise version, and task status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A SocialDataX API key is required at runtime.

Mitigation: Provide it through SOCIALDATAX_API_KEY, keep it out of skill files and chat transcripts, and rotate it if exposed.

Risk: The direct CLI may fetch and run the socialdatax-skills package with npx.

Mitigation: Run it only in an environment where Node.js, npm, package installation, and network access are approved.

Risk: Transcript jobs can be asynchronous and may consume credits if duplicate submissions are made.

Mitigation: Keep and reuse the returned job_id for polling, and do not submit a second job while one is pending.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/douyin-video-copy-extract)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown text with transcript sections and inline CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include job_id, current job status, and the next polling command when transcription is not complete.]

## Skill Version(s):

0.1.7 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
