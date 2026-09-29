## Description:

Helps remove watermarks, text, badges, and decorative overlays from authorized images while reconstructing the covered background.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and e-commerce teams use this skill to prepare clean versions of images they own or are authorized to edit by removing promotional text and overlays before reuse in other workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected images and prompts may be sent to third-party cloud image providers.

Mitigation: Choose the provider deliberately and review credentials before submitting sensitive customer, product, or copyrighted material.

Risk: Removing watermarks or labels from images without authorization can misrepresent ownership or obscure required notices.

Mitigation: Use only images you own or are authorized to edit; do not remove others' copyright marks or legally required labels.

Risk: Image reconstruction can alter perspective, textures, or covered product details.

Mitigation: Inspect edited images and use professional retouching when original pixels or exact product details must be preserved.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/remove-watermark)
- [Provider CLI reference](artifact/references/provider-cli.md)
- [Image model options](artifact/references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image files]

**Output Format:** [Markdown instructions and edited JPEG, PNG, or WebP images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reconstructed regions are inferred and may differ from the original image.]

## Skill Version(s):

1.0.14 (source: skill frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
