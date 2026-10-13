## Description:

Places product photos into realistic new scenes while matching lighting, reflections, and contact shadows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Sellers and creative teams use this skill to turn plain-background product photos into realistic lifestyle images while preserving the product's appearance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images, background references, and prompts may be sent to a cloud image provider.

Mitigation: Use only an approved provider for confidential or unreleased assets; inspect requests with dry-run before generation.

Risk: Generated scenes may alter product details or suggest an inaccurate use case.

Mitigation: Check each result against the original product and reject misleading or physically implausible scenes.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/item-change-background)
- [Image model options](artifact/references/model-flags.md)
- [Image provider and data-flow reference](artifact/references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Images, Shell commands, Guidance]

**Output Format:** [Saved product images (JPEG, PNG, or WebP), with text guidance and commands]

**Output Parameters:** [2D images and 1D text]

**Other Properties Related to Output:** [Supports a requested output path and multiple image variants.]

## Skill Version(s):

1.0.20 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
