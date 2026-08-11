## Description:

Privora connects AI agents to multi-asset market data, Python backtesting, paper-trading workflows, portfolio attribution, alerts, and orchestration through a scoped Bearer-token API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[guangfuwu](https://clawhub.ai/user/guangfuwu)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and investment-workflow operators use this skill to let an AI agent query Privora data, run analysis and backtests, manage authorized workflows, and review paper-trading or alert outputs under scoped token permissions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Privora Bearer token can expose sensitive data or workflow capabilities according to its granted scopes.

Mitigation: Start with a read-only or test token, grant only the scopes needed for the current task, and rotate the token immediately if it may be exposed.

Risk: Workflow execution, portfolio or trading writes, and webhook-triggering actions can create persistent or external side effects.

Mitigation: Require explicit user confirmation before workflow execution, portfolio or trading writes, or webhook-triggering actions.

Risk: Market data, backtests, alerts, and paper-trading outputs may be mistaken for investment advice or live trading instructions.

Mitigation: Treat outputs as analysis for operator review, verify data freshness and assumptions, and keep real-money trading outside autonomous agent execution.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/guangfuwu/skills/privora-cn-quant)
- [Privora product homepage](https://privora.cn)
- [Privora marketplace](https://privora.cn/marketplace)
- [Privora realtime and minute-data coverage](https://privora.cn/features/realtime-minute-data-coverage)
- [Privora agent skill catalog](https://privora.cn/agent/skills)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires LG_AGENT_BASE_URL and LG_AGENT_TOKEN; outputs depend on the granted Privora token scopes.]

## Skill Version(s):

1.0.48 (source: server release metadata and SKILL.md frontmatter, updated 2026-08-11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
