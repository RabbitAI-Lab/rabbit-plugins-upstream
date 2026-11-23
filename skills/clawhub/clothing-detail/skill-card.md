## Description:

Guides an agent to create macro close-up garment detail images from clothing photos, focusing on fabric texture and construction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and product-content creators use this skill to prepare close-up images of a garment's fabric and construction for product detail pages. It guides selection of a visible garment area and image-generation prompts or commands for that area.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan flags possible undisclosed transfer of images and prompts to external image services, a task-purpose mismatch, and incomplete assessment (55.6% of components fully assessed).

Mitigation: Before installing, confirm that any image and prompt transfer to external providers is disclosed and authorized; avoid confidential material unless authorized, and review the requested task and generated images while recognizing that some behavior remains unassessed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/clothing-detail)
- [Provider CLI guide](artifact/references/provider-cli.md)
- [Image model flags](artifact/references/model-flags.md)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image files]

**Output Format:** [Markdown guidance with image-generation prompts and CLI examples; generated garment-detail images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports square or portrait images; output detail depends on source image clarity and visibility of the selected garment area.]

## Skill Version(s):

1.0.35 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
