## Description:

学习系统协调器负责判断一次学习问题该由哪个 SKILL 接手，并在用户请求时汇总全景月报。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students use this skill to route a learning question to the appropriate specialist skill, prevent duplicate work, or request a five-area monthly learning summary. It uses only task-relevant information after the required consent, and elementary students should use it with a parent or teacher present.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release evidence notes inconsistent wording about which linked skill saves authorized profile updates; storage and consent enforcement depend on the platform and linked skills.

Mitigation: Enable only the profile, sharing, parent-access, and reminder options you want, and confirm the intended recipient skill and its storage and consent behavior before authorizing profile updates.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-skill-coordinator)
- [One-week linkage record](references/one-week-linkage-record.md)
- [Handover protocol schema](schemas/handover-protocol.schema.json)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown, JSON]

**Output Format:** [Conversational guidance, Markdown monthly summaries, and structured JSON handoff records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Routes requests and prepares user-requested, consent-scoped summaries; it does not teach lessons, analyze errors itself, create questions, or send reminders.]

## Skill Version(s):

2.12.5 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
