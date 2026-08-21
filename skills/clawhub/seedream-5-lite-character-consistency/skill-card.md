## Description:

使用 Seedream 5.0 Lite 和授权角色参考图建立角色连续性圣经和镜头变更单，帮助在多场景、表情、动作、服装和渠道版本中保持身份与品牌边界一致。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Designers, marketers, and developers use this skill to generate character-consistent images for authorized people, mascots, brand IP, illustrated characters, storyboards, stickers, and social media series. The workflow guides users to define a continuity bible, write per-shot change orders, run fixed Seedream 5.0 Lite image-generation commands through AI Hive, and review generated outputs for identity, continuity, and rights issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference images and prompts are sent to AI Hive for generation.

Mitigation: Use only authorized character or person references, avoid sensitive or misleading contexts, and review outputs for rights, endorsement, and brand-boundary issues before use.

Risk: The AI Hive API key may be supplied through the environment, command line, or a local config file.

Mitigation: Protect AI_HIVE_API_KEY and ~/.ai-hive/config.json, keep local config permissions restricted, and rotate the key if it is exposed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/seedream-5-lite-character-consistency)
- [Publisher profile](https://clawhub.ai/user/wubin1836)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API key setup](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, files, guidance]

**Output Format:** [Markdown guidance with bash command examples, JSON configuration, API task JSON, and locally saved image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires at least one user-specified reference image, uses the fixed public_model_seedream_5_0_lite model, uploads selected images to AI Hive, polls generation tasks, and saves successful outputs locally.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
