## Description: <br>
帮助零基础用户通过交互式问答完成ISO31000合规风险评估与应对；当用户需要风险识别、风险分析、风险应对或生成风险管理报告时使用 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[duding-engicool](https://clawhub.ai/user/duding-engicool) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Manufacturing, quality, and operations teams use this skill to run an ISO31000-style risk assessment conversation, import Excel risk lists when provided, score and prioritize risks, and generate Markdown risk assessment reports or response action plans. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The Excel parser may read all sheets in an uploaded workbook and print extracted business-risk data. <br>
Mitigation: Use non-sensitive test workbooks first, specify a sheet name where possible, and run the skill only in environments where command output and logs are protected. <br>
Risk: Generated risk reports and response plans may contain sensitive operational, supplier, quality, or safety information and may be saved locally. <br>
Mitigation: Review generated files before sharing, store them in approved locations, and avoid including confidential data unless the workspace meets the organization’s data-handling requirements. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/duding-engicool/skills/skill-iso31000-risk-assessment) <br>
- [Server-resolved source repository](https://github.com/duding-engicool/skill-iso31000-risk-assessment) <br>
- [Publisher profile](https://clawhub.ai/user/duding-engicool) <br>
- [Report templates](references/report-templates.md) <br>
- [Risk response strategies](references/response-strategies.md) <br>
- [Risk numbering mechanism](references/risk-numbering.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration, text] <br>
**Output Format:** [Markdown reports, Markdown tables, conversational guidance, and JSON output from the optional Excel parser script] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save local Markdown report files and may print parsed Excel workbook data when the optional parser is used.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
