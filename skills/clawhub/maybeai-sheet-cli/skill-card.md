## Description:

Guides agents using the mbs CLI to inspect, import, edit, export, share, and verify MaybeAI spreadsheets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[no7dw](https://clawhub.ai/user/no7dw)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate MaybeAI spreadsheet workflows through the mbs CLI, including workbook discovery, imports, Sheet and Base reads and writes, SQL materialization, formatting, dashboard refresh/export, and sharing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent that has a MaybeAI API token to read, create, modify, delete, export, and share spreadsheets.

Mitigation: Install only for intended MaybeAI spreadsheet automation, review workbook-changing actions before execution, and prefer dry-run plus verification for mutations.

Risk: Sharing workflows, public/editor permissions, remote URL imports, and dashboard template exports can broaden access or move spreadsheet data outside the current context.

Mitigation: Confirm source URLs, export destinations, recipients, and permission levels before execution, and use least-privilege sharing when access changes are required.

Risk: The installed mbs CLI command surface can differ from examples in the skill documentation.

Mitigation: Run mbs --help and the relevant subcommand help before generating commands, and report a capability gap when public commands do not support the requested operation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/no7dw/skills/maybeai-sheet-cli)
- [MaybeAI unified repository](https://github.com/OmniMCP-AI/maybeai-uni)
- [README](README.md)
- [CLI commands](references/cli-commands.md)
- [Read and write workflows](references/read-write.md)
- [File management](references/file-management.md)
- [Workbook profile](references/workbook-profile.md)
- [Base mode verification](references/base-mode-verification.md)
- [Formulas and SQL](references/formulas-sql.md)
- [Charts and formatting](references/charts-formatting.md)
- [Sharing and permissions](references/permission-sharing.md)
- [Errors and recovery](references/errors-recovery.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON or configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include dry-run, verification, and runtime-help command discovery steps.]

## Skill Version(s):

v0.21.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
