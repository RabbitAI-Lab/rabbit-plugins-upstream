## Description:

Creates social-commerce outfit images that keep the clothing while changing the model, pose, and setting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators and commerce teams can use the skill to create lifestyle and social-commerce images from outfit photos, changing the model, pose, or scene while aiming to preserve the clothing details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan reports that image workflows send user images to external services without a privacy warning, and its inspection covered only 5 of 9 components.

Mitigation: Before use, decide whether sending the supplied images to an external service is acceptable and account for the four components that were not fully inspected.

Risk: The skill notes that unclear or obscured clothing details may be redrawn in generated images.

Mitigation: Inspect generated images for changes to garments and accessories before publishing them.

## Reference(s):

- [Provider CLI reference](references/provider-cli.md)
- [Image model flags](references/model-flags.md)
- [dLazy](https://dlazy.com)
- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/clothing-grass-planting)

## Skill Output:

**Output Type(s):** [Image files]

**Output Format:** [Generated JPEG images, typically in a vertical 1024x1536 format]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can generate multiple image variants; output size and format depend on the selected provider and settings.]

## Skill Version(s):

1.0.34 (source: frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
