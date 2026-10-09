## Description:

Uses a garment style image and fabric swatch to preview the same garment silhouette in a different material.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Apparel designers and merchandisers use this skill to preview different fabrics on a garment before making physical samples. It provides image-generation instructions and helps check the resulting silhouette, texture, and color.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Garment images, fabric swatches, prompts, and generated outputs may be sent to a cloud image provider.

Mitigation: Use the skill only when sharing these materials with the selected provider is acceptable.

Risk: Untrusted image paths or URLs and an unchecked save destination may expose or overwrite unintended material.

Mitigation: Use trusted image sources and review the output path before running.

Risk: Unrelated shared tasks, including watermark removal, can be invoked without a legitimate purpose.

Mitigation: Avoid unrelated tasks unless you have the rights and a legitimate reason to use them.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/fabric-on-body)
- [Provider CLI reference](artifact/references/provider-cli.md)
- [Image model options](artifact/references/model-flags.md)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Files]

**Output Format:** [Markdown guidance and shell commands; generated JPEG images saved locally]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Images are visual previews, not guarantees of physical fabric behavior.]

## Skill Version(s):

1.0.18 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
