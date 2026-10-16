## Description:

Creates close-up garment detail images showing fabric texture, stitching, and construction from clothing photos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce teams and creators use garment photos to prepare macro views of collars, cuffs, stitching, and fabric for product detail pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Garment photos and prompts are sent to the selected cloud provider.

Mitigation: Confirm the provider and obtain permission before uploading proprietary product photos.

Risk: Image generation can consume paid credits.

Mitigation: Use --dry-run and --provider to check routing and cost before generating images.

Risk: Generated close-ups may invent details or alter colors when source details are unclear.

Mitigation: Use clear, high-resolution source photos and review each result against the original garment.

## Reference(s):

- [Clothing Detail skill release](https://clawhub.ai/dlazyai/skills/clothing-detail)
- [Provider CLI reference](artifact/references/provider-cli.md)
- [Image model options](artifact/references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image files]

**Output Format:** [Markdown prompts and commands; generated JPEG images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Square or portrait garment detail images; quality depends on the source photo.]

## Skill Version(s):

1.0.22 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
