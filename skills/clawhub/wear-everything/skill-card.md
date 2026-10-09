## Description:

Creates on-model ecommerce images of shoes, bags, and accessories from product and model reference photos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce teams and creators use product and model reference images to generate realistic on-model product photos of shoes, bags, and accessories.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product and model images and prompts are sent to the chosen image-generation provider.

Mitigation: Use only images approved for sharing, and confirm the selected provider and request with a dry run before generating.

Risk: Edited images could imply a false endorsement or use a person's likeness without consent.

Mitigation: Use reference images you have rights to edit; obtain consent and avoid fake endorsements.

Risk: Generated placement, product details, or the model's appearance may differ from the references.

Mitigation: Review each output for accurate product details, realistic placement, and unintended changes before publishing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/wear-everything)
- [Provider setup and output guide](references/provider-cli.md)
- [Image model options](references/model-flags.md)
- [dLazy CLI](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Images, Shell commands, Guidance]

**Output Format:** [Saved image files and Markdown guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports multiple product views and batch generation; generated images need visual review.]

## Skill Version(s):

1.0.18 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
