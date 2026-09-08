## Description:

Alibaba Bailian Fun-ASR recording transcription supports Chinese, English, and other languages, with auto language detection and speaker diarization for subtitles, transcription, and meeting notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to invoke dLazy Fun-ASR for audio transcription, subtitle preparation, and meeting-note workflows. It is suited to recordings that may need language detection, Chinese or English recognition, and optional speaker diarization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audio files and request data may be processed through the dLazy hosted service.

Mitigation: Only pass audio files you are willing to upload to dLazy and review the service terms before using sensitive recordings.

Risk: The dLazy API key is stored in local CLI configuration or supplied through an environment variable.

Mitigation: Protect ~/.dlazy/config.json and rotate or revoke the API key from the dLazy dashboard if compromise is suspected.

Risk: Installing a third-party npm CLI globally can increase supply-chain exposure.

Mitigation: Use npx or an isolated environment when you do not want to keep a persistent global binary.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-fun-asr)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON CLI results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return asynchronous task identifiers when invoked with no-wait behavior.]

## Skill Version(s):

1.3.13 (source: server release evidence; artifact frontmatter is 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
