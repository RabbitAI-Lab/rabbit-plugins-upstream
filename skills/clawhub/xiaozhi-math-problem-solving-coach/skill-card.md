## Description:

A Chinese-language math coach that guides middle- and high-school students through problems with graduated hints, practice questions, and pre-exam review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students in middle and high school use this skill to work through individual math problems, identify mistakes, practice similar questions, and review before exams. Educators can use its guided-question approach to support learning without immediately giving answers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Student profiles, wrong-answer records, cross-skill sharing, or reminders could expose or retain minors' learning data.

Mitigation: Keep use session-only by default; require explicit consent in the current turn for reading, saving, sharing, or reminders, and enforce local guardian-consent requirements.

Risk: Generated math practice or explanations may contain mistakes.

Mitigation: Check generated questions for solvability and correctness before presenting them, and have an educator review consequential guidance.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-math-problem-solving-coach)
- [Hint ladder](shared/hint-ladder.md)
- [Practice-question quality checks](shared/ai-item-check.md)
- [Math coaching guide](references/math-socrates-guide.md)
- [Platform and consent conventions](shared/platform-conventions.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese-language conversational text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Graduated hints, worked explanations when needed, similar practice questions, and optional consent-gated handoffs.]

## Skill Version(s):

2.7.0 (source: ClawHub release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
