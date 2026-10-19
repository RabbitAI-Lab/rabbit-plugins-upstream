## Description:

Edits an existing e-commerce model or mannequin photo to create new model and background variations while aiming to preserve the product.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce teams and content creators use this skill to create product-photo variants for different audiences and settings from an existing model or mannequin image.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and source or model-reference images are sent to the selected cloud image provider.

Mitigation: Use only a provider and images approved for the intended use; check the selected provider with dry-run or doctor before sending images.

Risk: Model or face references may implicate privacy, consent, and misleading-endorsement concerns.

Mitigation: Use photos and face references only with necessary rights and consent; do not present generated images as a real person's endorsement.

Risk: Demographic defaults or generated edits may be unsuitable for the audience or alter product details.

Mitigation: Review brand settings and inspect each image for demographic fit and faithful product details before publishing.

## Reference(s):

- [One Shot skill listing](https://clawhub.ai/dlazyai/skills/one-shot)
- [Provider setup and image handling](references/provider-cli.md)
- [Image model options](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Image files, Shell commands, Guidance]

**Output Format:** [JPEG images with Markdown instructions and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images should be checked for product fidelity, model alignment, hands, and lighting.]

## Skill Version(s):

1.0.22 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
