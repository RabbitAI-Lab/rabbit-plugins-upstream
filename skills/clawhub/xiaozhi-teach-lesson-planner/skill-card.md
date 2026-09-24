## Description:

教案设计器 helps Chinese K-12 teachers draft UbD-based lesson plans with observable objectives, assessment evidence, timed lesson segments, question-chain drafts, and A/B/C differentiation when class-tier data is available.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External K-12 teachers use this skill to turn a lesson topic, exam-review need, or existing lesson draft into a structured teaching plan. It is designed for Chinese curriculum contexts and supports observable learning goals, assessment evidence, classroom timing, question-chain drafts, and differentiated A/B/C lesson variants.

### Deployment Geography for Use:

China mainland Chinese K-12 contexts; localize curriculum terms, safety referral guidance, and consent rules before use elsewhere.

## Known Risks and Mitigations:

Risk: The skill can rely on class summaries, student tiers, weakness rankings, review-plan context, and exam-blueprint context.

Mitigation: Use it only where those student-data inputs are authorized and appropriate for teacher lesson planning; respect the artifact's privacy controls for viewing, correcting, deleting, pausing, sharing, and exporting lesson records.

Risk: The artifact is designed for China mainland Chinese K-12 curriculum, safety-referral, and consent assumptions.

Mitigation: Before use outside that context, localize curriculum terminology, emergency and crisis-referral guidance, and minor-data consent rules.

Risk: AI-generated examples, variants, and classroom exercises may contain mistakes.

Mitigation: Keep the required teacher-facing label for AI-generated items and have a human verify generated questions before adding them to a resource bank, test, or classroom plan.

Risk: Lesson plans, goals, questions, and differentiated tasks could be treated as final instructional judgments.

Mitigation: Use the output as teacher-reviewed drafts; the artifact states that the teacher confirms or adjusts goals, questions, tasks, and any student- or parent-facing content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-lesson-planner)
- [Publisher profile](https://clawhub.ai/user/qizhitang)
- [Lesson plan template](references/lesson-plan-template.md)
- [Layered lesson example](references/layered-lesson-example.md)
- [Class teaching workspace schema](shared/class-teaching-workspace.schema.json)
- [AI item check protocol](shared/ai-item-check.md)
- [Crisis referral protocol](shared/crisis-referral-protocol.md)
- [Platform conventions](shared/platform-conventions.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Configuration]

**Output Format:** [Markdown lesson-plan drafts, checklists, question chains, and differentiated task cards]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read class summaries, weakness rankings, period length, and student-tier data when available; degrades to a basic lesson plan when student tiers are unavailable.]

## Skill Version(s):

2.3.0 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
