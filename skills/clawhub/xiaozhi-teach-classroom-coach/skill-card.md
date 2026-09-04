## Description:

课堂互动教练 helps teachers turn lecture-heavy lessons into interactive classes by planning wait-time prompts, group activities, cold-classroom recovery moves, feedback routines, and post-class observation records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers use this skill to design classroom interaction flows, scaffold questions for different student tiers, recover from silence during class, structure group work, and record aggregate post-class observations. It is intended for Chinese-medium classroom coaching and does not replace teacher judgment about which students should speak or how classroom records are shared.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Classroom records may expose personal student information or overstate low-confidence classroom impressions.

Mitigation: Use aliases or seat numbers rather than real student names, keep interaction logs aggregate, and review sharing controls before records are used by other skills or shown to parents.

Risk: Classroom interaction suggestions may be unsuitable for a specific class context if applied without teacher review.

Mitigation: Treat outputs as teacher-facing proposals; the teacher decides who speaks, adapts prompts to the class, and checks any AI-generated examples before use.

Risk: Student crisis or safety signals are outside the normal classroom coaching workflow.

Mitigation: Stop the coaching workflow, follow the crisis referral protocol, direct the student to trusted adults and emergency channels when needed, and record only the referral fact.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-classroom-coach)
- [Group task card and scripts](references/group-task-card-and-scripts.md)
- [Post-class record template](references/post-class-record-template.md)
- [Questioning strategies](references/questioning-strategies.md)
- [Class teaching workspace schema](shared/class-teaching-workspace.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown with structured classroom templates and teacher-facing guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Chinese-language classroom interaction output; may reference classWorkspace fields and aggregate classroom records.]

## Skill Version(s):

2.1.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
