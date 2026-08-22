## Description:

Converts static images into dynamic videos with the Vidu Q2 image-to-video model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, developers, and agents use this skill to turn image inputs, prompts, and generation settings into short generated videos through dLazy's hosted Vidu Q2 service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected prompts and media files are sent to dLazy's hosted service for generation.

Mitigation: Install and use the skill only when that data sharing is acceptable for the user's content and policy context.

Risk: The dLazy API key is a local credential stored by the CLI or supplied through an environment variable.

Mitigation: Prefer one-off npx use when appropriate, protect the local config file, and rotate or revoke the key from the dLazy dashboard if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-viduq2-i2v)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return generated media URLs or an asynchronous task identifier for polling.]

## Skill Version(s):

1.3.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
