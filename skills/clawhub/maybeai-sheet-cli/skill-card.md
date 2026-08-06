## Description: <br>
Helps agents inspect, import, edit, style, calculate, dashboard, and share MaybeAI spreadsheets through the mbs CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[no7dw](https://clawhub.ai/user/no7dw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external agents use this skill to operate MaybeAI spreadsheets with repeatable CLI workflows for workbook inspection, data import/export, worksheet and table writes, formula calculation, dashboard refreshes, and sharing. It is intended for spreadsheet operations where explicit targeting, dry runs, and verification steps reduce the chance of writing to the wrong workbook or exposing data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Workbook commands can change spreadsheet data, formulas, styles, charts, images, dashboards, or sharing settings. <br>
Mitigation: Inspect workbook metadata first, target worksheets or tables explicitly, use dry-run modes where available, and verify writes with bounded readback before reporting success. <br>
Risk: Workbook metadata, profile, sample, and read commands can expose spreadsheet content to backend services or LLM processing. <br>
Mitigation: Avoid using the skill on confidential spreadsheets unless approved, use least-privilege MaybeAI tokens, and limit reads to the smallest worksheet, range, table, or sample needed. <br>
Risk: Sharing commands can make a workbook public or grant editor access. <br>
Mitigation: Require explicit user confirmation for the exact workbook, audience, and permission level before public or editor sharing, then verify the resulting permissions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/no7dw/skills/maybeai-sheet-cli) <br>
- [Project homepage](https://github.com/OmniMCP-AI/maybeai-uni) <br>
- [Command catalog](references/cli-commands.md) <br>
- [Read/Write Reference](references/read-write.md) <br>
- [File Management Reference](references/file-management.md) <br>
- [Permission And Sharing Reference](references/permission-sharing.md) <br>
- [Formulas and SQL Reference](references/formulas-sql.md) <br>
- [Workbook Profile Reference](references/workbook-profile.md) <br>
- [Charts and Formatting Reference](references/charts-formatting.md) <br>
- [Pivot Tables Reference](references/pivot-tables.md) <br>
- [Errors and Recovery Reference](references/errors-recovery.md) <br>
- [Formula Lineage Trace Reference](references/lineage-trace.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON or configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include MaybeAI spreadsheet commands that read or mutate workbook data; requires MAYBEAI_API_TOKEN.] <br>

## Skill Version(s): <br>
0.19.1 (source: server release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
