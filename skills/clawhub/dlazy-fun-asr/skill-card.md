## Description:

Transcribes recordings through Fun-ASR, with language selection and optional speaker diarization for subtitles and meeting notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, teams, and developers use this skill to transcribe recordings for subtitles, written transcripts, and meeting notes, optionally separating speakers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected recordings are uploaded to dLazy's cloud service and may contain sensitive information.

Mitigation: Only submit recordings when the data handling requirements permit cloud processing; obtain appropriate permission for recorded voices.

Risk: Running the third-party dLazy CLI introduces package and installation trust considerations.

Mitigation: Review the package and its source before use; choose on-demand npx execution instead of a global install when appropriate.

Risk: A dLazy API key is required and can be exposed if handled carelessly.

Mitigation: Keep the key private and rotate or revoke it if exposed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-fun-asr)
- [dLazy CLI source (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package (linked in skill metadata)](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [JSON response containing transcription results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional speaker diarization; asynchronous requests may return a task ID before results are ready.]

## Skill Version(s):

1.3.24 (source: ClawHub release; skill frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
