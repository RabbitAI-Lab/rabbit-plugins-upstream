## Description:

用 Cue 一键深度拆解热门赛道与 ETF，支持赛道全景分析、同类 ETF 横向对比、底层持仓穿透和估值水位研判。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

ETF investors, financial advisors, and asset allocators use this skill to research A-share sector and thematic ETFs, compare ETF products, inspect holdings exposure, and frame valuation and risk considerations before making their own investment decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends ETF names, sector research questions, and Cue API-authenticated requests to Cue-operated services.

Mitigation: Use it only when sharing those queries with Cue is acceptable, and keep the Cue API key private.

Risk: Generated ETF and sector analysis can be mistaken for trading advice.

Mitigation: Treat reports as informational research, review source links and assumptions, and make investment decisions independently.

Risk: Diagnostic commands access local Cue configuration and should run only in trusted shells.

Mitigation: Run diagnostics in a trusted environment and avoid exposing local configuration or API credentials.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-sector-etf)
- [ClawHub publisher profile](https://clawhub.ai/user/panting09266-ai)
- [Cue API key portal](https://cuecue.cn/hub/api-key)
- [Cue skills runner](https://github.com/sensedeal/cue-skills)
- [Cue skills runner Gitee mirror](https://gitee.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown research report with comparison tables, source links, risk notes, and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated reports are informational investment research and may require several minutes depending on query scope and Cue service availability.]

## Skill Version(s):

1.0.2 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
