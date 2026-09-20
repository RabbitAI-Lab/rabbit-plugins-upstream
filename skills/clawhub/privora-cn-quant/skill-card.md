## Description:

Privora gives AI agents a Bearer-token workflow backend for A-share, Hong Kong, U.S. equity, gold, fund, financial-event, Python backtesting, paper-trading, portfolio-attribution, alerting, and workflow-orchestration tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[guangfuwu](https://clawhub.ai/user/guangfuwu)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, AI-agent operators, and quantitative-investment users use this skill to let an agent discover Privora capabilities, query market and portfolio data, run backtests, manage paper-trading workflows, and configure alerts through scoped Privora API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A token can expose broad financial-data and workflow-changing capabilities to an autonomous agent.

Mitigation: Use a dedicated least-privilege Privora token, start with read-only scopes, and avoid wildcard or bundled write scopes unless the use case requires them.

Risk: Some destructive, reset, revoke, scheduling, datasource, dashboard, webhook, or team-Python actions may be reachable without an independently enforced human approval step.

Mitigation: Keep those scopes out of autonomous-agent tokens unless there is a separate human approval process outside the skill.

Risk: Loopback or self-hosted requests with large JSON bodies can exceed the wrapper's conservative curl config-line limit.

Mitigation: Split large payloads into smaller calls or use the Privora platform UI for oversized workflow changes.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/guangfuwu/skills/privora-cn-quant)
- [Privora Product Homepage](https://privora.cn)
- [Privora Data Coverage](https://privora.cn/features/realtime-minute-data-coverage)
- [Privora Token Management](https://privora.cn/profile/tokens)
- [Privora Public Agent Capabilities](https://privora.cn/api/public/agent/capabilities)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance, shell command invocations, and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires LG_AGENT_TOKEN and optionally LG_AGENT_BASE_URL; API calls are authorized by the token's Privora scopes.]

## Skill Version(s):

1.0.56 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
