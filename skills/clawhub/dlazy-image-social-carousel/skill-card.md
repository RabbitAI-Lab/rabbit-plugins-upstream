## Description:

Guides the design and cover-first generation of social-media carousel images through a confirmed slide plan and the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketing teams use this skill to plan platform-specific social carousels, confirm a visual direction, approve a generated cover, and produce matching slides.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced media are sent to dLazy services for generation.

Mitigation: Review prompts and media for sensitive content before submitting them.

Risk: The dLazy API key is stored locally when configured through the CLI.

Mitigation: Use the environment-variable option if local key storage is unsuitable, and rotate or revoke keys when needed.

Risk: Installing the dLazy CLI globally adds third-party software to the system.

Mitigation: Review the CLI source before installation, or use the documented npx alternative.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-image-social-carousel)
- [dLazy CLI source (linked in skill metadata; not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Shell commands]

**Output Format:** [Markdown with a slide plan, progress updates, generation commands, and resulting image links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires approval of the direction and cover before continuing with subsequent slides.]

## Skill Version(s):

1.3.29 (source: ClawHub release metadata; artifact frontmatter says 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
