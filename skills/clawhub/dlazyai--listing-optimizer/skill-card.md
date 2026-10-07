## Description:

为电商商品主图设计单变量 A/B 对照，生成候选图片、实验假设和转化复盘模板。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

电商运营人员和商品营销团队使用此技能生成单变量主图对照与预先记录的假设，并在投放后填写点击和转化数据进行复盘。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and prompts may be sent to the selected image-generation provider.

Mitigation: Confirm the provider and its data policy before sending confidential or unreleased assets.

Risk: Image-generation calls may incur charges.

Mitigation: Use --dry-run to inspect the chosen provider and estimated cost before generating images.

Risk: Automatic image corrections may overwrite or alter source material.

Mitigation: Run check_listing.py --fix on copies or specify a separate output directory.

Risk: Built-in marketplace image rules may be outdated or unable to detect visual policy violations.

Mitigation: Check current platform requirements and manually review text, watermarks, and composites before publishing.

## Reference(s):

- [平台图片规格](references/platform-specs.md)
- [图像生成服务调用参考](references/provider-cli.md)
- [主图平台合规技能](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/platform-compliance/skill.md)
- [品牌素材管理技能](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/brand-kit/skill.md)

## Skill Output:

**Output Type(s):** [Image files, Markdown, Guidance]

**Output Format:** [Generated product images and Markdown experiment/review table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Performance data must be supplied by the user; the skill does not determine statistical significance.]

## Skill Version(s):

1.0.13 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
