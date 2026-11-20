## Description:

Refines product photos by smoothing random wrinkles, aligning layouts, evening lighting, and cleaning backgrounds while preserving product details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and product-content teams use this skill to prepare catalog-ready product images from casual product photos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends images and prompts to a hosted image-processing service, and some bundled content was only partially analyzed.

Mitigation: Use only images you are comfortable sending to the selected provider, and review the bundled files before use.

Risk: Generated edits may alter product details or conceal defects.

Mitigation: Compare each result with its source image, checking product structure, color, hardware, and visible damage before publication.

## Reference(s):

- [Image model flags](references/model-flags.md)
- [Provider CLI reference](references/provider-cli.md)
- [dLazy](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [Related material enhancement skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/material-enhancement/skill.md)

## Skill Output:

**Output Type(s):** [Image files, Shell commands, Prompt text, Guidance]

**Output Format:** [Edited product images (JPEG, PNG, or WebP) with command and prompt examples in Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts 1–4 images of the same product; image size, quality, format, and save path can be specified. Generated edits should be checked against the source images.]

## Skill Version(s):

1.0.34 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
