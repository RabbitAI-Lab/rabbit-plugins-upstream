## Description:

Alibaba Bailian Fun-ASR recording transcription supports Chinese, English, and other languages, with automatic language detection and speaker diarization for subtitles, transcription, and meeting notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agents, and workflow users use this skill to submit recording files or audio URLs for speech transcription, optional language selection, and speaker diarization. It is suited for generating subtitles, transcripts, and meeting notes through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audio files and invocation parameters are processed by dLazy's hosted service.

Mitigation: Only submit audio files and content that are acceptable to upload to the service, and review applicable dLazy terms before use.

Risk: The skill requires a dLazy API key for use.

Mitigation: Store the key with the dLazy CLI or DLAZY_API_KEY only in trusted environments, and rotate or revoke the key if access is no longer needed or exposure is suspected.

Risk: A global npm installation can persist a third-party CLI on the system.

Mitigation: Prefer npx or a local install when appropriate, avoid running npm as administrator or root, and install only if the publisher and pinned CLI package are trusted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-fun-asr)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON result payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return asynchronous task identifiers when no-wait mode is used; saved result assets may be downloaded to a local path when requested.]

## Skill Version(s):

1.3.14 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
