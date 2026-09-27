## Description:

Generates macro e-commerce detail images from clothing photos, focusing on fabric texture, stitching, weave, and visible construction details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce operators, merchandisers, and creative production teams use this skill to turn garment product images into close-up detail shots for collars, cuffs, hems, buttons, zippers, embroidery, prints, weave structures, and fabric fibers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled generation runner can send prompts and images to cloud providers and supports tasks beyond this clothing-detail workflow.

Mitigation: Use only images suitable for the selected provider, pin or restrict the provider when possible, avoid sensitive local files, and review command parameters before execution.

Risk: Low-quality, obstructed, or unclear source images can lead to unrealistic textures or invented garment construction details.

Mitigation: Use high-resolution source images where the target detail is visible, generate one detail area per prompt, and add explicit instructions not to invent construction details.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/clothing-detail)
- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 parameter reference](references/model-flags.md)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown guidance with inline bash commands and optional JavaScript helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces prompts and commands for image generation; saved assets are JPEG clothing-detail images when the commands are executed.]

## Skill Version(s):

1.0.13 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
