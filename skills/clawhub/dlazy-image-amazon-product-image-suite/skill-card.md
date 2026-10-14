## Description:

Guides the creation of Amazon product listing images and A+ content, from the main image through secondary visuals and branded modules.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Sellers, designers, and marketing teams use this skill to plan and generate Amazon product main images, secondary images, and A+ brand content with a consistent visual style.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected product media are sent to dLazy-hosted services for image generation.

Mitigation: Avoid submitting sensitive local files or confidential product details; use the service only when this data transfer is acceptable.

Risk: Using the external CLI requires a dLazy API key, and a global installation persists on the system.

Mitigation: Prefer on-demand npx use when a persistent install is unnecessary, and rotate or revoke the key in the dLazy dashboard if needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-image-amazon-product-image-suite)
- [dLazy CLI repository (listed in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Image URLs]

**Output Format:** [Markdown with image plans, generation prompts, status checklists, and links to generated images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tracks the current image, visual consistency, and next item awaiting approval.]

## Skill Version(s):

1.3.30 (source: ClawHub release metadata; artifact frontmatter says 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
