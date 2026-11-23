## Description:

Creates visual previews of a garment style in a different fabric using a garment style image and a fabric swatch.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Apparel designers and product teams use the skill to preview how a fabric swatch may look on an existing garment style before physical sampling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Image processing may send supplied images to an external service, which may not be appropriate for every image.

Mitigation: Before use, confirm that external image processing is acceptable for the images being supplied.

Risk: The security scan is partial, with some executable scripts and provider code not fully analyzed.

Mitigation: Before installation, consider whether the additional generator modes and tool scope fit the intended use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/fabric-on-body)
- [Model flags reference](references/model-flags.md)
- [Provider CLI reference](references/provider-cli.md)
- [dLazy](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Image files, Shell commands, Guidance]

**Output Format:** [Visual image previews, with Markdown guidance and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a garment style image and fabric swatch as inputs; previews do not represent a physical sample or guarantee real-world fabric properties.]

## Skill Version(s):

1.0.35 (source: frontmatter, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
