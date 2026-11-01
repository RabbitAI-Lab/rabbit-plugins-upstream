## Description:

为电商商品主图规划单变量 A/B 测试，生成对照组方案、预设假设和复盘模板。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

电商运营人员和商品内容创作者可用它规划主图单变量实验、记录测试前的预期并复盘表现；平台数据需由用户填写，技能不判断统计显著性。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A compliance check can succeed even when an image could not be read, so a passing result may be incomplete.

Mitigation: Verify that each image loaded and review every compliance report manually; resolve unreadable images and checks that require human review.

Risk: Image-provider runs may spend credits or upload private product or model images.

Mitigation: Choose the provider explicitly and inspect a dry run before spending credits or uploading private images.

Risk: Optional installation tools and reused output folders can make runs harder to reproduce or review.

Mitigation: Pin optional installation tools and use a fresh output directory for each experiment.

## Reference(s):

- [Platform image specifications](references/platform-specs.md)
- [Image provider reference](references/provider-cli.md)
- [Platform compliance skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/platform-compliance/skill.md)
- [Brand kit skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/brand-kit/skill.md)

## Skill Output:

**Output Type(s):** [Images, Markdown, Shell commands, Guidance]

**Output Format:** [Generated product images, Markdown experiment plans and review tables, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Performance data is supplied by the user; image generation requires a configured provider.]

## Skill Version(s):

1.0.21 (source: SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
