## Description:

帮助初高中数学教师从作业和试卷错题中识别共性错因、定位知识薄弱点，并制定下节课的教学干预建议。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

面向获准处理学生测评数据的初高中数学教师：分析班级和个体错因，生成知识点热力图、错因画像与需教师确认的教学建议。

### Deployment Geography for Use:

Mainland China (localize curriculum, privacy and crisis referral guidance before use elsewhere)

## Known Risks and Mitigations:

Risk: Student assessment data or individual error profiles could expose minors' information.

Mitigation: Use only authorized data, pseudonymize students, restrict sharing, and require consent and teacher confirmation before student-record writeback.

Risk: Sampled errors or AI-generated exercises could be mistaken for verified whole-class findings or checked assessments.

Mitigation: Label sample size and scope, avoid percentages for very small samples, and have a teacher check exercises and recommendations before classroom use.

Risk: Curriculum, privacy rules, and crisis referral channels may not fit use outside the intended Chinese-language teaching context.

Mitigation: Localize these requirements and verify authorized handling and local referral options before deployment elsewhere.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-math-error-analyzer)
- [错因分类细则](artifact/references/error-classification-rubric.md)
- [知识图谱模板](artifact/references/knowledge-map-template.md)
- [教学干预设计](artifact/references/intervention-design.md)
- [班级错因报告模板](artifact/references/class-error-report-template.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown analysis reports and teaching recommendations; optional structured workspace updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Distinguishes sampled results from whole-class statistics; teacher confirmation required before writeback.]

## Skill Version(s):

2.9.0 (source: ClawHub release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
