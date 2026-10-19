## Description:

Turns slides or documents into narrated slideshow videos with voiceover and transitions using dLazy's hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, educators, and teams use this skill to turn presentations and documents into narrated explainer, training, or report videos through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files may be sent to dLazy's hosted service.

Mitigation: Review content and obtain appropriate approval before sending sensitive material.

Risk: The CLI may save an API key in a local configuration file.

Mitigation: Protect the local credential, or provide it per invocation and rotate it if exposed.

Risk: Installing the external CLI allows it to execute with normal command-line permissions.

Mitigation: Review the package before execution and use the pinned npx invocation if a persistent global install is unnecessary.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-slideshow-video)
- [dLazy CLI repository (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Text with project updates and commands for creating a hosted video]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video creation and follow-up are handled by dLazy's hosted service.]

## Skill Version(s):

1.0.28 (source: ClawHub release; artifact frontmatter lists 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
