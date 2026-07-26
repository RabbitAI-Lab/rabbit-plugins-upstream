## Description: <br>
Privora connects AI agents to a token-authenticated investment workflow platform for A-share, Hong Kong stock, gold, fund, and financial-report data, with Python backtesting, paper trading, portfolio attribution, cloud alerts, and workflow orchestration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[guangfuwu](https://clawhub.ai/user/guangfuwu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to let AI agents query Privora market and portfolio data, run quantitative backtests, operate paper-trading workflows, configure alerts, and retrieve analysis for operator review. It is aimed at investment research workflows, not autonomous real-money trading or regulated financial advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bearer tokens can grant access to financial workflow data and state-changing Privora actions. <br>
Mitigation: Use a dedicated least-privilege token, start with read-only scopes, set LG_AGENT_BASE_URL explicitly, and rotate the token if exposed. <br>
Risk: Workflow execution, webhook triggers, alert changes, portfolio writes, and paper-trading actions can create persistent records or external side effects. <br>
Mitigation: Require operator confirmation before these actions and reserve autonomous use for read-only or explicitly idempotent operations. <br>
Risk: Investment analysis, backtests, paper-trading output, and alerts may be incomplete or misleading if treated as advice. <br>
Mitigation: Treat outputs as analytical inputs for operator review; verify data freshness, strategy assumptions, and execution boundaries before decisions. <br>


## Reference(s): <br>
- [ClawHub Skill Listing](https://clawhub.ai/guangfuwu/skills/privora-cn-quant) <br>
- [Privora Product Homepage](https://privora.cn) <br>
- [Privora Marketplace](https://privora.cn/marketplace) <br>
- [Privora Token Management](https://privora.cn/profile/tokens) <br>
- [Privora Public Skill Version](https://privora.cn/api/public/agent/skill-version) <br>
- [Privora Public Capabilities Catalog](https://privora.cn/api/public/agent/capabilities) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, API calls, Guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires LG_AGENT_BASE_URL and LG_AGENT_TOKEN for authenticated Privora calls; anonymous preview is limited to documented public marketplace and preview endpoints.] <br>

## Skill Version(s): <br>
1.0.45 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
