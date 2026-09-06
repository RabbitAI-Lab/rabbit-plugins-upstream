## Description:

Creates personalized weekly or 30-day study plans from a student's stated goals and, when explicitly authorized, learning profile summaries, then helps track execution gaps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students and learning-support agents use this skill to turn exam goals, weak-area summaries, available time, and grade band constraints into concrete study plans. It can also produce student-facing progress checks, parent-visible task dashboards, and reminder queue entries when the relevant consent gates are satisfied.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The shared handoff schema is too loose for student profile data.

Mitigation: Enforce consent checks in application code, restrict profile writebacks to documented plan fields, and validate recipient and handoff type routing independently of the bundled schema.

Risk: Parent-visible dashboards and reminder queue entries can expose or act on student learning data if consent routing is not enforced by the host platform.

Mitigation: Require independent checks for parentSharingConsent, crossSkillSharing, and reminderConsent before generating parent-facing content, profile writebacks, or reminder handoffs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-learning-plan)
- [Publisher profile](https://clawhub.ai/user/qizhitang)
- [Plan templates](artifact/references/plan-templates.md)
- [Grade band parameters](artifact/shared/grade-bands.md)
- [Consent and vocabulary reference](artifact/shared/vocab.md)
- [Crisis exception protocol](artifact/shared/crisis-exception.md)
- [Handover protocol schema](artifact/shared/handover-protocol.schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Configuration, Guidance]

**Output Format:** [Markdown or plain text study plans and dashboards, with optional JSON handoff records for consented reminders or profile writebacks.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are gated by profile, parent-sharing, cross-skill-sharing, and reminder consent states; crisis handling takes priority over planning and dashboard generation.]

## Skill Version(s):

2.1.10 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
