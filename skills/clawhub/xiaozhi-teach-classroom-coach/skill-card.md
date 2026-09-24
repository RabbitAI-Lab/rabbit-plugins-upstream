## Description:

Helps Chinese-language K12 teachers turn lecture plans into classroom interaction plans with staged questions, wait-time prompts, group activity timing, cold-call recovery paths, and post-class observation notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

K12 teachers use this skill to adapt lesson-plan context, student tiers, and class profile information into practical classroom facilitation moves. It is intended for teacher-reviewed interaction guidance, not for replacing the teacher, naming students to answer, writing full lesson plans, generating assessments, or calculating learning analytics.

### Deployment Geography for Use:

China mainland by default; localize curriculum assumptions, minor-data requirements, and crisis-support channels before use in other regions.

## Known Risks and Mitigations:

Risk: The skill uses lesson-plan context and pseudonymous student tier or weakness signals, which can affect how students are grouped or supported.

Mitigation: Keep data minimal and pseudonymous, preserve teacher confirmation for any classroom-record writeback, and avoid using the skill to make final judgments about individual students.

Risk: The skill's curriculum assumptions and crisis-support contacts are designed for China-mainland Chinese K12 classrooms.

Mitigation: Localize curriculum terminology, minor-data requirements, and crisis escalation contacts before deploying it in another region or language.

Risk: Classroom facilitation suggestions can be inappropriate if used without teacher judgment in a live classroom.

Mitigation: Use outputs as drafts for the teacher, with the teacher deciding who speaks, how feedback is delivered, and whether any observation note should be retained.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-classroom-coach)
- [Classroom questioning strategies and scripts](artifact/references/questioning-strategies.md)
- [Group task card and scripts](artifact/references/group-task-card-and-scripts.md)
- [Post-class observation record template](artifact/references/post-class-record-template.md)
- [Class teaching workspace schema](artifact/shared/class-teaching-workspace.schema.json)
- [Crisis referral protocol](artifact/shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Configuration]

**Output Format:** [Chinese-language Markdown or text templates for classroom facilitation, group activity scripts, wait-time prompts, and post-class observation records.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires teacher review and confirmation before classroom use or record writeback; no executable code is produced.]

## Skill Version(s):

2.3.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
