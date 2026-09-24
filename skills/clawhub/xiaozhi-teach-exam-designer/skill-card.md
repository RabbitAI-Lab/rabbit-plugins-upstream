## Description:

帮助中国 K12 教师按双向细目表设计测验、试卷、评分细则和错题讲评清单，并控制难度、认知层级和题目返修流程。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

K12 teachers in Chinese classroom contexts use this skill to plan formative, diagnostic, and summative assessments from curriculum goals through blueprint, item selection or adaptation, rubrics, and post-exam item repair guidance.

### Deployment Geography for Use:

Mainland China by default; other regions require localized curriculum, legal, privacy, and crisis-referral guidance.

## Known Risks and Mitigations:

Risk: AI-generated or adapted questions may be incorrect, ambiguous, over-scoped, or misaligned with the assessment blueprint.

Mitigation: Require teachers to verify every AI-generated item, answer, score value, and rubric before the item enters a formal test.

Risk: Confidential unreleased exam materials or personal student data could be entered into the skill.

Mitigation: Avoid entering confidential exam papers, answer keys, scoring standards, or personal student data; use anonymized class-level information where possible.

Risk: The default safety, curriculum, legal, and crisis-referral guidance is written for mainland China and may not fit other regions.

Mitigation: Localize curriculum standards, privacy rules, legal constraints, and crisis-referral channels before using the skill outside mainland China.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-exam-designer)
- [Publisher profile](https://clawhub.ai/user/qizhitang)
- [Exam blueprint reference](artifact/references/exam-blueprint.md)
- [Class teaching workspace schema](artifact/shared/class-teaching-workspace.schema.json)
- [AI item self-check protocol](artifact/shared/ai-item-check.md)
- [Crisis referral protocol](artifact/shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Markdown and structured text tables with JSON-compatible classWorkspace fields when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Teacher review is required before AI-generated items are used in formal assessments.]

## Skill Version(s):

2.3.0 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
