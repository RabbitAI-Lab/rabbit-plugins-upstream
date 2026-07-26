## Description: <br>
Plaud lets an agent work with a user's connected Plaud account to list recordings, retrieve recording details, fetch AI notes, and pull speaker-attributed transcripts through AgentPMT-hosted remote tool calls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[agentpmt](https://clawhub.ai/user/agentpmt) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, teams, and agents use this skill to turn Plaud recordings, notes, and transcripts into follow-up emails, CRM notes, task lists, shared summaries, and project updates while respecting the connected user's Plaud account permissions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Plaud recordings, AI notes, and transcripts may contain confidential meeting, call, interview, or voice memo content. <br>
Mitigation: Treat returned notes and transcripts as sensitive, use the narrowest practical file, date, and query filters, and confirm before sharing excerpts or summaries with external tools. <br>
Risk: The skill depends on the user's connected Plaud account and AgentPMT setup, so incorrect account selection or unclear schema details can produce failed or unintended calls. <br>
Mitigation: Use the stored account connection only, respect Plaud account permissions, and fetch live schema or instructions before new production integrations or when parameters and outputs are unclear. <br>


## Reference(s): <br>
- [Plaud Marketplace Product](https://www.agentpmt.com/marketplace/plaud) <br>
- [ClawHub Skill Page](https://clawhub.ai/agentpmt/skills/plaud) <br>
- [AgentPMT Account MCP/REST Setup](https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup) <br>
- [What AgentPMT Is](https://clawhub.ai/agentpmt/what-is-agentpmt) <br>
- [Plaud Schema](schema.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON request examples and structured remote-tool response handling] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces agent instructions for AgentPMT-hosted Plaud actions; no local command runtime is declared.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
