## Description:

Guides agents through planning and generating Amazon product images and A+ content using the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Sellers, designers, and marketing teams use this skill to plan and generate main images, secondary product visuals, and A+ page modules for Amazon listings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced media are sent to dLazy services for generation.

Mitigation: Only submit prompts and media you are comfortable sharing with dLazy.

Risk: The CLI can store an API key locally, and global installation persists the package.

Mitigation: Review the CLI package before installation; consider npx and environment-variable authentication to reduce persistent local state.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-image-amazon-product-image-suite)
- [dLazy CLI source (tooling reference; not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Shell commands, Image URLs]

**Output Format:** [Markdown with image links, generation commands, and progress updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Images are generated via dLazy services and returned as hosted URLs.]

## Skill Version(s):

1.3.29 (source: server-resolved release; artifact frontmatter says 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
