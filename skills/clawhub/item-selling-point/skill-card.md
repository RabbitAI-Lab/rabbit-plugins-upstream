## Description:

Generates e-commerce main product images from a product photo and selling points, including Chinese marketing copy layout for thumbnail-readable conversion images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce operators, designers, and agent users use this skill to turn a product image plus concise product and promotion claims into a single marketplace main image with readable Chinese copy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and prompts may be sent to dLazy or the configured image provider.

Mitigation: Use trusted local files or public image URLs, avoid internal or private URLs, and choose only providers approved for the product data.

Risk: Generated commercial artwork can include product features or promotional claims that need substantiation.

Mitigation: Verify product capabilities, discounts, original prices, and marketplace policy compliance before publishing the image.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/item-selling-point)
- [Provider CLI Reference](artifact/references/provider-cli.md)
- [seedream-5.0-pro Model Flags](artifact/references/model-flags.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands and file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance targets 1:1 or 3:4 e-commerce image generation; generated assets are saved to user-selected paths when the commands are executed.]

## Skill Version(s):

1.0.1 (source: server release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
