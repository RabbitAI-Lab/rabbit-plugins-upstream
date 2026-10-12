## Description:

Enhances garment texture in product photos using a high-resolution image of the same item as a reference while aiming to preserve the model, composition, and color.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce creators and image editors use this skill to restore realistic fabric detail in an otherwise usable clothing photo, guided by a high-resolution image of the same product.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and prompts are sent to the configured cloud image provider.

Mitigation: Use only providers whose terms permit the assets; avoid sensitive unreleased images without authorization.

Risk: Image-editing requests may incur charges.

Mitigation: Run a dry-run first to inspect requests and estimated cost.

Risk: Embedding API keys in prompts or files may expose credentials.

Mitigation: Keep keys in standard environment variables or provider CLI configuration.

Risk: Edited images may alter color, model details, or background along with fabric texture.

Mitigation: Compare each output with the source and reject images that change non-fabric details.

## Reference(s):

- [Provider CLI reference](references/provider-cli.md)
- [Image model flags](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image files]

**Output Format:** [Markdown instructions and commands; generated JPEG images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses an original photo and a high-resolution product reference; output should be checked against the original.]

## Skill Version(s):

1.0.19 (source: frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
