## Description:

Extracts clothing from model, street, buyer, or competitor images into clean white-background e-commerce flat-lay product images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce operators, merchandisers, and agents use this skill to turn authorized clothing photos into product-ready flat-lay image generation prompts and commands. It is especially useful when only worn, lifestyle, buyer-show, or screenshot source material is available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Source images and prompts may be sent to a configured cloud image provider.

Mitigation: Use the skill only when that data flow is acceptable for the images being processed, and process only images you own or are authorized to use.

Risk: Occluded garment details may be inferred rather than faithfully recovered from the source image.

Mitigation: Manually review generated flat-lays, especially areas previously covered by hands, bags, hair, or other garments.

Risk: The workflow could be misused to remove or obscure third-party brand marks or watermarks.

Mitigation: Avoid using shared tooling for watermark or brand-mark removal from third-party content, and do not present altered third-party goods as original products.

Risk: Generated files are written locally and may overwrite or create outputs in unintended locations if paths are chosen carelessly.

Mitigation: Use explicit output paths and review generated files before downstream use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/clothing-extraction)
- [Provider CLI Reference](references/provider-cli.md)
- [gpt-image-2 Model Flags](references/model-flags.md)
- [dLazy](https://dlazy.com)
- [dLazy CLI](https://github.com/dlazyai/cli)
- [Related Flat-Lay Skill](https://github.com/dlazyai/ecommerce-skills/blob/main/skills/flat-lay/skill.md)
- [Related To-3D Skill](https://github.com/dlazyai/ecommerce-skills/blob/main/skills/to-3d/skill.md)
- [Related Fabric-On-Body Skill](https://github.com/dlazyai/ecommerce-skills/blob/main/skills/fabric-on-body/skill.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with prompt templates, parameter tables, and inline bash commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides image-editing calls that can save generated flat-lay image files locally.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
