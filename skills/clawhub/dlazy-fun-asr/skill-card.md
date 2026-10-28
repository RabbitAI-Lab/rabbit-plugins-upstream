## Description:

Transcribes audio recordings with Alibaba Bailian Fun-ASR, supporting Chinese, English, other languages, automatic language detection, and speaker diarization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can transcribe recordings for subtitles, meeting notes, and other transcription tasks, with optional speaker diarization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected recordings are uploaded to dLazy for transcription.

Mitigation: Upload only recordings you are authorized to share, and review the service privacy terms and usage charges.

Risk: The dLazy API key is used for authentication and may be stored in the local CLI configuration.

Mitigation: Protect the stored key, rotate or revoke it when needed, or provide it through DLAZY_API_KEY instead.

## Reference(s):

- [dLazy CLI project page](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [JSON response containing transcription text and optional speaker information]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous jobs may initially return a task ID.]

## Skill Version(s):

1.3.35 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
