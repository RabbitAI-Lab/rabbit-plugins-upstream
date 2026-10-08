## Description:

Creates controlled A/B variants of ecommerce listing images, records a hypothesis for each variant, and provides a template for reviewing campaign results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce sellers and marketers use this skill to compare product listing images while changing one variable at a time, document predictions, and review results after entering their own campaign metrics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference images and prompts may be sent to the selected external image-generation provider.

Mitigation: Use only intended product assets, review the selected provider and credentials, and run --dry-run to inspect the request before uploading images.

Risk: Image generation can consume provider credits and write local image files.

Mitigation: Review the dry-run cost estimate and output path before generating variants.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/listing-optimizer)
- [Platform image specifications](references/platform-specs.md)
- [Image provider and CLI guidance](references/provider-cli.md)
- [Platform compliance skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/platform-compliance/skill.md)

## Skill Output:

**Output Type(s):** [Images, Markdown, Shell commands, Guidance]

**Output Format:** [Generated image files and a Markdown A/B experiment recap template with suggested generation and compliance commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The user supplies performance metrics; the skill does not access platform analytics or establish statistical significance.]

## Skill Version(s):

1.0.14 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
