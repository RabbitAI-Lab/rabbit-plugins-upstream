## Description:

Transcribes recordings with Fun-ASR for subtitles and meeting notes, with language selection and optional speaker diarization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators and teams use this skill to transcribe audio for subtitles, written transcripts, and meeting notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private recordings are uploaded to dLazy for transcription.

Mitigation: Only submit audio you are comfortable sharing with dLazy.

Risk: The skill relies on an installed dLazy CLI and a stored API key.

Mitigation: Review the CLI package before installing, use npx if a global installation is unwanted, and protect or rotate the API key as needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-fun-asr)
- [dLazy CLI source (listed in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Transcription text presented from a JSON result]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional speaker diarization and audio-event tagging; asynchronous tasks may return a task ID first.]

## Skill Version(s):

1.3.28 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
