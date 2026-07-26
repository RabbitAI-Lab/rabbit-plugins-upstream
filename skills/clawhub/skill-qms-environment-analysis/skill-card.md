## Description: <br>
基于QMS框架的内外部环境因素分析与可视化；用于ISO 9001质量管理体系内审/管理评审时识别机遇与风险、制定改进计划、生成SWOT/PESTEL分析报告 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[duding-engicool](https://clawhub.ai/user/duding-engicool) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
质量管理、内审和管理评审人员可使用该技能整理组织内外部环境因素，生成SWOT/PESTEL分析、风险矩阵图和QMS环境因素分析报告。它适用于年度管理评审、内审整改验证、质量目标制定和体系换版准备等场景。 <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Input JSON may include organization-specific QMS, risk, or business context. <br>
Mitigation: Use only data approved for this analysis workflow and avoid including unnecessary confidential details. <br>
Risk: Generated PDF reports and charts may contain sensitive internal analysis. <br>
Mitigation: Choose the output directory deliberately, review generated files before sharing, and apply the organization's document handling rules. <br>


## Reference(s): <br>
- [QMS环境因素技能 ClawHub listing](https://clawhub.ai/duding-engicool/skills/skill-qms-environment-analysis) <br>
- [Server-resolved GitHub provenance](https://github.com/duding-engicool/skill-qms-environment-analysis) <br>
- [QMS环境因素分析模板与格式规范](references/analysis-templates.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, Files] <br>
**Output Format:** [Markdown guidance with JSON examples and CLI commands; the bundled script can produce PNG charts and a PDF report.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reads user-provided JSON locally and writes generated analysis artifacts to a user-selected output directory.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata; artifact frontmatter and release changelog mention 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
