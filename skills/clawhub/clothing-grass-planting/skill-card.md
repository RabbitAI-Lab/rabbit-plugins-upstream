## Description:

Generates social-commerce outfit images by keeping the clothing consistent while changing the model, pose, scene, lighting, and camera framing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators, ecommerce teams, and external agents use this skill to turn clear outfit images into lifestyle social-commerce visuals for posts, campaigns, and scene variations while preserving garment details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-provided prompts and outfit or reference images are sent to the configured image-generation provider.

Mitigation: Use only images and prompts that are appropriate to upload to the selected provider, review configured credentials before generation, and avoid private portraits or images without consent.

Risk: Generated lifestyle images can be misused to imply endorsement, identity use, or lived experience that did not occur.

Mitigation: Do not generate specific real-person face swaps, celebrity likenesses, or fake testimonials; review outputs before publication.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/clothing-grass-planting)
- [Provider CLI Reference](references/provider-cli.md)
- [gpt-image-2 Model Flags](references/model-flags.md)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy Website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash commands and generated JPEG image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses prompt text and one or more local image inputs; default generation settings are 1024x1536, medium quality, and JPEG output.]

## Skill Version(s):

1.0.12 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
