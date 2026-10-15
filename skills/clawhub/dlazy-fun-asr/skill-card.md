## Description:

Transcribes audio recordings with Fun-ASR, with language selection and optional speaker diarization for subtitles and meeting notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and teams use this skill to transcribe recordings for subtitles, written transcripts, and meeting notes, optionally identifying speakers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audio is uploaded to dLazy's cloud service for transcription.

Mitigation: Submit confidential recordings only with authorization and after reviewing the service terms.

Risk: The CLI may save an API key locally after login.

Mitigation: Use a per-invocation DLAZY_API_KEY if you do not want a saved credential.

Risk: Saving results can write to an unintended local path.

Mitigation: Check the --save path before running the command.

Risk: The skill documentation contains inconsistent examples and version details.

Mitigation: Confirm supported arguments with dlazy fun-asr -h before use.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-fun-asr)
- [dLazy CLI repository (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [JSON transcription results or an asynchronous task identifier]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional speaker diarization and audio event tags.]

## Skill Version(s):

1.3.29 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
