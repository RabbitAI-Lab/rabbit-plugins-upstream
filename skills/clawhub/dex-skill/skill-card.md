## Description:

Dex helps agents manage a user's personal CRM by finding and updating contacts, logging notes and follow-ups, organizing tags, groups, and custom fields, searching connected email metadata, and reading or managing connected calendars.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ocruzv](https://clawhub.ai/user/ocruzv)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to maintain a professional network in Dex: prepare for meetings, update contacts, log relationship notes, manage reminders, organize CRM taxonomy, and review correspondence or calendar context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access and modify Dex CRM records, connected calendar data, and mailbox metadata.

Mitigation: Connect only accounts the user is comfortable exposing to Dex, retrieve the minimum needed data, and keep read-only requests read-only unless the user asks for changes.

Risk: Bulk updates, destructive CRM operations, and calendar writes can alter or remove user data or affect external attendees.

Mitigation: Preview exact targets and consequences, obtain explicit confirmation before writes, re-resolve current IDs before execution, and verify representative changed records afterward.

Risk: Dex API keys and bearer tokens are sensitive credentials.

Mitigation: Do not ask users to paste API keys into chat, do not print or log secrets, and use local credential files with restrictive permissions when credential setup is required.

## Reference(s):

- [Dex homepage](https://getdex.com)
- [Dex skill release page](https://clawhub.ai/ocruzv/skills/dex-skill)
- [Dex MCP setup guide](https://getdex.com/docs/ai/mcp-server)
- [Dex Tools Reference](references/tools-reference.md)
- [Dex CLI Command Reference](references/cli-commands.md)
- [CRM Workflows & Relationship Management](references/crm-workflows.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain text with JSON tool arguments and inline shell commands when CLI setup or execution is needed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce CRM action previews, confirmation prompts, summaries of read results, MCP tool arguments, CLI commands, and credential-handling guidance.]

## Skill Version(s):

2.1.1 (source: server release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
