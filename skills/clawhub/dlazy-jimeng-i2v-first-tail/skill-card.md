## Description:

Generate coherent transition videos from supplied first and last frame images using Jimeng's first-tail image-to-video model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to invoke dLazy's Jimeng first-tail video generation workflow with a prompt plus first and last frame images, then receive hosted result information or save the output locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected first and last frame media are sent to dLazy's hosted cloud service.

Mitigation: Use the skill only when cloud processing by dLazy is acceptable for the prompt and media involved.

Risk: Authentication can store a dLazy API key in the local CLI configuration.

Mitigation: Prefer per-run DLAZY_API_KEY or the pinned npx invocation when persistent local credentials or a global binary are not desired, and keep local config file permissions restricted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-i2v-first-tail)
- [dLazy CLI homepage](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result objects]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted result URLs, asynchronous task status, or save generated media to a local path when requested.]

## Skill Version(s):

1.3.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
