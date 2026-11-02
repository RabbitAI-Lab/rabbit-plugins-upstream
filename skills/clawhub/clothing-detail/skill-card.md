## Description:

Creates macro-style clothing detail images from garment photos, highlighting fabric texture, stitching, and construction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and product-content teams use this skill to create close-up garment images for product detail pages. It focuses on visible seams, fabric texture, trims, and construction while aiming to preserve the source garment's appearance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference photos are sent to the selected cloud image provider, and generation may incur charges.

Mitigation: Choose the provider explicitly, use --dry-run to preview inputs and estimated cost, upload only images you are authorized to share, and review the provider's privacy terms.

Risk: Generated close-ups can depict fabric or construction details that are unclear or absent in the source photo.

Mitigation: Use a clear, high-resolution source image and check the generated color, texture, seams, and trims for accuracy before publishing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/clothing-detail)
- [Provider setup and data flow](artifact/references/provider-cli.md)
- [Image model parameters](artifact/references/model-flags.md)

## Skill Output:

**Output Type(s):** [Image files]

**Output Format:** [JPEG by default; PNG and WebP are also supported. Images are saved to the selected path.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typically square close-ups; 3:4 framing is also supported.]

## Skill Version(s):

1.0.25 (source: SKILL.md frontmatter, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
