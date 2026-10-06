## Description:

Transcribes audio with ElevenLabs scribe_v1 through the dLazy CLI, with language selection and optional speaker diarization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers transcribe audio for subtitles, transcripts, and meeting notes, with optional speaker separation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected audio files may be uploaded to dLazy-hosted services for transcription.

Mitigation: Confirm that audio may be shared with dLazy before submitting sensitive recordings.

Risk: The CLI stores an API key persistently in the user's local configuration after login.

Mitigation: Protect the local configuration and rotate or remove the key when no longer needed.

Risk: Running a third-party CLI adds a software supply-chain dependency.

Mitigation: Review the linked CLI source and package before use; use the pinned npx invocation if a global installation is unwanted.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-stt)
- [dLazy CLI source (linked in skill metadata; not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [JSON CLI response containing transcription results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional speaker diarization; asynchronous requests return a task ID for polling.]

## Skill Version(s):

1.3.25 (source: ClawHub server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
