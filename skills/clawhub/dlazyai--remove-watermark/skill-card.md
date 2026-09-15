## Description:

Removes watermarks, text, badges, promotional borders, and similar overlays from images, then reconstructs the covered areas for cleaner product-photo inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, ecommerce operators, and developers use this skill to prepare cleaner product images by removing visible text, watermarks, badges, borders, coupons, and similar overlays before downstream image-generation workflows. Users should review reconstructed areas because the covered content is inferred rather than pixel-preserved.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Source images and prompts can be uploaded to cloud providers during generation.

Mitigation: Install only if this data transfer is acceptable, and avoid private, regulated, or rights-sensitive images unless the selected provider and account policy permit that use.

Risk: Provider routing and custom endpoint settings can send images, prompts, or credentials outside the expected cleanup workflow.

Mitigation: Prefer the documented dLazy or fixed provider endpoints, avoid custom ARK_BASE_URL values, and verify provider configuration before execution.

Risk: Removed regions are reconstructed by a model and may alter perspective, texture, or product details.

Mitigation: Review outputs for fidelity and use professional editing tools when pixel-level preservation is required.

Risk: The skill can be misused to remove copyright watermarks, brand marks, or required legal labels.

Mitigation: Use only on images the user has rights to edit, and do not remove legal, safety, certification, or ownership marks for deceptive purposes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/remove-watermark)
- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 model flags](references/model-flags.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy provider information](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with command examples; generation runs can save image files and return JSON result envelopes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include cleaned JPEG, PNG, or WebP image files; batch mode can produce multiple variants for review.]

## Skill Version(s):

1.0.9 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
