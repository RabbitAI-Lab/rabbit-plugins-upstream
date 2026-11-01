## Description:

当用户需要做抖音趋势洞察、抖音趋势分析、热点观察、内容方向判断、趋势线索归纳或营销灵感整理时使用。面向内容运营、品牌调研和创作者。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

内容运营人员、品牌研究者和创作者可用此 skill 查询抖音热榜与关键词内容，并整理趋势信号、相关样本和后续分析角度。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms are sent to SocialDataX and could include confidential details.

Mitigation: Exclude secrets and confidential information from search terms.

Risk: An exposed API key could be misused.

Mitigation: Protect SOCIALDATAX_API_KEY in the user's environment and do not include it in skill files or queries.

Risk: Large page or item limits can increase usage charges.

Mitigation: Start with a small sample and limit pages or items to the amount needed.

Risk: The installed package may change when using an unpinned latest version, and read-only account behavior does not sandbox downloaded software.

Mitigation: Prefer a reviewed, pinned package version.

## Reference(s):

- [SocialDataX API key information](https://socialdatax.com/ai?from=clawhub)
- [SocialDataX billing](https://socialdatax.com/dashboard/billing)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/douyin-trend-insights)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Shell commands]

**Output Format:** [Trend results summarized in Markdown, with JSON data available from the CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only trend and search results may include rankings, heat signals, titles, authors, links or content IDs, and follow-up angles.]

## Skill Version(s):

0.1.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
