## Description:

Guides agents using the mbs CLI to inspect, import, edit, refresh, export, dashboard, and share MaybeAI spreadsheets with runtime command discovery and verification practices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[no7dw](https://clawhub.ai/user/no7dw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and spreadsheet operators use this skill to have an agent plan and generate mbs CLI workflows for MaybeAI workbooks, including inspection, import/export, Sheet and Base edits, formulas, SQL materialization, formatting, sharing, and recovery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credentialed spreadsheet operations can import, edit, delete, export, or share MaybeAI workbooks using MAYBEAI_API_TOKEN.

Mitigation: Install only when that access is intended, and review requests before deletion, public sharing, editor grants, sensitive imports, or local exports.

Risk: Destructive or unfamiliar mutations may alter worksheet data, Base records, workbook contents, or workbook lifecycle state.

Mitigation: Use dry-run before execution, then use --verify and target-appropriate readback; preserve expected-revision or idempotency keys when concurrency protection is needed.

Risk: The installed mbs CLI command surface may differ from examples or older compatibility aliases.

Mitigation: Start sessions with mbs --version and mbs --help, inspect command-specific help before generating commands, and report capability gaps instead of using hidden compatibility commands.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/no7dw/skills/maybeai-sheet-cli)
- [MaybeAI Sheet CLI Homepage](https://github.com/OmniMCP-AI/maybeai-uni)
- [README](artifact/README.md)
- [CLI Command Reference](artifact/references/cli-commands.md)
- [Read/Write Reference](artifact/references/read-write.md)
- [File Management Reference](artifact/references/file-management.md)
- [Permission And Sharing Reference](artifact/references/permission-sharing.md)
- [Errors and Recovery Reference](artifact/references/errors-recovery.md)
- [Charts and Formatting Reference](artifact/references/charts-formatting.md)
- [Workbook Inspection Reference](artifact/references/workbook-profile.md)
- [Formulas and SQL Reference](artifact/references/formulas-sql.md)
- [Base Mode Verification Runbook](artifact/references/base-mode-verification.md)
- [Formula Lineage and Computation Evidence](artifact/references/lineage-trace.md)
- [Pivot Tables Reference](artifact/references/pivot-tables.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, code, configuration]

**Output Format:** [Markdown with inline shell commands and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires MAYBEAI_API_TOKEN and the maybeai-sheet-cli mbs command; emphasizes runtime help, dry-run previews, verification, and readback for mutations.]

## Skill Version(s):

v0.21.6 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
