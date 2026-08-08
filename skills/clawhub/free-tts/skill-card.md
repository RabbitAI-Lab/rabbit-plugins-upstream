## Description:

free-tts helps an agent generate text-to-speech output and voice-cloning workflows through Fish Audio and Xiaomi MiMo, including setup, engine selection, voice management, and audio generation commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[darker314159](https://clawhub.ai/user/darker314159)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and end users use this skill when they need an agent to set up API keys, choose between Fish Audio and Xiaomi MiMo, synthesize speech, clone voices with consent, or manage reusable Fish voice IDs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Synthesis text and selected voice samples are sent to third-party TTS services.

Mitigation: Use the skill only when users are comfortable sharing that content with Fish Audio or Xiaomi MiMo.

Risk: Voice cloning can misuse a speaker's identity or capture sensitive recordings.

Mitigation: Clone voices only with the speaker's consent and avoid sensitive or regulated recordings on free tiers.

Risk: API keys and Fish voice IDs or models may persist after setup or cloning.

Mitigation: Store keys only in environment variables, rotate exposed keys, and remove Fish voice models or cached IDs when they are no longer needed.

## Reference(s):

- [Fish Audio API reference](references/fish-api.md)
- [Xiaomi MiMo TTS API reference](references/mimo-api.md)
- [Fish Audio documentation](https://docs.fish.audio)
- [Fish Audio s2.1 Pro Free API announcement](https://fish.audio/zh-CN/blog/s2-1-pro-free-api/)
- [Fish Audio OpenAPI schema](https://api.fish.audio/openapi.json)
- [Xiaomi MiMo speech synthesis V2.5 documentation](https://mimo.mi.com/docs/zh-CN/quick-start/usage-guide/audio/speech-synthesis-v2.5)
- [ClawHub skill page](https://clawhub.ai/darker314159/skills/free-tts)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files, JSON]

**Output Format:** [Markdown guidance with shell commands; helper scripts can emit audio files and JSON voice metadata.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local environment variables for Fish Audio and Xiaomi MiMo API keys; generated audio is written to user-selected output paths.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
