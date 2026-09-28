## Description:

Creates visual previews of a garment in a new fabric from a garment reference and a fabric swatch while aiming to preserve the original design.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Fashion designers and product teams use this skill to preview how different fabrics might look on an existing garment design before making physical samples.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Garment, fabric, and on-body reference images and prompts are sent to the configured cloud image provider.

Mitigation: Use local files or trusted public image URLs; avoid private URLs and sensitive personal photos, and confirm you are comfortable sharing the inputs with the provider.

Risk: Cloud image generation may incur charges and requires provider credentials.

Mitigation: Review provider credentials and billing before running generation commands.

Risk: A visual preview may misrepresent fabric color, texture, drape, or garment details.

Mitigation: Check the output against both references and label it as a visual preview rather than a physical sample.

## Reference(s):

- [Fabric on Body on ClawHub](https://clawhub.ai/dlazyai/skills/fabric-on-body)
- [Provider setup and data flow](references/provider-cli.md)
- [Image generation parameters](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Images, Shell commands, Guidance]

**Output Format:** [Generated garment preview images with Markdown guidance and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Visual previews only; not a guarantee of real fabric drape, weight, or feel.]

## Skill Version(s):

1.0.14 (source: frontmatter, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
