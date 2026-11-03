## Description:

A structured workflow skill for planning social media carousels by confirming the design direction first, then generating a cover before the remaining slides.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers and social media content creators use the skill to plan platform-specific carousels, confirm the direction, and guide cover-first generation of a visually consistent slide set.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media are sent to dLazy's hosted service, and generated media is hosted there.

Mitigation: Send only prompts and media approved for that service; avoid including sensitive material.

Risk: The CLI stores a reusable API key in the user's local configuration.

Mitigation: Protect access to the local configuration and rotate or revoke the key when needed.

Risk: The external CLI package performs the service interaction, and its executable behavior is outside the artifact review.

Mitigation: Review the CLI package before installing or running it.

## Reference(s):

- [CLI project link in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands, Images]

**Output Format:** [Markdown plans and confirmation tables, with CLI command guidance and generated carousel images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a confirmed cover as the visual reference for the remaining slides.]

## Skill Version(s):

1.3.38 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
