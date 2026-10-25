## Description:

Work with Google Sheets through AgentPMT-hosted remote tool calls to read, create, update, format, share, and export spreadsheets using targeted workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentpmt](https://clawhub.ai/user/agentpmt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams use this skill to manage Google Sheets through AgentPMT-hosted tool calls, including targeted reads and edits, spreadsheet formatting and sharing, and tab exports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connected-account access and paid calls can expose data or incur charges.

Mitigation: Limit connected-account permissions and spending to what the task requires.

Risk: Edits, row deletions, or sharing changes can affect the wrong data or recipients.

Mitigation: Specify the exact spreadsheet, deletion targets, and sharing recipients; verify targets and keep backups before destructive changes.

Risk: AgentPMT processes requests and stores spreadsheet exports.

Mitigation: Review data-handling expectations before exporting sensitive content and manage stored exports appropriately.

Risk: Separate credential-setup skills have unpinned installation sources.

Mitigation: Review those setup skills and their sources before use, and reassess future updates.

## Reference(s):

- [AgentPMT Google Sheets Marketplace](https://www.agentpmt.com/marketplace/google-sheets-api)
- [ClawHub Google Sheets Skill](https://clawhub.ai/agentpmt/skills/google-sheets)

## Skill Output:

**Output Type(s):** [API Calls, Files, Guidance]

**Output Format:** [Structured tool-call inputs, spreadsheet data, and exported CSV, TSV, PDF, XLSX, ODS, HTML, or ZIP files.]

**Output Parameters:** [Varies by action; may include spreadsheet, tab, range, rows, and export options.]

**Other Properties Related to Output:** [Some actions change spreadsheet data or sharing settings; some export formats require Drive access.]

## Skill Version(s):

1.0.2 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
