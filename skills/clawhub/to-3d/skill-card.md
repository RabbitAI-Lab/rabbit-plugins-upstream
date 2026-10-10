## Description:

Turns flat-lay garment photos into dimensional ghost-mannequin product images while aiming to preserve the original garment details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and creative teams use this skill to turn flat-lay clothing photographs into dimensional, model-free product images for listings and detail pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product images and prompts are sent to the configured image provider.

Mitigation: Use --dry-run to inspect requests, select an approved provider explicitly, and avoid confidential images unless that provider is approved.

Risk: Generated garment details or proportions may not match the source photo.

Mitigation: Review generated images against the original for color, fabric pattern, fit, and unintended mannequin or body parts before publishing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/to-3d)
- [Provider setup and output guide](artifact/references/provider-cli.md)
- [Image model options](artifact/references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image files]

**Output Format:** [Markdown guidance and CLI commands; generated JPEG product images saved locally]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports square or portrait images, quality settings, and multiple candidates for review.]

## Skill Version(s):

1.0.19 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
