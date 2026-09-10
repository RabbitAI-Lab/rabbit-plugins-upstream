## Description:

Manage a Dex personal CRM by helping agents search, filter, create, archive, and update contacts; log notes; manage follow-ups, tags, groups, and custom fields; search connected email; manage connected calendars; and prepare relationship workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ocruzv](https://clawhub.ai/user/ocruzv)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate a Dex personal CRM through MCP tools or the Dex CLI, including contact management, meeting preparation, follow-up workflows, calendar operations, and read-only correspondence search.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path can use an unpinned auto-confirmed MCP installer that modifies detected AI client configurations.

Mitigation: Prefer existing MCP tools or a scoped, reviewed CLI install; if using add-mcp, verify the package, publisher, and version first and avoid connecting clients you do not intend to use.

Risk: Dex access can read and modify CRM records, connected calendars, and email metadata.

Mitigation: Use the minimum necessary data, summarize sensitive relationship information, and require explicit confirmation before destructive changes, calendar writes, or actions that may notify attendees.

Risk: Authentication secrets could be exposed if API keys or device-flow tokens are pasted, printed, logged, or passed on a visible command line.

Mitigation: Do not ask users to paste keys into chat; keep token handling out of visible logs and store credentials only in the documented local files with restrictive permissions.

## Reference(s):

- [Dex Skill on ClawHub](https://clawhub.ai/ocruzv/skills/dex-skill)
- [Dex Homepage](https://getdex.com)
- [Dex MCP Server Setup Guide](https://getdex.com/docs/ai/mcp-server)
- [Dex CLI Command Reference](references/cli-commands.md)
- [Dex Tools Reference](references/tools-reference.md)
- [CRM Workflows & Relationship Management](references/crm-workflows.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, API calls]

**Output Format:** [Markdown guidance with JSON tool inputs and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce CRM record proposals, confirmations, summaries, and verification steps; MCP and CLI JSON modes return structured JSON.]

## Skill Version(s):

2.4.2 (source: release evidence and frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
