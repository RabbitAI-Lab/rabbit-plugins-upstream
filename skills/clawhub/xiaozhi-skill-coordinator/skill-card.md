## Description:

Routes Chinese K–12 learning questions to the appropriate study skill and, on request, summarizes consented learning data in a monthly overview.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students, families, and educators use this coordinator to find the right learning skill for a question, check learning-system progress, or request a five-part monthly overview. It routes and summarizes rather than teaching subjects or sending reminders itself.

### Deployment Geography for Use:

Mainland China by default; localize curricula, consent settings, and crisis contacts before use elsewhere.

## Known Risks and Mitigations:

Risk: Learning records or emotion details about minors may be shared more broadly than intended.

Mitigation: Review consent for profile storage, cross-skill sharing, parent and emotion sharing, and teacher writeback; use only authorized, task-relevant summaries.

Risk: Unwanted reminders or reports may be generated without the student's agreement.

Mitigation: Require explicit agreement before creating monthly overviews or queuing reminders, and respect pause and sharing controls.

Risk: China-specific curricula and crisis contacts may be unsuitable in other regions.

Mitigation: Localize learning guidance and crisis contacts before deploying outside Mainland China; confirm location before giving emergency numbers.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-skill-coordinator)
- [One-week coordination example](artifact/references/one-week-linkage-record.md)
- [Handover protocol schema](artifact/schemas/handover-protocol.schema.json)
- [Consent and sharing conventions](artifact/shared/vocab.md)
- [Regional and platform conventions](artifact/shared/platform-conventions.md)
- [Crisis referral protocol](artifact/shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Conversational routing guidance, Markdown learning summaries, and structured handover data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Monthly overviews are on request and use only consented, task-relevant summaries; handovers follow the supplied schema.]

## Skill Version(s):

2.7.1 (source: ClawHub release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
