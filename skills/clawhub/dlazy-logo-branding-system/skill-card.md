## Description:

Guides agents through a staged logo and brand-identity design process, from core marks to consistent visual applications and deliverables.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers, marketers, and other external users can use this skill to plan and refine a logo, explore brand directions, and develop coordinated variants and visual applications with approval at each stage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing a third-party CLI and storing a dLazy API key locally may expose credentials if the environment is not trusted.

Mitigation: Install only in a trusted environment; prefer the one-time npx invocation if a persistent global installation is unnecessary, and protect or rotate the API key.

Risk: Prompts and referenced media files are sent to dLazy cloud endpoints for generation.

Mitigation: Check the content and obtain permission before sending sensitive prompts or media to dLazy.

Risk: Installation metadata pins CLI version 1.2.3, while the prose also mentions an older 1.0.9 version.

Mitigation: Confirm the intended @dlazy/cli version before installing or running it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-logo-branding-system)
- [dLazy CLI repository (linked in skill metadata; not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Shell commands, Image links]

**Output Format:** [Markdown with design rationales, stepwise plans, commands, and links to generated images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Delivers logo concepts and brand-system applications incrementally, with user confirmation between stages.]

## Skill Version(s):

1.2.23 (source: ClawHub release metadata; embedded skill frontmatter says 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
