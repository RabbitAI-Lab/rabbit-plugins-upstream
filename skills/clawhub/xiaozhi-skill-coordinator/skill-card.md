## Description:

学习系统协调器 routes learning requests to the appropriate Xiaozhi skill and, with user consent, summarizes authorized learning data into whole-system monthly reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External learners and education agents use this skill to route a study request to the right learning skill, avoid duplicate cross-skill actions, and generate consent-scoped monthly or system-health summaries when requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The handover schema may be mistaken for a complete authorization boundary.

Mitigation: Enforce current consent, authenticated sender identity, sender-recipient topology, and teacher writeback authorization outside the schema before production use.

Risk: Monthly reports and cross-skill summaries may expose more learning data than the current task requires.

Mitigation: Limit summaries to user-requested or user-approved flows and retrieve only the minimum authorized fields needed for the current task.

Risk: Crisis signals could be mishandled if normal routing or parent-facing summaries continue.

Mitigation: Stop normal routing and summary generation when crisis signals appear, follow the crisis exception protocol, and record only the referral fact.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-skill-coordinator)
- [Complete one-week linkage record example](references/one-week-linkage-record.md)
- [Handover protocol schema](schemas/handover-protocol.schema.json)
- [Vocabulary, consent, and reminder conventions](shared/vocab.md)
- [Crisis exception protocol](shared/crisis-exception.md)
- [Platform capability and degradation conventions](shared/platform-conventions.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, JSON, Configuration]

**Output Format:** [Markdown guidance with structured JSON handover examples and schema references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Routes and summarizes only after task need and user consent; reminder output is limited to queue handoff rather than direct reminder delivery.]

## Skill Version(s):

2.1.6 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
