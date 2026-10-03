## Description:

Generates photorealistic close-ups of visible garment construction and fabric details from clothing photos for e-commerce product pages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and product-content teams use garment photos to create close-ups of collars, cuffs, seams, and fabric textures for product listings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Garment images and prompts are sent to the selected cloud image provider.

Mitigation: Submit only images and prompts approved for upload, and confirm the selected provider before running.

Risk: Image generation may incur charges and create details not visible in the source photo.

Mitigation: Use --dry-run to review the request and cost, then check generated details against the source before publishing.

## Reference(s):

- [Clothing Detail skill release](https://clawhub.ai/dlazyai/skills/clothing-detail)
- [Provider CLI and data flow reference](references/provider-cli.md)
- [Image model options](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Image files, Prompt guidance, Shell commands]

**Output Format:** [JPEG garment-detail images with Markdown usage guidance and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Square or portrait close-ups saved to a specified output path; generation can use a style reference image.]

## Skill Version(s):

1.0.16 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
