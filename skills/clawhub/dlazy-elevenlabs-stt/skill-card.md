## Description:

ElevenLabs scribe_v1 speech-to-text with automatic language detection and optional speaker diarization for subtitles, transcription, and meeting notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users invoke this skill to transcribe audio with ElevenLabs scribe_v1 through the dLazy CLI, including optional speaker diarization for subtitles, transcripts, and meeting notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review notes that saved credential protections are overclaimed.

Mitigation: Use npx or a per-run DLAZY_API_KEY when persistent CLI installation or saved credentials are not desired, and verify permissions on ~/.dlazy/config.json after login or auth setup.

Risk: Audio and request parameters are processed through dLazy-hosted services and uploaded media may be stored on files.dlazy.com.

Mitigation: Avoid sending sensitive audio unless the user is comfortable with dLazy-hosted processing and storage for the intended use case.

Risk: The usage documentation contains inconsistent examples for command flags.

Mitigation: Check dlazy elevenlabs-stt -h before execution and prefer --audio_url for audio input.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-stt)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [JSON transcription result with Markdown guidance and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; local audio paths may be uploaded to dLazy-hosted storage; async mode can return a generateId for polling.]

## Skill Version(s):

1.3.10 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
