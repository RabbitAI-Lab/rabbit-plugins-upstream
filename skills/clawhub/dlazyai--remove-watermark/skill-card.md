## Description:

Removes watermarks, text, logos and promotional overlays from images while reconstructing the obscured background.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers and other image-editing users can prepare clean product images by removing authorized watermarks, text and promotional graphics and reconstructing covered areas.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Source images and prompts are sent to the configured cloud provider.

Mitigation: Use only if you are comfortable sharing the source images and prompts with that provider.

Risk: Removing copyright marks, required labels or brand identifiers can facilitate misuse.

Mitigation: Edit only images you own or are authorized to modify; do not remove legal or safety labels or impersonate a brand.

Risk: Inpainting can invent details or subtly change perspective and textures.

Mitigation: Review edited areas and product details before use; use professional retouching when pixel-level fidelity is required.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/remove-watermark)
- [Model flags](references/model-flags.md)
- [Provider CLI reference](references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Image files, Shell commands, Text guidance]

**Output Format:** [JPEG, PNG or WebP images with Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reconstructed areas are inferred and may differ from the original image.]

## Skill Version(s):

1.0.20 (source: SKILL.md frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
