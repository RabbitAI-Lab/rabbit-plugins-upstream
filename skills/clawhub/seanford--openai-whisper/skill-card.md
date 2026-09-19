## Description:

Local speech-to-text with the Whisper CLI (no API key).

This skill is ready for commercial/non-commercial use.

## Publisher:

[seanford](https://clawhub.ai/user/seanford)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and users use this skill to install and run the local Whisper CLI for transcribing or translating audio files without an API key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the skill's dependency adds the local Whisper CLI through Homebrew.

Mitigation: Review the Homebrew install action before installation and confirm the target environment should receive the whisper binary.

Risk: First model use may download model files into the local cache.

Mitigation: Plan for local model storage before first use and allow downloads only in environments where cached model files are acceptable.

Risk: Audio files may contain sensitive content.

Mitigation: Run the CLI only on audio files the user intends to transcribe or translate.

## Reference(s):

- [OpenAI Whisper](https://openai.com/research/whisper)
- [Openai Whisper on ClawHub](https://clawhub.ai/seanford/skills/openai-whisper)
- [seanford publisher profile](https://clawhub.ai/user/seanford)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the local whisper binary; first model use may download model files into a local cache.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
