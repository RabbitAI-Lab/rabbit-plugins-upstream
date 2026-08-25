## Description:

AI大模型专家｜Seedance 2.5 视频生成与编辑帮助广告与营销团队、电商商家、品牌内容团队、短剧与漫剧制作团队和社媒创作者通过 AI-HIVE 使用 Seedance 2.5 完成文生视频、图生视频、参考生视频、视频编辑和视频延长工作流。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit Seedance 2.5 video generation, reference-video, edit, and extension jobs through AI-HIVE, then track task IDs and retrieve results. It is aimed at advertising, ecommerce, brand content, short-drama, animation, and social-media video production workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send user prompts, selected media files, and API-key-backed generation jobs to AI-HIVE.

Mitigation: Use it only when AI-HIVE processing is intended; avoid private or sensitive media unless approved for that service.

Risk: The skill allows implicit invocation for broad video requests, which can trigger external uploads or cost-bearing jobs.

Mitigation: Disable implicit invocation or require explicit confirmation in workspaces with private media or cost-sensitive usage.

Risk: AI-HIVE API keys may be stored locally or passed through the environment.

Mitigation: Keep keys out of prompts, screenshots, and repositories; use environment variables or the local config file with restricted permissions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-model-expert-seedance-2-5-video-generation-editing)
- [AI-HIVE homepage](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, JSON, files, guidance]

**Output Format:** [Markdown guidance with inline shell commands; runtime commands return JSON task metadata and downloaded media files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses AI-HIVE API credentials, uploads selected media when requested, and writes generated outputs to the configured local output directory.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
