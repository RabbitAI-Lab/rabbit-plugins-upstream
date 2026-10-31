## Description:

Automates office document creation, editing, analysis, conversion, and reporting across WPS Office, Microsoft Office, LibreOffice, and pure-Python workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and office teams use this skill to create and edit documents, spreadsheets, and presentations; convert formats; analyze or redact files; and generate reports. It supports workflows using installed office applications or Python libraries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unsafe file handling could expose documents or damage work.

Mitigation: Use an isolated workspace and copies of documents; save and close Office work before diagnostics or cleanup.

Risk: Search-result auto-opening and untrusted templates or watcher rules can trigger unsafe actions; watcher dry-run may still have side effects.

Mitigation: Avoid search-result auto-opening, inspect templates and watcher rules before use, and do not treat watcher dry-run as side-effect-free.

Risk: Scheduled task cancellation may leave Linux crontab entries active.

Mitigation: Verify crontab entries directly after cancellation and avoid unattended scheduling until task state is confirmed.

Risk: Blanket offline or backup assurances may not reflect actual behavior.

Mitigation: Keep independent backups and confirm where each workflow processes or stores document data. For local meeting summaries, select the rule-engine.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/fyniujin/skills/wps-office-suite)

## Skill Output:

**Output Type(s):** [Files, Text, Shell commands, Guidance]

**Output Format:** [Office documents and reports (DOCX, XLSX, PPTX, PDF, HTML, CSV, and JSON), with text or command-line output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or modify user-selected local files; capabilities depend on installed applications and optional libraries.]

## Skill Version(s):

5.4.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
