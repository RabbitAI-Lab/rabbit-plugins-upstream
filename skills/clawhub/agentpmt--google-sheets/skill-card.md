## Description:

Google Sheets: Work with Google Sheets using safe short actions for creating and finding spreadsheets, listing tabs, reading data, appending rows or columns at the data edge, updating selected fields by key, formatting, sharing, and exporting sheets through AgentPMT-hosted remote tool calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentpmt](https://clawhub.ai/user/agentpmt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill to operate Google Sheets through AgentPMT workflows, including safe table appends, keyed row updates, tab management, formatting, sharing, and exports. It is intended for agents that need the tool behavior, invocation schema, and supported action names for Google Sheets automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can authorize broad Google Sheets actions, including sharing, deletion, export, and changes to protected ranges.

Mitigation: Require explicit human approval before share, delete, export, owner or writer permission, and unprotect actions.

Risk: Unpinned setup commands can install changed dependency or setup behavior after publication.

Mitigation: Prefer the OpenClaw install path or pinned setup references over unpinned npx commands.

Risk: Spreadsheet exports and broad reads can expose sensitive sheet data outside the original document context.

Mitigation: Keep tool inputs scoped to the minimum needed range or tab and review export destinations before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/agentpmt/skills/google-sheets)
- [AgentPMT Google Sheets marketplace page](https://www.agentpmt.com/marketplace/google-sheets-api)
- [Generated Google Sheets action schema](schema.md)

## Skill Output:

**Output Type(s):** [guidance, configuration, API calls, JSON]

**Output Format:** [Markdown guidance with JSON MCP and REST call examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [AgentPMT-hosted Google Sheets actions may read, create, update, format, share, delete, protect, unprotect, and export spreadsheet content.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
