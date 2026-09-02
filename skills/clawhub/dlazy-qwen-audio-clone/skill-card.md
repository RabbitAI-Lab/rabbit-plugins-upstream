## Description:

Alibaba Bailian qwen3-tts voice cloning uploads a clean voice sample to clone a custom voice for later text-to-speech use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to call the dLazy hosted qwen-audio-clone tool, uploading an authorized voice sample and receiving a cloned voice identifier or hosted result for later TTS workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Voice cloning can be misused or performed without consent.

Mitigation: Use the skill only with your own voice or a voice you have explicit permission to clone.

Risk: Voice recordings and generated outputs are processed or hosted by dLazy services.

Mitigation: Avoid uploading sensitive recordings unless you accept dLazy hosting and processing of the audio.

Risk: Persisting an API key in the local dLazy configuration can expose credentials if the host account or config file is compromised.

Mitigation: Prefer supplying DLAZY_API_KEY per invocation when you do not want a persistent local API key file, and rotate or revoke keys from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-qwen-audio-clone)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill invokes a hosted API through the dLazy CLI and may return synchronous JSON output or an asynchronous task identifier.]

## Skill Version(s):

1.3.10 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
