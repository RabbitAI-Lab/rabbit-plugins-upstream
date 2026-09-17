## Description:

Excel lets agents operate Microsoft Excel through an OOMOL-connected account to read, create, update, and delete workbook data, worksheets, ranges, tables, and files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Excel connector action schemas and run OOMOL CLI actions for workbook, worksheet, range, table, file search, session, filtering, sorting, merge, insert, and update workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes remote installer commands that can execute arbitrary code.

Mitigation: Install the OOMOL CLI only through a verified package or a separately downloaded, inspected, and checksum-verified installer.

Risk: Write and destructive connector actions can change, overwrite, or delete Excel workbook data.

Mitigation: Approve write or destructive actions only after checking the exact workbook, worksheet, range, action, and JSON payload.

Risk: Connector actions use a connected Excel account and may access account data through server-side credentials.

Mitigation: Use an appropriate OOMOL-connected account and confirm that the requested operation matches the user's intended Excel files and permissions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-excel)
- [OOMOL CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Microsoft Excel](https://www.microsoft.com/microsoft-365/excel)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May run OOMOL CLI connector actions that return JSON responses with data and execution metadata.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
