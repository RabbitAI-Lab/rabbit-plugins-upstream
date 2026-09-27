## Description:

为中文 K–12 学习请求选择合适的学习技能、避免重复交接，并在用户同意后汇总全景月报。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students and their supporting adults use this skill to route learning questions across a Chinese K–12 skill suite, check how its learning workflow is working, and request a consent-based monthly overview.

### Deployment Geography for Use:

Mainland China by default; localize curricula, consent practices and crisis resources before use elsewhere.

## Known Risks and Mitigations:

Risk: Cross-skill sharing or parent-visible summaries may expose a minor's learning or emotional information without permission.

Mitigation: Require explicit consent for sharing, reminders, parent visibility and profile memory; use only the minimum authorized summary fields.

Risk: Loose handover permissions could let the coordinator create profile or teacher writebacks outside its routing role.

Mitigation: Enforce allowed sender and recipient pairs at runtime and block coordinator-originated profile or teacher writebacks.

Risk: A crisis signal or region-specific emergency advice could be mishandled during routine learning coordination.

Mitigation: Stop routine routing for crisis signals, refer to a trusted adult and local services, and localize emergency guidance before deployment outside mainland China.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-skill-coordinator)
- [One-week coordination example](references/one-week-linkage-record.md)
- [Handover protocol schema](schemas/handover-protocol.schema.json)
- [Platform capabilities and fallback behavior](shared/platform-conventions.md)
- [Crisis referral protocol](shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese-language routing advice, workflow checks and monthly summaries in text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Monthly summaries require a request or consent and cover only authorized data; without cross-session records, summaries are limited to information supplied in the current session.]

## Skill Version(s):

2.7.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
