## Description:

Helps agents inspect, import, edit, dashboard, template, and share MaybeAI spreadsheets through the mbs CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[no7dw](https://clawhub.ai/user/no7dw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and spreadsheet operators use this skill to guide agents through MaybeAI workbook inspection, imports, worksheet and table edits, formula and SQL workflows, styling, dashboard refreshes, and sharing tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide agents to read, edit, import, export, profile, and share MaybeAI spreadsheets using MAYBEAI_API_TOKEN.

Mitigation: Install it only for agents intended to operate on MaybeAI spreadsheets, and avoid metadata profiling for sensitive workbooks unless sample rows can be processed by the service or LLM.

Risk: Spreadsheet writes, imports, and refreshes can alter workbook data or formulas.

Mitigation: Use documented dry-run and verification steps, read back changed ranges or sentinel cells, and confirm the target worksheet identity before destructive updates.

Risk: Public or editor sharing can expose workbook contents or grant write access.

Mitigation: Require explicit confirmation before public visibility or editor grants, and check current permissions before changing access.

Risk: Converting a Sheet-backed worksheet to Base is a one-way migration that can remove source Sheet-engine cell content.

Mitigation: Target exactly one worksheet by gid or worksheet name, run convert-to-base with --dry-run first, then execute with --yes --verify only after confirming the intended migration.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/no7dw/skills/maybeai-sheet-cli)
- [MaybeAI Uni homepage](https://github.com/OmniMCP-AI/maybeai-uni)
- [CLI Command Reference](references/cli-commands.md)
- [Read/Write Reference](references/read-write.md)
- [File Management Reference](references/file-management.md)
- [Formulas and SQL Reference](references/formulas-sql.md)
- [Pivot Tables Reference](references/pivot-tables.md)
- [Permission And Sharing Reference](references/permission-sharing.md)
- [Errors and Recovery Reference](references/errors-recovery.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires MAYBEAI_API_TOKEN and a local mbs CLI installation for execution.]

## Skill Version(s):

0.20.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
