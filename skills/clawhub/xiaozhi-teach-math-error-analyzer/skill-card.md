## Description:

数学教师的班级错因分析：把作业与试卷的错题变成“下节数学课讲什么”，通过错题收集、阈值触发、抽样、错因分类、知识图谱定位、班级/个体画像和教学干预建议支持教师复盘。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External educators and teaching assistants use this skill to analyze middle-school math homework or assessment errors, identify class-wide and individual misconceptions, map them to knowledge points, and draft targeted intervention plans. It is intended to support teacher review and planning, not to replace grading, ranking, classroom teaching, or teacher judgment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Student assessment data and error profiles may contain sensitive minor-related education information.

Mitigation: Use pseudonyms or student numbers in reports, keep real student names out of error records, and confirm consent before profile writeback or parent-facing sharing.

Risk: Sampled error analysis or small sample sizes can be mistaken for whole-class statistics.

Mitigation: Label sampled results with the sample count, avoid percentages for samples below 10, and keep insufficient-sample findings out of long-term profiles.

Risk: Generated practice items or intervention suggestions may be mathematically incorrect or unsuitable for assessment use.

Mitigation: Mark AI-generated items for teacher verification and require human checking before adding them to homework, tests, or resource banks.

Risk: Crisis or safety signals from students can require responses outside normal learning analytics.

Mitigation: Stop the normal analysis flow, use the bundled crisis referral protocol, and localize emergency contacts and legal assumptions for the deployment region.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-math-error-analyzer)
- [Class error report template](references/class-error-report-template.md)
- [Error classification rubric](references/error-classification-rubric.md)
- [Error-knowledge link template](references/error-knowledge-link-template.md)
- [Intervention design template](references/intervention-design.md)
- [Student error profile template](references/student-error-profile-template.md)
- [Class teaching workspace schema](shared/class-teaching-workspace.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Markdown reports, structured analysis templates, and schema-aligned guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include class error reports, knowledge-point heatmaps, student error profiles, intervention suggestions, consent-aware writeback guidance, and labels for sampled or AI-generated content.]

## Skill Version(s):

2.3.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
