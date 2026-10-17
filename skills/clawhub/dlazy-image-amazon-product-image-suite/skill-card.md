## Description:

Guides the creation of Amazon product listing images and A+ content with a consistent visual style using dLazy's image-generation service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers and product marketers use this skill to plan and generate main images, secondary images, and A+ page visuals for product listings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the third-party CLI may require a global installation and access to a dLazy API key.

Mitigation: Review the CLI before installation; use npx for an on-demand run and an environment variable for the key if persistent installation or saved credentials are undesirable.

Risk: Prompts and selected local media files are sent to dLazy cloud services for generation.

Mitigation: Do not submit confidential product information or media unless that transfer is acceptable for the workflow.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-image-amazon-product-image-suite)
- [dLazy CLI source and usage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Image URLs]

**Output Format:** [Markdown with image plans, prompt drafts, CLI commands, and generated-image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Stepwise delivery with user approval before each image generation.]

## Skill Version(s):

1.3.31 (source: server-resolved ClawHub release; artifact frontmatter says 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
