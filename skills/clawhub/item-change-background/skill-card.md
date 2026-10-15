## Description:

Turns plain-background product photos into realistic lifestyle scenes with lighting and shadows matched to the new setting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Merchants and creative teams use the skill to place product photos into plausible scenes for product listings and marketing while preserving the product's appearance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected product images are sent to the configured image-generation provider.

Mitigation: Use local product images or trusted public URLs, avoid sensitive or private photos, and select a provider explicitly if automatic selection is unwanted.

Risk: Generated scenes may alter product details or imply misleading product uses.

Mitigation: Review product shape, color, logo, lighting, and scene suitability against the source image before publishing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/item-change-background)
- [Provider CLI reference](references/provider-cli.md)
- [Model flags reference](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Image files, Shell commands, Guidance]

**Output Format:** [Generated product-scene images (typically JPEG) with textual instructions and status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports text-described or supplied backgrounds and batch variants; generated images can be saved locally.]

## Skill Version(s):

1.0.21 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
