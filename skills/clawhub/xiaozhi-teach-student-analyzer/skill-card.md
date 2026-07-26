## Description: <br>
帮助老师从凭经验判断学情升级为数据驱动的教学决策，基于成绩数据生成班级画像、共性弱项、个体诊断和差异化教学建议。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[qizhitang](https://clawhub.ai/user/qizhitang) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External teachers use this skill to analyze class assessment data, identify common weak points, diagnose individual learning patterns, and turn findings into differentiated teaching actions. It is intended for authorized education data supplied by the teacher or connected teaching skills. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive student or class data could be exposed in reports or cross-skill sharing. <br>
Mitigation: Use only authorized class data, prefer student IDs or aliases, avoid public reports with real names, and confirm before sharing or writing outputs into other skills. <br>
Risk: Individual diagnoses may be overstated when the data sample is too small. <br>
Mitigation: Require repeated evidence for stable conclusions and mark conclusions as evidence insufficient when history is limited. <br>
Risk: Score analysis could turn into misleading forecasts, labels, or anxiety-inducing parent communication. <br>
Mitigation: Do not predict future scores or rankings, avoid character judgments, and keep parent-facing output grounded in objective evidence and practical next steps. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-student-analyzer) <br>
- [学情分析框架与模板](references/analysis-framework.md) <br>
- [班级学情报告模板](references/class-report-template.md) <br>
- [学生个体诊断卡模板](references/student-diagnosis-card-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Analysis, Guidance] <br>
**Output Format:** [Markdown reports and structured text templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses teacher-provided class data; outputs should avoid real names in public reports and mark insufficient evidence when data is limited.] <br>

## Skill Version(s): <br>
2.0.0 (source: release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
