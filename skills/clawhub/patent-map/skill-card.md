## Description:

将某一技术方向的专利统计整理为一页 HTML 可视化专利地图和数据表，涵盖趋势、主要申请人、地区、技术构成、专利类型及法律状态。

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

Patent researchers and technology teams use this skill to turn a technology query into presentation-ready patent statistics, a browser-ready visual map, and a data table.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reported credential-redirect and cache-path validation flaws could expose an API key or write files outside the intended cache.

Mitigation: Prefer a release that fixes these issues before using a valuable API key or sensitive workspace; keep production keys out of chat and verify where task data is stored.

Risk: Patent searches reach PatentMax and may spend account credit; submitted queries may contain sensitive information.

Mitigation: Use approved, nonconfidential search terms and set a spending limit before running searches.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/ip930/skills/patent-map)
- [PatentMax API platform](https://api.ip930.com/features/api-platform)
- [PatentMax API reference](references/api-reference.md)
- [Patent search workflow](references/search-workflow.md)
- [Patent query syntax](references/query-syntax.md)

## Skill Output:

**Output Type(s):** [Files, Analysis, Text]

**Output Format:** [Self-contained HTML patent map and UTF-8 CSV data table, with concise text conclusions.]

**Output Parameters:** [One technology query across six patent-statistics dimensions.]

**Other Properties Related to Output:** [HTML is browser-openable and designed for presentation or screenshots; statistics are limited to returned API data.]

## Skill Version(s):

1.0.1 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
