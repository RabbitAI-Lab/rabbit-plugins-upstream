## Description:

Generates detailed vector-style illustrations from text prompts using Recraft V4 Pro Vector through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers and developers use this skill to create detailed vector-style illustrations and production assets from text prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any user-selected local media may be sent to dLazy's hosted service.

Mitigation: Avoid submitting confidential prompts or files unless the service's data handling is acceptable.

Risk: The dLazy API key may be stored in local CLI configuration.

Mitigation: Protect the key and rotate or revoke it in the dLazy dashboard if exposed.

Risk: Installing the CLI globally leaves a persistent executable on the system.

Mitigation: Use the documented pinned npx option when a persistent global installation is not desired.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-pro-vector)
- [dLazy CLI source (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Image asset links]

**Output Format:** [JSON with hosted image URL; optional downloaded asset]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests can return a task ID for later polling.]

## Skill Version(s):

1.3.27 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
