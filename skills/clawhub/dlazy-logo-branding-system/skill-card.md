## Description:

A professional pipeline for building everything from a core mark to a complete brand visual system, ensuring creative quality, execution consistency, and shippable delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers, brand teams, and agent users use this skill to plan logo and brand identity work, generate core mark directions, and extend approved assets into variants, applications, and brand system guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The dLazy CLI can store an API key in local user configuration.

Mitigation: Prefer npx or the DLAZY_API_KEY environment variable when long-lived local CLI state is not desired, and rotate or revoke keys from the dLazy dashboard as needed.

Risk: Prompts and user-designated media files are sent to dLazy services for cloud generation.

Mitigation: Review prompts and assets before execution, and do not pass private files unless they are intended to be uploaded.

Risk: Global CLI installation increases local dependency and update surface.

Mitigation: Use the version-pinned npx command or review the linked CLI source before installing globally.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-logo-branding-system)
- [dLazy CLI source and homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration instructions]

**Output Format:** [Markdown with concise summaries, prompt drafts, inline shell commands, and generated image URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses phased user confirmation and may produce hosted dLazy media URLs when generation commands are run.]

## Skill Version(s):

1.2.10 (source: server release metadata; artifact frontmatter reports 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
