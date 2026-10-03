## Description:

Creates a visual garment preview with a new fabric from a style reference and a fabric swatch while aiming to preserve the garment's cut and composition.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Fashion designers and e-commerce teams use the skill to preview how a garment might look in a different fabric before selecting materials or making physical samples.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Garment photos, fabric samples, prompts, and referenced image URLs may be sent to a selected cloud image provider.

Mitigation: Avoid sensitive personal photos and proprietary unreleased designs unless the provider's account and data policies permit their use.

Risk: Automatic provider selection and image generation may route data unexpectedly or incur charges.

Mitigation: Select the provider explicitly and use dry-run to check the request and estimated cost before generating.

Risk: The generated preview may not reflect the fabric's real feel, weight, or achievable drape.

Mitigation: Label results as visual previews and verify material suitability with physical samples before production.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/fabric-on-body)
- [Provider CLI and data flow](references/provider-cli.md)
- [Image generation options](references/model-flags.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image files]

**Output Format:** [Markdown guidance and commands; generated JPEG, PNG, or WebP previews]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Visual previews only; not physical fabric samples.]

## Skill Version(s):

1.0.16 (source: skill frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
