## Description:

Alibaba Bailian Fun-ASR recording transcription supports Chinese, English, and other languages, with automatic language detection and speaker diarization for subtitles, transcription, and meeting notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to invoke dLazy's hosted Fun-ASR service for transcribing audio files, optionally with speaker diarization and event tagging.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses an external npm CLI and sends selected audio inputs and parameters to dLazy's hosted service.

Mitigation: Review the data before invocation and only submit audio and parameters appropriate for processing by the dLazy hosted service.

Risk: A global CLI install persists a binary on the system.

Mitigation: Use the pinned on-demand command `npx @dlazy/cli@1.2.3` when a persistent global install is not desired.

Risk: API keys can be saved in the local dLazy CLI configuration.

Mitigation: Use per-invocation `DLAZY_API_KEY` when avoiding local credential persistence is preferred, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: The artifact's included `--prompt` example appears inconsistent with the documented `dlazy fun-asr -h` options.

Mitigation: Verify current command usage with `dlazy fun-asr -h` before running transcription tasks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-fun-asr)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return a completed JSON output or an asynchronous task identifier for polling.]

## Skill Version(s):

1.3.18 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
