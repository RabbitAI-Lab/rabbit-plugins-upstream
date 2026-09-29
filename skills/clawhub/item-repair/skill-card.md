## Description:

Retouches product photos for listings by reducing incidental wrinkles, straightening presentation, evening lighting, and cleaning backgrounds while preserving product details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and creative teams use this skill to prepare product photos for listings, removing incidental creases and visual distractions without changing the product itself.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and prompts are sent to dLazy or a configured cloud image provider.

Mitigation: Use only images approved for that provider and account; avoid confidential photos unless the provider settings are appropriate.

Risk: Retouching can alter structural folds, colors, or visible defects and misrepresent the product.

Mitigation: Provide explicit source photos and preservation instructions, then compare every result with the original before publishing.

## Reference(s):

- [Item Repair skill release](https://clawhub.ai/dlazyai/skills/item-repair)
- [Provider and data-flow guidance](references/provider-cli.md)
- [Image model parameters](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image files]

**Output Format:** [Markdown guidance and commands; locally saved product images when run]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image size, format, quality and batch count are configurable; review results against source photos before publishing.]

## Skill Version(s):

1.0.14 (source: server-resolved release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
