## Description:

Guides image generation that turns flat-lay garment photos into dimensional ghost-mannequin product images while aiming to preserve the garment's visible color, pattern, and construction details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and ecommerce developers use the skill to create dimensional product images from single-garment flat-lay photos for catalog and product listings, with guidance for retaining the garment's visible details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected images and prompts are sent to a cloud provider for processing, which may expose confidential garment designs.

Mitigation: Choose the provider explicitly, review its privacy terms before uploading confidential designs, and use --dry-run to check routing and estimated cost.

Risk: Existing environment credentials can affect provider routing, and an unreviewed CLI version may introduce avoidable risk.

Mitigation: Set the provider explicitly with --provider and install a reviewed CLI version.

## Reference(s):

- [Provider CLI reference](references/provider-cli.md)
- [Model flags reference](references/model-flags.md)
- [ClawHub release](https://clawhub.ai/dlazyai/skills/to-3d)
- [dLazy](https://dlazy.com)
- [One-shot skill for worn-garment photos](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/one-shot/skill.md)
- [Material enhancement skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/material-enhancement/skill.md)

## Skill Output:

**Output Type(s):** [Images, Shell commands, Guidance]

**Output Format:** [JPEG product images with accompanying prompts and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports square 1:1 and portrait 3:4 compositions; image generation may vary across batch outputs.]

## Skill Version(s):

1.0.25 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
