## Description:

Guides agents in creating photorealistic close-ups of garment fabric, stitching, and construction from product photos for ecommerce detail pages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce sellers and content creators use this skill to direct image-generation tools to produce garment detail shots of collars, cuffs, textile texture, and stitching from existing product images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product images and prompts are uploaded to the configured image-generation provider.

Mitigation: Use only images approved for upload and confirm the selected provider before running generation.

Risk: Image-generation requests may incur charges and consume provider credits.

Mitigation: Run a dry-run first to review requests and estimated cost.

Risk: Provider credentials and generated files may be exposed or saved in unintended locations.

Mitigation: Use scoped, revocable API keys and save outputs only to intended project paths.

Risk: Generated close-ups may invent construction details or change garment colors.

Mitigation: Compare each generated image against the source garment before publishing.

## Reference(s):

- [Clothing Detail on ClawHub](https://clawhub.ai/dlazyai/skills/clothing-detail)
- [Provider and authentication guide](references/provider-cli.md)
- [Image model options](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with image-generation prompts and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can save generated JPEG detail images to a chosen project path.]

## Skill Version(s):

1.0.21 (source: SKILL.md frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
