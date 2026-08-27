## Description:

Alibaba Bailian qwen3-tts voice cloning uploads a clean voice sample to clone a custom voice for later text-to-speech calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's Qwen audio-cloning command, submit an authorized clean voice sample, and receive a cloned voice asset usable in later TTS workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded voice samples are sensitive biometric-like media and may be used to clone a speaker's voice.

Mitigation: Use only recordings you are authorized to submit and where the speaker has consented to voice cloning.

Risk: Local audio files passed to the CLI may be uploaded to dLazy-hosted services for processing.

Mitigation: Review dLazy CLI/package behavior and service terms before installation or use, and avoid submitting confidential audio unless the upload path is acceptable.

Risk: Persisting an API key in the local CLI configuration can leave credentials on disk.

Mitigation: Use per-invocation DLAZY_API_KEY when persistent local credentials are not desired, and rotate or revoke keys from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-qwen-audio-clone)
- [dLazy CLI metadata homepage](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown guidance with CLI commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses dLazy CLI authentication and may return asynchronous task identifiers for polling.]

## Skill Version(s):

1.3.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
