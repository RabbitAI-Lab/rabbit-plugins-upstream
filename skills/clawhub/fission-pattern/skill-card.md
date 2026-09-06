## Description:

一张商品图裂变成整套素材。商品图 + 卖点 -> 多角度多场景成套图，够铺满一屏。当用户说「裂变套图」「一张变一屏」「凑够详情页」「出一套图」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, ecommerce operators, and creative production teams use this skill to turn one product image plus selling points into a consistent set of product photos across multiple angles, scenes, and detail shots.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images, prompts, and optional brand or model references may be sent to the selected image-generation provider.

Mitigation: Use only inputs that are appropriate to share with the chosen provider, and review provider selection before running generation commands.

Risk: Generation commands can consume paid provider credits and write image files to local paths.

Mitigation: Run dry-run or doctor checks first, confirm credentials and output paths, and review commands before executing paid generation.

## Reference(s):

- [Model flags](references/model-flags.md)
- [Provider CLI](references/provider-cli.md)
- [dLazy CLI](https://github.com/dlazy-ai/cli)
- [Remove Watermark Skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/remove-watermark/skill.md)
- [Creative Scene Skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/creative-scene/skill.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents to generate and save ecommerce image sets through selected image-generation providers.]

## Skill Version(s):

1.0.5 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
