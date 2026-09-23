## Description:

学习系统协调器判断学习请求应由哪个 Skill 接手，并在用户请求或同意后汇总授权摘要形成全景月报。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students, parents, teachers, and learning-support agents use this skill to route learning requests among related study skills, avoid duplicate handoffs, and generate consent-bounded system health checks or monthly learning summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Learning summaries may include student data that is routed among related skills.

Mitigation: Enable cross-skill sharing only after confirming consent settings and limit summaries to the fields needed for the current task.

Risk: Parent views, teacher writebacks, reminders, and long-term profiles can expose or retain sensitive learning information.

Mitigation: Confirm who may view, change, delete, pause, or export linkage records before enabling those features.

Risk: Reminder handoff and linkage-record wording has minor ambiguity in the security review.

Mitigation: Review reminder and linkage-record messages before deployment so users understand what is queued, stored, or merely suggested.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/qizhitang/skills/xiaozhi-skill-coordinator)
- [One-week linkage record example](references/one-week-linkage-record.md)
- [Handover protocol schema](schemas/handover-protocol.schema.json)
- [Platform conventions](shared/platform-conventions.md)
- [Crisis exception protocol](shared/crisis-exception.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, JSON, Configuration]

**Output Format:** [Markdown guidance with structured JSON handoff examples and text reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are consent-bounded routing decisions, summary reports, and handoff payload guidance; the skill does not directly teach, analyze root causes, issue reminders, or write records without authorization.]

## Skill Version(s):

2.2.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
