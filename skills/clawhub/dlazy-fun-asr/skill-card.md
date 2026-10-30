## Description:

Transcribes audio recordings with Alibaba Bailian Fun-ASR, with language detection and speaker diarization for subtitles, transcripts, and meeting notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users can transcribe recordings for subtitles, written transcripts, and meeting notes, with optional speaker diarization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audio sent for transcription is uploaded to dLazy's hosted service and may contain sensitive information.

Mitigation: Upload only recordings you are authorized to share, review the service's data-retention terms, and protect or rotate the saved API key.

Risk: The documented example uses a generic --prompt option although the help output identifies --audio_url for audio input.

Mitigation: Check `dlazy fun-asr -h`, use a supported audio option, and run `--dry-run` to inspect the request and estimated cost before submission.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-fun-asr)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, JSON, Files]

**Output Format:** [JSON response containing transcription results, with optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports language selection and optional speaker diarization; asynchronous runs may return a task identifier.]

## Skill Version(s):

1.3.36 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
