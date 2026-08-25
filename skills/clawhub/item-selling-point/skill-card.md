## Description:

Generates e-commerce main product images with Chinese selling-point copy, preserving the product appearance while arranging feature text, promotional badges, and category-appropriate backgrounds.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce operators, designers, and agents use this skill to create conversion-oriented product main images from a product image plus verified feature and promotion copy. It supports campaign badge variants, multi-SKU reuse, and thumbnail-readable Chinese layout guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product images, reference images, and prompt text are uploaded to dLazy's hosted service for generation.

Mitigation: Use the skill only when that upload is acceptable, avoid sensitive unreleased assets, and prefer per-invocation API keys when a saved local key is not desired.

Risk: Generated selling-point or promotional copy could create misleading product claims or invalid discounts if the input text is not verified.

Mitigation: Provide only verified feature and promotion copy, avoid absolute claims, and review generated images before publishing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/item-selling-point)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazyai/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI command examples and JSON output examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces prompts and dLazy CLI invocations for image generation; generated assets are returned as hosted URLs or saved files by the CLI.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
