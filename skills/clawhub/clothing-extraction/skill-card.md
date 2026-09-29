## Description:

Guides agents in turning clothing photos into clean, white-background flat-lay product images using an image-editing provider.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce creators and developers use this skill to extract individual garments from model or street-style photos for product listings or downstream visual workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Source photos and prompts are sent to dLazy or the selected third-party image provider.

Mitigation: Use only photos permitted by the provider's data policies; avoid private, regulated, or highly sensitive people photos and prefer local files or trusted URLs.

Risk: Hidden garment details can be guessed incorrectly, causing misleading product images.

Mitigation: Check generated details, colors, and patterns against the source; use a less-obscured photo or manually correct uncertain areas.

Risk: Removing another seller's branding can misrepresent product ownership.

Mitigation: Do not remove others' brand marks to present their products as your own.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/clothing-extraction)
- [Provider and authentication guide](references/provider-cli.md)
- [Image model options](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown instructions and CLI commands for producing JPG or PNG images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generates one flat-lay image per item; obscured garment details may be inferred.]

## Skill Version(s):

1.0.15 (source: SKILL.md frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
