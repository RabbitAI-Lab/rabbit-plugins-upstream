## Description:

Turns flat-lay garment photos into dimensional ghost-mannequin product images while aiming to preserve the garment's color, texture, and shape.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce teams and product photographers use this skill to create dimensional, model-free garment listings from flat-lay photos, with optional pose references and brand styling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and prompts are sent to the selected cloud provider.

Mitigation: Use trusted local files or image URLs, and send confidential or customer-linked assets only when your organization permits provider processing.

Risk: Image generation may incur provider charges.

Mitigation: Check the selected provider and credentials, and estimate the cost with a dry run before paid generation.

Risk: Generated garment details or proportions may differ from the source photo.

Mitigation: Review the output against the source garment for color, texture, labels, shape, and unwanted mannequin artifacts before using it.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/to-3d)
- [Provider CLI reference](references/provider-cli.md)
- [Image model flags](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image files]

**Output Format:** [Markdown guidance with shell commands; generated JPEG, PNG, or WebP image files when run]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs can be saved locally or returned as provider-hosted image links; inspect garment details before publication.]

## Skill Version(s):

1.0.21 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
