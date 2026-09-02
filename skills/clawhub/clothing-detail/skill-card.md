## Description:

Generates macro clothing detail images from product photos, focusing on fabric texture, stitching, weave, and visible construction details for e-commerce detail pages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce operators, catalog teams, and agents use this skill to turn clear clothing product photos into macro detail shots for product pages. It is intended for visible garment details such as collars, cuffs, hems, buttons, zippers, stitching, prints, weave structure, and fabric fibers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Clothing images and prompts are sent to the selected cloud provider.

Mitigation: Use --dry-run to inspect requests first, submit only trusted local files or URLs, and choose a provider that fits the user's data-handling requirements.

Risk: Low-resolution, compressed, or obstructed source images can produce unrealistic or invented textile details.

Mitigation: Use source images larger than 400x400 with the target detail clearly visible, keep each prompt focused on one garment part, and review outputs before catalog use.

Risk: Reusable brand templates can propagate incorrect visual constraints across a catalog.

Mitigation: Review brand template fields before reuse and confirm they match the product line and SKU-specific prompt.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/dlazyai/skills/clothing-detail)
- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 parameter reference](references/model-flags.md)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with bash commands and saved JPEG image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports dry-run request inspection, batch generation, cloud-provider selection, and local save paths.]

## Skill Version(s):

1.0.4 (source: server evidence release.version and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
