## Description:

A Chinese modern-text reading comprehension tutoring skill that helps learners understand passages first, then express answers in exam-aligned structures.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External students, tutors, and education agents use this skill to coach Chinese modern prose reading comprehension for upper-primary and middle-school contexts. It supports passage analysis, question-type diagnosis, answer-structure feedback, and opt-in learning-profile handoff.

### Deployment Geography for Use:

China and Chinese-language education contexts; localize education and crisis-support assumptions before use in another region.

## Known Risks and Mitigations:

Risk: The skill can use long-term learning-profile data for minors when profile features are enabled.

Mitigation: Keep profile memory, parent sharing, and cross-skill sharing disabled by default; enable them only with appropriate student or guardian consent and honor view, correct, delete, pause, sharing, and export controls.

Risk: Education conventions and crisis-support references are China-specific.

Mitigation: Review and localize curricula, scoring assumptions, escalation language, and referral resources before deployment outside the intended region.

Risk: Premature answers can weaken tutoring value or mislead a learner before they attempt the original question.

Mitigation: Use the hint ladder and same-type examples first; avoid giving the original answer before the learner has tried and the answer can be grounded in the passage.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-chinese-reading-decoder)
- [Publisher profile](https://clawhub.ai/user/qizhitang)
- [语文错因维度表](references/chinese-error-dimension-table.md)
- [阅读五坑专项训练策略](references/pit-training.md)
- [现代文各题型出题逻辑与答题模板详解](references/question-type-library.md)
- [平台能力约定与降级路径](shared/platform-conventions.md)
- [提示阶梯与完整示例出口](shared/hint-ladder.md)
- [Learning DNA profile schema](shared/dna-profile.schema.json)
- [Handover protocol schema](shared/handover-protocol.schema.json)
- [危机识别与转介协议](shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis, Guidance, Configuration]

**Output Format:** [Chinese tutoring dialogue in Markdown, with optional JSON-compatible profile or handoff snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Concise student-facing responses; profile memory and cross-skill sharing are opt-in.]

## Skill Version(s):

2.1.12 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
