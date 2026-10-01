## Description:

A read-only daily dashboard for independent teachers that organizes lessons, homework, parent follow-ups, lesson packages, and evidence-based student alerts into seven actionable sections.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Independent teachers use this skill to review their authorized student workspace records, prioritize today's teaching and follow-up tasks, and spot risks based on recorded facts. The dashboard does not change records or send messages to families.

### Deployment Geography for Use:

Mainland China; localize language, curriculum, emergency resources, and minor-data consent rules before use elsewhere.

## Known Risks and Mitigations:

Risk: A dashboard could expose minors' records to an unauthorized viewer or disclose sensitive details.

Mitigation: Use only with a teacher authorized to view the records; use student aliases, limit shared fields, and check consent before preparing shareable content.

Risk: Chinese K12 assumptions and crisis resources could be inappropriate outside mainland China.

Mitigation: Localize language, curriculum, emergency contacts, and minor-data consent requirements before use in another region.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-solo-dashboard)
- [Daily dashboard template](references/dashboard-template.md)
- [Seven-section dashboard templates](references/daily-dashboard-block-templates.md)
- [Complete daily dashboard example](references/daily-dashboard-full-sample.md)
- [Teacher workspace schema](shared/solo-teacher-workspace.schema.json)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown daily dashboard with seven sections, student alerts, and prioritized actions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only; uses student aliases and cites recorded reasons for alerts.]

## Skill Version(s):

2.9.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
