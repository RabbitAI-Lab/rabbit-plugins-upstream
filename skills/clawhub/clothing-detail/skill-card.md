## Description:

Generates macro clothing-detail images from garment photos, focusing on fabric texture, stitching, weave, and construction details for e-commerce product pages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketers, and e-commerce operators use this skill to turn product photos into macro close-ups for product detail pages, such as collar, cuff, stitch, weave, zipper, button, embroidery, and fabric-texture shots.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images, prompts, and brand reference images may be sent to the configured cloud provider.

Mitigation: Use only provider configurations approved for the data being processed, and run --doctor or --dry-run to confirm the selected backend before uploading sensitive or unreleased designs.

Risk: Generated close-ups can invent or misrepresent construction details when the source image is low-resolution, compressed, obscured, or asks for too many target areas at once.

Mitigation: Use clear high-resolution source images, focus each prompt on one visible garment area, and review outputs for texture realism, color consistency, and nonexistent details before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/clothing-detail)
- [gpt-image-2 parameter reference](references/model-flags.md)
- [Provider CLI reference](references/provider-cli.md)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown guidance with prompt templates, bash command examples, and optional JavaScript/YAML helper files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can save generated image files locally and may emit JSON envelopes for dry-run or scripted workflows.]

## Skill Version(s):

1.0.11 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
