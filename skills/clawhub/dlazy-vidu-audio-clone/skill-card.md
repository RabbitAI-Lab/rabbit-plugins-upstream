## Description:

Clone voice and generate new text reading audio with one click using Vidu Audio Clone.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to call dLazy's Vidu Audio Clone service for voice cloning and text-to-speech generation from a reference audio sample and prompt.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Voice samples and prompts are sent to dLazy's cloud service for inference.

Mitigation: Use only audio you are authorized to process, avoid private or third-party voice samples without consent, and review dLazy's terms and retention practices before use.

Risk: Authentication can persist an API key in the local dLazy CLI configuration.

Mitigation: Use per-run DLAZY_API_KEY or the pinned npx invocation when persistent credentials are not desired, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Local audio paths passed to the CLI may be uploaded to files.dlazy.com.

Mitigation: Confirm file paths before execution and pass only files intended for cloud processing.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-vidu-audio-clone)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Guidance]

**Output Format:** [JSON responses and Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is returned as hosted output URLs; async calls may return a generateId for polling.]

## Skill Version(s):

1.3.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
