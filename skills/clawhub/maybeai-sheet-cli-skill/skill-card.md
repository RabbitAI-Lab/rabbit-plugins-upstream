## Description: <br>
Use when the user works with MaybeAI spreadsheets through the mbs CLI for workbook inspection, local or remote-URL file import, native cross-workbook import/export, worksheet/range/table writes, full worksheet data refreshes that keep headers, formulas, worksheet styling, chart/image CRUD, dashboard validate/refresh flows, or sharing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[no7dw](https://clawhub.ai/user/no7dw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and spreadsheet operators use this skill to inspect, import, edit, format, calculate, and share MaybeAI workbooks through the mbs CLI while following worksheet targeting and verification guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The CLI can access MaybeAI workbook content through MAYBEAI_API_TOKEN. <br>
Mitigation: Use a token scoped for the intended workbooks and install the skill only where that workbook access is acceptable. <br>
Risk: Metadata and profile commands may expose sample rows or sensitive workbook details. <br>
Mitigation: Review workbook sensitivity before profiling or sampling data, and avoid running these commands on confidential sheets unless disclosure is acceptable. <br>
Risk: Sharing, deletion, or full worksheet replacement commands can expose or change workbook data. <br>
Mitigation: Require explicit user confirmation before public sharing, editor grants, deletion, or replacement, and prefer dry-run and verification flags when available. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/no7dw/skills/maybeai-sheet-cli-skill) <br>
- [MaybeAI Uni homepage](https://github.com/OmniMCP-AI/maybeai-uni) <br>
- [CLI Command Reference](references/cli-commands.md) <br>
- [Read/Write Reference](references/read-write.md) <br>
- [File Management Reference](references/file-management.md) <br>
- [Permission And Sharing Reference](references/permission-sharing.md) <br>
- [Formulas and SQL Reference](references/formulas-sql.md) <br>
- [Charts and Formatting Reference](references/charts-formatting.md) <br>
- [Pivot Tables Reference](references/pivot-tables.md) <br>
- [Workbook Profile Reference](references/workbook-profile.md) <br>
- [Formula Lineage Trace Reference](references/lineage-trace.md) <br>
- [Errors and Recovery Reference](references/errors-recovery.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and configuration snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires MAYBEAI_API_TOKEN for workbook access through the mbs CLI.] <br>

## Skill Version(s): <br>
0.16.1 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
