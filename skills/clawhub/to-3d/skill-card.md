## Description:

Converts flat-lay garment photos into ghost-mannequin 3D product images with realistic volume while preserving garment details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce operators, designers, and agent developers use this skill to turn single flat-lay clothing images into product-ready ghost-mannequin views. It helps prepare prompts and commands that preserve garment color, pattern, ribbing, labels, and proportions while adding realistic volume.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and garment images may be sent to the configured cloud image provider for generation.

Mitigation: Use dry-run and provider selection before running, avoid sensitive or unreleased product imagery unless that provider is approved, and review configured credentials.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/to-3d)
- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 parameter reference](references/model-flags.md)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash commands and generated JPEG image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports square and vertical image sizes, JPEG output, optional batching, dry-run cost checks, and provider selection.]

## Skill Version(s):

1.0.13 (source: evidence release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
