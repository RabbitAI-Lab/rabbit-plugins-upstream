## Description:

课堂互动教练 helps teachers turn one-way instruction into classroom interaction by suggesting follow-up questions, participation paths, small-group activity timing, cold-call alternatives, and post-class observation notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External teachers use this skill to plan and run classroom interactions, including differentiated questioning, wait-time prompts, group-work roles and timing, and teacher-confirmed classroom observation records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses class workspace context, including student tiers and weakness rankings that may be sensitive educational records.

Mitigation: Install and use it only where teachers are authorized to process class workspace data, and avoid displaying tier labels or individual performance notes to students or parents unless consent rules allow it.

Risk: Saved classroom logs could contain inaccurate or over-specific observations if recorded without teacher review.

Mitigation: Keep the teacher-confirmation step for any saved classroom log and limit records to teacher-confirmed aggregate classroom notes.

Risk: Classroom interaction suggestions may be mistaken for direct student assignment or automated decision-making.

Mitigation: Treat suggestions as teacher-facing guidance; the teacher decides whom to call on, when to intervene, and what to save.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-classroom-coach)
- [Publisher profile](https://clawhub.ai/user/qizhitang)
- [课堂提问策略与互动话术库](references/questioning-strategies.md)
- [小组合作任务卡模板与话术模板](references/group-task-card-and-scripts.md)
- [课后 5 分钟观察记录模板](references/post-class-record-template.md)
- [Class teaching workspace schema](shared/class-teaching-workspace.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown guidance with structured classroom interaction plans, scripts, checklists, and observation-note templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces teacher-facing suggestions and records only teacher-confirmed aggregate classroom notes.]

## Skill Version(s):

2.1.10 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
