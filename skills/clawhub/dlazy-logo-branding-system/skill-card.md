## Description:

A professional pipeline for building everything from a core mark to a complete brand visual system, ensuring creative quality, execution consistency, and shippable delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and brand designers use this skill to plan a stepwise logo and brand identity workflow, generate core mark concepts with the dLazy CLI, and extend confirmed assets into variants, applications, and brand system deliverables.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced media files may be sent to dLazy-hosted services.

Mitigation: Use the skill only when uploading those prompts and media is acceptable, and avoid sensitive brand assets unless their upload is approved.

Risk: A global install can leave the dLazy CLI and stored API key on the user's system.

Mitigation: Prefer npx or the DLAZY_API_KEY environment variable for one-off use when a persistent install or stored credential is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-logo-branding-system)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with inline shell commands and generated image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call the dLazy CLI to send prompts and referenced media to dLazy-hosted services after user confirmation.]

## Skill Version(s):

1.2.8 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
