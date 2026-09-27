## Description:

A professional pipeline for building everything from a core mark to a complete brand visual system, ensuring creative quality, execution consistency, and shippable delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, and external users use this skill to plan logo concepts, generate brand-system derivatives, and organize identity-system deliverables through a stepwise dLazy workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media can be uploaded to the dLazy service, and a dLazy API key may be stored in local CLI configuration.

Mitigation: Confirm the user trusts the @dlazy/cli package and dLazy service before installing or running commands, and use the documented npx path when avoiding a global CLI install.

Risk: The artifact contains a stale 1.0.9 package-version reference while the install metadata uses 1.2.3 and the server release metadata is 1.2.16.

Mitigation: Verify the intended @dlazy/cli package version before installation or execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-logo-branding-system)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands and generated image result URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires dLazy authentication; the workflow generates one image command at a time and waits for user confirmation between phases.]

## Skill Version(s):

1.2.16 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
