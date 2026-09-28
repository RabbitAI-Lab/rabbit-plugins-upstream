## Description:

Creates lifestyle social-commerce outfit images while preserving clothing details and changing the model, pose, setting, and lighting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and marketers use this skill to turn an outfit photo into social-commerce lifestyle images with new models, poses, and scenes while keeping the outfit consistent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected prompts and reference images are sent to the configured image provider.

Mitigation: Use only images you have rights to share, inspect the selected provider with doctor or dry-run first, and avoid sensitive imagery.

Risk: Model likeness or generated lifestyle imagery could imply an unauthorized endorsement or real-world experience.

Mitigation: Obtain consent for likeness references and do not present generated imagery as a real endorsement or customer experience.

Risk: Generated garments or accessories may differ from the source outfit.

Mitigation: Review each output against the source before publishing and regenerate images with inaccurate product details.

## Reference(s):

- [Clothing Grass Planting on ClawHub](https://clawhub.ai/dlazyai/skills/clothing-grass-planting)
- [Provider CLI and data flow](references/provider-cli.md)
- [Image model options](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Image files, Shell commands, Guidance]

**Output Format:** [JPEG images with optional Markdown guidance and shell commands]

**Output Parameters:** [2D images, typically 1024×1536]

**Other Properties Related to Output:** [Saves generated images locally; optional batches provide multiple candidates for review.]

## Skill Version(s):

1.0.13 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
