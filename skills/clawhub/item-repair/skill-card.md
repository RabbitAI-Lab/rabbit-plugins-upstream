## Description:

商品精修、去褶皱。随手拍的商品图 → 可直接上架的精修图。当用户说「精修」「去褶皱」「修图」「拍得不好看」「整理一下」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers, catalog teams, and product photographers use this skill to prepare product images for listings by reducing random wrinkles, improving placement and lighting, and cleaning the background while preserving product details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images may be sent to an external image provider during editing, creating a privacy concern.

Mitigation: Before use, confirm the selected provider's image handling and avoid sending images that contain sensitive information unless the provider is approved for that data.

Risk: The security scan covered only part of the artifact, so unreported behavior has not been established as safe.

Mitigation: Review the partially inspected files and rerun an adequate security review before enabling the skill in a sensitive environment.

## Reference(s):

- [Model flags reference](artifact/references/model-flags.md)
- [Provider and CLI reference](artifact/references/provider-cli.md)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [Related material enhancement skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/material-enhancement/skill.md)
- [Item Repair ClawHub release page](https://clawhub.ai/dlazyai/skills/item-repair)

## Skill Output:

**Output Type(s):** [Guidance, Text, Shell commands, Image files]

**Output Format:** [Markdown guidance with image-editing prompts and CLI examples; generated product images in the selected image format]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts 1–4 views of the same product per workflow; output size and format depend on the selected model and options.]

## Skill Version(s):

1.0.35 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
