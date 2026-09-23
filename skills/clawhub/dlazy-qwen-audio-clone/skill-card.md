## Description:

Alibaba Bailian qwen3-tts voice cloning uploads a clean voice sample to create a custom voice for later text-to-speech use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to invoke dLazy's hosted qwen-audio-clone workflow, supplying a permitted voice sample and metadata to create a reusable cloned voice for TTS workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Voice samples are sensitive biometric-like data and are uploaded to dLazy cloud services.

Mitigation: Use only recordings from speakers who gave explicit permission, review dLazy retention and deletion terms, and avoid uploading confidential audio.

Risk: The security summary reports that the docs conflict with the advertised audio-cloning interface.

Mitigation: Validate the current CLI help and output schema with a dry run or test account before depending on the documented examples.

Risk: Persistent API keys may be stored in the local dLazy CLI configuration.

Mitigation: Prefer per-run API keys where practical and rotate or revoke organization keys from the dLazy dashboard when access changes.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-qwen-audio-clone)
- [dLazy Homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The invoked CLI returns JSON containing task status or hosted output URLs.]

## Skill Version(s):

1.3.18 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
