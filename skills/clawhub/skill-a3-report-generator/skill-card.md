## Description: <br>
辅助用户完成A3改善报告；通过强制交互收集信息、逐步追问验证、生成可编辑的HTML格式报告，适用于生产现场改善、质量问题分析等场景。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[duding-engicool](https://clawhub.ai/user/duding-engicool) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external users, and developers use this skill to guide A3 continuous-improvement reporting for production-site improvement, quality analysis, and improvement proposals. The skill collects structured inputs, validates STAR, SMART, 5Why, action-plan, and verification details, then helps generate an editable HTML A3 report. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated HTML reports can include sensitive operational details or browser-added images that may be exposed if shared broadly. <br>
Mitigation: Keep reports in normal project or output folders, review content before sharing, and avoid adding sensitive information to reports intended for distribution. <br>
Risk: An incomplete A3 input set can lead to an incomplete or misleading improvement report. <br>
Mitigation: Use the skill's staged validation prompts for STAR, current-state data, SMART goals, 5Why root causes, action plans, and verification before generating the report. <br>


## Reference(s): <br>
- [A3 report standard reference](references/a3-standard.md) <br>
- [ClawHub skill page](https://clawhub.ai/duding-engicool/skills/skill-a3-report-generator) <br>
- [Server-resolved source repository](https://github.com/duding-engicool/skill-a3-report-generator) <br>


## Skill Output: <br>
**Output Type(s):** [text, guidance, shell commands, code, files] <br>
**Output Format:** [Markdown guidance with inline shell command examples and a generated editable HTML report file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The generated report is a local A3 landscape HTML file with editable fields, print/export controls, and optional browser-added images.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release metadata; artifact frontmatter reports 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
