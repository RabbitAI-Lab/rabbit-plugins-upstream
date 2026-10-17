## Description:

Turns plain-background product photos into photorealistic lifestyle scenes with consistent lighting, reflections, and contact shadows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce merchants and creative teams use this skill to place product photos in believable commercial scenes while preserving product appearance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images, prompts, and optional background images may be sent to an external image provider.

Mitigation: Use only approved, non-confidential assets and avoid untrusted internal URLs unless network egress is controlled.

Risk: Generated scenes may alter product details or depict misleading use conditions.

Mitigation: Review product appearance, lighting, shadows, and scene suitability before publishing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/item-change-background)
- [Image model options](artifact/references/model-flags.md)
- [Image provider usage](artifact/references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Executing the commands can save generated product images as JPEG, PNG, or WebP files.]

## Skill Version(s):

1.0.22 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
