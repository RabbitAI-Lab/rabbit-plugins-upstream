## Description:

Helps teachers design time-bounded, differentiated K–12 assignments with scoring rubrics, feedback templates, and aggregate completion summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers in Mainland China use this skill to draft differentiated homework, grading criteria, and student or parent feedback for their own review. It can record anonymized class-level completion summaries, but does not grade submissions or create exam papers.

### Deployment Geography for Use:

Mainland China; localize curriculum, privacy rules, and crisis contacts before use elsewhere.

## Known Risks and Mitigations:

Risk: AI-generated questions or scoring guidance may be inaccurate.

Mitigation: Teachers verify generated questions and rubrics before formal use; do not use this skill to grade submissions automatically.

Risk: Student information or sensitive feedback could be exposed in shared summaries.

Mitigation: Use student aliases, honor parental sharing consent, and write back only aggregate completion and error data.

Risk: Curriculum, privacy expectations, and crisis contacts may not apply outside Mainland China.

Mitigation: Localize these requirements before deployment elsewhere and route crisis signals to appropriate local support.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-assignment-designer)
- [Assignment scoring rubric](references/assignment-rubric.md)
- [AI-generated question checks](shared/ai-item-check.md)
- [Crisis referral protocol](shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Markdown task cards and feedback; structured aggregate completion summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Task cards include estimated time per question; teacher review is required before classroom use.]

## Skill Version(s):

2.11.2 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
