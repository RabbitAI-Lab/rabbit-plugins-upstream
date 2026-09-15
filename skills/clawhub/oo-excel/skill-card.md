## Description:

Use this skill to operate Microsoft Excel through an OOMOL-connected account, including reading, creating, updating, and deleting workbook data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to inspect Excel connector schemas and run OOMOL CLI actions for workbook, worksheet, range, table, and file operations in a connected Microsoft account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The connector can read and change Excel workbook data through the user's connected Microsoft account.

Mitigation: Confirm exact workbook, worksheet, range, table, and payload details before any write or destructive action.

Risk: Remote installer pipe commands can execute unverified code during setup.

Mitigation: Use a verified, version-pinned installation path instead of running installer pipe commands blindly.

Risk: File search and drive listing can expose OneDrive item metadata beyond the intended workbook.

Mitigation: Limit searches and listings to the narrowest necessary scope and review returned item metadata before continuing.

## Reference(s):

- [ClawHub Excel Skill Page](https://clawhub.ai/oomol/skills/oo-excel)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Microsoft Excel](https://www.microsoft.com/microsoft-365/excel)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are returned as JSON by the oo CLI.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
