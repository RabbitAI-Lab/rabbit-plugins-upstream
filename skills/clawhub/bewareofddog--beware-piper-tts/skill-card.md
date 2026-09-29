## Description:

Piper TTS generates local text-to-speech audio with Piper and returns MP3 voice-message paths for supported delivery channels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bewareofddog](https://clawhub.ai/user/bewareofddog)

### License/Terms of Use:


## Use Case:

Developers and agent operators use this skill to generate on-demand local voice messages from text for Telegram, Discord, or other channels that support audio delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup script can modify the local Python environment and install ffmpeg through Homebrew or sudo apt without confirmation prompts.

Mitigation: Review the exact setup commands before installation, avoid elevated privileges unless necessary, and add confirmation prompts for environment or system package changes.

Risk: The setup script downloads unpinned packages and voice model files.

Mitigation: Pin package versions and voice model URLs or hashes before deployment in managed environments.

Risk: Voice-name handling and temporary audio file creation have avoidable hardening gaps.

Mitigation: Validate requested voice names against an approved list and use private temporary directories with appropriate permissions.

## Reference(s):

- [Piper text-to-speech engine](https://github.com/rhasspy/piper)
- [Piper voices](https://huggingface.co/rhasspy/piper-voices)

## Skill Output:

**Output Type(s):** [Shell commands, Markdown, Files, Guidance]

**Output Format:** [Markdown with inline bash commands and generated MP3 file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generates local MP3 audio files in a temporary directory for voice-message delivery.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
