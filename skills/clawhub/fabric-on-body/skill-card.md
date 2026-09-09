## Description:

Fabric on Body helps agents generate garment preview images by applying a supplied fabric swatch to an existing garment style reference while preserving the garment shape and construction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External fashion and e-commerce users use this skill to preview how a garment pattern or style reference would look in a different fabric before sampling. Developers can use the bundled commands and configuration to run repeatable fabric-swatch-to-garment image generation workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper code can fetch arbitrary image URLs from the user's machine and send selected prompts and images to the configured image-generation provider.

Mitigation: Prefer local trusted image files, avoid internal or private URLs, review all image sources before execution, and disclose provider data transfer before use.

Risk: Generated garment images may not reflect real-world fabric hand feel, weight, or manufacturing feasibility.

Mitigation: Treat outputs as visual previews only and validate fabric choices through normal sampling or product review before production decisions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/fabric-on-body)
- [Provider CLI Reference](artifact/references/provider-cli.md)
- [gpt-image-2 Parameter List](artifact/references/model-flags.md)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with bash commands; generated JPEG image files when executed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses ordered garment-reference and fabric-swatch image inputs; generated images are visual previews, not physical sampling evidence.]

## Skill Version(s):

1.0.7 (source: server release, SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
