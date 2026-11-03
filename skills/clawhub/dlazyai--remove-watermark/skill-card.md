## Description:

Removes watermarks, text, badges, and decorative overlays from images and reconstructs the covered areas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

People preparing product or other photographs use this skill to remove unwanted overlays and create clean images for later editing or use by other skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images and prompts are sent to a cloud provider for processing, and existing credentials may affect provider routing.

Mitigation: Select the intended provider, preview with --dry-run, and review its privacy terms before submitting confidential images.

Risk: Reconstruction infers covered content and may subtly change other parts of the image.

Mitigation: Review the output against the original, especially where text covers the product, and use pixel-preserving editing when exact fidelity is required.

## Reference(s):

- [Provider and CLI reference](artifact/references/provider-cli.md)
- [Image model flags reference](artifact/references/model-flags.md)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [Fission Pattern skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/fission-pattern/skill.md)
- [Clothing Grass Planting skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/clothing-grass-planting/skill.md)
- [ClawHub release page](https://clawhub.ai/dlazyai/skills/remove-watermark)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Guidance]

**Output Format:** [Image files (JPEG by default) with Markdown guidance and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reconstructed areas are model-inferred and may subtly change the surrounding image.]

## Skill Version(s):

1.0.29 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
