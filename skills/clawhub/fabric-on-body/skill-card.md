## Description:

Creates visual garment previews by applying a fabric swatch's material appearance to a garment reference image while aiming to preserve its cut and construction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Fashion designers and ecommerce teams use the skill to preview how a fabric swatch may look on a garment reference before producing physical samples.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected garment images and prompts are sent to the chosen cloud image provider, whose retention practices are not verified.

Mitigation: Choose an approved provider explicitly and confirm its data handling before sending confidential designs.

Risk: A generated image may not predict the physical fabric's hand or weight.

Mitigation: Treat the image as a visual preview and validate material choices with physical samples before production.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/fabric-on-body)
- [Provider CLI reference](references/provider-cli.md)
- [Image model flags](references/model-flags.md)
- [dLazy CLI source repository](https://github.com/dlazy-ai/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, Shell commands, Guidance]

**Output Format:** [Garment preview images (JPEG, PNG, or WebP) with Markdown prompts and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Visual previews only; they do not represent physical fabric hand or weight.]

## Skill Version(s):

1.0.29 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
