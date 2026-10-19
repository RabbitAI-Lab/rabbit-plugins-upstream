## Description:

Creates photorealistic close-up views of garment textures, stitching, and construction from clothing product photos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce teams use this skill to generate close-up garment detail images for product pages from existing clothing photos, highlighting visible fabric texture and construction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product photos and prompts may be sent to the selected external image provider.

Mitigation: Use only approved providers and images cleared for external processing; avoid private-network or internal image URLs.

Risk: Generated fabric or construction details may differ from the source garment.

Mitigation: Use clear, high-resolution source photos and review each image for invented details, texture, and color before publishing.

Risk: Image generation may incur provider charges.

Mitigation: Run with --dry-run first to review the request and estimated cost.

## Reference(s):

- [Clothing Detail release on ClawHub](https://clawhub.ai/dlazyai/skills/clothing-detail)
- [Provider setup and data flow](references/provider-cli.md)
- [Image model options](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Files]

**Output Format:** [Markdown guidance and commands; generated JPEG image files when run]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Square or portrait garment detail images; optional local file saving.]

## Skill Version(s):

1.0.23 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
