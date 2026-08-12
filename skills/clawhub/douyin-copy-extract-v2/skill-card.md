## Description:

粘贴抖音公开可访问的视频链接、分享文案、aweme_id 或已有 job_id，提取或查询视频标题/基础信息、原视频简介、口播逐字稿、可复制文案和精简版，适合内容创作、自媒体运营、短视频脚本整理、抖音文案提取、抖音视频转文字、抖音口播转文字、口播文案整理和逐字稿复盘。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, operators, and agent users use this skill to submit public Douyin video links, share text, aweme_id values, or existing job_id values and receive video metadata, descriptions, speech transcripts, copy-ready text, summaries, or task status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Douyin links, share text, aweme_id values, job_id values, and resulting transcript data are sent to SocialDataX for processing.

Mitigation: Use only public, authorized content and avoid submitting private, sensitive, or regulated material.

Risk: Using the npm package without a pinned version can reduce reproducibility.

Mitigation: Pin the socialdatax-skills package version when reproducible installs are required.

Risk: Polling an unfinished transcription task incorrectly can resubmit the same video instead of checking the existing job.

Mitigation: After a job_id is returned, query that same job_id until the task reaches a terminal status.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/devinchen2014/skills/douyin-copy-extract-v2)
- [SocialDataX AI](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and structured task result fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Successful results may include video metadata, original description, transcript text, copy-ready text, a concise summary, and visible job status or error details.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
