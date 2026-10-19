## Description:

Transforms outfit photos into lifestyle-style promotional images with a new model, pose, and setting while aiming to preserve the clothing and accessories.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and merchants use this skill to turn an existing outfit photo into social-media-style promotional images with different models and settings while retaining the depicted outfit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Copying a reference person's identity into promotional images without consent may misrepresent their endorsement.

Mitigation: Use only model reference images you own, have licensed, or have permission to transform; do not imply a real person's endorsement or experience.

Risk: Photos and prompts may be uploaded to a selected image provider.

Mitigation: Check the provider and obtain appropriate permission for the images before submitting them.

Risk: Generation commands may use credentials, incur charges, and write images to disk.

Mitigation: Review the provider, credentials, estimated cost, and save path before running the commands.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/clothing-grass-planting)
- [Image model options](artifact/references/model-flags.md)
- [Provider and CLI guidance](artifact/references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image files]

**Output Format:** [Text instructions and generation commands; generated images saved to local files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image format, dimensions, batch size, and save path are configurable.]

## Skill Version(s):

1.0.22 (source: skill frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
