## Description:

ElevenLabs scribe_v1 speech-to-text with auto language detection and optional speaker diarization for subtitles, transcription, and meeting notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's ElevenLabs speech-to-text command for audio transcription, language detection, speaker diarization, subtitles, and meeting notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audio, transcripts, and related parameters are sent to dLazy cloud services.

Mitigation: Use the skill only for recordings whose sensitivity is acceptable under dLazy's retention and third-party processing terms.

Risk: The dLazy API key is stored locally when using the CLI login or auth setup flow.

Mitigation: Protect the local config file, prefer scoped organization keys, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Some examples in the artifact use a stale --prompt flow for a speech-to-text command.

Mitigation: Prefer the documented --audio_url option and check command help with dlazy elevenlabs-stt -h before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-stt)
- [dLazy CLI homepage](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API Calls, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return asynchronous task identifiers when --no-wait is used; completed results contain JSON outputs.]

## Skill Version(s):

1.3.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
