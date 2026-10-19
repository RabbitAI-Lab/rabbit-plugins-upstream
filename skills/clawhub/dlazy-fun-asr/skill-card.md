## Description:

Transcribes audio with Fun-ASR through dLazy's hosted service, with language and speaker-labeling options for subtitles and meeting notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams transcribe recordings into text for subtitles, transcripts, and meeting notes, optionally identifying speakers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audio supplied to the skill may be uploaded to dLazy's hosted service.

Mitigation: Use only recordings you are comfortable sending to dLazy.

Risk: The CLI may save an API credential locally during login.

Mitigation: Use a per-invocation DLAZY_API_KEY when you do not want to store the credential locally.

Risk: The published --prompt example does not match the audio input option.

Mitigation: Check the CLI help and provide audio through --audio_url instead.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-fun-asr)
- [dLazy CLI source listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Transcription text or JSON results with command-line guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Speaker labels when requested; asynchronous jobs can return a task identifier before transcription completes.]

## Skill Version(s):

1.3.31 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
