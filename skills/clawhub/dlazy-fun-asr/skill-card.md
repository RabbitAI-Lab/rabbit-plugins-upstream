## Description:

Transcribes recordings with Alibaba Bailian Fun-ASR, supporting Chinese and English recognition, automatic language detection, and optional speaker diarization for subtitles, transcripts, and meeting notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to send audio recordings to dLazy's hosted Fun-ASR transcription service and receive structured transcription results for subtitles, transcripts, and meeting notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audio, prompts, and parameters are sent to dLazy cloud services for processing.

Mitigation: Use only recordings and prompts that your data handling policy permits for third-party cloud processing.

Risk: Configured authentication can store a dLazy API key in a local user configuration file.

Mitigation: Use the DLAZY_API_KEY environment variable for per-run authentication on shared machines, and rotate or revoke keys when access requirements change.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-fun-asr)
- [dLazy CLI homepage](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, json, shell commands, configuration, guidance]

**Output Format:** [Markdown instructions with shell commands and JSON output examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI returns synchronous JSON outputs or an asynchronous task identifier when no-wait mode is used.]

## Skill Version(s):

1.3.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
