## Description:

Turns garment flat-lay and pose-reference images into on-model ecommerce photos while aiming to preserve garment details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce sellers and creative teams use the skill to turn garment photos and pose references into on-model product imagery, including single garments and coordinated outfits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Garment images, reference photos, and prompts may be sent to a selected cloud image provider.

Mitigation: Use only material approved for the selected provider; confirm credentials and retention terms for personal likenesses, proprietary apparel, or regulated data, and dry-run first.

Risk: Generated images may misrepresent garment colors, texture, logos, fit, or a model's appearance.

Mitigation: Review outputs against the source images before publishing and do not use them to imply an unauthorized personal endorsement.

Risk: The bundled generator supports ecommerce tasks beyond this virtual try-on workflow.

Mitigation: Use the flat-lay task profile unless the additional tasks are explicitly intended.

## Reference(s):

- [ClawHub flat-lay skill](https://clawhub.ai/dlazyai/skills/flat-lay)
- [Provider and CLI guidance](references/provider-cli.md)
- [Image model options](references/model-flags.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Image files]

**Output Format:** [JPEG images with optional JSON generation status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports multiple generated images, local save paths, and a dry-run cost estimate.]

## Skill Version(s):

1.0.22 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
