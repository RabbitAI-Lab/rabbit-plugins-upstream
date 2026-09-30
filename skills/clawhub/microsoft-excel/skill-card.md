## Description:

Helps agents read and update Microsoft Excel workbooks, worksheets, ranges, tables, and charts in OneDrive or SharePoint through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

People and developers use this skill to inspect and manage Excel spreadsheets in connected Microsoft accounts, including cell values, worksheets, tables, and charts. It can also guide approved automation using hosted functions and triggers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting Maton grants access to Excel and OneDrive data within the authorized account.

Mitigation: Obtain approval before connecting, prefer OAuth, and select the narrowest available Microsoft permissions.

Risk: Workbook changes or deletions can alter or remove user data.

Mitigation: Confirm the exact workbook, target, payload, and intended effect before every write or delete.

Risk: Hosted functions, triggers, and destinations can create ongoing data access or forwarding.

Mitigation: Require explicit approval for automation and destinations, including what data flows, where it goes, and how often.

Risk: Raw API keys can expose long-lived account access.

Mitigation: Prefer OAuth login and avoid exposing MATON_API_KEY in commands, logs, or shared environments.

## Reference(s):

- [ClawHub Microsoft Excel skill release](https://clawhub.ai/byungkyu/skills/microsoft-excel)
- [Maton](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Microsoft Graph Excel API overview](https://learn.microsoft.com/en-us/graph/api/resources/excel)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration guidance]

**Output Format:** [Text or Markdown with command and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include spreadsheet data from the authorized connection.]

## Skill Version(s):

1.2.4 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
