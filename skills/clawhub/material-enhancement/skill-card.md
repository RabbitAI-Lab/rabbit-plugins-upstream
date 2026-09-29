## Description:

Enhances clothing fabric texture in an existing product image using a high-resolution image of the same garment as reference.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce creators and image editors use a high-resolution product photo to restore fabric texture in an on-model image while aiming to preserve its pose, composition, and color.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product or model images and prompts may be sent to dLazy or another configured cloud provider.

Mitigation: Use --dry-run or --doctor to confirm the provider first; avoid private or regulated images unless that provider is approved.

Risk: Generated edits can alter color, garment shape, or details outside the intended fabric area.

Mitigation: Compare each result with the source image and reject outputs that change the model, background, garment silhouette, or color.

## Reference(s):

- [Provider and authentication reference](references/provider-cli.md)
- [Image model options](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image files]

**Output Format:** [Markdown guidance and commands with saved JPEG images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses an original image and a high-resolution image of the same garment; outputs should be checked against the original for unwanted changes.]

## Skill Version(s):

1.0.13 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
