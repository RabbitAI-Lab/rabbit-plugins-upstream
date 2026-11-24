## Description:

A professional pipeline for building everything from a core mark to a complete brand visual system, ensuring creative quality, execution consistency, and shippable delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers and brand teams use this agent skill to guide logo ideation and build consistent brand assets, from a core mark through variants and real-world applications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow requires dLazy CLI authentication and installation or invocation, which the security review found not clearly connected to the branding purpose.

Mitigation: Review the CLI and installation requirements before use, and proceed with authentication only if the CLI and service are acceptable for the task.

Risk: Prompts and supplied media are sent to dLazy hosted services, and the CLI stores an API key in its user configuration when using login.

Mitigation: Avoid sending sensitive prompts or media, use an API key only when comfortable with the service, and rotate or revoke it if needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-logo-branding-system)
- [dLazy CLI project information (link listed by the skill)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)
- [dLazy API key management](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Images]

**Output Format:** [Markdown plans and design rationales, shell commands, configuration guidance, and generated image assets or URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Progressive, phase-confirmed workflow; image generation is invoked through the dLazy CLI and hosted service.]

## Skill Version(s):

1.2.39 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
