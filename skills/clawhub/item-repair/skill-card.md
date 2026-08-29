## Description:

Retouches casual product photos into listing-ready images by reducing wrinkles, straightening layout, evening lighting, cleaning backgrounds, and preserving product style, color, structure, and visible details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, e-commerce operators, and developers use this skill to generate prompts and commands for cloud image providers that retouch product photos for marketplace listings. It is intended for improving layout, wrinkles, lighting, background cleanliness, and clarity without changing product identity or hiding defects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product photos and prompts may be sent to dLazy or another configured cloud image provider.

Mitigation: Use only approved providers for confidential or unreleased products, and avoid uploading sensitive product imagery when provider approval is not in place.

Risk: Image retouching can unintentionally alter product structure, fabric texture, colors, or visible defects.

Mitigation: Compare outputs against source photos before publication and use preservation prompts that keep style, color, hardware, structural folds, and defects unchanged.

Risk: Optional brand presets can broadly affect visual style across generated SKU images.

Mitigation: Review brand configuration before applying it to batches, especially background, lighting, crop, model-reference, and forbidden-content settings.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/item-repair)
- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 parameter reference](references/model-flags.md)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [Related material-enhancement skill](https://github.com/dlazyai/ecommerce-skills/blob/main/skills/material-enhancement/skill.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with inline bash commands and saved image file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save retouched product-image files locally and may return generated asset URLs from the selected cloud image provider.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
