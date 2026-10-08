## Description:

Generates close-up images of garment details, such as fabric texture, stitching, and knit construction, from clothing photos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce teams and designers use this skill to create product-page close-ups of visible garment features, such as collars, cuffs, and fabric texture, from existing clothing images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Garment images and prompts may be sent to the selected external image provider.

Mitigation: Avoid sensitive product photos and private image URLs unless third-party processing is acceptable.

Risk: Cloud image generation may incur charges or save files to an unintended location.

Mitigation: Preview with --dry-run before paid runs and choose the output directory explicitly.

Risk: Generated close-ups may invent construction details or shift garment colors.

Mitigation: Use clear source photos and review every result against the garment before publication.

Risk: Provider API credentials may grant access beyond this task.

Mitigation: Keep API keys scoped and revocable.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/clothing-detail)
- [Provider CLI reference](references/provider-cli.md)
- [Image model options](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image files]

**Output Format:** [Markdown guidance and saved JPEG images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports square or portrait detail images; provider and save path are configurable.]

## Skill Version(s):

1.0.18 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
