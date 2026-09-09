## Description:

商品图生成带文案排版的转化主图：商品图和卖点生成带中文文案的电商主图。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, designers, and agent users use this skill to turn a product image plus concise selling points into a square or vertical main listing image with Chinese marketing copy. It helps separate product features from promotional benefits, choose category-appropriate layout and colors, and generate provider commands for image creation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and product images may be sent to the selected cloud image-generation provider.

Mitigation: Review the selected provider and its data-handling terms before use, and avoid submitting confidential product assets unless that provider is approved for the data.

Risk: Optional provider paths handle credentials, custom endpoints, and downloads in ways that may exceed user expectations.

Mitigation: Use trusted provider endpoints, protect API keys, avoid untrusted npx CLI execution, and set ARK_BASE_URL only to a trusted HTTPS endpoint.

Risk: Generated ecommerce main images can contain unreadable text, unverified product claims, or inaccurate promotions.

Mitigation: Review generated images at thumbnail size and verify product claims, promotional terms, and platform compliance before publishing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/item-selling-point)
- [Provider CLI Reference](references/provider-cli.md)
- [seedream-5.0-pro Parameters](references/model-flags.md)
- [dLazy](https://dlazy.com)
- [dLazy CLI](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash commands and saved image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default output is a 1:1 ecommerce main image; 3:4 is also documented for platform-specific vertical main images, and batch generation may produce multiple candidates.]

## Skill Version(s):

1.0.7 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
