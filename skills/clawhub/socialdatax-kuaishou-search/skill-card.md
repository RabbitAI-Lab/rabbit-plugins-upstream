## Description:

用于快手数据分析、快手作品研究、关键词观察、内容调研、竞品分析和趋势研究。覆盖 Kuaishou / Kwai work research，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts and social media researchers use this skill to search Kuaishou videos by keyword and review results for content research, competitor analysis, and trend monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms are sent to SocialDataX, and API usage may incur charges.

Mitigation: Avoid confidential terms and consider account charges before running searches.

Risk: The downloaded CLI implementation and future package releases were not inspected.

Mitigation: Prefer a reviewed, pinned CLI version and inject the API key narrowly into the execution environment.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-kuaishou-search)

## Skill Output:

**Output Type(s):** [JSON, Analysis, Guidance]

**Output Format:** [Structured Kuaishou search results with concise Markdown summaries when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Keyword-based search with optional pagination; result completeness depends on the requested pages and available results.]

## Skill Version(s):

0.1.22 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
