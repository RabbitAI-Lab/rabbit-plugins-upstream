## Description:

Handle images with ImageMagick and oxipng: inspect metadata, resize, crop, rotate, convert formats, combine images, add overlays or watermarks, and losslessly compress images before delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ofoxai](https://clawhub.ai/user/ofoxai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to prepare image assets for inspection, transformation, upload, or delivery while keeping image transfers smaller and avoiding exposure of local file paths.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Compression and stripping commands may remove image metadata.

Mitigation: Keep untouched originals for evidentiary, signed, forensic, or metadata-sensitive images, and avoid metadata-stripping options unless metadata removal is intended.

## Reference(s):

- [hal-image homepage](https://github.com/ofoxai/skills/tree/main/skills/hal-image)
- [Image processing recipes](references/recipes.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill may direct agents to create or modify local image files before attaching or uploading them.]

## Skill Version(s):

1.1.0 (source: ClawHub release metadata, SKILL.md frontmatter, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
