## Description:

为中小学教师提供课堂追问、小组互动、冷场应对和课后观察记录建议。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

面向小学中高段、初中和高中教师，用于围绕课程目标组织课堂参与、调整追问与小组活动，并整理待教师确认的课堂观察记录。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated classroom prompts may need adaptation to the lesson and students.

Mitigation: The teacher reviews questions and interaction suggestions before using them with students.

Risk: Classroom observations could expose student identities or sensitive disclosures.

Mitigation: Use aliases, keep personal or sensitive disclosures out of observations, and approve records before saving; use “这次不要记忆” to pause record access, storage, and handoffs.

Risk: A student may disclose a safety or crisis concern during classroom support.

Mitigation: Stop the classroom workflow, follow the crisis response guidance, connect the student with a trusted adult and appropriate local help, and record only the referral action.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-classroom-coach)
- [Questioning strategies and interaction prompts](artifact/references/questioning-strategies.md)
- [Group task card and scripts](artifact/references/group-task-card-and-scripts.md)
- [Post-class observation record template](artifact/references/post-class-record-template.md)
- [Crisis response exception](artifact/shared/crisis-exception.md)
- [Class teaching workspace schema](artifact/shared/class-teaching-workspace.schema.json)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown]

**Output Format:** [Chinese text and Markdown interaction plans, prompts, and observation-record drafts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Teacher reviews generated suggestions and approves classroom records before saving; the skill does not identify students in interaction logs.]

## Skill Version(s):

2.12.6 (source: release evidence, frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
