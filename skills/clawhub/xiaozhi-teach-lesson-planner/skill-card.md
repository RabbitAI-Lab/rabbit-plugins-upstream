## Description:

Helps teachers design UbD-aligned lesson plans with observable learning goals, assessment evidence, timed activities, question prompts, and optional differentiated tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers use this skill to draft Chinese K–12 lessons, revision sessions, and assessment reviews with measurable objectives and differentiated activities when class data is available. Teachers review the plans before classroom use.

### Deployment Geography for Use:

Chinese mainland by default; localize crisis referral guidance before use elsewhere.

## Known Risks and Mitigations:

Risk: Lesson planning may use sensitive class records, including student tiers and learning weaknesses.

Mitigation: Enforce the documented read boundary for class context, write only lesson plans, and respect consent, sharing, memory, and deletion controls; omit identifying student details.

Risk: AI-generated exercises and lesson suggestions can be inaccurate or unsuitable for a class.

Mitigation: Have the teacher review objectives, timing, and questions; check generated exercises and mark them for human verification before reuse.

Risk: Default crisis referral contacts are specific to the Chinese mainland.

Mitigation: Confirm the user's region and provide locally appropriate emergency or support contacts outside the Chinese mainland.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-lesson-planner)
- [Lesson plan template](artifact/references/lesson-plan-template.md)
- [Differentiated lesson example](artifact/references/layered-lesson-example.md)
- [Class teaching workspace schema](artifact/shared/class-teaching-workspace.schema.json)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown lesson plans and question-chain drafts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Differentiation requires available class tiers; teacher review is required before classroom use.]

## Skill Version(s):

2.4.0 (source: server release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
