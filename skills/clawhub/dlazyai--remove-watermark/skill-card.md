## Description:

Guides agents in removing watermarks, text, logos, and promotional overlays from images while reconstructing obscured areas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and e-commerce teams use this skill to prepare authorized product images for reuse by removing overlaid text or graphics and reconstructing covered backgrounds.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Removing watermarks or logos can obscure ownership or misrepresent a product.

Mitigation: Edit only images you own or have permission to modify; do not remove legal marks or third-party branding.

Risk: Input images are sent to the selected cloud image-editing provider.

Mitigation: Review the selected provider and avoid uploading images you are not authorized to share.

Risk: Reconstructed regions and surrounding details can differ from the source image.

Mitigation: Inspect the result, especially obscured product details; use pixel-accurate editing when exact preservation is required.

## Reference(s):

- [Remove Watermark skill release](https://clawhub.ai/dlazyai/skills/remove-watermark)
- [Provider and CLI usage](references/provider-cli.md)
- [Image model options](references/model-flags.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with shell commands and image-editing prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Edited images require visual review because reconstructed areas may differ from the original.]

## Skill Version(s):

1.0.18 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
