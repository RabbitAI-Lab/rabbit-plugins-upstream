## Description:

Generates photorealistic close-ups of visible garment details, such as fabric texture, seams, and knit construction, from product photos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and creative teams use this skill to turn garment product photos into detail images of collars, cuffs, seams, and textiles for product listings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product photos and prompts are sent to the selected cloud image provider.

Mitigation: Avoid sensitive or private photos and confirm the chosen provider before sending images.

Risk: Image generation may incur charges or require additional CLI installation.

Mitigation: Check the request with --dry-run or --doctor first and pin any separately installed npx package.

Risk: Generated close-ups can suggest garment details absent from the source photo.

Mitigation: Use clear source images and review each result against the garment before publishing.

## Reference(s):

- [Provider setup and data flow](references/provider-cli.md)
- [Image model options](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image files]

**Output Format:** [Text instructions and generated JPEG product-detail images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Square or portrait close-ups of one visible garment feature per image.]

## Skill Version(s):

1.0.14 (source: server-resolved release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
