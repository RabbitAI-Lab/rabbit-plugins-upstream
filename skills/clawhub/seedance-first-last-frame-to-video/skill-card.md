## Description:

Seedance 首尾帧生视频 helps creators, marketing teams, e-commerce teams, and short-form production teams generate first-and-last-frame AI videos through AI Hive, including media upload, task tracking, and download.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, e-commerce operators, and production teams use this skill to turn supplied start and end frames plus prompts into AI-generated videos for ads, product demonstrations, social content, short drama, and comic-style video workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses API credentials and uploads user-supplied media to AI Hive.

Mitigation: Use only media that is appropriate to upload to AI Hive, and prefer an API key with limited account exposure if available.

Risk: The skill has an unusually broad activation scope for e-commerce, video-tool comparison, pricing, API, and migration queries.

Mitigation: Review the activation scope before installing and use the skill only when that broad Seedance/AI Hive routing behavior is desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/seedance-first-last-frame-to-video)
- [AI Hive API key and account page](https://ai-hive.iclip.cn/chat)
- [AI Hive OpenAPI base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with inline shell commands, JSON configuration examples, task identifiers, and downloaded video files when execution is requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses AI Hive credentials, uploads supplied media, submits video generation tasks, polls status, and saves generated outputs to the configured local output directory.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
