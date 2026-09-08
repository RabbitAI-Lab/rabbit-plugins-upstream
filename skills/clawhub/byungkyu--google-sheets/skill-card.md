## Description:

Google Sheets API integration with managed OAuth for reading and writing spreadsheet data, creating sheets, applying formatting, and managing ranges through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to access Google Sheets through Maton-managed authentication, including reading spreadsheet values, updating ranges, creating sheets, and composing Google Sheets API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Google Sheets requests route through Maton and require a local Maton OAuth profile or API key.

Mitigation: Install only when this routing and local credential storage are acceptable; prefer OAuth over API keys and avoid exposing credential values.

Risk: Write, delete, sharing, or raw API calls can change spreadsheet data or access controls.

Mitigation: Review the target spreadsheet, range, payload, connection, and intended effect before approving any modifying operation.

Risk: Multiple Maton accounts or Google Sheets connections can cause requests to target the wrong account.

Mitigation: Specify the intended profile or connection when more than one account or connection exists.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/google-sheets)
- [Maton homepage](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Google Sheets API overview](https://developers.google.com/workspace/sheets/api/reference/rest)
- [Google Sheets batchUpdate reference](https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/batchUpdate)
- [Google Sheets values reference](https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets.values)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Maton CLI commands, raw API call examples, SDK snippets, and review guidance for Google Sheets read and write operations.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
