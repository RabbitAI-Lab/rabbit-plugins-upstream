## Description:

ElevenLabs scribe_v1 speech-to-text with automatic language detection and optional speaker diarization for subtitles, transcripts, and meeting notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

People who need subtitles, transcripts, or meeting notes can submit audio for transcription and optionally request speaker diarization. The skill sends audio to dLazy's hosted service, so use it only for recordings you are permitted to share.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected recordings are uploaded to dLazy's hosted service for transcription.

Mitigation: Use only recordings you are authorized to share, and avoid sending sensitive audio unless the service is approved for it.

Risk: The CLI stores an API key in local configuration, and API requests consume service credits.

Mitigation: Protect the local configuration and rotate or revoke the key if exposed; check current command help and review the cost before submitting audio.

## Reference(s):

- [dLazy service](https://dlazy.com)
- [CLI project page (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, JSON, Files]

**Output Format:** [JSON transcription result with text; an output file can optionally be saved.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include speaker diarization and asynchronous task status.]

## Skill Version(s):

1.3.37 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
