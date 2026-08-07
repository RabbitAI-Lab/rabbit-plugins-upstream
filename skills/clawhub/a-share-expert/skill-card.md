## Description:

A-share China stock trading decision support skill that coordinates stock-data MCP sources and structured analysis workflows for Shanghai and Shenzhen main-board scenarios.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiaoze-hub](https://clawhub.ai/user/xiaoze-hub)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill for A-share market decision support, including candidate screening, real-time quote checks, fundamentals, capital flow, event-driven analysis, portfolio adjustment, post-market review, theme-launch hunting, and sell-discipline workflows. It should be treated as decision-support guidance rather than guaranteed investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill provides highly actionable speculative A-share trading guidance that users may mistake for personalized financial advice.

Mitigation: Present outputs as decision-support guidance, include clear capital-loss and educational-use warnings, and require explicit user confirmation before any buy, sell, or position-sizing action.

Risk: Broad trigger phrases may activate the skill for general stock or finance questions where a narrower response would be safer.

Mitigation: Narrow activation phrases during deployment and ask clarifying questions when the user intent, market scope, or desired risk level is unclear.

Risk: Monitoring, notifications, or decision-history workflows may involve user holdings and trading behavior.

Mitigation: Keep monitoring and notifications opt-in, state retention and deletion expectations clearly, and avoid storing decision history unless the user explicitly enables it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xiaoze-hub/skills/a-share-expert)
- [7 大实战场景详细流程](references/scenarios-7-flow.md)
- [MCP 数据源详细能力矩阵](references/mcp-fallback-matrix.md)
- [MCP 协同策略表](references/mcp-coordination-strategy.md)
- [题材刚启动识别框架](references/theme-launch-hunting.md)
- [纪律执行框架](references/discipline-execution.md)
- [多 Agent 决策框架](references/multi-agent-decision-framework.md)
- [实战交易规则与排雷手册](references/trading-rules-essentials.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with structured decision summaries and inline tool or shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference external MCP stock-data tools and user-supplied holdings; recommendations require user review before action.]

## Skill Version(s):

1.0.10 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
