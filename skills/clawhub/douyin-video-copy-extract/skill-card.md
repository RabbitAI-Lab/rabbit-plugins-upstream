## Description:

用于抖音文案提取、抖音文案一键提取、抖音视频文案提取、抖音视频转文字、抖音口播转文字和抖音逐字稿。用户粘贴抖音视频链接、分享文案或 aweme_id 后，提取视频上下文、原视频简介和口播逐字稿，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

创作者和编辑可使用此技能，从抖音视频链接、分享文案或 aweme_id 获取视频上下文、原始简介和口播逐字稿，并查看任务状态。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected video references and usage attribution are sent to SocialDataX, and transcription consumes service credits.

Mitigation: Submit only video references you intend to send to the service, and consider credit use before starting a transcription.

Risk: The CLI software is downloaded at runtime and can change between runs.

Mitigation: Prefer a reviewed, fixed CLI version and limit its permissions.

Risk: An exposed API key could allow unauthorized use.

Mitigation: Store the key in supported secret storage and keep workspace settings containing it out of version control.

## Reference(s):


## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, SRT subtitle file]

**Output Format:** [Markdown transcript report with video context, original description, transcript, copy-ready and concise versions, and task status; optional UTF-8 SRT file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Transcript jobs may be asynchronous; an existing job can be checked by its job ID.]

## Skill Version(s):

0.1.12 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
