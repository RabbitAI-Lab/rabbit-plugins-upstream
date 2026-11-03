## Description:

为 A 股市场生成盘后复盘，涵盖指数、资金流向、板块表现、涨跌驱动与次日观察要点。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

面向希望复盘 A 股市场的投资者，整理收盘或盘中市场快照、资金与板块动向，并准备次日观察事项。技能仅处理市场和板块层面的问题。

### Deployment Geography for Use:

Global (A-share market focus)

## Known Risks and Mitigations:

Risk: The security review found that the automatically updated runner includes advice to remove sandbox protections.

Mitigation: Use a reviewed, pinned runner version, retain sandbox protections, and allow only the network access needed for the task.

Risk: Queries are sent to Cue, the API key is stored locally, and each run consumes credits; recurring runs can incur repeated usage.

Mitigation: Keep the API key local, review the requested data access, and enable recurring runs only on a schedule you choose.

## Reference(s):

- [Cue platform](https://cuecue.cn/)
- [Cue runner repository (referenced by the skill)](https://github.com/sensedeal/cue-skills)
- [Cue runner Gitee mirror (referenced by the skill)](https://gitee.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, HTML, Shell commands, Configuration instructions]

**Output Format:** [Structured A-share market recap in Markdown, with an optional standalone HTML dashboard and usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Market and sector analysis only; intraday snapshots should state their data time. Reports include source attribution and limitations.]

## Skill Version(s):

1.0.15 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
