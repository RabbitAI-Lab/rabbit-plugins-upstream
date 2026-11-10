## Description:

Edits existing product photos to replace the model, the background, or both while preserving the garment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce creative teams use the skill to create product-photo variants for different audiences or settings from an existing model or mannequin image, while aiming to preserve the garment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Source images and face references may be sent to an external image provider.

Mitigation: Review the selected provider's data handling terms and obtain permission before submitting images or face references.

Risk: The security scan reports incomplete file analysis, so its benign verdict does not establish that all behavior was assessed.

Mitigation: Review the skill files and provider configuration before running it with images or credentials.

Risk: Generated edits can unintentionally change product details or image anatomy.

Mitigation: Inspect each result for garment accuracy, alignment, and hand artifacts before publishing.

## Reference(s):

- [ClawHub release](https://clawhub.ai/dlazyai/skills/one-shot)
- [Provider and data-flow guidance](artifact/references/provider-cli.md)
- [Image model options](artifact/references/model-flags.md)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, Guidance, Shell commands]

**Output Format:** [Generated image files (typically JPEG) and Markdown guidance with image-editing prompts and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image size, format, quality, and batch count can be selected for the generation request.]

## Skill Version(s):

1.0.29 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
