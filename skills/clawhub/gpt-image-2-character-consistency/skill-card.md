## Description:

使用 GPT Image 2 建立角色设定并在不同姿势、表情、服装、镜头和场景中保持身份一致；通过 AI Hive 上传角色参考并生成角色三视图、表情表、绘本角色、短剧人物、漫画分镜、品牌 IP、虚拟人和连续图片。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, and creative teams use this skill to create character-consistent GPT Image 2 image generations from one or more reference images. It helps define identity anchors, generate baseline views and expression sheets, and keep visual identity stable across scenes, outfits, and sequential panels.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires an AI Hive API key and may store it in ~/.ai-hive/config.json.

Mitigation: Use command-line or environment-variable credentials when preferred, review the local config file after initialization, and rotate or remove the key when access is no longer needed.

Risk: Selected reference images and prompts are uploaded to AI Hive for generation.

Mitigation: Use explicit --image paths, avoid uploading sensitive media unless that use is acceptable, and review prompts and references before submitting a generation task.

Risk: Generated files are saved locally by default.

Mitigation: Set --output-dir to a controlled location or use --no-download when only task submission is needed, then review downloaded outputs before reuse.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/gpt-image-2-character-consistency)
- [AI Hive API base URL](https://ai-hive.iclip.cn/api)
- [AI Hive API key setup](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API Calls, Files]

**Output Format:** [Markdown guidance with bash command examples; generated image files are downloaded locally by the helper script.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses AI Hive credentials, uploads selected reference media, submits GPT Image 2 image-generation tasks, and saves generated outputs locally unless no-download mode is selected.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
