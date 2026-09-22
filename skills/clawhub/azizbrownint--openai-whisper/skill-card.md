## Description:

Local speech-to-text with the Whisper CLI (no API key).

This skill is ready for commercial/non-commercial use.

## Publisher:

[azizbrownint](https://clawhub.ai/user/azizbrownint)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to run local audio transcription or translation with the Whisper CLI, including selecting output formats and model sizes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs local transcription and writes output files for user-provided audio.

Mitigation: Only process audio files the user is comfortable handling locally and writing outputs for.

Risk: Whisper model files are downloaded and cached under the user's home directory on first use.

Mitigation: Plan for first-run model downloads and review local cache/storage expectations before use.

## Reference(s):

- [OpenAI Whisper](https://openai.com/research/whisper)
- [ClawHub skill page](https://clawhub.ai/azizbrownint/skills/openai-whisper)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance covers local Whisper CLI usage, Homebrew installation metadata, model cache behavior, and output format selection.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
