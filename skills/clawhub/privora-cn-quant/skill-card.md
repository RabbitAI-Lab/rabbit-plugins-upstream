## Description: <br>
Privora connects AI agents to investment research workflows for multi-asset market data, Python backtesting, paper trading, portfolio attribution, alerts, and workflow orchestration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[guangfuwu](https://clawhub.ai/user/guangfuwu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers, investors, and small teams use this skill to let an AI agent query Privora market data, run Python backtests, manage paper-trading workflows, inspect portfolio analytics, and prepare alerts for operator review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A broadly scoped Bearer Token can give an agent access to private data, workflow execution, alerts, or paper-trading actions. <br>
Mitigation: Use a dedicated least-privilege token, start with read-only scopes when possible, avoid broad write/webhook/paper-trading scopes on general agents, and rotate the token if exposed. <br>
Risk: Workflow execution, alert webhook triggering, and write operations can create persistent records or external side effects. <br>
Mitigation: Require explicit operator confirmation before workflow execution, webhook triggering, or any write operation. <br>
Risk: Market data, backtests, portfolio analysis, paper trading, and alert results may be mistaken for investment advice or live-trading authorization. <br>
Mitigation: Treat outputs as analysis for human review, verify data freshness and assumptions, and keep live trading or irreversible financial decisions outside autonomous execution. <br>
Risk: Anonymous preview mode exposes only limited public read-only data and may not reflect full datasets. <br>
Mitigation: Use anonymous preview for discovery only; use an authenticated token and verify complete data before analysis. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/guangfuwu/skills/privora-cn-quant) <br>
- [Privora product homepage](https://privora.cn) <br>
- [Privora data coverage reference](https://privora.cn/features/realtime-minute-data-coverage) <br>
- [Privora marketplace](https://privora.cn/marketplace) <br>
- [Privora token management](https://privora.cn/profile/tokens) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown, JSON API responses, Python snippets, and shell command invocations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Authenticated use requires LG_AGENT_BASE_URL and LG_AGENT_TOKEN; anonymous preview is limited to public read-only marketplace data.] <br>

## Skill Version(s): <br>
1.0.47 (source: frontmatter, evidence.release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
