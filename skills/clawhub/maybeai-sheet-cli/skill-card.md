## Description:

Guides agents using the `mbs` CLI to inspect, import, edit, style, dashboard, template, and share MaybeAI spreadsheets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[no7dw](https://clawhub.ai/user/no7dw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and spreadsheet automation agents use this skill to operate MaybeAI workbooks through the `mbs` CLI, including workbook inspection, Sheet and Base mode reads and writes, imports, exports, formulas, pivots, dashboard maintenance, and sharing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose workbook contents through profiling, imports, exports, and sharing operations available to the MaybeAI account.

Mitigation: Install only with a token scoped to intended workbooks, use metadata and worksheet listing before sensitive operations, and avoid LLM-backed workbook profiling for sensitive workbooks.

Risk: Sharing commands can make workbooks public or grant editor access without strong confirmation safeguards.

Mitigation: Require explicit user confirmation before public or editor sharing changes and verify permissions after any share operation.

Risk: Remote URL import or export workflows can move workbook data to or from untrusted locations.

Mitigation: Verify external URLs before import or export and use preview, dry-run, or verification commands when the artifact workflow supports them.

## Reference(s):

- [MaybeAI Uni homepage](https://github.com/OmniMCP-AI/maybeai-uni)
- [CLI Command Reference](references/cli-commands.md)
- [Read/Write Reference](references/read-write.md)
- [File Management Reference](references/file-management.md)
- [Base Mode Verification Runbook](references/base-mode-verification.md)
- [Errors and Recovery Reference](references/errors-recovery.md)
- [Permission And Sharing Reference](references/permission-sharing.md)
- [Charts and Formatting Reference](references/charts-formatting.md)
- [Formulas and Worksheet SQL Reference](references/formulas-sql.md)
- [Pivot Tables Reference](references/pivot-tables.md)
- [Workbook Profile Reference](references/workbook-profile.md)
- [Formula Lineage and Computation Evidence](references/lineage-trace.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code, markdown, JSON]

**Output Format:** [Markdown with inline shell commands, JSON examples, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a MaybeAI API token and a locally available `mbs` CLI for live workbook operations.]

## Skill Version(s):

0.20.1 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
