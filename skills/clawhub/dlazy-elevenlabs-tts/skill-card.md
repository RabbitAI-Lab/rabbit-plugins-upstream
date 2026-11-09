## Description:

ElevenLabs eleven_v3 text-to-speech with 12 curated multilingual voices and stability, similarity, and style controls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content creators use this skill to turn text into multilingual speech for dubbing, audiobooks, and character dialogue, with controls for voice and delivery style.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan found login and authentication commands that are not clearly connected to the stated text-to-speech purpose; coverage is partial and the scan could not establish the CLI's internal behavior.

Mitigation: Before installation, review whether the dlazy login and dlazy auth set flows match the intended use, and configure credentials only if they do.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-tts)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)
- [CLI repository listed in skill metadata (import provenance unavailable)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Audio, JSON metadata]

**Output Format:** [Generated audio asset URL or downloaded audio file, with JSON task and result metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Voice selection and stability, similarity, and style controls; asynchronous task identifiers may be returned when requested.]

## Skill Version(s):

1.3.39 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
