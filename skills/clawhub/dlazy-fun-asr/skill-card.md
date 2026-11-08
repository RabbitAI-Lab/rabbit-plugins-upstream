## Description:

Transcribes recordings with Alibaba Bailian Fun-ASR, supporting Chinese, English, language detection, and speaker diarization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can transcribe authorized recordings for subtitles, searchable transcripts, and meeting notes, with optional speaker separation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Recordings may be uploaded to dLazy media storage for transcription.

Mitigation: Submit only recordings you are authorized to share, and review dLazy's privacy and retention terms.

Risk: The CLI stores an API key locally, and the security review did not verify the CLI's credential-protection claims.

Mitigation: Protect the stored key and revoke or rotate it if it is exposed or no longer needed.

## Reference(s):

- [dLazy service homepage](https://dlazy.com)
- [CLI project page listed in skill metadata](https://github.com/dlazy-ai/cli)
- [@dlazy/cli package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [JSON containing transcription results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include speaker diarization and asynchronous task status.]

## Skill Version(s):

1.3.38 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
