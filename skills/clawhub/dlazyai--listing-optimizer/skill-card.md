## Description:

主图 A/B 组与转化复盘。商品图 + 卖点 → 多组对照主图 + 每组的差异假设 + 复盘模板。当用户说「A/B 测试」「主图优化」「提点击率」「哪版更好」「换个版本试试」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

电商运营人员可用它为商品主图设计单变量 A/B 实验，生成带事前假设的对照图，并准备由自己填写投放数据的复盘模板。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scanner reported a mismatch with the stated purpose and only partial component inspection; its verdict was benign with medium confidence.

Mitigation: Review the relevant scripts and behavior before using the skill, especially components the scan did not fully inspect.

Risk: The scanner noted external API calls.

Mitigation: Review the provider calls and decide whether the listed image-generation and listing-compliance capabilities fit your needs before authorizing use.

## Reference(s):

- [Platform image specifications](references/platform-specs.md)
- [Provider CLI guide](references/provider-cli.md)
- [Platform compliance skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/platform-compliance/skill.md)
- [Brand kit skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/brand-kit/skill.md)

## Skill Output:

**Output Type(s):** [Images, Markdown, Shell commands]

**Output Format:** [Generated image files, experiment hypotheses, and a Markdown review template; optional image-compliance check results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Each experiment changes one variable. Marketplace metrics must be entered by the user; the skill does not connect to platform analytics or determine statistical significance.]

## Skill Version(s):

1.0.28 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
