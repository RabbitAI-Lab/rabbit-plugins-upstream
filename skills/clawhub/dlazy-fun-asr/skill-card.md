## Description:

Transcribes audio recordings with Alibaba Bailian Fun-ASR, with language detection and optional speaker diarization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams can turn audio recordings into transcripts, subtitles, or meeting notes, with optional speaker separation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI login flow is not clearly connected to transcription, and the CLI package and some referenced material were not inspected.

Mitigation: Review the pinned CLI package and verify the login flow before authenticating; use a scoped API key and rotate or revoke it when needed.

## Reference(s):

- [CLI homepage listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [JSON transcription result, with optional speaker labels and asynchronous task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports Chinese and English language selection, automatic language detection, and optional speaker diarization.]

## Skill Version(s):

1.3.41 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
