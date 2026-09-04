## Description:

学习系统协调器 routes Chinese-language learning requests to the appropriate study skill, prevents duplicate handoffs, and creates consent-gated system health checks or monthly learning summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students, families, and learning agents use this skill to coordinate a multi-skill study workflow across wrong-answer review, Feynman checks, Cornell notes, planning, focus support, reminders, and monthly summaries. It is designed to route, deduplicate, summarize, and validate handoffs rather than teach, grade, or independently analyze subject content.

### Deployment Geography for Use:

Global, with mainland China crisis and emergency resources configured by default; localize those resources before use elsewhere.

## Known Risks and Mitigations:

Risk: Cross-skill sharing, long-term profile storage, reminder consent, teacher writeback, and parent or emotion sharing can expose sensitive learning information if enabled too broadly.

Mitigation: Configure each consent setting before use and keep handoffs to the minimum authorized summary fields needed for the current task.

Risk: The skill includes mainland China crisis and emergency referral resources that may be inappropriate for users in other regions.

Mitigation: Replace crisis and emergency resources with local, reviewed resources before deploying outside mainland China.

Risk: A coordinator can be mistaken for a subject tutor or autonomous reminder sender.

Mitigation: Use it only for routing, deduplication, consent-gated summaries, and reminder queue handoffs; delegate teaching, error analysis, question generation, and reminder delivery to the appropriate skills.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-skill-coordinator)
- [One-week linkage record](references/one-week-linkage-record.md)
- [Handover protocol schema](schemas/handover-protocol.schema.json)
- [Platform conventions](shared/platform-conventions.md)
- [Crisis exception protocol](shared/crisis-exception.md)
- [Vocabulary and consent conventions](shared/vocab.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Chinese-language Markdown or plain text, with JSON handoff examples and schema-backed configuration references when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are consent-gated and limited to routing decisions, deduplication notes, summaries, health checks, reminder queue handoffs, and validated handover payload guidance.]

## Skill Version(s):

2.1.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
