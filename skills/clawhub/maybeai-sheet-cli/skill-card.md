## Description:

Guides agents using the mbs CLI to inspect, import, edit, validate, export, and share MaybeAI spreadsheets across Sheet, SheetTable, Base, and worksheet SQL workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[no7dw](https://clawhub.ai/user/no7dw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate MaybeAI spreadsheets with the mbs CLI, including workbook discovery, file import, worksheet and table edits, formulas, dashboard flows, export, and sharing. It is best suited for workflows that need explicit target selection, verification, and command-level guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide workbook imports, edits, deletions, restores, public sharing changes, editor grants, exports, and one-way Sheet-to-Base conversions.

Mitigation: Confirm workbook IDs, worksheet targets, sharing changes, destructive actions, and conversions before execution; use dry-run and verification options where available.

Risk: The skill operates on MaybeAI spreadsheets through MAYBEAI_API_TOKEN when commands are executed.

Mitigation: Install it only where the agent should access MaybeAI spreadsheets, scope the token appropriately, and avoid exposing token values in outputs.

## Reference(s):

- [MaybeAI Uni homepage](https://github.com/OmniMCP-AI/maybeai-uni)
- [maybeai-sheet-cli-skill](README.md)
- [Base Mode Verification Runbook](references/base-mode-verification.md)
- [Charts and Formatting Reference](references/charts-formatting.md)
- [CLI Command Reference](references/cli-commands.md)
- [MaybeAI Sheet CLI Plan](references/cli-packaging-plan.md)
- [Maybe Sheet Clickable References](references/clickable-refs.md)
- [Engine Selection When Creating Data Products](references/engine-selection-when-create.md)
- [Errors and Recovery Reference](references/errors-recovery.md)
- [Sheet Worksheets With Multiple Tables](references/excelize-multiple-tables.md)
- [File Management Reference](references/file-management.md)
- [Formulas and Worksheet SQL Reference](references/formulas-sql.md)
- [Formula Lineage and Computation Evidence](references/lineage-trace.md)
- [Permission And Sharing Reference](references/permission-sharing.md)
- [Pivot Tables Reference](references/pivot-tables.md)
- [Read/Write Reference](references/read-write.md)
- [Legacy SQL Formula Showcase](references/sql-formula-showcase.md)
- [Workbook Metadata Reference](references/workbook-profile.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands, JSON snippets, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a MaybeAI API token when executing mbs commands; recommends dry-run, verification, and explicit target selection for risky operations.]

## Skill Version(s):

0.21.1 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
