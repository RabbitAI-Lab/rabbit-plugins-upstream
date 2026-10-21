## Description:

Creates visual previews of garment designs in a new fabric from a style image and fabric swatch while aiming to preserve the original silhouette.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Fashion designers and e-commerce teams use the skill to preview how a garment might look in different fabrics before making physical samples.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Supplied garment and fabric images, including photos of people or commercial designs, may be sent to an external image provider.

Mitigation: Only submit images and prompts approved for external processing; avoid private files and internal URLs.

Risk: Image generation may incur costs or expose credentials if handled carelessly.

Mitigation: Use dry-run to check routing and cost, and keep API keys in provider configuration or environment variables.

Risk: A visual preview may misrepresent garment construction or real-world fabric properties.

Mitigation: Check silhouette, seams, color, and texture against the source images, and label results as visual previews rather than physical samples.

## Reference(s):

- [Fabric on Body skill release](https://clawhub.ai/dlazyai/skills/fabric-on-body)
- [Provider CLI reference](artifact/references/provider-cli.md)
- [Image model options](artifact/references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Text]

**Output Format:** [Markdown with image-editing prompts and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images are visual previews, not physical fabric samples.]

## Skill Version(s):

1.0.24 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
