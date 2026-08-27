## Description:

Privora gives AI agents token-based access to multi-asset market data, Python backtesting, paper trading, portfolio attribution, real-time alerts, and workflow orchestration for investment research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[guangfuwu](https://clawhub.ai/user/guangfuwu)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, investment researchers, and quantitative workflow operators use this skill to let agents retrieve market data, run backtests, inspect portfolios, configure alerts, and operate paper-trading workflows for review. It supports research and workflow automation, not autonomous real-money trading or financial advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A single agent integration can reach persistent workflow, alert, scheduling, token-revocation, and paper-trading actions when granted broad scopes.

Mitigation: Install with a dedicated least-privilege token, start with the default read-data scopes, and require operator review before granting or using schedule, delete/update, token revoke, webhook, portfolio write, or paper-trading scopes.

Risk: Authenticated API access can return decrypted portfolio or account data to any agent holding the Bearer Token.

Mitigation: Treat LG_AGENT_TOKEN as sensitive, use only trusted agents, avoid bundling unrelated scopes, and rotate exposed tokens immediately.

Risk: Workflow state transitions and outbound webhook actions can create persistent platform records or send external notifications.

Mitigation: Require explicit operator confirmation before process execution, scheduler state changes, alert changes, or webhook-triggering workflows.

Risk: Market data, backtest output, alerts, and paper-trading results may be mistaken for investment advice or live trading instructions.

Mitigation: Use outputs as review inputs only, validate data freshness and strategy assumptions, and keep real-money trading outside autonomous agent execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/guangfuwu/skills/privora-cn-quant)
- [Privora product homepage](https://privora.cn)
- [Privora marketplace](https://privora.cn/marketplace)
- [Privora market data coverage](https://privora.cn/features/realtime-minute-data-coverage)
- [Privora token management](https://privora.cn/profile/tokens)
- [Privora public skill version endpoint](https://privora.cn/api/public/agent/skill-version)
- [Privora public capabilities endpoint](https://privora.cn/api/public/agent/capabilities)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires LG_AGENT_BASE_URL and LG_AGENT_TOKEN for authenticated use; API results may include market data, backtest records, portfolio data, alert state, workflow state, and paper-trading records.]

## Skill Version(s):

1.0.50 (source: SKILL.md frontmatter and server release metadata, updated 2026-08-27)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
