## Description:

用于抖音文案提取、抖音文案一键提取、抖音视频文案提取、抖音视频转文字、抖音口播转文字和抖音逐字稿。用户粘贴抖音视频链接、分享文案或 aweme_id 后，提取视频上下文、原视频简介和口播逐字稿，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and analysts use this skill to submit a Douyin video URL, share text, or aweme_id and receive video context, the original description, and a speech transcript.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected video references are processed by SocialDataX and may consume paid credits.

Mitigation: Submit only references you intend to process and check applicable credit costs before use.

Risk: An exposed API key could be used by others.

Mitigation: Store the key in supported secret storage and keep it out of chat, logs, and version control.

Risk: The downloaded CLI and hosted service are outside the scope of the supplied-instructions review.

Mitigation: Use a reviewed, fixed CLI version with limited local permissions.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with video context, the original description, transcript, copy-ready and concise versions, and job status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [For unfinished jobs, includes the job ID, current status, and a continuation command; transcript content is limited to results visible from the service.]

## Skill Version(s):

0.1.11 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
