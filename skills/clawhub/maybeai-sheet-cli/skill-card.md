## Description:

Guides agents using the MaybeAI `mbs` CLI to inspect, import, edit, style, calculate, dashboard, template, and share MaybeAI spreadsheets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[no7dw](https://clawhub.ai/user/no7dw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, spreadsheet operators, and agents use this skill to perform MaybeAI workbook and worksheet operations through the `mbs` CLI, including data import/export, targeted reads and writes, SQL-backed results, pivots, styling, dashboard refreshes, and sharing workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent with `MAYBEAI_API_TOKEN` can modify workbook content or change sharing settings.

Mitigation: Require explicit user confirmation before public visibility changes, editor grants, access removals, workbook writes, and sharing operations; verify the target workbook and worksheet before and after mutation.

Risk: Raw post calls and SQL overwrite or materialization can apply unintended backend changes or publish incorrect derived data.

Mitigation: Prefer first-class `mbs` commands, review raw request bodies and SQL before execution, use preview or dry-run paths when available, and verify materialized results.

Risk: Deletes, restores, and Sheet-to-Base conversion can be destructive or one-way.

Mitigation: Use dry-run flows where available, require explicit confirmation flags such as `--yes` or documented confirmation options, record stable worksheet identity such as `gid`, and read back results after the operation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/no7dw/skills/maybeai-sheet-cli)
- [MaybeAI CLI Source Homepage](https://github.com/OmniMCP-AI/maybeai-uni)
- [CLI Command Reference](references/cli-commands.md)
- [Read/Write Reference](references/read-write.md)
- [File Management Reference](references/file-management.md)
- [Base Mode Verification Runbook](references/base-mode-verification.md)
- [Formulas and Worksheet SQL Reference](references/formulas-sql.md)
- [Permission And Sharing Reference](references/permission-sharing.md)
- [Pivot Tables Reference](references/pivot-tables.md)
- [Charts and Formatting Reference](references/charts-formatting.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, markdown, code]

**Output Format:** [Markdown with inline shell commands, JSON snippets, and workflow guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires `MAYBEAI_API_TOKEN` and the `mbs` CLI for live workbook operations.]

## Skill Version(s):

0.20.4 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
