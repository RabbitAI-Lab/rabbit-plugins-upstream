## Description:

Reads FDDS metrics from a user-specified Google Sheet and generates a report comparing the latest available day with the same day from the previous week.

This skill is ready for commercial/non-commercial use.

## Publisher:

[craken-ia86](https://clawhub.ai/user/craken-ia86)

### License/Terms of Use:

MIT-0

## Use Case:

External users and logistics operations teams use this skill to analyze FDDS performance from Google Sheets data, compare D-1 against W-1, and produce an updated reporting template or report text.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires access to a Google Sheet that may contain shared business data.

Mitigation: Grant access only to the intended spreadsheet and use the least privilege needed for the report.

Risk: Optional write-back can modify report data if the spreadsheet, tab, or range is incorrect.

Mitigation: Confirm the spreadsheet, tab, and target range before allowing any write-back.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/craken-ia86/skills/google-sheets-fdds-report)

## Skill Output:

**Output Type(s):** [Text, Markdown, API Calls, Guidance]

**Output Format:** [Text or Markdown report, with optional Google Sheets write-back when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update the requested Google Sheet when the user authorizes write-back.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
