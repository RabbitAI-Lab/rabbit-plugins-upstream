## Description:

房地产房源与备案价数据的查询、标准化与可视化分析工作流，支持定位项目、定位公开数据源、提取并标准化数据、生成多 Sheet Excel 报告、执行跨期对比与异常告警。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chriskinhaha](https://clawhub.ai/user/chriskinhaha)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to collect publicly available real-estate filing and listing data, normalize property and price fields, and produce Excel reports with statistics, historical comparisons, and anomaly alerts. Users must confirm the target platform allows automated access and must avoid authenticated, restricted, or non-public data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automation against real-estate platforms may violate terms, robots policies, access controls, or local legal requirements if used on an unsuitable source.

Mitigation: Confirm the target platform permits automated access before collection; stop when data requires authentication, restricted network access, or automation is prohibited.

Risk: Raw response caches may contain identifiers or other sensitive fields from public filing responses.

Mitigation: Delete or protect raw cache files such as output/api_captured.json and retain only the minimum data needed for analysis.

## Reference(s):

- [Real Estate Collection Technical Reference](references/real-estate-guide.md)
- [ClawHub Skill Page](https://clawhub.ai/chriskinhaha/skills/real-estate-filing-query)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with code and command examples for producing Excel reports and local JSON snapshots]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Expected artifacts include Excel workbooks, raw-response cache JSON, historical snapshot JSON, and concise analysis summaries.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
