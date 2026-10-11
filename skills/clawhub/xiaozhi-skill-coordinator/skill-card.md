## Description:

Coordinates Chinese K–12 study requests across learning skills and, with user consent, summarizes authorized study data in a panoramic monthly report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students and educators in Chinese K–12 settings use this skill to route study questions to the appropriate learning skill, check study-system health, and request consent-based monthly summaries. It does not teach lessons, generate questions, or send reminders itself.

### Deployment Geography for Use:

Mainland China; localize curriculum, consent handling, and crisis-support channels before use elsewhere.

## Known Risks and Mitigations:

Risk: Student data or sensitive emotions could be shared across skills or with parents without appropriate consent.

Mitigation: Check consent before each handoff or parent-facing summary, use only the minimum necessary data, and honor requests to exclude sharing or writeback.

Risk: Crisis guidance and curriculum assumptions may be unsuitable outside mainland China.

Mitigation: Localize support channels, curriculum, and consent rules before deployment elsewhere; ask the user's location before offering region-specific crisis contacts.

Risk: A report could imply historical precision when cross-session data is unavailable.

Mitigation: Limit the report to supplied or authorized records, state its coverage, and do not invent historical statistics.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-skill-coordinator)
- [One-week coordination example](artifact/references/one-week-linkage-record.md)
- [Handoff protocol schema](artifact/schemas/handover-protocol.schema.json)
- [Crisis referral protocol](artifact/shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, JSON handoff requests]

**Output Format:** [Chinese-language routing guidance and Markdown reports; structured JSON handoffs when authorized]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports use only authorized, task-relevant summaries; reminder requests are queued, not sent by this skill.]

## Skill Version(s):

2.11.1 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
