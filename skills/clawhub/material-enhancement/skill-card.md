## Description:

Enhances clothing product images by rebuilding realistic fabric texture and micro-detail from a high-resolution reference image while preserving the original composition, model, pose, background, color, and garment silhouette.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce content teams and image-production agents use this skill to improve fabric realism in otherwise acceptable clothing photos or generated product images. It is suited for post-processing cases where texture is blurred or flattened, but composition, color, model, and garment structure should stay unchanged.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-selected clothing images are uploaded to dLazy for processing.

Mitigation: Avoid sensitive or restricted images unless this service data flow is acceptable for the deployment.

Risk: dLazy authentication may store an API key in the local CLI configuration.

Mitigation: Use organization-scoped keys, keep local config access limited to the OS user, and rotate or revoke keys when access changes.

Risk: The enhancement can produce misleading results if the original image and high-resolution reference are not the same product.

Mitigation: Confirm the two inputs are the same item and compare the output against the original for unchanged model, background, color, and silhouette.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/material-enhancement)
- [dLazy Homepage](https://dlazy.com)
- [dLazy CLI Source](https://github.com/dlazyai/cli)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance, image files]

**Output Format:** [Markdown guidance with bash command examples and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses an original image, a high-resolution product reference image, optional garment/material details, high-quality generation settings, and optional save paths for enhanced image outputs.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
