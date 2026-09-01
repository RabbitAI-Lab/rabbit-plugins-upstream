## Description:

Privora lets AI agents query multi-asset market data, run Python backtests, simulate paper trades, analyze portfolios, configure alerts, and orchestrate investment research workflows through a scoped Bearer token.

This skill is ready for commercial/non-commercial use.

## Publisher:

[guangfuwu](https://clawhub.ai/user/guangfuwu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect AI agents to Privora for investment data retrieval, quantitative analysis, backtesting, paper trading, portfolio attribution, alerting, and workflow orchestration. Outputs are intended as operator-reviewed analysis and automation support, not financial advice or autonomous real-money trading instructions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bearer tokens can expose sensitive investment workflow capabilities, including read access, write actions, workflow transitions, webhook notifications, and selected destructive or reset operations.

Mitigation: Install with a dedicated Privora token scoped to the exact task, start with read-only scopes, add broader scopes only when needed, and require human review before workflow transitions, plugin or dependency replacement, token revocation, resets, or portfolio and trading actions.

Risk: Generated market analysis, backtests, paper trades, alerts, and portfolio reports may be incorrect, stale, or misapplied as investment advice.

Mitigation: Treat outputs as operator-reviewed analysis only, verify data freshness and assumptions before use, and keep real-money trading or irreversible financial decisions outside autonomous agent execution.

Risk: Webhook and plugin configuration can send data outside Privora or replace existing job bindings when saved as a complete desired state.

Mitigation: Review webhook endpoints and current plugin bindings before triggering notifications or saving plugin configuration, and preserve any existing bindings that should remain active.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/guangfuwu/skills/privora-cn-quant)
- [Privora product homepage](https://privora.cn)
- [Privora data coverage reference](https://privora.cn/features/realtime-minute-data-coverage)
- [Privora marketplace](https://privora.cn/marketplace)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, JSON API responses, and Python-oriented strategy guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires LG_AGENT_BASE_URL and LG_AGENT_TOKEN for authenticated Privora API calls.]

## Skill Version(s):

1.0.51 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
