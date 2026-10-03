## Description:

Helps create realistic on-model product images of shoes, bags, and accessories from product photos and a model reference image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce creators and product photographers use this skill to place shoes, bags, and accessories onto a model reference image for product photography, while aiming to preserve the product's details and the rest of the scene.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product and model images and prompts are sent to the configured cloud image provider.

Mitigation: Use only images you are authorized to share and confirm the selected provider before submitting sensitive material.

Risk: Image generation may consume paid provider credits.

Mitigation: Use the dry run to check the request and estimated cost before generating images.

Risk: Generated images are written to a local output path and may misleadingly imply a real person's endorsement.

Mitigation: Choose the output path deliberately, inspect the results, and do not use a person's likeness to fabricate an endorsement.

## Reference(s):

- [Wear Everything ClawHub release](https://clawhub.ai/dlazyai/skills/wear-everything)
- [Provider setup and output guide](references/provider-cli.md)
- [Image model options](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image files]

**Output Format:** [Markdown guidance and locally saved JPEG images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports multiple image variations and a dry run to inspect the request before generation.]

## Skill Version(s):

1.0.16 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
