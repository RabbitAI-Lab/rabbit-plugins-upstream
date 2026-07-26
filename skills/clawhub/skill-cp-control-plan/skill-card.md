## Description: <br>
提供CP控制计划模板生成、数据分析、风险预警、可视化及版本管理指导，帮助质量工程师编制、审查和优化控制计划。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[duding-engicool](https://clawhub.ai/user/duding-engicool) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Quality engineers and manufacturing teams use this skill to create CP control plans, analyze CSV or Excel quality data, identify process-capability and FMEA/SPC risks, and generate report-ready JSON results and PNG charts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Quality datasets may contain confidential production, supplier, or customer information. <br>
Mitigation: Review CSV and Excel inputs before use and keep generated JSON and PNG outputs in approved local storage locations. <br>
Risk: Incorrect source data, specification limits, or thresholds can produce misleading process-capability and risk recommendations. <br>
Mitigation: Have a qualified quality engineer verify inputs, thresholds, and generated recommendations before using them in controlled quality processes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/duding-engicool/skills/skill-cp-control-plan) <br>
- [Publisher profile](https://clawhub.ai/user/duding-engicool) <br>
- [Server-resolved GitHub provenance](https://github.com/duding-engicool/skill-cp-control-plan) <br>
- [CP template guide](references/cp_template_guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Shell commands, Configuration, JSON, Files, Guidance] <br>
**Output Format:** [Markdown guidance with bash examples, local JSON analysis outputs, and PNG chart files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reads user-selected CSV, Excel, or JSON files and writes local JSON and PNG outputs to caller-specified paths.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
