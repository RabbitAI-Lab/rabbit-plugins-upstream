## Description:

Use when the user works with MaybeAI spreadsheets through the mbs CLI for workbook inspection, local or remote-URL file import, native cross-workbook import/export, worksheet/range/table writes, full worksheet data refreshes that keep headers, formulas, worksheet styling, chart/image CRUD, dashboard validate/refresh/export-template flows, or sharing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[no7dw](https://clawhub.ai/user/no7dw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and spreadsheet automation agents use this skill to inspect, import, modify, style, calculate, export, and share MaybeAI workbooks through the mbs CLI. It is suited for workflows that need metadata-first targeting, verified worksheet or table writes, Base table operations, formula and SQL materialization, dashboard refresh flows, and permission checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide agents through broad workbook mutations, including overwrites, migration flows, imports, and sharing changes.

Mitigation: Require explicit user confirmation for destructive overwrites, public sharing, editor grants, migrations, and remote URL imports; prefer dry runs and verification reads when the skill describes them.

Risk: Use of a raw API escape hatch could bypass safer first-class CLI workflows.

Mitigation: Use first-class mbs commands whenever possible and review the exact endpoint and request body before allowing raw API calls.

Risk: The skill operates with the user's MaybeAI API token and can affect accessible spreadsheets.

Mitigation: Install only when the agent is expected to operate on MaybeAI spreadsheets, and scope use to workbooks and commands the user has approved.

## Reference(s):

- [MaybeAI Sheet CLI homepage](https://github.com/OmniMCP-AI/maybeai-uni)
- [CLI Command Reference](references/cli-commands.md)
- [Read/Write Reference](references/read-write.md)
- [File Management Reference](references/file-management.md)
- [Base Mode Verification Runbook](references/base-mode-verification.md)
- [Errors and Recovery Reference](references/errors-recovery.md)
- [Permission And Sharing Reference](references/permission-sharing.md)
- [Charts and Formatting Reference](references/charts-formatting.md)
- [Workbook Metadata Reference](references/workbook-profile.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, code, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON or configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires MAYBEAI_API_TOKEN and a locally available mbs CLI; many workflows include verification reads or explicit confirmation flags before mutation.]

## Skill Version(s):

0.20.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
