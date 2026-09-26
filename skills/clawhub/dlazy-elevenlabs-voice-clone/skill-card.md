## Description:

Uploads a clean voice sample through dLazy's ElevenLabs Instant Voice Cloning wrapper to create a custom voice for ElevenLabs TTS.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to authenticate with the dLazy CLI and call ElevenLabs Instant Voice Cloning with an audio URL or local audio path. It supports creating a reusable custom voice for ElevenLabs TTS workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uploads voice samples and uses a locally stored or environment-provided dLazy API key.

Mitigation: Use only voice samples the user is authorized to process, rotate or revoke API keys from the dLazy dashboard when needed, and avoid sharing local config files.

Risk: The artifact contains conflicting copied examples for prompt, image, and voice-cloning behavior, making required inputs and returned outputs unclear.

Mitigation: Review the CLI help for `dlazy elevenlabs-voice-clone` before use and confirm that `--audio_url`, `--name`, and returned voice identifiers match the intended workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-voice-clone)
- [dLazy CLI project page](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, JSON, guidance]

**Output Format:** [Markdown instructions with bash commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; local audio inputs may be uploaded to dLazy-hosted storage; asynchronous runs can return a generateId for polling.]

## Skill Version(s):

1.3.19 (source: server release metadata; artifact frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
