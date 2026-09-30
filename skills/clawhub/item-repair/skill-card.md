## Description:

Retouches product photos by removing incidental wrinkles, straightening the presentation, evening lighting, and cleaning backgrounds while preserving product details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Merchants and creative teams use the skill to prepare product photos for listings, removing incidental wrinkles and visual clutter without changing the product's actual design or condition.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and prompts are sent to a configured cloud image provider.

Mitigation: Use only approved providers and avoid uploading confidential or unreleased commercial assets without authorization.

Risk: Retouching may alter product details or conceal defects, misleading buyers.

Mitigation: Compare outputs with original photos and reject changes to design, color, structural folds, damage, or stains before publishing.

## Reference(s):

- [ClawHub item-repair release](https://clawhub.ai/dlazyai/skills/item-repair)
- [Provider setup and data flow](references/provider-cli.md)
- [Image model options](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image files]

**Output Format:** [Markdown guidance and locally saved product images, typically JPEG]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports one to four views of the same product; compare retouched images with originals before publishing.]

## Skill Version(s):

1.0.15 (source: SKILL.md frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
