## Description:

Combines up to eight product photos into a styled ecommerce image of a complete outfit on one model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce teams and creators use product photos to plan and generate complete outfit images for listings and campaigns, optionally matching a reference pose or model.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product photos, reference images, and prompts are uploaded to the selected generation provider.

Mitigation: Preview requests with --dry-run, choose a trusted provider, and avoid uploading sensitive material.

Risk: Using third-party or licensed images without permission can violate others' rights.

Mitigation: Use only images you own or are authorized to process and publish.

Risk: Generated outfits may omit, merge, or alter product details.

Mitigation: Review each generated image against its inputs before publishing.

Risk: Bundled shared scripts include additional ecommerce generation helpers beyond image fusion.

Mitigation: Review the bundled scripts before running them if the additional capabilities are not expected.

## Reference(s):

- [ClawHub Image Fusion release](https://clawhub.ai/dlazyai/skills/image-fusion)
- [Provider and data-flow guide](references/provider-cli.md)
- [Image model options](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image files]

**Output Format:** [Markdown guidance and shell commands; generated ecommerce images saved locally]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts up to eight product photos per outfit, with optional pose and model references; results require visual review.]

## Skill Version(s):

1.0.21 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
