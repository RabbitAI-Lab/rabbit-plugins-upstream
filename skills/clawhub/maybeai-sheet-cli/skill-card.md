## Description: <br>
Use when the user works with MaybeAI spreadsheets through the mbs CLI for workbook inspection, local or remote-URL file import, native cross-workbook import/export, worksheet/range/table writes, full worksheet data refreshes that keep headers, formulas, worksheet styling, chart/image CRUD, dashboard validate/refresh/export-template flows, or sharing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[no7dw](https://clawhub.ai/user/no7dw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to inspect, import, edit, verify, export, and share MaybeAI spreadsheets through the mbs CLI. It is suited for workbook operations that require precise worksheet targeting, post-write verification, formula handling, styling, dashboard execution, and guarded sharing changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read, modify, export, and share MaybeAI workbooks using the user's MAYBEAI_API_TOKEN. <br>
Mitigation: Install only when workbook automation is intended, keep the token scoped and protected, and confirm document IDs, worksheet names, writes, exports, deletes, conversions, and sharing changes before execution. <br>
Risk: Workbook metadata profiling on sensitive sheets may expose sample rows for summarization. <br>
Mitigation: Avoid metadata profiling on highly sensitive workbooks unless sample rows are permitted for the task. <br>
Risk: Some worksheet migrations and data refreshes are destructive or one-way. <br>
Mitigation: Use dry-run flows where available, target a single worksheet explicitly, and run verification after execution. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/no7dw/skills/maybeai-sheet-cli) <br>
- [Metadata Homepage](https://github.com/OmniMCP-AI/maybeai-uni) <br>
- [CLI Command Reference](references/cli-commands.md) <br>
- [Read/Write Reference](references/read-write.md) <br>
- [File Management Reference](references/file-management.md) <br>
- [Workbook Profile Reference](references/workbook-profile.md) <br>
- [Permission And Sharing Reference](references/permission-sharing.md) <br>
- [Formulas and SQL Reference](references/formulas-sql.md) <br>
- [Pivot Tables Reference](references/pivot-tables.md) <br>
- [Formula Lineage Trace Reference](references/lineage-trace.md) <br>
- [Charts and Formatting Reference](references/charts-formatting.md) <br>
- [Errors and Recovery Reference](references/errors-recovery.md) <br>
- [Maybe Sheet Clickable References](references/clickable-refs.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Code] <br>
**Output Format:** [Markdown with inline bash commands, JSON examples, and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are agent-facing instructions for using the mbs CLI with MaybeAI workbooks; commands may read, modify, export, or share spreadsheets when run with a valid MAYBEAI_API_TOKEN.] <br>

## Skill Version(s): <br>
0.19.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
