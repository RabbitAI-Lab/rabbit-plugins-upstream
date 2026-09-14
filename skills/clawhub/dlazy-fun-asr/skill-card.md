## Description:

Alibaba Bailian Fun-ASR recording transcription supports Chinese, English, and other languages with automatic language detection and speaker diarization for subtitles, transcription, and meeting notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to transcribe audio recordings through dLazy's Fun-ASR CLI workflow. It is suited for generating transcription output for subtitles, meeting notes, and multilingual audio review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The dLazy CLI and hosted API receive audio files, local file inputs, parameters, and API credentials used for transcription.

Mitigation: Use the skill only when that data sharing is acceptable, prefer the pinned npx invocation for non-persistent use, and rotate or revoke the dLazy API key when access is no longer needed.

Risk: Global npm installation adds a persistent third-party CLI binary to the user's environment.

Mitigation: Use the pinned npx command when possible and avoid running npm installation commands as administrator or root.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-fun-asr)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides an agent to call the dLazy CLI; completed invocations return JSON output and asynchronous invocations may return a task identifier for polling.]

## Skill Version(s):

1.3.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
