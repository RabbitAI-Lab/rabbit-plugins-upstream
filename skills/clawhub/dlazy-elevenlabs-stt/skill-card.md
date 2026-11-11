## Description:

Transcribes audio with ElevenLabs scribe_v1, with automatic language detection and optional speaker diarization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can turn audio into transcripts, subtitle text, and meeting notes, with optional speaker labels.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports an undocumented `dlazy` login operation and could not fully review the CLI's behavior or referenced material.

Mitigation: Review the CLI and its authentication behavior before installation, and confirm that its login and API-key handling fit your expectations.

## Reference(s):

- [dLazy homepage](https://dlazy.com)
- [dLazy CLI project page](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [JSON transcription response with text results and optional speaker labels or asynchronous task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Language selection and optional speaker diarization.]

## Skill Version(s):

1.3.40 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
