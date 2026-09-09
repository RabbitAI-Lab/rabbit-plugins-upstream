## Description:

数学概念解释器帮助初中学生用生活类比、图解可视化和逐步拆分来理解数学概念，而不是只记公式。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External Chinese K12 learners use this skill when they understand a formula or rule only by memorization and need a concept rebuilt through familiar examples, visual reasoning, and short guided checks. It is scoped to middle-school math concept explanation rather than full problem solving, word-problem modeling, error tracking, or graded practice programs.

### Deployment Geography for Use:

China Mainland by default; localize emergency contacts, curriculum scope, and minor-data consent requirements before student-facing use in other regions.

## Known Risks and Mitigations:

Risk: Student tutoring conversations can reveal self-harm, bullying, severe distress, or family safety signals outside the skill's learning scope.

Mitigation: Follow the bundled crisis exception: stop tutoring flow, state the AI boundary, direct the student to trusted adults and localized emergency resources, and avoid storing sensitive event details.

Risk: The skill can rely on student learning profiles and cross-skill sharing, which may involve minor education data.

Mitigation: Confirm platform consent, guardian requirements, sharing controls, and delete/export/pause controls before enabling persistent profiles or cross-skill sharing.

Risk: Generated practice or transfer-check items can be wrong, ambiguous, or outside the intended grade band.

Mitigation: Apply the bundled AI item self-check before output: self-solve, ensure the item has a valid answer, keep values friendly, and stay within the middle-school scope.

Risk: China-mainland emergency contacts, curriculum assumptions, and minor-data defaults may not fit other regions.

Mitigation: Localize emergency contacts, curriculum terminology, and consent rules before deploying outside the default China-mainland Chinese K12 setting.

## Reference(s):

- [ClawHub skill release page](https://clawhub.ai/qizhitang/skills/xiaozhi-math-concept-explainer)
- [Publisher profile](https://clawhub.ai/user/qizhitang)
- [Initial middle-school math analogy bank](artifact/references/analogy-bank.md)
- [AI-generated item self-check protocol](artifact/shared/ai-item-check.md)
- [Platform conventions and localization requirements](artifact/shared/platform-conventions.md)
- [Crisis exception and referral protocol](artifact/shared/crisis-exception.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Concise Chinese tutoring dialogue in text or Markdown, with simple math notation, follow-up questions, examples, and understanding checks.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill caps ordinary replies at about 120 Chinese characters, limits follow-up turns, and requires a student restatement or new example before ending a concept explanation.]

## Skill Version(s):

2.1.12 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
