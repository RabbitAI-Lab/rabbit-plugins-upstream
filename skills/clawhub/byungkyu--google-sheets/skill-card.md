## Description:

Helps agents read and update Google Sheets, create spreadsheets, format ranges, and set up user-approved automations through a Maton-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams use this skill to retrieve or change spreadsheet data and configure narrowly scoped, user-approved automations for their workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A write or deletion may change the wrong spreadsheet or range.

Mitigation: Confirm the exact spreadsheet, range, and intended change with the user before proceeding; default to read-only actions.

Risk: Functions, triggers, and destinations can continue acting on or forwarding data after setup.

Mitigation: Request approval, scope each automation to the minimum necessary, and remove it when the task ends.

Risk: Account credentials or excessive permissions could expose spreadsheet data.

Mitigation: Prefer OAuth with only required scopes, keep credentials out of outputs and destinations, and authorize only trusted connections.

## Reference(s):

- [Maton](https://maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Google Sheets API Overview](https://developers.google.com/workspace/sheets/api/reference/rest)
- [Time Trigger Reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with CLI commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Maton account, network access, and authorization to access the connected spreadsheet.]

## Skill Version(s):

1.2.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
