## Description:

Generates macro close-ups of garment details such as fabric texture, stitching, and weave from clothing images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce teams use the skill to create close-up product images that show visible garment construction and material details for product pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Source or reference images may be sent to an external image provider, and the scan notes that provider disclosure is unclear.

Mitigation: Check which provider will receive the images and review its data-handling terms before sending them.

Risk: The generated close-up may invent textile details that are not visible in the source image.

Mitigation: Choose a clearly visible target area and compare each generated detail with the source before using it.

Risk: The security analysis was incomplete, so its assessment may miss issues.

Mitigation: Treat the scan as incomplete and review the skill before installation or use.

## Reference(s):

- [Model flags and image options](references/model-flags.md)
- [Provider CLI guide](references/provider-cli.md)
- [ClawHub release page](https://clawhub.ai/dlazyai/skills/clothing-detail)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, Shell commands, Guidance]

**Output Format:** [JPEG close-up image files and Markdown instructions with inline Bash commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Photorealistic garment-detail close-ups, typically square or 3:4 portrait, generated from supplied images.]

## Skill Version(s):

1.0.31 (source: frontmatter; server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
