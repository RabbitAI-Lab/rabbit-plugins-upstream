## Description:

Generates square e-commerce product main images with Chinese selling-point copy, promotional badges, and layout guidance from product images and concise feature or benefit text.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce operators, marketplace designers, and agents preparing product listings use this skill to convert a product image plus verified feature and promotion copy into generation prompts, shell commands, and saved main-image assets. It is intended for concise commercial product imagery where claims, discounts, and product appearance must be checked before publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and prompts may be sent to the selected image-generation provider.

Mitigation: Use dry-run before generation, choose the provider explicitly when needed, and avoid uploading confidential product imagery unless that provider is approved for the use case.

Risk: Generated marketing images may include unsupported product claims, promotions, or text that is unsuitable for marketplace compliance.

Mitigation: Verify product functions and promotion terms before generation, keep copy concise, avoid absolute claims, and review generated text before publishing.

Risk: Brand defaults can propagate incorrect visual assumptions across many generated assets.

Mitigation: Review brand.yaml defaults before using them at scale and confirm that model references, tone, colors, and output paths match the campaign.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/item-selling-point)
- [Provider CLI reference](references/provider-cli.md)
- [seedream-5.0-pro model flags](references/model-flags.md)
- [dLazy provider website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with prompt templates, inline bash commands, and locally saved image file paths when generation commands are run.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces 1:1 or 3:4 e-commerce main-image generation instructions, supports dry-run checks, and may save generated JPEG outputs locally.]

## Skill Version(s):

1.0.12 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
