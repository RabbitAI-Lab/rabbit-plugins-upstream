## Description:

把“单向讲授”变成有追问、有参与路径的课堂，帮助老师围绕目标与分层设计候场追问、小组活动、冷场应对和课后观察记录。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External K12 teachers use this skill to turn classroom plans and tier summaries into interactive questioning paths, group activity timing, cold-call alternatives, and brief post-class observation notes. It is designed for Chinese-language, mainland China classroom workflows and should be localized before use elsewhere.

### Deployment Geography for Use:

Global, with mainland China K12 defaults requiring localization before use in other regions

## Known Risks and Mitigations:

Risk: Mainland China curriculum, privacy, and emergency-contact assumptions may be inappropriate in other regions.

Mitigation: Localize language, curriculum assumptions, privacy/legal defaults, and emergency-contact guidance before deployment outside that context.

Risk: Classroom plans, tier summaries, and post-class observations can include sensitive student information.

Mitigation: Require teacher confirmation before record writes and avoid real student names in interaction logs.

Risk: The skill can produce teacher-facing classroom interaction drafts that may be incomplete or unsuitable for a specific class.

Mitigation: Keep outputs as drafts for teacher review and adapt them to the actual lesson objective, class profile, and student tiers.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-classroom-coach)
- [Publisher profile](https://clawhub.ai/user/qizhitang)
- [Group task card and scripts](artifact/references/group-task-card-and-scripts.md)
- [Post-class record template](artifact/references/post-class-record-template.md)
- [Questioning strategies](artifact/references/questioning-strategies.md)
- [Class teaching workspace schema](artifact/shared/class-teaching-workspace.schema.json)
- [Platform conventions](artifact/shared/platform-conventions.md)
- [Crisis referral protocol](artifact/shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Configuration]

**Output Format:** [Markdown with structured classroom templates and teacher-facing guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are drafts for teacher review and may reference classWorkspace lesson plans, student tiers, class profiles, and aggregate interaction logs.]

## Skill Version(s):

2.2.0 (source: artifact/SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
