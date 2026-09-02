## Description:

Transforms an existing e-commerce model or mannequin photo into new model and background variants while keeping the product unchanged.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce teams and developers use this skill to prepare prompts and generation commands for replacing the model, background, or both in a product photo while preserving garment details for market and campaign variants.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product and model images may be sent to cloud image-generation providers.

Mitigation: Install and run the skill only where cloud processing is acceptable, and review provider data handling before using sensitive or restricted product imagery.

Risk: The skill supports demographic model changes for advertising, including ethnicity, skin tone, age, and face-reference workflows.

Mitigation: Require explicit user direction, consent where applicable, and human review for compliance with advertising, platform, anti-discrimination, and likeness rules.

Risk: Generated variants may alter garment details, model anatomy, lighting, or product positioning.

Mitigation: Review outputs against the source image for product preservation, hand anatomy, lighting consistency, and garment alignment before publication.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/one-shot)
- [Provider CLI Reference](references/provider-cli.md)
- [gpt-image-2 Model Flags](references/model-flags.md)
- [dLazy CLI](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Files]

**Output Format:** [Markdown with inline shell commands and saved image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses image inputs and can save generated JPEG outputs; dry-run mode can estimate cost before execution.]

## Skill Version(s):

1.0.4 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
