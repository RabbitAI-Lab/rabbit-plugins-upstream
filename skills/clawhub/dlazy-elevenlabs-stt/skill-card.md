## Description:

Transcribes audio with ElevenLabs scribe_v1, including automatic language detection and optional speaker diarization for subtitles, transcripts, and meeting notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content teams use this skill to turn audio into text for subtitles, meeting notes, and other transcription workflows. Users can choose a language and optionally request speaker labels.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audio recordings are uploaded to dLazy media storage and processed by its hosted service, which may expose sensitive content.

Mitigation: Review dLazy's privacy terms and obtain appropriate consent before uploading recordings; use only audio approved for cloud processing.

Risk: Logging in saves the API key in the local dLazy CLI configuration.

Mitigation: Use the DLAZY_API_KEY environment variable for per-run credentials if you prefer not to save a key locally, and rotate or revoke keys from the dLazy dashboard.

Risk: Transcription requests may consume account credits.

Mitigation: Use the dry-run option to review the cost estimate before submitting a request.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-stt)
- [dLazy](https://dlazy.com)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [JSON response containing speech transcription text and optional speaker information]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return an asynchronous task identifier when run without waiting.]

## Skill Version(s):

1.3.36 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
