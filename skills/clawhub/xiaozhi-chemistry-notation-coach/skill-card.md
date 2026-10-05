## Description:

面向中国大陆初高中化学学习者，分级练习元素符号、化合价、化学式和方程式的书写与配平，并延伸至高中化学用语。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

学生使用本技能循序练习化学用语、诊断书写错误，并通过提示自行完成化学式和方程式；教师或监护人可在适用情境下陪同使用。

### Deployment Geography for Use:

中国大陆；其他地区使用前须调整课程范围、危机求助渠道及未成年人数据同意规则。

## Known Risks and Mitigations:

Risk: Curriculum assumptions, crisis resources and minor-data consent rules may not fit users outside mainland China.

Mitigation: Use in the intended Chinese-language mainland China K12 context, or localize these rules and resources before deployment elsewhere.

Risk: Learning-progress summaries and reminders may expose a minor's study data if enabled without informed consent.

Mitigation: Keep session-only practice as the default; review profile, sharing and reminder permissions with the student or guardian and enable them only with explicit consent.

Risk: Incorrect chemical formulas or unbalanced equations could mislead students.

Mitigation: Check generated exercises against the included notation rules and verify formulas and atom counts before presenting them.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-chemistry-notation-coach)
- [化学用语基础规则](artifact/references/chemistry-notation-rules.md)
- [高中必修化学用语](artifact/references/chemistry-hs2-notation.md)
- [高中选择性必修化学用语](artifact/references/chemistry-hs3-notation.md)
- [化学错因维度表](artifact/shared/chemistry-error-dimension-table.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown text with short exercises, staged hints and notation checks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Up to five questions per practice set; learning profiles and reminders require explicit consent.]

## Skill Version(s):

2.10.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
