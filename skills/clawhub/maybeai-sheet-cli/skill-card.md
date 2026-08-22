## Description:

Use when the user works with MaybeAI spreadsheets through the mbs CLI for workbook inspection, local or remote-URL file import, native cross-workbook import/export, worksheet/range/table writes, full worksheet data refreshes that keep headers, formulas, worksheet styling, chart/image CRUD, dashboard validate/refresh/export-template flows, or sharing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[no7dw](https://clawhub.ai/user/no7dw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect, import, edit, style, validate, export, and share MaybeAI spreadsheets through the mbs CLI while choosing the correct Sheet, Base Table, or SQL Config workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent to change, share, delete, restore, or migrate MaybeAI workbooks using MAYBEAI_API_TOKEN.

Mitigation: Require explicit approval before public links, editor grants, workbook deletion, history restore, or one-way conversion, and verify workbook metadata plus post-operation results.

Risk: Spreadsheet operations may touch sensitive business or personal data.

Mitigation: Confirm the intended workbook, worksheet, and data classification before import, export, sharing, or write operations; avoid public or editor access unless specifically approved.

Risk: The skill includes environment-changing install and setup guidance.

Mitigation: Review package installation and setup commands before execution and install only in approved environments.

## Reference(s):

- [MaybeAI Sheet CLI Skill Page](https://clawhub.ai/no7dw/skills/maybeai-sheet-cli)
- [MaybeAI CLI Homepage](https://github.com/OmniMCP-AI/maybeai-uni)
- [README](README.md)
- [Command Catalog](references/cli-commands.md)
- [Read and Write Reference](references/read-write.md)
- [Base Mode Verification](references/base-mode-verification.md)
- [File Management](references/file-management.md)
- [Formulas and SQL](references/formulas-sql.md)
- [Permission and Sharing](references/permission-sharing.md)
- [Charts and Formatting](references/charts-formatting.md)
- [Pivot Tables](references/pivot-tables.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON/configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires mbs and MAYBEAI_API_TOKEN for live spreadsheet operations.]

## Skill Version(s):

0.20.6 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
