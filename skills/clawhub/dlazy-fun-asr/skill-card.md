## Description:

Transcribes audio recordings with Alibaba Bailian Fun-ASR, supporting Chinese, English, other languages, automatic language detection, and speaker diarization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can turn recorded audio into transcripts for subtitles, meeting notes, and other text workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review had medium confidence because it could not verify the CLI login flow or its connection to the advertised transcription service.

Mitigation: Review the external CLI and its login flow before installation, and confirm the service meets your requirements.

Risk: The documented workflow sends prompts and uploaded audio to dLazy hosted services, which may matter for sensitive recordings.

Mitigation: Check the service's data handling terms and avoid submitting recordings you are not authorized to share.

## Reference(s):

- [dLazy service](https://dlazy.com)
- [@dlazy/cli package](https://www.npmjs.com/package/@dlazy/cli)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-fun-asr)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [JSON containing transcription results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return an asynchronous task identifier or save the result to a file.]

## Skill Version(s):

1.3.40 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
