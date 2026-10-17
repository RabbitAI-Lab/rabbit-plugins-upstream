## Description:

Combines up to eight clothing and accessory images into a styled ecommerce look on one model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce merchants and creative teams use this skill to plan and generate consistent product-outfit images from separate garment and accessory photos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product, model, and reference images and prompts are sent to the selected cloud provider.

Mitigation: Use only images you are authorized to share and confirm the provider before generating.

Risk: Generation can incur charges or select a different provider than expected.

Mitigation: Use a dry run or set the provider explicitly before a paid generation.

Risk: Generated looks may omit items or change colors, layering, or model identity.

Mitigation: Review every image against the inputs and customize the example model description before publishing.

## Reference(s):

- [ClawHub image-fusion release](https://clawhub.ai/dlazyai/skills/image-fusion)
- [Provider setup and output guide](references/provider-cli.md)
- [Image model options](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with prompts and shell commands for generated image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Images can be saved locally; check each result against its source products.]

## Skill Version(s):

1.0.22 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
