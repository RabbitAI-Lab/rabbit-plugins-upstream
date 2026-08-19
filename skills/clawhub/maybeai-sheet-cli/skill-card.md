## Description:

Use when the user works with MaybeAI spreadsheets through the mbs CLI for workbook inspection, local or remote-URL file import, native cross-workbook import/export, worksheet/range/table writes, full worksheet data refreshes that keep headers, formulas, worksheet styling, chart/image CRUD, dashboard validate/refresh/export-template flows, or sharing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[no7dw](https://clawhub.ai/user/no7dw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and spreadsheet operators use this skill to inspect, import, edit, format, export, and share MaybeAI workbooks through the mbs CLI. It emphasizes metadata-first routing across Sheet, Base Table, and SQL Config targets before mutations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use a MaybeAI API token to read, modify, import, export, delete, restore, and share workbooks.

Mitigation: Install only when this workbook access is intended, and confirm the exact workbook, worksheet, and operation before destructive or sharing commands.

Risk: Sharing commands can expose workbook data through public visibility or editor grants.

Mitigation: Confirm the recipient, visibility, and permission level before changing access, and inspect current permissions when the task involves sharing.

Risk: Using the wrong workbook target model can send writes to an incompatible Sheet, Base Table, or SQL Config surface.

Mitigation: Run workbook metadata or list-worksheets first, resolve the required target identity, and use dry-run or verify flags where the CLI supports them.

## Reference(s):

- [MaybeAI Uni homepage](https://github.com/OmniMCP-AI/maybeai-uni)
- [CLI Command Reference](references/cli-commands.md)
- [Read/Write Reference](references/read-write.md)
- [File Management Reference](references/file-management.md)
- [Base Mode Verification Runbook](references/base-mode-verification.md)
- [Workbook Metadata Reference](references/workbook-profile.md)
- [Formulas and Worksheet SQL Reference](references/formulas-sql.md)
- [Permission And Sharing Reference](references/permission-sharing.md)
- [Errors and Recovery Reference](references/errors-recovery.md)
- [Pivot Tables Reference](references/pivot-tables.md)
- [Charts and Formatting Reference](references/charts-formatting.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline mbs CLI commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires MAYBEAI_API_TOKEN and a locally available mbs CLI for execution.]

## Skill Version(s):

0.20.5 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
