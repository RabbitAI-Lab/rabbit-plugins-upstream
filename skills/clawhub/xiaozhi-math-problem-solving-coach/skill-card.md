## Description:

A Chinese-language math coach that guides middle- and high-school students through individual problems with questions, graduated hints, and similar practice problems.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students in Chinese Mainland middle- and high-school math curricula use the skill to work through a problem, identify where they are stuck, and check understanding with a similar problem. It also supports review when the student explicitly says an exam is imminent.

### Deployment Geography for Use:

Mainland China curriculum and Simplified Chinese contexts

## Known Risks and Mitigations:

Risk: Student profile details or wrong answers may be shared without the student's or guardian's understanding.

Mitigation: Confirm relevant sharing permissions with the student or guardian before profile reads or wrong-answer handoffs; otherwise keep the session self-contained.

Risk: Unwanted reminders or curriculum-inappropriate tutoring may affect students.

Mitigation: Enable reminders only with explicit permission and deploy where Mainland China K12 curriculum assumptions and Simplified Chinese tutoring fit.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/qizhitang/skills/xiaozhi-math-problem-solving-coach)
- [Four-step problem-solving workflow](references/photo-4step-statemachine.md)
- [Math questioning guide](references/math-socrates-guide.md)
- [High-school worked examples](references/math-hs1-worked-examples.md)
- [Advanced high-school worked examples](references/math-hs3-worked-examples.md)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown]

**Output Format:** [Chinese-language conversational text with math notation and practice questions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Hints escalate gradually; optional profile use, wrong-answer handoffs, and reminders require current-session consent.]

## Skill Version(s):

2.11.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
