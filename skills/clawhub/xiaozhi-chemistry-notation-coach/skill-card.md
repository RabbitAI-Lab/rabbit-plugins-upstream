## Description:

面向初高中学生的中文化学用语教练，分级练习元素符号、化合价、化学式及方程式书写与配平，并延伸至高中化学表征。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

中文初高中学生使用分级提示练习化学符号、化合价、化学式及方程式的书写与配平；教师或监护人可协助核对练习内容及未成年人的数据授权。

### Deployment Geography for Use:

Global (Chinese-language K12 learning; follow local curricula and safeguarding requirements)

## Known Risks and Mitigations:

Risk: Student learning records, cross-skill sharing, reminders or parent-facing summaries could expose minors' information without appropriate consent.

Mitigation: Confirm student and guardian consent and local requirements before enabling any profile access, writeback, sharing, reminders or summaries; otherwise keep practice within the session.

Risk: Incorrect chemical formulas or unbalanced equations could mislead students.

Mitigation: Check generated formulas, coefficients and reaction conditions against the skill's chemistry references before presenting exercises.

## Reference(s):

- [ClawHub 技能页面](https://clawhub.ai/qizhitang/skills/xiaozhi-chemistry-notation-coach)
- [化学用语规则与配平](artifact/references/chemistry-notation-rules.md)
- [高中必修化学用语](artifact/references/chemistry-hs2-notation.md)
- [高中选择性必修化学用语](artifact/references/chemistry-hs3-notation.md)
- [化学错因维度表](artifact/shared/chemistry-error-dimension-table.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese-language conversational text with chemistry notation and worked practice prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May provide short practice sets, corrections and consent-based review reminders.]

## Skill Version(s):

2.9.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
