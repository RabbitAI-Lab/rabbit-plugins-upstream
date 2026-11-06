## Description:

把“从头再讲一遍”变成有间隔、有交叉、有取舍的复习排期。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

面向小学至高中教师，依据复习范围、班级共性薄弱点和考试时间，梳理知识图谱与重难点，并起草阶段策略、间隔回看和易混知识交叉练习的排期。

### Deployment Geography for Use:

China (mainland-focused curriculum and exam examples)

## Known Risks and Mitigations:

Risk: Class review plans may expose sensitive student information when they include identifiable or individual-level data.

Mitigation: Use aggregated class information and pseudonyms, review each plan, and get teacher approval before storage; confirm that the platform's consent, deletion, sharing, and reminder controls are in place.

Risk: AI-generated review questions may contain errors.

Mitigation: Manually check generated questions before using them with students.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-review-planner)
- [Publisher profile](https://clawhub.ai/user/qizhitang)
- [Skill instructions and boundaries](artifact/SKILL.md)
- [Spacing and interleaving review strategy](artifact/references/review-strategy.md)
- [Knowledge map example](artifact/references/knowledge-map-example.md)
- [Review activity examples](artifact/references/review-activity-library.md)
- [Key points checklist template](artifact/references/key-points-checklist-template.md)
- [Class teaching workspace data schema](artifact/shared/class-teaching-workspace.schema.json)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Configuration]

**Output Format:** [Markdown review plans with structured review-plan entries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Drafts for teacher review; storage requires explicit approval. The skill plans review activities and timing rather than producing complete assignments or exams.]

## Skill Version(s):

2.12.6 (source: server-resolved release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
