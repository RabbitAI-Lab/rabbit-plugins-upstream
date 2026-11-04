## Description:

Transforms white-background product photos into realistic scene images with lighting and shadows matched to the new environment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce teams and developers use this skill to place product photos into realistic lifestyle scenes while preserving the product's appearance. It guides image selection, prompt writing, and image generation for product listings and marketing assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and prompts are sent to a cloud provider, whose retention practices were not independently verified.

Mitigation: Use images approved for cloud processing, select the provider explicitly, and check its retention terms.

Risk: Image generation may consume credits or save results to an unintended file path.

Mitigation: Preview the provider, batch size, and request with --dry-run before generation, and choose a fresh output path.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/item-change-background)
- [Provider CLI reference](artifact/references/provider-cli.md)
- [gpt-image-2 model flags](artifact/references/model-flags.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, Shell commands, Guidance]

**Output Format:** [Generated product-scene image files plus natural-language prompts and shell commands in Markdown guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts a product image and optionally a background image; generated image files are saved to the requested output path.]

## Skill Version(s):

1.0.29 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
