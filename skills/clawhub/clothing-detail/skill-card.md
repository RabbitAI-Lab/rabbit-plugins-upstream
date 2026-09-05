## Description:

Generates e-commerce macro close-ups from clothing images, focusing on fabric texture, stitching, construction, and garment details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce content teams and agents use this skill to turn clear garment photos into 1:1 or vertical macro detail images for product detail pages. It is intended for collars, cuffs, hems, buttons, zippers, pockets, embroidery, prints, stitch structures, and fabric fibers that are visible in the source image.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Input clothing images and prompts may be sent to dLazy or another configured cloud provider.

Mitigation: Use dry-run first for request and cost visibility, avoid private or sensitive images, and choose the provider deliberately.

Risk: Provider API keys are required for configured cloud backends.

Mitigation: Store keys according to provider guidance, prefer environment variables or provider auth tooling, and rotate keys when access changes.

Risk: Generated macro details can misrepresent garments when the source image is low-resolution, compressed, or the target detail is obscured.

Mitigation: Use high-resolution source images, enlarge one visible detail at a time, and review outputs for invented construction, texture, or color changes before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/clothing-detail)
- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 model flags](references/model-flags.md)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy provider website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Code, Files, Guidance]

**Output Format:** [Markdown guidance with bash commands, provider configuration notes, local image output paths, and optional JSON run envelopes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default output is JPEG clothing detail imagery saved to local paths; dry-run mode reports request details and estimated credits without calling a provider.]

## Skill Version(s):

1.0.5 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
