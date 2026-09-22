## Description:

商品精修、去褶皱。随手拍的商品图 -> 可直接上架的精修图。当用户说「精修」「去褶皱」「修图」「拍得不好看」「整理一下」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, catalog operators, and ecommerce content teams use this skill to retouch product photos into listing-ready images by reducing random wrinkles, improving alignment, evening lighting, and cleaning backgrounds while preserving the product's style, color, pattern, hardware, and structure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product photos and prompts may be uploaded to dLazy or another configured image-generation provider.

Mitigation: Use only product or catalog images the user is authorized to process, avoid private or sensitive photos, and confirm provider selection before running.

Risk: Broad activation phrases can make ambiguous retouching requests trigger the skill.

Mitigation: Confirm ambiguous user intent before execution, especially when source images include defects, private material, or multiple products.

Risk: Image retouching can unintentionally hide product defects or alter product structure.

Mitigation: Preserve style, color, pattern, hardware, and structural folds; review before and after images and do not remove holes, stains, damage, or other material defects.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/item-repair)
- [Provider CLI Reference](references/provider-cli.md)
- [gpt-image-2 Parameter Reference](references/model-flags.md)
- [dLazy](https://dlazy.com)
- [material-enhancement Companion Skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/material-enhancement/skill.md)
- [dLazy CLI](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash commands and generated image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default examples target product-photo image editing with saved JPEG outputs; dry-run mode can preview requests before paid execution.]

## Skill Version(s):

1.0.12 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
