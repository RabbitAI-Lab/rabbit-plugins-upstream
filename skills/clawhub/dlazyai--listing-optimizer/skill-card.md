## Description:

根据商品图片和卖点规划主图 A/B 实验，生成对照图片方案、差异假设和复盘模板。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

电商运营人员可用它设计主图对照实验，每轮只改变一个变量并预先记录假设。它会提供图片生成指引和复盘模板；投放数据由使用者填写。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports a mismatch between the A/B testing purpose and the reported compliance and image-adjustment tools, and notes that four of ten components were only partially inspected.

Mitigation: Review the relevant tool behavior and manually check each generated image against the current platform requirements before relying on compliance results.

Risk: The security guidance flags external image API calls and validation error behavior as areas to review, especially when images are sensitive or compliance decisions matter.

Mitigation: Use only images approved for the selected provider, and inspect outputs and validation results before using them in a listing.

## Reference(s):

- [Platform image specifications](references/platform-specs.md)
- [Image generation provider guide](references/provider-cli.md)
- [Platform compliance skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/platform-compliance/skill.md)
- [Brand kit skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/brand-kit/skill.md)
- [ClawHub release](https://clawhub.ai/dlazyai/skills/listing-optimizer)

## Skill Output:

**Output Type(s):** [Images, Markdown, Guidance]

**Output Format:** [Generated image files and Markdown experiment plans or review templates, with image-generation command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The user supplies performance metrics; the skill does not connect to marketplace analytics or determine statistical significance.]

## Skill Version(s):

1.0.27 (source: SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
