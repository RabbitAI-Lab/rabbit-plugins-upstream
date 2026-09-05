## Description:

Helps teachers turn lesson topics or draft plans into observable UbD lesson designs with learning evidence, competency-aligned goals, timed classroom phases, question-chain drafts, and A/B/C differentiation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External K12 teachers use this skill to design new, review, or layered lessons from a topic, existing draft, or classroom context. It is intended for teacher-facing planning outputs, including assessment evidence, classroom timing, question-chain drafts, and differentiated learning tasks.

### Deployment Geography for Use:

China mainland by default; localize curriculum assumptions, minor-data consent handling, and crisis referral channels before deployment elsewhere.

## Known Risks and Mitigations:

Risk: The skill may use classroom analytics, including pseudonymous student tiers, weakness summaries, exam-review inputs, review plans, and recent classroom interaction notes.

Mitigation: Install only where this classroom data use is acceptable, and keep parent sharing and student-profile writeback disabled unless consent has been checked.

Risk: AI-generated examples, variants, or classroom exercises could contain mistakes if accepted without review.

Mitigation: Apply the bundled AI item check protocol and keep the teacher-facing label that generated items need human verification before reuse or storage.

Risk: The artifact's default curriculum, school-stage assumptions, and crisis referral channels are designed for China mainland.

Mitigation: Localize curriculum assumptions, minor-data consent handling, and emergency or youth-support contact guidance before deployment in other regions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-lesson-planner)
- [Lesson plan template](artifact/references/lesson-plan-template.md)
- [Layered lesson example](artifact/references/layered-lesson-example.md)
- [Class teaching workspace schema](artifact/shared/class-teaching-workspace.schema.json)
- [AI item check protocol](artifact/shared/ai-item-check.md)
- [Platform conventions](artifact/shared/platform-conventions.md)
- [Crisis exception guidance](artifact/shared/crisis-exception.md)
- [Crisis referral protocol](artifact/shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Configuration]

**Output Format:** [Markdown lesson-plan drafts and structured text sections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include UbD learning results, assessment evidence, six-phase timing matrices, question-chain drafts, differentiated A/B/C tasks, and teacher review labels for AI-generated exercises.]

## Skill Version(s):

2.1.6 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
