## Description: <br>
Guides agents using the `mbs` CLI to inspect, import, edit, format, dashboard, template, and share MaybeAI spreadsheets. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[no7dw](https://clawhub.ai/user/no7dw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and spreadsheet automation agents use this skill to operate MaybeAI workbooks through the `mbs` CLI, including data import, worksheet and table edits, formulas, styling, dashboards, and sharing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Authenticated write, share, and delete workflows can change workbook data or access. <br>
Mitigation: Use the skill only on intended spreadsheets, inspect workbook metadata before acting, and prefer dry-run, --verify, and readback checks for mutating commands. <br>
Risk: Public or editor sharing can expose sensitive workbook content. <br>
Mitigation: Review target emails, visibility, and permission level before running share commands; prefer private visibility and viewer access unless the user explicitly requests broader access. <br>
Risk: The raw API escape hatch can issue broad MaybeAI API requests. <br>
Mitigation: Avoid `mbs raw post` unless the endpoint and request body have been explicitly reviewed and a first-class CLI command is unavailable. <br>
Risk: A MaybeAI API token may grant access to sensitive workbooks. <br>
Mitigation: Protect MAYBEAI_API_TOKEN, use the least-privileged token available, and avoid running the skill against workbooks outside the user's stated task. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/no7dw/skills/maybeai-sheet-cli) <br>
- [Publisher profile](https://clawhub.ai/user/no7dw) <br>
- [MaybeAI Uni homepage](https://github.com/OmniMCP-AI/maybeai-uni) <br>
- [CLI Command Reference](references/cli-commands.md) <br>
- [Read/Write Reference](references/read-write.md) <br>
- [File Management Reference](references/file-management.md) <br>
- [Permission And Sharing Reference](references/permission-sharing.md) <br>
- [Charts and Formatting Reference](references/charts-formatting.md) <br>
- [Formulas and SQL Reference](references/formulas-sql.md) <br>
- [Pivot Tables Reference](references/pivot-tables.md) <br>
- [Errors and Recovery Reference](references/errors-recovery.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, code, markdown] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires MAYBEAI_API_TOKEN for live MaybeAI workbook operations.] <br>

## Skill Version(s): <br>
0.18.0 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
