## Description:

用 Cue 穿透基金组合的底层持仓，分析股票、行业和风格暴露，并检测重复配置与集中度风险。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, fund investors, advisors, and portfolio researchers use this skill to diagnose public fund portfolios for duplicated holdings, industry concentration, style exposure, and rebalancing considerations. It is intended for analysis of publicly disclosed Chinese public-fund holdings, not private funds, intraday holdings, or future performance prediction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends fund queries and a Cue API key to cuecue.cn as part of normal operation.

Mitigation: Install and use it only if you trust sensedeal/Cue, and avoid submitting sensitive portfolio details unless that data sharing is acceptable.

Risk: The workflow installs or updates an external Cue runner before use.

Mitigation: Review or pin the runner source before use in sensitive environments.

Risk: Optional Word or PDF export can require system package installation.

Mitigation: Skip optional sudo package installs unless document conversion is required.

Risk: Portfolio analysis relies on public fund disclosure data that can lag current holdings.

Mitigation: Treat results as decision support and check the report's disclosure date before acting on time-sensitive decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-fund-penetration)
- [Cue](https://cuecue.cn)
- [Cue API key setup](https://cuecue.cn/hub/api-key)
- [Cue runner source](https://github.com/sensedeal/cue-skills)
- [Cue runner Gitee mirror](https://gitee.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown report with source link, plus setup and troubleshooting commands when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include fund holdings analysis, overlap matrices, concentration ratings, rebalancing suggestions, and a Cue source link when available.]

## Skill Version(s):

1.0.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
