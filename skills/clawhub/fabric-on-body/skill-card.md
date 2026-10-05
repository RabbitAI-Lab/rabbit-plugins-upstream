## Description:

Creates visual previews of a garment in a new fabric from a garment reference and fabric swatch while aiming to preserve its cut and construction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Fashion designers and ecommerce teams use a garment image and fabric swatch to compare how a style might look in different materials before physical sampling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Garment photos, fabric swatches, and prompts may be sent to a cloud image provider.

Mitigation: Use approved providers for sensitive designs; use dry-run or explicitly select the provider to check what will be sent.

Risk: Generated previews may not preserve every garment detail or reflect the fabric's real-world drape and weight.

Mitigation: Check silhouette, construction details, color, and texture against the inputs; label results as visual previews rather than physical samples.

## Reference(s):

- [Fabric on Body skill release](https://clawhub.ai/dlazyai/skills/fabric-on-body)
- [Provider and CLI usage](references/provider-cli.md)
- [Image model options](references/model-flags.md)
- [dLazy CLI source and documentation](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image files]

**Output Format:** [Markdown instructions and generated image previews]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Previews show appearance, not verified fabric feel, weight, or manufacturability.]

## Skill Version(s):

1.0.17 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
