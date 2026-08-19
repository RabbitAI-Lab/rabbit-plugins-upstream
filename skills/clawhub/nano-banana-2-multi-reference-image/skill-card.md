## Description:

使用 Nano Banana 2 和 AI Hive 将两张或更多授权参考图按身份、结构、服装、材质、构图、色板和风格分工，生成来源清晰、冲突可控的新图片。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, and content teams use this skill to create multi-reference Nano Banana 2 image-generation prompts and commands where each authorized source image has a clear role and conflict priority. It supports product visuals, character consistency, scene composition, materials, palettes, and style references while keeping source responsibilities explicit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference images and prompts selected by the user are sent to AI Hive for image generation.

Mitigation: Use only inputs that are appropriate to share with AI Hive, and avoid confidential or sensitive reference images unless that transfer is approved.

Risk: The skill can store an AI Hive API key in a local configuration file.

Mitigation: Keep the API key file private, rely on the script's restrictive file permissions, and rotate the key if it may have been exposed.

Risk: Generated images may involve people, brands, products, or artwork whose use requires authorization.

Mitigation: Use authorized reference material, preserve the skill's reference-role table, and review rights before publishing or using generated outputs commercially.

Risk: Multi-reference generation can create misleading composites or imply false endorsement, events, tests, or product capabilities.

Mitigation: Follow the skill's stated boundary against fabricating official collaborations, news scenes, detection results, or functional claims, and review outputs before release.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/nano-banana-2-multi-reference-image)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API key setup](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API Calls, Files]

**Output Format:** [Markdown guidance with bash commands and JSON configuration; runtime outputs downloaded image files or task JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires at least two reference images and an AI Hive API key; generated image files are downloaded locally unless no-download mode is used.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
