## Description:

Midjourney style generation for artistic, strongly stylized image creation with aspect ratio, bot type, and grid or U1-U4 output selection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to run the dLazy Midjourney-style image generation CLI, submit prompts and generation parameters, and return hosted image outputs or async task status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and intentionally supplied local media paths may be sent to the dLazy hosted service.

Mitigation: Avoid sending sensitive prompts or media unless the user has confirmed the data is appropriate for the dLazy service.

Risk: Generated image outputs are hosted by dLazy.

Mitigation: Treat returned URLs as externally hosted content and avoid assuming private storage unless the service terms confirm it.

Risk: Authentication can store an API key in the local dLazy configuration.

Mitigation: Use per-command DLAZY_API_KEY injection when persistent local credentials are not acceptable, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: The skill depends on npm or npx and a third-party CLI.

Mitigation: Review and trust the pinned dLazy CLI package before installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-mj-imagine)
- [dLazy CLI homepage](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, text, json, guidance]

**Output Format:** [Markdown instructions with shell commands and JSON result envelopes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The dLazy CLI returns hosted image URLs, or an async task identifier when no-wait mode is used.]

## Skill Version(s):

1.3.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
