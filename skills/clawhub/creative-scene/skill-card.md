## Description:

Generates original scene images from text prompts and makes targeted changes to subjects, poses, and outfits using optional reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and developers use the skill to draft scene images and adjust a subject's appearance, pose, or outfit for visual content and ecommerce workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference images are sent to the selected cloud image-generation provider.

Mitigation: Confirm the selected provider and send confidential images only when that provider is approved for the data.

Risk: An optional brand-kit setup hint suggests installing a skill from GitHub.

Mitigation: Verify the source and installation command before running the optional setup.

## Reference(s):

- [Creative Scene skill listing](https://clawhub.ai/dlazyai/skills/creative-scene)
- [Provider setup and output reference](references/provider-cli.md)
- [Image model options](references/model-flags.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Prompt guidance, Shell commands, Image files]

**Output Format:** [Text prompts and shell commands; generated image files when run]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports optional reference images, aspect ratio, resolution, and batches.]

## Skill Version(s):

1.0.14 (source: skill frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
