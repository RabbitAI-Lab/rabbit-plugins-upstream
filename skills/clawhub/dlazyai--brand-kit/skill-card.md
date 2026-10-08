## Description:

Keeps ecommerce product imagery consistent across SKUs by applying a shared brand configuration to generation prompts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce teams use a shared brand configuration to keep model appearance, color, photography, and layout consistent across product images and SKUs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected prompts and reference images are sent to the configured generation provider.

Mitigation: Review brand.yaml and reference images, and use --dry-run to preview requests before generating.

Risk: Batch generation can use provider credits and write image files.

Mitigation: Confirm style on one SKU before batch use, and review the output location and estimated cost.

Risk: A missing model reference image is skipped, which can weaken visual consistency.

Mitigation: Check the reference image path and resolve warnings before running a batch.

## Reference(s):

- [Brand configuration schema](references/brand-schema.md)
- [Generation provider guide](references/provider-cli.md)
- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/brand-kit)

## Skill Output:

**Output Type(s):** [Text, Configuration, Shell commands, Image files]

**Output Format:** [Plain-text brand prompts, YAML or JSON configuration, and generated image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Applies task-specific visual constraints; dry-run previews requests before generation.]

## Skill Version(s):

1.0.16 (source: SKILL.md frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
