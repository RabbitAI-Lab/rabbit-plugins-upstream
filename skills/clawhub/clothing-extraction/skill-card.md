## Description:

Transforms clothing photos into clean, white-background flat-lay product images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce teams and sellers use the skill to turn clothing photos into clean, front-facing product flat-lay images for product listings and downstream creative workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Original photos, including visible people, are sent to the selected cloud provider.

Mitigation: Use photos authorized for external processing, select the provider explicitly, and review its privacy terms before sending images.

Risk: Garment details hidden by people or objects are inferred rather than recovered from the photo.

Mitigation: Prefer minimally occluded source photos and manually verify important design details in the generated image.

Risk: Saving to an existing output path may overwrite a file.

Mitigation: Choose a unique output path and confirm the destination before running generation.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/dlazyai/skills/clothing-extraction)
- [Provider CLI reference](references/provider-cli.md)
- [Model flags reference](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Image files, Shell commands, Guidance]

**Output Format:** [PNG or JPEG product images, with Markdown guidance and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typically one garment image per run; occluded details may be inferred.]

## Skill Version(s):

1.0.26 (source: SKILL.md frontmatter, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
