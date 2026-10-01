## Description:

Guides agents in planning and generating Amazon product listing images and A+ content with the dLazy image-generation CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and designers use this skill to plan and generate main images, secondary images, and A+ content for Amazon product pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected product media are sent to dLazy's cloud services.

Mitigation: Review prompts and media for sensitive content before using the CLI.

Risk: The CLI can store the API key in local configuration.

Mitigation: Protect the local configuration or use the DLAZY_API_KEY environment-variable option.

Risk: The artifact frontmatter version differs from the ClawHub release version.

Mitigation: Ask the publisher to reconcile the version metadata before relying on the artifact version.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-image-amazon-product-image-suite)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Image URLs]

**Output Format:** [Markdown with image links and command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Stepwise main, secondary, and A+ image planning and delivery.]

## Skill Version(s):

1.3.24 (source: ClawHub release evidence; artifact frontmatter lists 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
