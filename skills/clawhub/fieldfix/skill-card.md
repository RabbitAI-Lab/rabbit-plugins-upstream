## Description: <br>
Query and manage heavy equipment fleets through the FieldFix API, including machines, maintenance records, expenses, service history, alerts, and diagnostics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[blueprintstudioco](https://clawhub.ai/user/blueprintstudioco) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Fleet operators, developers, and service teams use this skill to inspect FieldFix machine records, expenses, service history, and alerts, and to log service entries, expenses, and hour-meter updates. It is suited to agents that need FieldFix account access for heavy-equipment maintenance and cost tracking workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses FIELDFIX_API_KEY to access a FieldFix account and can expose the key if it is pasted into chats, logs, shell history, or version control. <br>
Mitigation: Store FIELDFIX_API_KEY in a secure local environment or secret manager, avoid sharing it in prompts or logs, and rotate the key if it is exposed. <br>
Risk: Write commands can log service entries, expenses, and hour-meter updates against FieldFix fleet records. <br>
Mitigation: Manually confirm machine IDs, costs, notes, and hour readings before running write commands, and prefer least-privilege or dedicated API credentials when available. <br>


## Reference(s): <br>
- [FieldFix ClawHub Skill Page](https://clawhub.ai/blueprintstudioco/skills/fieldfix) <br>
- [FieldFix API Documentation](https://www.fieldfix.ai/api) <br>
- [FieldFix App](https://app.fieldfix.ai) <br>
- [FieldFix MCP Server](https://www.npmjs.com/package/fieldfix-mcp-server) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration, API calls] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands require FIELDFIX_API_KEY and may read or write FieldFix fleet records through the FieldFix API.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata, artifact frontmatter, and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
