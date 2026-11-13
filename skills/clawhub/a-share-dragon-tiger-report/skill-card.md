## Description:

生成中文 A 股涨停板与龙虎榜研究报告，并结合四层筛选框架提供市场分析、观察名单和风险情景。

This skill is for research and development only.

## Publisher:

[yjkj999999](https://clawhub.ai/user/yjkj999999)

### License/Terms of Use:

MIT-0

## Use Case:

A 股研究者可按交易日整理涨停板、龙虎榜、行业与个股信息，生成结构化研判报告、观察名单和风险情景，供教育与研究参考。

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Scanner guidance flags repository publishing and delete-on-install workflows for review.

Mitigation: Before following those steps, inspect the destination, staged files, and exact files that would be removed.

Risk: The security review reports fail-open screening and financial reports whose conclusions may conflict with their stated safeguards; coverage was partial (47 of 57 components fully inspected).

Mitigation: Independently review the screening and report safeguards, and inspect components not fully covered before installation or use.

Risk: Market inputs may be delayed or fall back to sample data, which can make a report unsuitable as current trading information.

Mitigation: Check the report's data date, source, and delay; treat its conclusions as education and research, not investment advice.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/yjkj999999/skills/a-share-dragon-tiger-report)
- [SEC filing referenced by the skill](https://www.sec.gov/Archives/edgar/data/2130357/000162828026067168/anthropicpbc-sx1.htm)
- [Project homepage listed in source metadata](https://github.com/yjkj999999/a-share-dragon-tiger-strategy)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, HTML, PDF, PowerPoint]

**Output Format:** [Structured Chinese research reports and supporting analysis; HTML and PDF by default, with optional PowerPoint output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Daily A-share coverage; reports should identify the data date, source, latency, and any sample-data fallback.]

## Skill Version(s):

4.0.3 (source: artifact frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
