## Description:

ElevenLabs scribe_v1 speech-to-text with automatic language detection and optional speaker diarization for subtitles, transcription, and meeting notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agents, and workflow users use this skill to send a selected audio URL or local audio file to dLazy's hosted ElevenLabs STT wrapper and receive transcription output. It is suited to subtitle preparation, meeting notes, and general speech-to-text workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected audio files or URLs are sent to dLazy's hosted API and media storage.

Mitigation: Use only audio the user is authorized to process and review dLazy terms before submitting sensitive or regulated content.

Risk: API keys may be stored persistently in the local dLazy CLI configuration.

Mitigation: Prefer per-invocation DLAZY_API_KEY when persistence is not desired, and rotate or revoke organization keys from the dLazy dashboard when needed.

Risk: The artifact includes a documented --prompt example that does not match the STT option set.

Mitigation: Run dlazy elevenlabs-stt -h and use the speech-to-text flags, especially --audio_url, before invoking the command.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-stt)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [text, json, shell commands, configuration guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; selected audio URLs or local audio files are processed by dLazy's hosted service.]

## Skill Version(s):

1.3.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
