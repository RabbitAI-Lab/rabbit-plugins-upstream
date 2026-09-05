## Description:

This skill helps teachers turn direct instruction into classroom interaction by planning wait-time prompts, group activities, cold-start recovery moves, feedback moments, and short post-class observation records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT

## Use Case:

Teachers use this skill to adapt an existing lesson goal, student tier summary, and class profile into classroom interaction guidance. It produces practical prompts, grouping and timing recommendations, cold-start recovery options, and post-class observation drafts for teacher review.

### Deployment Geography for Use:

Mainland China by default; localize crisis contacts, curriculum assumptions, and minor-data rules before use elsewhere.

## Known Risks and Mitigations:

Risk: The skill can use student tiers and class weakness summaries in a teacher-facing classroom workflow.

Mitigation: Confirm school consent and sharing controls before use, keep individual names out of records, and require teacher confirmation before saving classroom observations.

Risk: The packaged safety contacts, curriculum assumptions, and minor-data defaults are designed for mainland China.

Mitigation: Localize crisis contacts, curriculum alignment, and minor-data consent rules before deploying the skill outside mainland China.

Risk: Improvised classroom examples or questions may be inaccurate if used without review.

Mitigation: Apply the included AI item self-check, use examples orally unless reviewed, and label any AI-generated item that is stored for later use as requiring human verification.

Risk: A classroom conversation may expose self-harm, bullying, severe despair, or family safety signals that exceed learning support.

Mitigation: Stop the classroom-coaching flow, avoid diagnosis and detailed probing, direct the student to trusted adults and localized emergency channels, and record only the referral fact.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-classroom-coach)
- [Classroom Questioning Strategies and Interaction Scripts](artifact/references/questioning-strategies.md)
- [Group Task Card and Scripts Template](artifact/references/group-task-card-and-scripts.md)
- [Post-Class Five-Minute Observation Record Template](artifact/references/post-class-record-template.md)
- [Class Teaching Workspace Schema](artifact/shared/class-teaching-workspace.schema.json)
- [Platform Conventions and Degradation Paths](artifact/shared/platform-conventions.md)
- [Crisis Exception](artifact/shared/crisis-exception.md)
- [Crisis Referral Protocol](artifact/shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Markdown with structured classroom templates and short record drafts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Teacher confirmation is required before classroom records are saved; classroom records should avoid individual student names.]

## Skill Version(s):

2.1.6 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
