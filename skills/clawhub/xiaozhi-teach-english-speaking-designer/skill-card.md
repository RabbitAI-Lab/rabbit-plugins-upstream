## Description:

Designs task-based English-speaking classroom activities with scenarios, scaffolding, feedback, rubrics, and optional classroom workspace writebacks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers use this skill to turn English-speaking lessons from recitation into task-based classroom activities with goals, input preparation, speaking tasks, feedback, and rubric-based assessment support. It is aimed at upper-primary and middle-school English-speaking instruction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Student assessment records and oral recordings may expose classroom or learner data.

Mitigation: Install only where teachers are allowed to handle student classroom data; keep recordings de-identified, consented, and retained only as needed.

Risk: Suggested student-profile writebacks could add inaccurate or overbroad learning records.

Mitigation: Limit workspace access to oral-activity fields where possible and require teacher review before confirming any student-profile writeback.

Risk: Pronunciation feedback can be overstated if based only on text or classroom observation.

Mitigation: Do not make phoneme-level pronunciation judgments; leave pronunciation scoring to the teacher or a platform with suitable speech-evaluation capability.

Risk: AI-generated task cards or assessment items may contain unsuitable scenarios, weak information gaps, or inappropriate language difficulty.

Mitigation: Apply the bundled AI item self-check and mark AI-generated items for teacher validation before they are added to classroom resources.

Risk: Student crisis signals can exceed the scope of learning support.

Mitigation: Stop the lesson-design workflow when crisis signals appear and follow the bundled crisis referral protocol, recording only the referral fact rather than sensitive details.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-english-speaking-designer)
- [Task-based speaking activity template](references/task-based-template.md)
- [English speaking assessment rubric](references/speaking-rubric.md)
- [Speaking profile template](references/speaking-profile-template.md)
- [Error correction strategies](references/error-correction-strategies.md)
- [Speaking feedback phrases](references/feedback-phrases.md)
- [Restaurant ordering task design sample](references/task-design-sample-restaurant.md)
- [Class teaching workspace schema](shared/class-teaching-workspace.schema.json)
- [AI item self-check protocol](shared/ai-item-check.md)
- [Platform conventions and fallback paths](shared/platform-conventions.md)
- [Crisis referral protocol](shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown guidance with lesson activity plans, rubrics, feedback phrases, task cards, and structured classroom workspace field suggestions.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose class workspace writebacks only with teacher review and consent; does not perform phoneme-level pronunciation scoring.]

## Skill Version(s):

2.1.6 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
