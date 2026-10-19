## Description:

使用 Cue 结合短期资金流向与中长期估值模型，分析个股的股价、业绩驱动与安全边际。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

投资研究人员和个人用户可用它研究个股或比较同业公司的短期走势、中长期估值及风险，并获取结构化研究报告。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs and runs a third-party Cue runner that may change when updated.

Mitigation: Install only if you trust the Cue service and runner repository; review or pin the runner before use.

Risk: Stock queries and Cue API authorization are sent to cuecue.cn.

Mitigation: Send only data you are comfortable sharing with Cue; manage the API key yourself.

Risk: Market data or valuation conclusions may be inaccurate or out of date.

Mitigation: Check source data and treat the report as research assistance, not investment advice.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/panting09266-ai/skills/cue-stock-valuation)
- [Cue platform](https://cuecue.cn)
- [Cue runner dependency on GitHub (listed in skill instructions; not release provenance)](https://github.com/sensedeal/cue-skills)
- [Cue runner dependency mirror on Gitee](https://gitee.com/sensedeal/cue-skills)
- [Cue API key management](https://cuecue.cn/api-key?src=clawhub-stock-valuation)

## Skill Output:

**Output Type(s):** [Financial analysis, Guidance]

**Output Format:** [Markdown report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes source links, a Cue report link when available, and a local Markdown copy.]

## Skill Version(s):

1.0.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
