## Description: <br>
Builds real, formula-driven Excel (.xlsx) models with centralized inputs, calculation sheets, live formulas, and readable formatting for editable financial, budget, forecast, pricing, or scenario workbooks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mohitagw15856](https://clawhub.ai/user/mohitagw15856) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and analysts use this skill to have an agent design and generate editable Excel workbook models with live formulas, centralized assumptions, and a short explanation of model structure and editable inputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires code execution to create workbook files. <br>
Mitigation: Run generated scripts only in an appropriate code-execution environment and review the script before executing it. <br>
Risk: The referenced bundled helper script is absent from the inspected artifact. <br>
Mitigation: Have the agent generate or inspect an openpyxl-based script directly instead of assuming the helper exists. <br>
Risk: A generated spreadsheet can contain incorrect formulas or misleading assumptions. <br>
Mitigation: Review the workbook formulas, centralized input cells, and README assumptions before relying on the model. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mohitagw15856/skills/excel-model) <br>
- [Skill homepage](https://mohitagw15856.github.io/pm-claude-skills/skill/excel-model.html) <br>


## Skill Output: <br>
**Output Type(s):** [files, markdown, code, shell commands, guidance] <br>
**Output Format:** [Excel .xlsx workbook plus a Markdown README and generated Python/openpyxl script when code execution is available.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a code-execution environment to create workbook files; without execution, the agent should provide a clear model specification instead of claiming a file was produced.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
