## Description:

Clones a custom voice for Alibaba Bailian Qwen3-TTS from a clean speech sample for later text-to-speech use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agents, and external users use this skill to invoke dLazy's Qwen audio-clone CLI, upload an authorized clean voice sample, and create a reusable custom voice for TTS workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uploads voice samples to a hosted third-party service.

Mitigation: Upload only voice samples you own or have explicit permission to clone, and avoid submitting sensitive audio unless the dLazy service terms meet your requirements.

Risk: The skill depends on an external npm CLI and dLazy API key.

Mitigation: Install only after trusting dLazy and @dlazy/cli, prefer npx for non-persistent use, and use API keys that can be rotated or revoked.

Risk: Global CLI installation leaves a persistent binary on the system.

Mitigation: Use the documented npx invocation when a one-off or lower-persistence execution path is preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-qwen-audio-clone)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, text]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return synchronous result URLs or an asynchronous generateId/task status from the dLazy CLI.]

## Skill Version(s):

1.3.15 (source: ClawHub release metadata; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
