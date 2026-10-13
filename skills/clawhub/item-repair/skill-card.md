## Description:

Retouches product photos for listings by reducing incidental wrinkles, straightening placement, balancing lighting, and cleaning backgrounds while preserving product details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Merchants and creative teams use this skill to prepare photographed products for e-commerce listings, preserving product features and visible defects while improving presentation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product photos, prompts, and remote image URLs may be sent to the selected cloud image provider.

Mitigation: Use only images and prompts approved for the chosen provider, and review the destination before sending sensitive product assets.

Risk: Cloud generation can incur charges and uses provider credentials.

Mitigation: Run a dry-run to inspect requests and estimated cost; use scoped, revocable API keys.

Risk: Generated images could overwrite originals or unintentionally alter product features and defects.

Mitigation: Save results in a separate directory and compare them with the originals before publishing.

## Reference(s):

- [Item Repair on ClawHub](https://clawhub.ai/dlazyai/skills/item-repair)
- [Provider and credential guidance](artifact/references/provider-cli.md)
- [Image model options](artifact/references/model-flags.md)
- [Related Material Enhancement skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/material-enhancement/skill.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image files]

**Output Format:** [Text instructions and edited product images (JPEG by default)]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports up to four views of one product and saves generated images to a specified path.]

## Skill Version(s):

1.0.20 (source: frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
