## Description: <br>
Plaud lets an agent work with the user's connected Plaud account to find recordings, retrieve AI notes, pull speaker-attributed transcripts, and inspect recording details through AgentPMT-hosted remote tool calls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[agentpmt](https://clawhub.ai/user/agentpmt) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, teams, and agents use this skill to turn Plaud recordings, AI notes, and transcripts into follow-up emails, CRM notes, task lists, project updates, shared documents, and exact transcript quotes. It is intended for workflows where the user has already connected a Plaud account and wants an assistant to act only on recordings that account can access. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Plaud transcripts, recordings, and AI notes may contain confidential meeting, call, or voice memo content. <br>
Mitigation: Confirm with the user before sending summaries, quotes, action items, or transcript content into CRM, email, shared documents, task managers, or other third-party tools. <br>
Risk: The skill can retrieve content from the connected Plaud account. <br>
Mitigation: Use only the stored account connection, scope requests to the minimum necessary recording or date range, and surface only recordings the connected account can access. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/agentpmt/skills/plaud) <br>
- [AgentPMT Plaud Marketplace Page](https://www.agentpmt.com/marketplace/plaud) <br>
- [Plaud Schema](artifact/schema.md) <br>
- [AgentPMT Account MCP/REST Setup](https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, API calls, guidance] <br>
**Output Format:** [Markdown and JSON tool-call instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a connected Plaud account through AgentPMT; retrieved notes and transcripts may contain confidential meeting or voice memo content.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
