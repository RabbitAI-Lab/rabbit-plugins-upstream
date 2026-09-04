## Description:

数学教师的班级错因分析：把作业与试卷的错题变成"下节数学课讲什么"。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External Chinese-language junior-high math teachers use this skill to analyze classwide and individual math error patterns from homework or exam data, connect errors to knowledge points, and plan follow-up teaching interventions. It supports reports, heatmaps, student error profiles, and teacher-confirmed writeback records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Student performance data may identify minors or expose sensitive learning patterns.

Mitigation: Use aliases or IDs, confirm teacher and student or guardian consent before writeback or parent sharing, and honor deletion, correction, pause, export, and sharing controls.

Risk: Generated practice items or interventions could be mathematically incorrect or unsuitable for assessment.

Mitigation: Require teacher review and manual verification before generated items are added to assignments, resources, or exams.

Risk: Sampled error classifications can be mistaken for whole-class statistics.

Mitigation: Label sampled findings with sample size, separate sampled results from full-class counts, and avoid percentages when samples are too small.

Risk: Embedded crisis support examples include mainland China emergency resources.

Mitigation: Use local emergency and mental-health resources when the skill is used outside mainland China.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-math-error-analyzer)
- [班级共性错因报告模板](references/class-error-report-template.md)
- [错因分类细则](references/error-classification-rubric.md)
- [错题-知识点关联样板](references/error-knowledge-link-template.md)
- [教学干预设计模板](references/intervention-design.md)
- [教学干预建议样板](references/intervention-report-template.md)
- [数学知识图谱模板](references/knowledge-map-template.md)
- [学员错因档案模板](references/student-error-profile-template.md)
- [Class teaching workspace schema](shared/class-teaching-workspace.schema.json)
- [AI 出题自检协议](shared/ai-item-check.md)
- [危机识别与转介协议](shared/crisis-referral-protocol.md)
- [全库统一词表](shared/vocab.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown reports, structured tables, heatmaps, templates, and teacher-confirmed records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Handles class error distributions, sampled error classifications, knowledge-point mappings, student profiles, and intervention suggestions.]

## Skill Version(s):

2.1.0 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
