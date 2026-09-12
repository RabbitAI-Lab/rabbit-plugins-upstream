## Description:

Alibaba Bailian qwen3-tts voice cloning uploads a clean voice sample to create a reusable custom voice for subsequent text-to-speech use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to call dLazy's hosted qwen-audio-clone workflow for creating a custom voice from an audio sample. It is intended for voice-cloning workflows where the user has the rights and permission to use the submitted recording.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Voice samples may contain sensitive biometric or personal information and are uploaded to a third-party service.

Mitigation: Use only recordings the user owns or has explicit permission to process, avoid confidential recordings, and review dLazy privacy, retention, and deletion terms before use.

Risk: A cloned voice can be misused if created without consent or used outside the user's authorization.

Mitigation: Confirm consent and rights for the source speaker before cloning, and keep generated voices limited to authorized text-to-speech workflows.

Risk: The skill installs or invokes a third-party CLI that requires a dLazy API key.

Mitigation: Prefer the pinned npx invocation when possible, store the API key in the documented configuration or environment variable, and rotate the key if the CLI or service is no longer trusted.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-qwen-audio-clone)
- [Publisher Profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI Homepage](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown instructions with bash commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The underlying CLI may return hosted output URLs or asynchronous task identifiers.]

## Skill Version(s):

1.3.14 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
