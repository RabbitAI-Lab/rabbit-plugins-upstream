## Description:

Routes study requests to the appropriate learning skill, prevents duplicate handoffs, and summarizes learning progress across the system when requested and authorized.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students, families, and educators use this skill to route study questions to the right learning skill, coordinate consented handoffs, and request cross-skill learning reports. Elementary-age students should use it with a parent or teacher present.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Student profile information may be shared across companion skills or included in reports.

Mitigation: Use only task-relevant fields after consent; review sharing, parent-sharing, and reminder preferences, along with companion skills’ data retention and deletion controls.

Risk: The skill documentation is inconsistent about which skill should save profile updates, creating a risk of misdirected writebacks.

Mitigation: Keep profile writes with the designated companion skills and clarify the coordinator’s conditional writeback wording before enabling updates.

## Reference(s):

- [One-week linkage record](references/one-week-linkage-record.md)
- [Handover protocol schema](schemas/handover-protocol.schema.json)
- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-skill-coordinator)
- [Publisher profile](https://clawhub.ai/user/qizhitang)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, Markdown, JSON]

**Output Format:** [Conversational guidance and summaries, Markdown monthly reports, and structured JSON handoff payloads.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses consented, task-relevant summaries; does not autonomously collect cross-skill data or trigger monthly reports.]

## Skill Version(s):

2.12.0 (source: artifact/SKILL.md frontmatter, ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
