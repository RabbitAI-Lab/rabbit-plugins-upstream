## Description: <br>
Fits a power-curve retention model to observed cohort data, projects retention and lifetime periods, and can generate an editable spreadsheet for ARPU-based LTV calculations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mohitagw15856](https://clawhub.ai/user/mohitagw15856) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Product, finance, and growth analysts use this skill to fit retention curves from real cohort data, project lifetime periods, and calculate horizon-bound LTV from ARPU. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The submitted artifact references a local helper script for workbook generation, but the submitted artifact did not include that script. <br>
Mitigation: Verify the package contents and execution environment before relying on workbook generation. <br>
Risk: Retention and LTV projections can be misleading when based on too few periods, a poor fit, or an unstated horizon. <br>
Mitigation: Require at least four observed periods, report fit quality and horizon, and treat poor-fit projections as unreliable beyond the observed tail. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/mohitagw15856/skills/cohort-curve-model) <br>
- [Skill Homepage](https://mohitagw15856.github.io/pm-claude-skills/skill/cohort-curve-model.html) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Shell commands, Files, Guidance] <br>
**Output Format:** [Markdown analysis with optional bash command and .xlsx workbook output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires observed retention inputs; optional ARPU and horizon; workbook generation depends on the referenced helper script being present.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
