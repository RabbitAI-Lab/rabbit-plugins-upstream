## Description:

Generates Midjourney-style images through the dLazy CLI with controls for aspect ratio, bot type, and grid or upscale output selection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to generate stylized images through dLazy's Midjourney-style image service, including selecting aspect ratio, bot type, and grid or U1-U4 outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local media paths supplied to the skill may be sent to dLazy's cloud service for generation.

Mitigation: Use the skill only with prompts and media that are appropriate to share with dLazy, and review dLazy's service terms before submitting sensitive content.

Risk: Authentication can store a dLazy API key in local CLI configuration.

Mitigation: Use a per-invocation API key when possible, and rotate or revoke stored keys from the dLazy dashboard when access should change.

Risk: Generated outputs are hosted by dLazy and returned as remote result URLs.

Mitigation: Treat returned URLs as externally hosted assets, and download or retain generated images according to the user's data handling policy.

## Reference(s):

- [Skill page](https://clawhub.ai/dlazyai/skills/dlazy-mj-imagine)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [json, image URLs, shell commands, guidance]

**Output Format:** [JSON response with image output metadata, hosted result URLs, and optional asynchronous task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports synchronous waits, asynchronous generateId polling, and optional local save paths through the dLazy CLI.]

## Skill Version(s):

1.3.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
