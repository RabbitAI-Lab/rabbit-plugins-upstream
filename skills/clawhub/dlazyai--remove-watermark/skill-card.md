## Description:

Removes text, watermarks, logos, and promotional overlays from images while reconstructing covered areas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, and content teams use this skill to clean images they are authorized to edit, removing overlays and reconstructing obscured areas before reuse.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected images and prompts are sent to dLazy or the configured cloud provider.

Mitigation: Use only providers you trust for the images and prompts you submit.

Risk: Removing copyright, legal, safety, or authenticity markings could misrepresent an image or violate rights.

Mitigation: Edit only images you own or have permission to edit, and retain required markings.

Risk: Reconstructed regions or surrounding details may differ from the original image.

Mitigation: Inspect edited images and use a pixel-preserving tool when exact fidelity is required.

## Reference(s):

- [ClawHub release](https://clawhub.ai/dlazyai/skills/remove-watermark)
- [Provider and CLI reference](references/provider-cli.md)
- [Image model flags](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image files]

**Output Format:** [Markdown guidance and CLI commands; edited images in JPEG, PNG, or WebP]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Covered content is reconstructed, not restored pixel-for-pixel; review edited images for accuracy.]

## Skill Version(s):

1.0.21 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
