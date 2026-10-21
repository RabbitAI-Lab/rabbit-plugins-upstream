## Description:

Selects a dLazy image model for a prompt and guides image generation or editing through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to select a dLazy model and generate or edit images from prompts and optional reference media.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and submitted local media may be sent to dLazy, and generated media is hosted by dLazy.

Mitigation: Use the service only for content you are comfortable sharing with dLazy; review media before submitting it.

Risk: The dLazy CLI saves an API key locally and a global installation persists on the system.

Mitigation: Prefer the documented npx invocation to avoid a global install, and rotate or revoke the key when no longer needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-image-generate)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with CLI commands and generated media links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI returns JSON containing URLs for generated media hosted by dLazy.]

## Skill Version(s):

1.3.33 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
