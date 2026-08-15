## Description:

Privora gives AI agents a Bearer-token workflow backend for multi-asset market data, Python backtesting, paper-trading workflows, portfolio attribution, cloud alerts, and process orchestration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[guangfuwu](https://clawhub.ai/user/guangfuwu)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and AI-agent operators use this skill to connect an agent to Privora for investment research workflows: market-data lookup, portfolio analysis, backtesting, paper-trading process flows, alerting, and workflow orchestration. Outputs are analysis and automation support for operator review, not investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide agents toward broad write, process, scheduler, alert, webhook, portfolio, or paper-trading authority when those scopes are granted.

Mitigation: Start with a dedicated read-only or low-scope token, add scopes only for the active workflow, and require explicit human confirmation before state-changing calls or webhook triggers.

Risk: Bearer tokens authorize access to decrypted account data through the API boundary, so token exposure can expose private portfolio information.

Mitigation: Use dedicated tokens with minimum scope, store them only in the agent environment, and rotate or revoke them immediately after suspected exposure.

Risk: Paper-trading token guidance is inconsistent in the evidence and may not match the platform's current issuance flow.

Mitigation: Do not rely on self-minted paper-trading tokens unless Privora confirms the issuance flow; prefer documented process-bound paper-trading workflows.

Risk: The skill's outputs concern market data, backtests, alerts, and simulated trading, which can be mistaken for investment advice or live-trading instructions.

Mitigation: Treat outputs as analysis for operator review, validate data freshness and assumptions, and keep real-money trading outside autonomous agent execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/guangfuwu/skills/privora-cn-quant)
- [Privora product home](https://privora.cn)
- [Privora data coverage](https://privora.cn/features/realtime-minute-data-coverage)
- [Privora token management](https://privora.cn/profile/tokens)
- [Privora agent skills catalog](https://privora.cn/agent/skills)
- [Privora agent skill execution endpoint](https://privora.cn/agent/skills/execute)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, Python snippets, API call examples, and JSON response patterns]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires LG_AGENT_BASE_URL and LG_AGENT_TOKEN for authenticated Privora calls; anonymous preview paths are documented for limited public discovery.]

## Skill Version(s):

1.0.48 (source: server release metadata and SKILL.md frontmatter, updated 2026-08-11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
