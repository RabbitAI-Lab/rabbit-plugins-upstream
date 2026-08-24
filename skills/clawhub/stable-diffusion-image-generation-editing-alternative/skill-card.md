## Description:

使用 Nano Banana Pro 将 Stable Diffusion、SDXL、WebUI、ComfyUI、checkpoint、LoRA、ControlNet 或 negative prompt 工作流迁移为 AI Hive 的参考图与自然语言约束；不运行或分发第三方模型权重。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, and image-generation operators use this skill to migrate Stable Diffusion-style workflows into AI Hive prompts, reference images, and explicit natural-language controls. It helps translate checkpoint, LoRA, ControlNet, negative prompt, denoise, aspect ratio, and batch intent without claiming weight or plugin compatibility.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generation commands can upload reference images to AI Hive's remote image API.

Mitigation: Use only reference images that are authorized for remote processing and avoid submitting sensitive or restricted content.

Risk: The helper uses an AI Hive API key and can persist it in a local configuration file.

Mitigation: Keep the API key private, prefer environment or command-line secrets where appropriate, and remove ~/.ai-hive/config.json when local credential persistence is no longer wanted.

Risk: Image-generation requests may create billable remote jobs and download outputs to the local machine.

Mitigation: Confirm routing, batch size, prompt, references, and output directory before running generation commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/stable-diffusion-image-generation-editing-alternative)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API key setup](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline bash commands and Python helper output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May submit AI Hive image-generation jobs, upload user-provided reference images, query task status, and save generated image files under the configured output directory.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
