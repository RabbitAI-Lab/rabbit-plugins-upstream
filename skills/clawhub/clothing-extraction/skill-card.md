## Description:

Extracts a clean, white-background flat-lay image of clothing from a person, street-style, or customer photo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users preparing ecommerce product imagery use the skill to isolate a garment from a model or customer photo and create a clean flat-lay image.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Source photos, including people and their surroundings, are sent to the selected cloud provider.

Mitigation: Use only photos you are authorized to share, choose the provider explicitly, and review its data handling practices before uploading.

Risk: Garment details hidden by a person, bag, or other obstruction are inferred and may be inaccurate.

Mitigation: Review the generated image and manually confirm important design details, or use a less obstructed source photo.

## Reference(s):

- [Provider and data flow guidance](references/provider-cli.md)
- [Image model parameters](references/model-flags.md)
- [Related flat-lay skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/flat-lay/skill.md)

## Skill Output:

**Output Type(s):** [Image files, Shell commands, Guidance]

**Output Format:** [JPEG or PNG product images, with Markdown instructions and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typically a 1024×1024 image of one garment; details hidden by occlusion may be inferred and need review.]

## Skill Version(s):

1.0.30 (source: SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
