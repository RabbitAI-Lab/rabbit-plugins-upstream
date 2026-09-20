## Description:

Alibaba Bailian Fun-ASR recording transcription supports Chinese, English, and other languages, with automatic language detection and speaker diarization for subtitles, transcription, and meeting notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and teams use this skill to invoke dLazy Fun-ASR for cloud-based audio transcription, subtitle generation, speaker diarization, and meeting-note workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audio files, prompts, and parameters are sent to dLazy infrastructure for cloud transcription.

Mitigation: Use the skill only with recordings approved for that cloud service, and avoid sensitive audio unless organizational policy permits it.

Risk: A persistent global install or saved API key may leave credentials on the local machine.

Mitigation: Prefer npx @dlazy/cli@1.2.3 or the DLAZY_API_KEY environment variable when users do not want a persistent global CLI install or saved key.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-fun-asr)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return asynchronous task identifiers when --no-wait is used; saved output files are controlled by the --save option.]

## Skill Version(s):

1.3.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
