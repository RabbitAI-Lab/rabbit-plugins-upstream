## Description:

当用户需要做小红书趋势洞察、小红书趋势分析、热点观察、内容方向判断、趋势线索归纳或营销灵感整理时使用。面向内容运营、品牌调研和创作者。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Content operations teams, brand researchers, marketers, and creators use this skill to inspect Xiaohongshu trend signals, search topic samples, compare hot-list and keyword results, and turn visible evidence into content or marketing angles.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Returned XHS note URLs can be share-sensitive when exported or forwarded outside the user's workspace.

Mitigation: Review reports before sharing and limit distribution of full returned XHS links to audiences that should receive the original URLs.

Risk: The skill depends on a SocialDataX API key and local Node.js/npm availability.

Mitigation: Configure SOCIALDATAX_API_KEY only in the user environment and confirm node, npm, and network access before running the CLI commands.

## Reference(s):

- [SocialDataX AI homepage](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/xhs-trend-insights-v2)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with CLI examples and trend-analysis summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include rankings, heat signals, titles, author or account names, full returned XHS note URLs or content IDs, and suggested follow-up questions.]

## Skill Version(s):

0.1.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
