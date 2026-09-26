## Description:

帮助中文 K–12 教师按双向细目表设计试卷、调整难度、改编试题并制定评分标准。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers use this skill to plan assessments, build two-way specification tables, select or revise questions, and draft marking rubrics. It can suggest item revisions from existing post-exam statistics but does not calculate those statistics or grade students.

### Deployment Geography for Use:

Mainland China; localize curriculum, privacy requirements, and crisis contacts before use elsewhere.

## Known Risks and Mitigations:

Risk: AI-generated questions or answer keys may be incorrect or unsuitable for students.

Mitigation: Have a teacher solve and check each generated question, answer, and score before adding it to a formal exam.

Risk: Exam materials and student information may be sensitive.

Mitigation: Do not submit unreleased standardized-exam questions or student names; use pseudonyms or seat numbers and limit stored results to item-level aggregates.

Risk: Curriculum, privacy rules, and crisis-help contacts may not apply outside mainland China.

Mitigation: Localize these settings before deployment elsewhere, and confirm the user's location before giving crisis contacts.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-exam-designer)
- [Exam blueprint and specification templates](references/exam-blueprint.md)
- [Class teaching workspace schema](shared/class-teaching-workspace.schema.json)
- [AI-generated item review checklist](shared/ai-item-check.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese-language exam blueprints, question drafts, scoring rubrics, and revision lists in structured text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May prepare exam-blueprint records in the class workspace; AI-generated questions require teacher verification before use.]

## Skill Version(s):

2.6.0 (source: server release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
