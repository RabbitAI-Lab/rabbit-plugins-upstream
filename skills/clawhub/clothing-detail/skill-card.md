## Description:

Guides the creation of close-up clothing-detail images from garment photos for e-commerce listings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce teams and product-content creators use this skill to draft prompts and commands for close-ups of visible garment construction, stitching, and fabric texture.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Clothing images, prompts, and product details are sent to the configured cloud image provider.

Mitigation: Use --dry-run first, select an approved provider explicitly, and avoid confidential designs unless its data handling meets your policies.

Risk: Generated close-ups may depict fabric or construction details not visible in the source photo.

Mitigation: Use a clear source image and review the resulting texture, construction, and color against the actual garment before publishing.

## Reference(s):

- [Clothing Detail on ClawHub](https://clawhub.ai/dlazyai/skills/clothing-detail)
- [Provider CLI reference](references/provider-cli.md)
- [Image model flags](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with prompt text and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can produce JPEG clothing-detail images through a configured cloud image provider.]

## Skill Version(s):

1.0.19 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
