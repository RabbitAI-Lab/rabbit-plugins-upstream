## Description:

Removes watermarks, text, logos, and promotional graphics from images by reconstructing the covered areas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce image editors and other image creators use this skill to remove unwanted text, watermarks, badges, and frames from images before further editing or derivative-image workflows. The reconstructed areas may differ from the original image, so review the result when visual accuracy matters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan rates this skill suspicious because scanners report a mismatch between its stated image-cleanup purpose and some described or detected behavior, while analysis was incomplete.

Mitigation: Review whether the skill's behavior matches the image-cleanup task, check the external provider destinations before sending images, and limit network and environment access to what is needed.

## Reference(s):

- [Provider CLI and data flow reference](artifact/references/provider-cli.md)
- [Model flags reference](artifact/references/model-flags.md)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/remove-watermark)
- [Publisher profile](https://clawhub.ai/user/dlazyai)
- [Related workflow: fission-pattern](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/fission-pattern/skill.md)
- [Related workflow: clothing-grass-planting](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/clothing-grass-planting/skill.md)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Image files, Shell commands, Guidance]

**Output Format:** [Edited image files (typically JPEG), with prompts and shell commands documented in Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image reconstruction is inferential and may alter covered content or make small changes elsewhere in the image.]

## Skill Version(s):

1.0.31 (source: frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
