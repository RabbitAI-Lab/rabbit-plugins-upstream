## Description:

Alibaba Bailian qwen3-tts voice cloning. Upload a clean voice sample to clone a custom voice usable in subsequent TTS calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can submit a clean voice sample to create a reusable custom voice for Qwen3-TTS calls through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The selected voice sample is sent to dLazy's hosted service, and login stores an API key locally.

Mitigation: Review dLazy's privacy and retention terms before uploading, protect the local key, and rotate or revoke it when needed.

Risk: The command examples in the skill are inconsistent.

Mitigation: Check the current command options with `dlazy qwen-audio-clone -h` before running a request.

## Reference(s):

- [dLazy CLI repository (referenced by the skill)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Shell commands, Guidance]

**Output Format:** [Command-line invocation and JSON result with voice-cloning status or result details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous runs may return a task identifier for later status checks.]

## Skill Version(s):

1.3.36 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
