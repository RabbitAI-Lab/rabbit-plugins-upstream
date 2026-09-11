## Description:

Generates macro clothing detail images for e-commerce pages, focusing on fabric texture, stitching, weave structure, and visible construction details from a source garment image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, merchants, and e-commerce content teams use this skill to turn normal garment product images into close-up detail images for collars, cuffs, hems, buttons, zippers, embroidery, prints, knit structures, and fabric fibers. Developers and agents can use the bundled commands and helper scripts to generate saved JPEG outputs through a configured image provider.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected garment images and prompts may be uploaded to a configured cloud generation provider.

Mitigation: Use only approved providers, avoid sensitive or private images, and use least-privileged API keys that can be rotated or revoked.

Risk: A custom ARK_BASE_URL could route requests to an untrusted endpoint.

Mitigation: Leave ARK_BASE_URL unset unless the endpoint is a trusted HTTPS service controlled by the user or organization.

Risk: The bundled shared task configuration includes a remove-watermark task that may be unnecessary for this clothing-detail workflow.

Mitigation: Review or remove the remove-watermark task before installation if the deployment does not require it.

Risk: Low-quality, obstructed, or unclear source images can lead to invented or misleading garment details.

Mitigation: Use high-resolution images where the target garment area is visible, and prompt the model not to invent construction details that are absent from the source.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/clothing-detail)
- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 parameter list](references/model-flags.md)
- [dLazy website](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash commands; generated assets are saved image files, typically JPEG.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The documented flow uses one garment source image, optional style reference images, high-quality image generation, and optional JSON command output.]

## Skill Version(s):

1.0.8 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
