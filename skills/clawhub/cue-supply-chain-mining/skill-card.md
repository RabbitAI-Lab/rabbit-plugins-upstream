## Description:

用 Cue 沿产业链挖掘具备业绩爆发潜力的"隐形冠军"，梳理产业链传导路径，基于基本面与弹性逻辑发现未被充分定价的优质标的。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Buy-side researchers, industry analysts, individual investors, and industry practitioners use this skill to generate public-information A-share supply-chain research reports, identify lesser-known listed companies in specific industry chains, and understand fundamental transmission logic without receiving trade timing or buy/sell advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research queries and API-key authenticated requests are sent to the Cue service at cuecue.cn.

Mitigation: Confirm that the user trusts the Cue service and runner source before installation or execution.

Risk: Generated financial research may be mistaken for trading advice.

Mitigation: Treat outputs as informational fundamental research, review the cited sources, and do not use the skill for buy/sell prices, timing, or execution recommendations.

Risk: Report quality and freshness depend on Cue service availability and external public data sources.

Mitigation: Check returned source links and risk notes, and rerun or defer analysis when the service reports timeouts, unavailable sources, or empty results.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/panting09266-ai/skills/cue-supply-chain-mining)
- [Cue Runner Source](https://github.com/sensedeal/cue-skills)
- [Cue Runner Gitee Mirror](https://gitee.com/sensedeal/cue-skills)
- [Cue API Key](https://cuecue.cn/hub/api-key)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Guidance]

**Output Format:** [Markdown research report with supply-chain map, transmission logic, hidden-champion candidates, elasticity assessment, risk notes, and source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Cue API key and Cue runner; research jobs typically take 2-15 minutes depending on service load and external data-source availability.]

## Skill Version(s):

1.1.0 (source: server evidence release.version and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
