## Description:

帮助内容运营、品牌研究人员和创作者分析小红书热榜与搜索结果，发现话题趋势和内容方向。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Content teams, brand researchers, and creators use this skill to examine Xiaohongshu hot searches and keyword results, identify emerging topics, and develop content ideas from cited examples.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs the latest npm package at use time, so its behavior may change without review.

Mitigation: Review the package and pin an approved version before enabling execution with an API key.

Risk: Returned Xiaohongshu note links can contain potentially sensitive xsec_token values.

Mitigation: Limit access to outputs and logs containing full note links; avoid sharing them publicly.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/xhs-trend-insights-v2)
- [SocialDataX API key and service](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with ranked topics, search examples, and analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only insights from available hot-list and paginated search results; results may include tokenized note links.]

## Skill Version(s):

0.1.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
