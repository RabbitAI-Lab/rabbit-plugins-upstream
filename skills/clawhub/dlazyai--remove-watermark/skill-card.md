## Description:

去水印去文字。带水印 / 文字 / logo 的图 -> 干净图，背景纹理自然补全。当用户说「去水印」「去文字」「擦掉 logo」「把字去了」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and ecommerce content operators use this skill to guide image-editing agents that remove visible watermarks, text, badges, promotional frames, and similar overlays from product images while reconstructing the covered area. It is also positioned as a cleanup step before passing images to other ecommerce image-generation skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected images and prompts may be uploaded to dLazy or another configured AI provider, and provider credentials may incur cost.

Mitigation: Use approved images and provider accounts only, review provider routing before execution, and run dry-run or doctor checks when cost or credential exposure is a concern.

Risk: The bundled generation runner can perform broader AI generation tasks than watermark removal.

Mitigation: Review or restrict scripts/gen.mjs and scripts/lib/tasks.json if the deployment should be limited strictly to watermark-removal image edits.

Risk: Removed areas are reconstructed by a model and may not preserve original pixels or exact product details.

Mitigation: Require human review of edited images, especially where overlays cover product details; use professional image-editing tools when pixel-level preservation is required.

Risk: The skill could be misused to remove copyright watermarks, brand marks, or legally required labels.

Mitigation: Use only on images the user is authorized to edit, and do not remove ownership, legal, safety, certification, or product-compliance markings.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/remove-watermark)
- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 model flags](references/model-flags.md)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [Example watermarked source image](https://raw.githubusercontent.com/dlazyai/ecommerce-skills/main/docs/remove-watermark/source-watermarked.jpg)
- [Example cleaned output image](https://raw.githubusercontent.com/dlazyai/ecommerce-skills/main/docs/remove-watermark/example-output.jpg)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with prompt templates, inline bash commands, and saved image file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typical execution uses one input image and may save JPEG output files; configured cloud providers receive selected images, prompts, and generation parameters.]

## Skill Version(s):

1.0.1 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
