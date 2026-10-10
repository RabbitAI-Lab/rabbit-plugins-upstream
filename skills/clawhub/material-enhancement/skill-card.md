## Description:

Enhances fabric texture in apparel product photos using a high-resolution image of the same item as reference while aiming to preserve the model, garment shape, color, and background.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce creators and product-image editors use this skill to reconstruct unclear garment texture in an otherwise usable photo, guided by a sharp reference photo of the same product.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product photos may be sent to external image-generation providers.

Mitigation: Use only images authorized for the selected provider, especially when working with proprietary photos.

Risk: The bundled generation helper can run tasks beyond material enhancement.

Mitigation: Review the requested task and provider with --dry-run before execution; limit credentials to the intended service.

Risk: Untrusted remote image URLs may introduce unintended content or data exposure.

Mitigation: Avoid untrusted remote image URLs and confirm reference images depict the same product.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/material-enhancement)
- [Model flags](references/model-flags.md)
- [Provider CLI reference](references/provider-cli.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image files]

**Output Format:** [Markdown guidance and commands; generated image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional batch outputs; compare results with the source image before use.]

## Skill Version(s):

1.0.18 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
