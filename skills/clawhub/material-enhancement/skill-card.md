## Description:

Enhances garment texture in an existing product photo using a high-resolution image of the same item as a material reference.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce creators and product photographers use the skill to restore realistic fabric detail in clothing photos without intentionally changing the model, garment shape, color, or background.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and prompts are sent to dLazy or the selected cloud image provider.

Mitigation: Use trusted provider credentials, inspect terms and retention settings, and avoid confidential imagery unless sharing is acceptable.

Risk: Generated texture may differ from the reference or unintentionally alter the model, garment color, or background.

Mitigation: Use two images of the same product and compare the generated image side by side with the original before use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/material-enhancement)
- [Model flags](references/model-flags.md)
- [Provider CLI and image-data flow](references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image files]

**Output Format:** [Markdown guidance and shell commands; generated image file when executed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses an original image and a high-resolution photo of the same garment; output requires visual comparison with the original.]

## Skill Version(s):

1.0.15 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
