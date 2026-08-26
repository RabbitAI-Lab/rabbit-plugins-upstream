## Description:

Guides agents in using the MaybeAI `mbs` CLI to inspect, import, edit, calculate, export, format, share, and materialize MaybeAI spreadsheet data safely.

This skill is ready for commercial/non-commercial use.

## Publisher:

[no7dw](https://clawhub.ai/user/no7dw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and spreadsheet automation agents use this skill to choose the correct MaybeAI `mbs` CLI commands for workbook inspection, Sheet and Base reads and writes, formulas, SQL materialization, formatting, file operations, and sharing workflows. It emphasizes runtime help discovery, target inspection, dry runs, verification, and readback before mutations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide agents to use an API token for MaybeAI spreadsheet edits, imports, exports, sharing changes, and SQL materialization.

Mitigation: Install only when the agent is intended to manage MaybeAI spreadsheets, and confirm token availability and intended scope before live operations.

Risk: Public-sharing and overwrite-style workflows could expose or replace sensitive spreadsheet data.

Mitigation: Confirm the exact workbook, worksheet or table target, access level, and data sensitivity before public sharing, overwrite, delete, or broad refresh commands.

Risk: Using the wrong Sheet, SheetTable, Base, or SQL target model can produce incorrect commands or unsafe mutations.

Mitigation: Inspect the workbook and list worksheets or tables before mutation, then use dry-run, verification flags, and target-appropriate readback.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/no7dw/skills/maybeai-sheet-cli)
- [ClawHub Metadata Homepage](https://github.com/OmniMCP-AI/maybeai-uni)
- [CLI Command Reference](references/cli-commands.md)
- [Read/Write Reference](references/read-write.md)
- [File Management Reference](references/file-management.md)
- [Permission And Sharing Reference](references/permission-sharing.md)
- [Errors and Recovery Reference](references/errors-recovery.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown with inline shell commands, JSON snippets, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the `mbs` CLI and `MAYBEAI_API_TOKEN` for live MaybeAI spreadsheet operations.]

## Skill Version(s):

v0.21.3 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
