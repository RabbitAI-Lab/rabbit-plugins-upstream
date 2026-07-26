## Description: <br>
Verifies whether an AI agent or x402 service is real and settlement-backed before payment, hiring, trust, or task-routing decisions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[andysalvo](https://clawhub.ai/user/andysalvo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Agents, developers, and service operators use this skill before settling x402 payments, extending credit, routing work, or gating callers by reputation. It guides them to check a wallet or domain with AgentRank and interpret the settlement-grounded score as one input to trust decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Review before execution as proposals could introduce incorrect or misleading guidance into skills. <br>
Mitigation: Review and scan skill before deployment. <br>

## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/andysalvo/skills/agentrank-verify) <br>
- [AgentRank](https://agentrank.info) <br>
- [AgentRank resolve API](https://api.agentrank.info/resolve/{wallet-or-domain}) <br>
- [AgentRank MCP server](https://api.agentrank.info/mcp) <br>
- [AgentRank agent card](https://agentrank.info/.well-known/agent-card.json) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with HTTP, MCP, and A2A examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only reputation lookups; results may include verified status, score, settlement details, verdict, and gating guidance. Review external service use and MCP permissions before adding the server, and treat scores as one input rather than proof of safety or financial advice.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
