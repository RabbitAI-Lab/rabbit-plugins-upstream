## Description: <br>
AgentPMT Audit Logs helps agents read authorized AgentPMT audit history, including chat sessions, transcripts, tool calls, workflow runs, and schedules through AgentPMT-hosted remote tool calls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[agentpmt](https://clawhub.ai/user/agentpmt) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to review authorized AgentPMT agent activity, summarize prior work, investigate failed runs, and audit tool-call or workflow history. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Returned transcripts and tool-call logs may include private user content or operational details. <br>
Mitigation: Treat returned audit records as sensitive and avoid sharing them beyond the intended review context. <br>
Risk: Broad audit scopes can expose activity across multiple authorized agent groups. <br>
Mitigation: Prefer current_agent_group scope and use all_authorized_agent_groups only when the review requires cross-group history. <br>


## Reference(s): <br>
- [AgentPMT Audit Logs marketplace page](https://www.agentpmt.com/marketplace/agentpmt-audit-logs) <br>
- [ClawHub skill page](https://clawhub.ai/agentpmt/skills/agentpmt-audit-logs) <br>
- [Generated action schema](artifact/schema.md) <br>
- [AgentPMT main MCP server](https://api.agentpmt.com/mcp/) <br>
- [AgentPMT REST invoke endpoint](https://api.agentpmt.com/products/purchase) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, configuration, shell commands, JSON] <br>
**Output Format:** [Markdown guidance with JSON request examples and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Remote responses are JSON audit records scoped to authorized AgentPMT agent groups.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
