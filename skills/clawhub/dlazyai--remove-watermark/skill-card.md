## Description:

去水印去文字。带水印 / 文字 / logo 的图 -> 干净图，背景纹理自然补全。当用户说「去水印」「去文字」「擦掉 logo」「把字去了」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, ecommerce operators, and developers use this skill to prepare cleaner product images by removing visible text, watermarks, badges, promotional frames, and similar overlays before downstream image workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected images and prompts may be sent to cloud image providers during use.

Mitigation: Use the skill only with images authorized for upload, avoid sensitive content, and confirm the selected provider and credentials before execution.

Risk: Watermark, logo, or text removal can be misused to obscure copyright, brand, legal, safety, or provenance markings.

Mitigation: Use the workflow only for authorized cleanup and do not remove marks in a misleading, unlawful, or safety-relevant context.

Risk: Covered areas are reconstructed by the image model rather than restored pixel-for-pixel.

Mitigation: Review outputs for residual text, changed perspective, texture artifacts, and incorrect reconstructed product details; use professional editing tools when exact pixel preservation is required.

## Reference(s):

- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 parameter reference](references/model-flags.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown instructions with inline shell commands; execution can save image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images are reconstructed outputs and should be reviewed before use.]

## Skill Version(s):

1.0.11 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
