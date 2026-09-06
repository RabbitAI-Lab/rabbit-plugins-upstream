## Description:

Alibaba Bailian Fun-ASR recording transcription supports Chinese, English, and other languages, with automatic language detection and speaker diarization for subtitles, transcripts, and meeting notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke the dLazy Fun-ASR CLI for transcription of audio files or audio URLs, including optional speaker diarization and asynchronous job polling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-provided audio files or URLs are uploaded to dLazy's hosted service for transcription.

Mitigation: Only submit recordings and URLs that are appropriate to process through the hosted service.

Risk: The dLazy API key may be stored in the local CLI configuration.

Mitigation: Use per-invocation DLAZY_API_KEY when persistent local key storage is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: The skill depends on a pinned external CLI package for execution.

Mitigation: Review the pinned dLazy CLI package before installing it in sensitive environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-fun-asr)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, json, shell commands, configuration]

**Output Format:** [JSON result returned by the dLazy CLI, with transcription output in the result payload.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return an asynchronous task identifier when --no-wait is used; --save can download the returned asset to a local path.]

## Skill Version(s):

1.3.11 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
