## Description:

Removes watermarks, text, logos, badges, promotional frames, and similar overlays from images, then reconstructs the covered background with natural-looking texture.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and ecommerce content operators use this skill to prepare cleaner product images by removing visible watermarks, text, logos, badges, coupon bars, and decorative frames before downstream image-generation workflows. Outputs require human review because covered regions are reconstructed rather than pixel-preserved.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can be used on private, regulated, copyrighted, or third-party branded images.

Mitigation: Use it only on images the operator has rights to edit, and review intended use before installation or execution.

Risk: Prompts and input images may leave the local machine when cloud backends are used.

Mitigation: Prefer a vetted provider configuration and confirm data-handling requirements before submitting sensitive images.

Risk: The artifact includes an optional npx-based CLI path that depends on package-source trust.

Mitigation: Avoid the optional npx path unless the package source and version are trusted.

Risk: Removed areas are reconstructed by a model and may alter perspective, texture, or occluded product details.

Mitigation: Manually inspect outputs for residual text, changed composition, and inaccurate reconstruction before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/remove-watermark)
- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 parameter reference](references/model-flags.md)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [Example input image](https://raw.githubusercontent.com/dlazy-ai/ecommerce-skills/main/docs/remove-watermark/source-watermarked.jpg)
- [Example output image](https://raw.githubusercontent.com/dlazy-ai/ecommerce-skills/main/docs/remove-watermark/example-output.jpg)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code, markdown]

**Output Format:** [Markdown guidance with shell command examples and optional JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces or saves cleaned image files through configured cloud image-generation providers; batch mode may create multiple candidate outputs.]

## Skill Version(s):

1.0.8 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
