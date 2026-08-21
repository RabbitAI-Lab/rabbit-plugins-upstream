## Description:

Generates a complete Chinese e-commerce item-detail image set from product images, category, and short selling points while preserving the product style, color, and material.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce operators, marketers, and agents use this skill to create item-detail page visuals with Chinese copy, banners, selling-point icon blocks, material details, product detail sections, and size or parameter blocks from product inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product images and prompts are uploaded to the dLazy hosted service for generation.

Mitigation: Review whether product imagery or copy is sensitive before use, and avoid sending restricted materials to the service.

Risk: Authentication may save a dLazy API key in local CLI configuration.

Mitigation: Use the documented login or environment-variable flow appropriate for the environment, restrict local config access, and rotate or revoke keys when needed.

Risk: Generated marketing copy or visuals may include inaccurate product claims, malformed Chinese text, or changes to product appearance.

Mitigation: Keep claims grounded in supplied product information, generate modules separately, and manually check text, layout, and product fidelity before publication.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy homepage](https://dlazy.com)
- [remove-watermark related skill](https://github.com/dlazyai/ecommerce-skills/blob/main/skills/remove-watermark/skill.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides the agent to produce dLazy image-generation commands that return hosted image URLs and optional saved image files.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
