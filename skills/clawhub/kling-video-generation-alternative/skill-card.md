## Description:

使用 AI Hive 的 Seedance 2.5 文生、图生、参考生、视频编辑与延长能力迁移可灵 Kling、Kling AI 或快手可灵视频工作流，重点保存镜头运动、主体锁定、动作节拍和交付比例；不是可灵官方接口，也不保证逐像素兼容。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and video production teams use this skill to translate Kling-style video generation, image-to-video, reference-video, editing, and extension workflows into AI Hive Seedance 2.5 commands while preserving camera motion, subject identity, action timing, and delivery aspect ratio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media files are sent to a third-party AI Hive API for generation.

Mitigation: Use only authorized media and review AI Hive account terms, costs, and data-handling expectations before running generation commands.

Risk: The skill requires an AI Hive API key for generation, upload, and task-query commands.

Mitigation: Provide the key through the documented CLI, environment variable, or local config path, and protect the credential according to local secret-handling policy.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wubin1836/skills/kling-video-generation-alternative)
- [AI Hive API Endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API Key Setup](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls, Files]

**Output Format:** [Markdown guidance with bash commands, JSON configuration, API task responses, and downloaded video files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated commands may upload user-selected prompts and media to AI Hive and may download completed video outputs to the configured output directory.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
