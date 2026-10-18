## Description:

Enhances clothing texture in an existing product photo using a high-resolution image of the same garment while aiming to preserve the model, composition, and color.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Product photographers and ecommerce teams use this skill to restore fabric detail in an otherwise acceptable garment photo using a high-resolution image of the same product.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product or model images and prompts are sent to the configured image provider.

Mitigation: Use trusted images and avoid confidential or unreleased imagery unless the provider policy permits it; review requests with --dry-run.

Risk: Generated fabric may not match the product, or other parts of the photo may change.

Mitigation: Use a reference photo of the same garment and compare the generated image with the original for texture, color, model, and background changes.

## Reference(s):

- [Material Enhancement on ClawHub](https://clawhub.ai/dlazyai/skills/material-enhancement)
- [Provider CLI reference](references/provider-cli.md)
- [Model flags reference](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with shell commands and image-editing prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The image-editing backend saves generated garment images to local files; compare them against the original before use.]

## Skill Version(s):

1.0.21 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
