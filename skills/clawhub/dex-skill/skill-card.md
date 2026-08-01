## Description: <br>
Manage Dex personal CRM records, notes, reminders, tags, groups, custom fields, connected email search, and calendars through Dex MCP tools or the Dex CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ocruzv](https://clawhub.ai/user/ocruzv) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and teams use this skill to maintain professional relationship data in Dex: finding and updating contacts, logging interactions, preparing meetings, organizing networks, and managing follow-ups, calendar context, and email metadata. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access and modify sensitive Dex CRM, calendar, and email-metadata data. <br>
Mitigation: Install and enable it only for users who want an assistant to manage Dex data, and retrieve only the records needed for the requested task. <br>
Risk: Bulk changes, deletion, merging, archiving, and calendar updates can alter or remove important relationship data. <br>
Mitigation: Preview exact affected records and consequences, require explicit confirmation before writes, and verify changed records after execution. <br>
Risk: Authentication tokens or API keys could be exposed if handled in chat or tool logs. <br>
Mitigation: Use browser OAuth or device-code flows when possible, never ask users to paste API keys into chat, and avoid printing or logging successful token responses. <br>
Risk: Calendar changes can affect attendees or provider notifications. <br>
Mitigation: Confirm attendees, account, recurrence scope, and notification-impacting changes before creating, updating, deleting, or transferring events. <br>


## Reference(s): <br>
- [Dex homepage](https://getdex.com) <br>
- [Dex MCP setup guide](https://getdex.com/docs/ai/mcp-server) <br>
- [CLI Command Reference](references/cli-commands.md) <br>
- [CRM Workflows](references/crm-workflows.md) <br>
- [Dex Tools Reference](references/tools-reference.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON tool inputs and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use Dex MCP tools directly or Dex CLI commands; email search returns metadata and snippets rather than full message bodies.] <br>

## Skill Version(s): <br>
2.1.0 (source: artifact SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
