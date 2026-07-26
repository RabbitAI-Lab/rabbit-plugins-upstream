## Description: <br>
Use when the user works with MaybeAI spreadsheets through the mbs CLI for workbook inspection, local or remote-URL file import, native cross-workbook import/export, worksheet/range/table writes, full worksheet data refreshes that keep headers, formulas, worksheet styling, chart/image CRUD, dashboard validate/refresh flows, or sharing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[no7dw](https://clawhub.ai/user/no7dw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to drive MaybeAI spreadsheet work through the mbs CLI, including workbook inspection, imports, targeted reads and writes, formulas, styling, chart and image operations, dashboard refreshes, and sharing. It is intended for deliberate spreadsheet automation where commands are inspected, targeted, and verified before results are reported. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Spreadsheet automation can expose sensitive workbook data or use a MaybeAI API token against unintended data. <br>
Mitigation: Install only if you trust MaybeAI with the referenced spreadsheet data and token; prefer worksheet listing or narrow reads before broad profiling of sensitive workbooks. <br>
Risk: Sharing commands can grant unintended workbook access. <br>
Mitigation: Confirm the exact workbook, recipient, and viewer/editor/public setting before running sharing commands. <br>
Risk: Exports can write spreadsheet files to unapproved or conflicting local paths. <br>
Mitigation: Export only to approved, non-conflicting local paths. <br>
Risk: Writes, imports, refreshes, formulas, and styling can modify the wrong worksheet or create misleading spreadsheet results. <br>
Mitigation: Inspect workbook metadata first, target worksheets explicitly, use dry runs where available, pass --verify on supported writes, and read back or check errors before reporting success. <br>


## Reference(s): <br>
- [MaybeAI Uni Homepage](https://github.com/OmniMCP-AI/maybeai-uni) <br>
- [Command Catalog](references/cli-commands.md) <br>
- [Read and Write Reference](references/read-write.md) <br>
- [File Management Reference](references/file-management.md) <br>
- [Workbook Profile Reference](references/workbook-profile.md) <br>
- [Sharing and Permissions Reference](references/permission-sharing.md) <br>
- [Formulas and SQL Reference](references/formulas-sql.md) <br>
- [Pivot Tables Reference](references/pivot-tables.md) <br>
- [Lineage Trace Reference](references/lineage-trace.md) <br>
- [Charts and Formatting Reference](references/charts-formatting.md) <br>
- [Errors and Recovery Reference](references/errors-recovery.md) <br>
- [Clickable References Guide](references/clickable-refs.md) <br>
- [SQL Formula Showcase](references/sql-formula-showcase.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should name exact workbooks, worksheets, ranges, files, and verification steps when proposing or reporting spreadsheet actions.] <br>

## Skill Version(s): <br>
0.16.2 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
