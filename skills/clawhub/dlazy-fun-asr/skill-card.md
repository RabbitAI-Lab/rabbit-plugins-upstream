## Description:

Alibaba Bailian Fun-ASR transcribes recordings in Chinese, English, and other languages, with automatic language detection and speaker diarization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

People who work with recorded audio can use this skill to create multilingual transcripts, subtitles, or meeting notes, with optional speaker separation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The partial security assessment leaves the effects of the CLI login command unclear.

Mitigation: Review the CLI login and installation details before installing or authorizing the CLI.

Risk: Audio supplied for transcription, including local files, is uploaded to dLazy's hosted media service.

Mitigation: Submit only recordings you are authorized to share, and avoid confidential audio unless your organization's policy permits it.

## Reference(s):

- [dLazy CLI source repository](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [JSON containing transcription text and optional speaker labels]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Language selection, optional speaker diarization, and optional audio event tags.]

## Skill Version(s):

1.3.44 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
