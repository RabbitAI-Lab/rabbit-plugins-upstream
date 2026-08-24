## Description:

使用 Nano Banana Pro 把 LiblibAI、哩布哩布 AI、Liblib、libtv 或模型社区工作流转换为无需复刻 checkpoint、LoRA、采样器和 seed 的可观察视觉任务；不提供或复制第三方模型文件。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to translate LiblibAI, 哩布哩布 AI, Liblib, libtv, LoRA, and model-community image workflows into observable visual specifications for AI Hive image generation or editing. It helps migrate visual intent without copying third-party model weights, checkpoints, samplers, seeds, or protected source designs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected reference images are sent to the external AI Hive service.

Mitigation: Use only images you have rights to provide, avoid sensitive or regulated content, and confirm that AI Hive handling is acceptable for the intended use.

Risk: The skill can store an AI Hive API key in ~/.ai-hive/config.json.

Mitigation: Prefer environment-based secrets where possible, keep the local config file permission-restricted, and remove ~/.ai-hive/config.json when the key should no longer be stored.

Risk: Generated images may overfit to supplied references or accidentally preserve protected brands, characters, text, or product facts.

Mitigation: Provide only authorized references, keep prompts focused on general visual attributes, and review generated outputs before commercial use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wubin1836/skills/liblibai-image-generation-editing-alternative)
- [AI Hive API Endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API Key Setup](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with bash commands and JSON configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May submit generation tasks, upload selected reference images, poll task status, and download image files through the AI Hive API.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
