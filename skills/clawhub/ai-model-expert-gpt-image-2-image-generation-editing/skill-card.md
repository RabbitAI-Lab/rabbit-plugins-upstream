## Description:

AI大模型专家｜GPT Image 2 图片生成与编辑 helps brand design, ecommerce, advertising, content, cross-border listing, and social media teams generate and edit commercial images through AI-HIVE using text prompts and reference media.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External commercial creative teams and developers use this skill to create product, advertising, ecommerce, and social media image assets with GPT Image 2 through AI-HIVE. The skill guides API-key setup, model and pricing checks, task submission, polling, and result download.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires an AI-HIVE API key that may be stored locally or supplied through the environment.

Mitigation: Store keys only in the documented local config or environment, keep local config permissions restricted, and never commit keys or include them in chats, screenshots, or public repositories.

Risk: Prompts and selected media files are uploaded to AI-HIVE for image generation or editing.

Mitigation: Upload only media the user is authorized to use, and avoid private, regulated, or unlicensed content unless the user explicitly intends it to be sent to AI-HIVE.

Risk: Batch or high-volume generation can create unexpected cost.

Mitigation: Review the runtime pricing snapshot, route, model settings, and batch size before submission, and get user confirmation for high-cost work.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wubin1836/skills/ai-model-expert-gpt-image-2-image-generation-editing)
- [AI-HIVE Homepage](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API Base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, API calls, Files]

**Output Format:** [Markdown with inline bash commands, task identifiers, JSON-like API responses, and downloaded image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated assets are downloaded to a local output directory when download is enabled; task IDs are preserved for later polling.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
