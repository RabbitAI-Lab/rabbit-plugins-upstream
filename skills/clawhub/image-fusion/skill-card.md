## Description:

Combines up to eight product images into a coordinated ecommerce look on one model while aiming to preserve each item's details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce teams and creators use the skill to generate coordinated product photography from separate clothing and accessory images, optionally matching a model or pose reference.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product and model reference images may be uploaded to the selected cloud provider.

Mitigation: Use only images approved for external processing and avoid sensitive private images.

Risk: Automatic provider selection may send images to an unintended provider or incur charges.

Mitigation: Set the provider explicitly and review the selected provider and request with --dry-run before generating.

Risk: Generated looks can omit or alter products or show an unsuitable default model; saved images may land in an unintended location.

Mitigation: Review each product and model description, inspect generated images against the source items, and choose the save path deliberately.

## Reference(s):

- [ClawHub image-fusion listing](https://clawhub.ai/dlazyai/skills/image-fusion)
- [Provider and CLI reference](references/provider-cli.md)
- [Model options](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image files]

**Output Format:** [Markdown guidance and generated image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts up to eight product images; optional model and pose references; generated images can be saved locally.]

## Skill Version(s):

1.0.16 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
