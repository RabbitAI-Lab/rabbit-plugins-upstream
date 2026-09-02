## Description:

Alibaba Bailian Fun-ASR recording transcription with Chinese, English, and multilingual support, automatic language detection, and speaker diarization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to transcribe audio from URLs or local paths into structured JSON for subtitles, meeting notes, and transcription workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audio submitted through the skill may be uploaded to dLazy's hosted transcription service.

Mitigation: Use the skill only with audio that is approved for processing by dLazy, and review organizational data handling requirements before invocation.

Risk: The dLazy API key can be saved in a local CLI configuration file.

Mitigation: Prefer per-invocation credentials when appropriate, protect the local config file, and rotate or revoke the key when access is no longer needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-fun-asr)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The invoked CLI returns JSON output and may return asynchronous task status when --no-wait is used.]

## Skill Version(s):

1.3.10 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
