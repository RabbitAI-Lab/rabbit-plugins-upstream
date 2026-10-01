## Description:

Turns flat-lay clothing photos into dimensional ghost-mannequin product images while aiming to preserve garment details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and creative teams use this skill to turn single-garment flat-lay photos into dimensional product imagery without photographing a model.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Garment photos and prompts are sent to the selected image provider.

Mitigation: Use an approved provider and avoid sensitive or confidential product imagery unless authorized.

Risk: Saving a generated image to an existing path may overwrite a file.

Mitigation: Choose a unique output path for each generation.

Risk: Generated images may alter garment proportions or material details.

Mitigation: Inspect outputs against the source photo before using them in product listings.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/to-3d)
- [Provider CLI guide](artifact/references/provider-cli.md)
- [Model flags](artifact/references/model-flags.md)
- [dLazy CLI documentation and source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image files]

**Output Format:** [Markdown instructions and CLI commands; generated product images saved as JPEG files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports dry-run cost estimates, image-size options, and explicit output paths.]

## Skill Version(s):

1.0.15 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
