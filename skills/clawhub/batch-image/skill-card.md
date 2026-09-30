## Description:

Generates visually consistent product images from a SKU manifest, with concurrent processing, retries, resumable runs, cost limits, and a contact sheet for review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce teams and content creators use this skill to generate and review consistent product photography across a SKU catalog, while tracking progress and limiting generation costs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and prompts are sent to the selected image provider, including private image URLs if supplied.

Mitigation: Use only images approved for provider upload and avoid private or internal URLs unless sharing is intended.

Risk: Large manifests and retries may consume substantial paid generation credits.

Mitigation: Run a dry-run first and set a credit cap before processing the full manifest.

Risk: Batch jobs create local image and report files.

Mitigation: Keep inputs and output directories within a scoped project folder and review generated images before publishing.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/batch-image)
- [Provider CLI and data flow](references/provider-cli.md)
- [Model options](references/model-flags.md)
- [Platform image specifications](references/platform-specs.md)
- [dLazy CLI](https://github.com/dlazy-ai/cli)
- [Image quality-check skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/detect-task/skill.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Files]

**Output Format:** [Markdown instructions and commands; generated image files, CSV reports, and an optional HTML contact sheet]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Output is organized by SKU; runs can be resumed and reviewed before publishing.]

## Skill Version(s):

1.0.15 (source: skill frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
