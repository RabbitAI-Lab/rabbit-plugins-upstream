## Description:

ElevenLabs scribe_v1 speech-to-text with automatic language detection and optional speaker diarization for subtitles, transcription, and meeting notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users can invoke this skill to submit audio URLs or local audio files to dLazy's hosted ElevenLabs STT wrapper and receive transcription results for subtitles, transcripts, or meeting notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audio files, prompts, and parameters are sent to dLazy-hosted services for transcription.

Mitigation: Use the skill only with recordings approved for dLazy processing, and avoid confidential, regulated, or sensitive audio unless organizational policy allows it.

Risk: The skill relies on the external @dlazy/cli npm package and a dLazy API key stored locally or supplied by environment variable.

Mitigation: Install only from trusted package sources, prefer npx or a restricted environment when avoiding global installs, and rotate or revoke the API key if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-stt)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, JSON, Files, Shell commands, Configuration]

**Output Format:** [JSON response containing generated transcription output, with optional saved result assets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports synchronous waiting, asynchronous task polling, dry-run cost estimates, and saving returned assets to a local path.]

## Skill Version(s):

1.3.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
