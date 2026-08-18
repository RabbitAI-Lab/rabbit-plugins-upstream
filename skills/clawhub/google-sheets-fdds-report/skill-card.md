## Description:

Reads FDDS logistics metrics from a user-specified Google Sheet and generates or updates a report comparing the latest available day with the same day from the previous week.

This skill is ready for commercial/non-commercial use.

## Publisher:

[craken-ia86](https://clawhub.ai/user/craken-ia86)

### License/Terms of Use:

MIT-0

## Use Case:

Logistics and operations users use this skill to turn Google Sheets FDDS data into a concise comparative performance report. It supports reviewing first-day delivery success, shipment counts, failure totals, and failure-category breakdowns for the latest available day versus the same weekday in the previous week.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads FDDS and logistics data from a user-specified Google Sheet.

Mitigation: Install only where the agent is allowed to access that spreadsheet and confirm the spreadsheet and required tabs before use.

Risk: The skill can write the generated report back to the spreadsheet when the user requests it.

Mitigation: Ask the agent to confirm the destination tab or range before any write-back.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/craken-ia86/skills/google-sheets-fdds-report)
- [Publisher profile](https://clawhub.ai/user/craken-ia86)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown or plain text report content, with optional spreadsheet write-back when requested by the user]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user-provided access to the target Google Sheet and the expected Template, DATA FDDS W, DATA FDDS W-1, and DATA Paquetes tabs.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
