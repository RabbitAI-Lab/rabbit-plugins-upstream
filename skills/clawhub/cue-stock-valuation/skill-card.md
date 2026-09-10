## Description:

用 Cue 对个股进行全周期估值分析，融合短线资金流向与中长线估值模型，帮助评估情绪博弈、支撑压力、业绩兑现与安全边际。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to run Cue-based stock valuation research for a target equity, including short-term money-flow context, medium-term earnings drivers, long-term valuation models, safety margin, risk factors, and source links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks the agent to use an external, unbundled Cue runner with access to a local Cue API key and report output directory.

Mitigation: Review or pin the runner before use, use a revocable Cue API key, avoid elevated privileges, and install only when the Cue runner source is trusted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-stock-valuation)
- [Cue example valuation report](https://cuecue.cn/share/NMJ36JGzIwOx8SPJXB_WR)
- [Cue runner source](https://github.com/sensedeal/cue-skills)
- [Cue runner Gitee mirror](https://gitee.com/sensedeal/cue-skills)
- [Cue API key page](https://cuecue.cn/hub/api-key)

## Skill Output:

**Output Type(s):** [markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown report with source links and optional shell commands for running Cue and converting reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The report is expected to preserve source links and avoid summarizing or changing reported figures.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
