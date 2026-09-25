## Description:

Local speech-to-text with the Whisper CLI (no API key).

This skill is ready for commercial/non-commercial use.

## Publisher:

[czubi1928](https://clawhub.ai/user/czubi1928)

### License/Terms of Use:


## Use Case:

Developers and agent users use this skill to generate local Whisper CLI commands and guidance for transcribing or translating audio files without requiring an API key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation uses Homebrew to install the Whisper CLI, and Whisper may download model files to a local cache on first use.

Mitigation: Review the install command and confirm local cache and storage expectations before running transcription commands.

Risk: Audio paths and generated transcript or subtitle outputs may include sensitive local content.

Mitigation: Review input audio paths and output directories before executing commands, and store generated files only in approved locations.

## Reference(s):

- [OpenAI Whisper research page](https://openai.com/research/whisper)
- [ClawHub skill listing](https://clawhub.ai/czubi1928/skills/openai-whisper-1-0-0)
- [ClawHub publisher profile](https://clawhub.ai/user/czubi1928)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands assume the openai-whisper CLI is installed and available as whisper.]

## Skill Version(s):

1.0.0 (source: artifact/_meta.json and evidence.json release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
