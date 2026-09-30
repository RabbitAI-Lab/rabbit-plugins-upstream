## Description:

Creates a visual garment preview using a style image and a fabric swatch, aiming to preserve the garment's cut while changing its material appearance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Apparel designers and merchandising teams use a garment style image and fabric swatch to compare material options before physical sampling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Garment images, fabric swatches, and prompts may be sent to the selected image-generation provider.

Mitigation: Use materials you are comfortable sharing and check the active provider and key with dry-run or doctor mode before generating.

Risk: Untrusted image sources or a substituted CLI binary may expose the workflow to unwanted content or behavior.

Mitigation: Use trusted image files or URLs and a trusted installation of the dLazy CLI.

## Reference(s):

- [Fabric on Body skill release](https://clawhub.ai/dlazyai/skills/fabric-on-body)
- [Provider CLI reference](artifact/references/provider-cli.md)
- [Image model flags](artifact/references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image files]

**Output Format:** [Markdown guidance and commands; generated garment preview image]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The image is a visual preview, not a physical fabric sample.]

## Skill Version(s):

1.0.15 (source: ClawHub release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
