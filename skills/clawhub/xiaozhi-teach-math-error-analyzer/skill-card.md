## Description:

数学教师的班级错因分析：把作业与试卷的错题变成"下节数学课讲什么"。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Chinese-language middle-school math teachers use this skill to turn homework and exam error data into class-level error analysis, knowledge-point weakness maps, student error profiles, and teaching intervention suggestions.

### Deployment Geography for Use:

China; localize curriculum, consent rules, and crisis/help-channel guidance before use in other regions.

## Known Risks and Mitigations:

Risk: The workflow handles middle-school assessment data and may involve student consent and sharing decisions.

Mitigation: Use pseudonyms or student IDs, honor consent and sharing controls, and keep teacher review in the loop before sharing student-facing or parent-facing content.

Risk: Generated practice items or intervention suggestions may be mathematically incorrect or unsuitable for the class.

Mitigation: Require teacher verification before assigning generated items, and label AI-generated exercises for manual checking before use.

Risk: The skill is tailored to Chinese-language middle-school math and China-oriented support guidance.

Mitigation: Localize curriculum mappings, consent expectations, and crisis/help-channel guidance before use in non-Chinese classrooms or outside China.

Risk: Student distress or safety signals can fall outside the scope of ordinary math error analysis.

Mitigation: Pause analysis when crisis signals appear and follow the bundled crisis referral path instead of continuing educational diagnosis.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-math-error-analyzer)
- [错因分类细则](references/error-classification-rubric.md)
- [教学干预设计模板](references/intervention-design.md)
- [数学知识图谱模板](references/knowledge-map-template.md)
- [班级共性错因报告模板](references/class-error-report-template.md)
- [学员错因档案模板](references/student-error-profile-template.md)
- [AI 出题自检协议](shared/ai-item-check.md)
- [危机例外](shared/crisis-exception.md)
- [平台能力约定与降级路径](shared/platform-conventions.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Configuration]

**Output Format:** [Markdown reports, teaching recommendations, error-profile templates, and structured class workspace guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are teacher-facing drafts that should identify sample scope, distinguish full-class data from sampled evidence, and mark AI-generated practice items for human verification.]

## Skill Version(s):

2.2.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
