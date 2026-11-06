## Description:

Routes learning questions to the appropriate companion skill and, when requested and consented, summarizes authorized learning data in a monthly overview.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students use this skill to route a learning question to the right companion skill, avoid duplicate analysis, and request a monthly learning overview assembled from only the summaries they have authorized. Primary-school students use it with an adult present.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Parent-visible sharing and reminders may expose learning information beyond what the student intended to share.

Mitigation: Enable only the sharing and reminders needed, and review parent-visible permissions and consent before producing a summary.

Risk: Crisis guidance includes exceptions to ordinary sharing preferences, and handling depends partly on components outside this bundle.

Mitigation: Follow the disclosed crisis referral protocol, explain relevant sharing exceptions, and do not assume this skill controls storage or permission enforcement.

Risk: Primary-school use requires adult accompaniment.

Mitigation: Use with a parent or teacher present.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/qizhitang/skills/xiaozhi-skill-coordinator)
- [One-week linkage record example](artifact/references/one-week-linkage-record.md)
- [Handover protocol schema](artifact/schemas/handover-protocol.schema.json)
- [Crisis referral protocol](artifact/shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, JSON]

**Output Format:** [Chinese text or Markdown summaries, with structured JSON handover payloads when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Routes tasks and summarizes minimum-necessary, authorized data on request; it does not independently teach, analyze errors, or send reminders.]

## Skill Version(s):

2.12.6 (source: release evidence, frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
