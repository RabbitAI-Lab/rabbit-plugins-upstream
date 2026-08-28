## Description:

Guides agents using the mbs CLI to inspect, import, edit, calculate, export, dashboard, template, and share MaybeAI spreadsheets with model-aware verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[no7dw](https://clawhub.ai/user/no7dw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and spreadsheet operators use this skill to have an agent work through MaybeAI spreadsheet workflows with the mbs CLI, including workbook discovery, imports, Sheet and Base reads or writes, formulas, SQL materialization, chart/image operations, dashboard flows, exports, and sharing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent using this skill can read or modify specified MaybeAI workbooks with the configured API token.

Mitigation: Install it only for intended spreadsheet automation, confirm workbook IDs before mutations, and use dry-run and verify flows for destructive or unfamiliar changes.

Risk: Sharing, export, and delete workflows can expose data, grant unintended access, or remove workbook content.

Mitigation: Avoid public or editor sharing unless explicitly requested, store exported files in secure locations, and require confirmation before destructive operations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/no7dw/skills/maybeai-sheet-cli)
- [Project homepage](https://github.com/OmniMCP-AI/maybeai-uni)
- [CLI Command Reference](references/cli-commands.md)
- [Read/Write Reference](references/read-write.md)
- [File Management Reference](references/file-management.md)
- [Permission And Sharing Reference](references/permission-sharing.md)
- [Formulas and SQL Reference](references/formulas-sql.md)
- [Charts and Formatting Reference](references/charts-formatting.md)
- [Errors and Recovery Reference](references/errors-recovery.md)
- [Workbook Inspection Reference](references/workbook-profile.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON configuration examples, and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are agent-facing instructions for using the installed mbs CLI and should be checked against runtime help before execution.]

## Skill Version(s):

v0.21.4 (source: SKILL.md frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
