## Description:

Audio generation skill. Automatically selects the best dlazy CLI audio/TTS model based on the prompt. 音频生成技能。根据提示词自动选择最佳的 dlazy CLI 音频/TTS 模型。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to select a suitable dLazy audio model and generate speech, dialogue, music, or sound effects from prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release review noted media-related capabilities beyond the stated audio focus and could not resolve some referenced resources.

Mitigation: Review the media-related examples and referenced resources, and confirm those capabilities are expected before installing.

Risk: Prompts and local media passed to the CLI are sent to dLazy's hosted API or media storage.

Mitigation: Only provide prompts and media that are appropriate to send to the service.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-audio-generate)
- [dLazy CLI project (metadata homepage)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Audio, JSON]

**Output Format:** [Generated audio with a JSON response containing output details or voice-search results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Audio outputs may be hosted URLs; available voices, models, and output details depend on the selected model.]

## Skill Version(s):

1.3.46 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
