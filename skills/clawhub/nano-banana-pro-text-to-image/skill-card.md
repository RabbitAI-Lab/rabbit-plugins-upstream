## Description:

使用 Nano Banana Pro 从纯文字建立高完成度视觉方向，以主体、空间、光线、色彩、材质、镜头和构图动作控制商业图片与创意作品。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, and creative teams use this skill to turn text-only art direction into Nano Banana Pro image-generation prompts and command examples for portraits, product still life, architecture concepts, fashion editorials, and campaign series. It uses AI Hive to submit prompts, poll generation tasks, and download generated outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts are sent to AI Hive for image generation.

Mitigation: Avoid submitting private, sensitive, or regulated content unless the user trusts AI Hive for that data.

Risk: The init flow stores an AI Hive API key locally.

Mitigation: Use a dedicated API key where possible and keep the local configuration file restricted to the current user.

Risk: Generated images are downloaded to a local output directory.

Mitigation: Review the configured output directory and generated files before sharing or reusing them.

Risk: Synthetic images involving real people or news-like scenes can be mistaken for documentary evidence.

Mitigation: Label generated images appropriately and do not present them as factual records.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/nano-banana-pro-text-to-image)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API key setup](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with inline bash commands; generated tasks can return JSON status and downloaded image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an AI Hive API key; generated files are downloaded to a local output directory unless downloads are disabled.]

## Skill Version(s):

1.0.1 (source: server release metadata and CHANGELOG.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
