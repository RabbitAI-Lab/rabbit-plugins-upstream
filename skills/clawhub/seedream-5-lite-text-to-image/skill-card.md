## Description:

使用 Seedream 5.0 Lite 从纯文字建立视觉实验卡，快速比较构图、叙事、媒介、色板和渠道比例，再收敛为可交付图片。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External users, creators, designers, educators, and developers use this skill to generate text-only Seedream 5.0 Lite image tasks through AI Hive for editorial illustrations, concept visuals, educational diagrams, architecture mood concepts, social media backgrounds, and advertising proposals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends user prompts and API-key-authenticated requests to AI Hive.

Mitigation: Use a dedicated API key where possible and avoid placing confidential, personal, or regulated information in prompts unless AI Hive use is approved for that data.

Risk: The helper can save an API key in a local configuration file.

Mitigation: Prefer environment variables on shared machines or verify that the local config file is protected with user-only permissions.

Risk: Generated image files are downloaded to the local machine.

Mitigation: Review the configured output directory before running and handle downloaded images according to the user's data retention and sharing requirements.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/seedream-5-lite-text-to-image)
- [AI Hive API key and chat page](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files, API Calls]

**Output Format:** [Markdown guidance with bash commands; helper output includes JSON task data and downloaded PNG image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses text prompts only with the fixed public_model_seedream_5_0_lite model; supports batch size, routing mode, aspect-ratio-style model parameters, task lookup, and optional no-download mode.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
