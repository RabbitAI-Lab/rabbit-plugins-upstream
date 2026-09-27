## Description:

Removes visible watermarks, text, logos, badges, coupon bars, and decorative frames from user-provided images, then reconstructs covered areas with image-editing models.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to prepare cleaner ecommerce or product images by removing overlays before passing images into downstream generation or editing workflows. Users should review the result because covered areas are reconstructed rather than pixel-preserved.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Input images and prompts may be sent to the configured cloud image provider.

Mitigation: Do not use confidential images or sensitive prompts unless the chosen provider and account controls are acceptable.

Risk: The skill can remove copyrighted watermarks, legal labels, or brand identifiers.

Mitigation: Use it only on assets you are authorized to alter, and do not remove required legal, safety, certification, or ownership marks.

Risk: Edited regions are reconstructed by a model and may change perspective, texture, or product details.

Mitigation: Review outputs manually, especially where text or marks covered product-critical areas; use professional retouching when pixel-level fidelity is required.

Risk: Generated files are saved to user-selected paths.

Mitigation: Run with --dry-run first when appropriate and choose --save destinations deliberately.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/remove-watermark)
- [Provider CLI reference](artifact/references/provider-cli.md)
- [gpt-image-2 parameter list](artifact/references/model-flags.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy provider](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Files]

**Output Format:** [Markdown guidance with bash commands and generated image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May upload input images and prompts to the configured cloud image provider; generated images can be saved as JPEG, PNG, or WebP files.]

## Skill Version(s):

1.0.13 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
