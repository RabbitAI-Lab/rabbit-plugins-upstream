## Description:

Transforms an existing model or mannequin product photo by replacing the model, the background, or both while aiming to preserve the product.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce teams use the skill to create product-photo variations for different models, backgrounds, and markets while keeping the featured garment consistent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference images are sent to the selected cloud image provider, whose retention practices were not audited.

Mitigation: Choose the provider explicitly and upload only images approved for sharing with that provider.

Risk: Cloud image generation can incur charges.

Mitigation: Inspect a dry run before generating and consider the requested batch size.

Risk: Generated files can overwrite existing files if an output path is reused.

Mitigation: Choose a fresh output filename for each generation.

## Reference(s):

- [Provider CLI guide](references/provider-cli.md)
- [Image model options](references/model-flags.md)
- [dLazy](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/one-shot)

## Skill Output:

**Output Type(s):** [Images, Shell commands, Guidance]

**Output Format:** [Markdown instructions and shell commands; generated product images (JPEG by default)]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can generate batches of image variations and save them to user-selected paths.]

## Skill Version(s):

1.0.28 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
