## Description:

使用 Nano Banana Pro 将 Midjourney、MJ、/imagine、风格参考和图片提示工作流迁移到 AI Hive，把参数化提示词转换为可观察的构图、风格、参考图职责和商业验收标准，且不访问 Discord 或 Midjourney 账号。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External users, creators, and developers use this skill to migrate Midjourney-style /imagine and image-reference workflows to AI Hive Nano Banana Pro. It guides prompt reconstruction, reference-image role assignment, candidate calibration, API-key setup, task polling, and result download.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can upload user-selected image references and send prompts to AI Hive.

Mitigation: Use only authorized reference images and avoid sending sensitive or confidential prompt content unless AI Hive is approved for that data.

Risk: Image generation can consume AI Hive API credits and download results to local storage.

Mitigation: Review batch size, routing mode, output directory, and task status before running generation commands.

Risk: The setup flow can open a browser and store an API key locally in ~/.ai-hive/config.json.

Mitigation: Prefer environment variables where appropriate, keep the local config file permission-restricted, and rotate keys if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/midjourney-image-generation-editing-alternative)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API key setup](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON, Files]

**Output Format:** [Markdown guidance with bash commands; the helper script can return JSON task status and download generated image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the fixed public_model_nano_banana_pro model, accepts prompt text, optional reference images, batch size, routing mode, model parameters, output directory, and task id.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
