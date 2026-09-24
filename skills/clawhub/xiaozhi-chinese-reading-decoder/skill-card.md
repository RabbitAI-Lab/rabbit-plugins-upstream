## Description:

A Chinese K12 reading-comprehension coaching skill that helps students first understand modern Chinese texts and then express answers in grading-oriented form across narrative, prose, argumentative, expository, and non-continuous texts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT

## Use Case:

Students, parents, teachers, and tutoring agents use this skill to coach modern Chinese reading-comprehension practice, diagnose recurring answer-pattern issues, guide text-grounded revision, and support consent-controlled learner-profile handoff.

### Deployment Geography for Use:

China mainland by default; other regions require localization of crisis resources, curriculum assumptions, and minor-data consent practices before deployment.

## Known Risks and Mitigations:

Risk: The skill may process minor learner data through profile memory, cross-skill sharing, reminders, or parent/guardian visibility.

Mitigation: Confirm deployment policy and user consent settings before enabling profile memory, sharing, reminders, or guardian-facing summaries.

Risk: Crisis-response channels and curriculum assumptions are designed for China mainland Chinese K12 contexts.

Mitigation: Localize emergency resources, curriculum alignment, and minor-data consent requirements before using the skill in other regions.

Risk: Generated practice questions or answer guidance can be misleading if used without review.

Mitigation: Apply the bundled AI item self-check and human review before adding generated questions to resource banks or assessments.

Risk: The skill could be misused during an active exam or timed assessment.

Mitigation: Follow the documented exam-in-progress rule: do not provide hints or answers until the assessment is complete.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-chinese-reading-decoder)
- [语文错因维度表](references/chinese-error-dimension-table.md)
- [阅读五坑专项训练策略](references/pit-training.md)
- [现代文各题型出题逻辑与答题模板详解](references/question-type-library.md)
- [危机例外](shared/crisis-exception.md)
- [平台能力约定与降级路径](shared/platform-conventions.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Chinese tutoring dialogue, structured Markdown feedback, and JSON-compatible profile handoff examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses short stepwise responses, avoids giving original-question answers before student attempts, and gates profile writes or cross-skill sharing on consent controls.]

## Skill Version(s):

2.3.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
