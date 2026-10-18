## Description:

为电商商品主图设计单变量 A/B 对照、生成候选图，并提供记录假设和转化结果的复盘模板。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

电商运营和营销团队用它对比商品主图的单一变化，记录预期效果，并在投放后填入曝光、点击和转化数据进行复盘。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images, prompts, and brand references may be sent to a cloud image provider.

Mitigation: Review requests with --dry-run, select an approved provider, and avoid confidential assets unless its terms permit them.

Risk: Outdated platform rules or insufficient experiment data can lead to rejected images or unreliable conclusions.

Mitigation: Check current platform requirements and review image compliance; supply performance data and avoid conclusions from small samples.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/listing-optimizer)
- [Platform image specifications](references/platform-specs.md)
- [Image provider usage](references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Image files]

**Output Format:** [Markdown A/B experiment plan and recap table with generated product images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Records a hypothesis per variant; performance metrics are entered by the user.]

## Skill Version(s):

1.0.18 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
