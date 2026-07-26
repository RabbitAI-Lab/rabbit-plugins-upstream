## Description: <br>
Google Calendar helps agents list calendars and events, create, update, delete, search, and quick-add events, manage recurrence, Google Meet links, attendees, and check free/busy availability through AgentPMT-hosted remote tool calls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[agentpmt](https://clawhub.ai/user/agentpmt) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to manage Google Calendar schedules through AgentPMT, including meeting creation, updates, cancellation, attendee coordination, recurrence, Google Meet links, and availability checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read calendar details and create, update, or delete events through AgentPMT. <br>
Mitigation: Install only when comfortable granting Google Calendar permissions through AgentPMT, and require the agent to show the target event before making changes. <br>
Risk: Deleting events, changing attendees, changing recurrence, or sending notifications can affect other participants. <br>
Mitigation: Require explicit confirmation before deletion, attendee changes, recurrence changes, or notification-sending actions. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/agentpmt/skills/google-calendar) <br>
- [AgentPMT Marketplace Page](https://www.agentpmt.com/marketplace/google-calendar) <br>
- [Action Schema](artifact/schema.md) <br>
- [AgentPMT Account MCP/REST Setup](https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup) <br>
- [What Is AgentPMT](https://clawhub.ai/agentpmt/what-is-agentpmt) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, JSON, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown instructions with JSON request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Google OAuth connection with calendar permissions through AgentPMT; returned JSON is treated as the source of truth for tool calls.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
