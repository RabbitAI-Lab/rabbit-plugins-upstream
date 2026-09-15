## Description:

Generates macro clothing detail images from garment photos, focusing on visible fabric texture, stitching, weave structure, and construction details for e-commerce product pages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce operators, creative teams, and agents use this skill to turn clear garment product photos into close-up product detail images. It is intended for visible garment areas such as collars, cuffs, hems, buttons, zippers, embroidery, prints, knit structures, and fabric fibers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence flags broad network and credential handling in helper scripts.

Mitigation: Install only when the workflow and operators are trusted, use approved provider credentials, and avoid custom provider base URLs unless they are verified HTTPS endpoints you control.

Risk: Local images, prompts, and generated outputs may be sent to cloud image providers selected by configuration.

Mitigation: Prefer local image files from trusted sources, avoid untrusted image URLs, and do not process sensitive unreleased designs unless the selected provider is approved for that data.

Risk: Low-resolution, compressed, or occluded garment photos can lead to invented or misleading construction details.

Mitigation: Use high-resolution inputs where the target area is clearly visible, prompt against invented details, and review outputs for texture realism, color consistency, and source-faithful construction.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/clothing-detail)
- [gpt-image-2 parameter reference](references/model-flags.md)
- [Provider CLI reference](references/provider-cli.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [Example input image](https://raw.githubusercontent.com/dlazy-ai/ecommerce-skills/main/docs/clothing-detail/garment-flatlay.jpg)
- [Example output image](https://raw.githubusercontent.com/dlazy-ai/ecommerce-skills/main/docs/clothing-detail/example-output.jpg)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Image files]

**Output Format:** [Markdown guidance with bash command examples; generated JPEG image files when executed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default clothing-detail generation uses high-quality JPEG output, typically 1024x1024 for square detail images or 1024x1536 for vertical product detail pages.]

## Skill Version(s):

1.0.9 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
