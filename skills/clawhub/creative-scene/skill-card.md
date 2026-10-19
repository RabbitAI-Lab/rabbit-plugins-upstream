## Description:

Helps create images from scene descriptions or make targeted changes to a model, pose, or outfit using a reference image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and e-commerce teams use this skill to describe and generate new scenes, or revise a model, pose, or outfit in an existing image while preserving other details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference images are sent to the selected image provider.

Mitigation: Send only content approved for that provider, and avoid private or internal image URLs.

Risk: Image generation can incur charges.

Mitigation: Use dry-run or request confirmation before billable generation.

Risk: Provider credentials and saved image paths need appropriate handling.

Mitigation: Review provider credentials and output destinations before running commands.

## Reference(s):

- [Creative Scene release](https://clawhub.ai/dlazyai/skills/creative-scene)
- [Image provider and CLI guidance](references/provider-cli.md)
- [Image model options](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image files]

**Output Format:** [Markdown instructions and CLI commands; generated image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports text-to-image generation and reference-image edits with selectable size, aspect ratio, and output path.]

## Skill Version(s):

1.0.23 (source: skill frontmatter and server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
