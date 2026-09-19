## Description:

Use when photo generation needs more control -- photoreal results, text in the image, or structured JSON with hex colors and bounding boxes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to route controlled still-image generation jobs to Pruna's p-image-ideogram model, especially when photoreal output, readable in-image text, structured JSON captions, brand colors, or repeatable layout placement matter.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts are sent to Pruna's cloud API for image generation.

Mitigation: Review prompts before submission and avoid including private, regulated, or sensitive data.

Risk: The skill depends on PRUNA_API_KEY for API access.

Mitigation: Keep PRUNA_API_KEY protected and avoid exposing it in logs, shared prompts, screenshots, or committed files.

Risk: Related Pruna skill installation commands use npx references that are not pinned to immutable versions.

Mitigation: Verify the related skill packages and versions before installing them in production environments.

## Reference(s):

- [P-Image-Ideogram official parameters](https://docs.api.pruna.ai/guides/models/p-image-ideogram)
- [Domain configurations](references/domain-configurations.md)
- [Ideogram JSON prompting](references/ideogram-json-prompting.md)
- [Ideogram 4.0 JSON Prompting](https://docs.ideogram.ai/using-ideogram/getting-started/prompting-guide/4.-json-prompting-ideogram-4.0)

## Skill Output:

**Output Type(s):** [guidance, text, shell commands, configuration]

**Output Format:** [Markdown with inline JSON and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides prompt drafting, model knob selection, and Pruna API request construction for image generation.]

## Skill Version(s):

1.0.13 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
