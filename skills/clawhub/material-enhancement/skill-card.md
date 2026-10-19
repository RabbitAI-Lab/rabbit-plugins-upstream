## Description:

Guides texture reconstruction in clothing product photos using a high-resolution photo of the same item while preserving the model, composition, and garment color.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce creators and image editors use this skill to restore fabric texture in otherwise usable clothing photos, guided by a high-resolution reference photo of the same product.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product images and prompts may be sent to the chosen image provider.

Mitigation: Confirm permission to process the images with that provider before running the skill.

Risk: Generation may use provider credentials and incur charges or write images to the selected path.

Mitigation: Run a dry-run to review the request and estimated cost, then confirm credentials and save path before generating.

Risk: Generated textures may change garment color or other details despite preservation instructions.

Mitigation: Compare results with the original and reference images before publishing.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/material-enhancement)
- [Model flags](references/model-flags.md)
- [Provider CLI guide](references/provider-cli.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides image editing and saving generated images to a user-specified path.]

## Skill Version(s):

1.0.22 (source: ClawHub release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
