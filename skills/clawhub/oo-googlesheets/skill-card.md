## Description:

Enables an agent to operate Google Sheets through OOMOL's oo CLI, including reading, creating, updating, deleting, formatting, filtering, and managing spreadsheet data and metadata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and users use this skill to work with Google Sheets through an OOMOL-connected account. It supports spreadsheet reads, searches, metadata inspection, and confirmed write or destructive operations such as updates, clears, deletes, formatting, validation rules, filters, and sheet copying.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup directs users to run remote installer scripts directly in a shell.

Mitigation: Review the installer source and prefer a verified, pinned, or package-manager-based installation path before running setup commands.

Risk: Write and destructive Google Sheets actions can modify, clear, or delete spreadsheet data.

Mitigation: Inspect the live action schema and confirm the exact spreadsheet, range, sheet, payload, and intended effect with the user before execution.

## Reference(s):

- [ClawHub Google Sheets skill page](https://clawhub.ai/oomol/skills/oo-googlesheets)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Google Sheets](https://workspace.google.com/products/sheets/)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance, Configuration instructions]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before actions; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: SKILL.md metadata and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
