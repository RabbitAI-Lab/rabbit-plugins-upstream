## Description:

Routes Chinese-language K–12 learning requests to the appropriate skill, avoids duplicate handoffs, and compiles a five-part monthly learning report only when requested or agreed to.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students and their supporting adults use this coordinator to route learning questions, check learning-system health, and request an authorized monthly summary of mistakes, understanding, notes, plans, and focus. It does not teach or solve problems itself.

### Deployment Geography for Use:

Mainland China; other regions require localized curriculum, consent rules, and crisis-help channels before student use.

## Known Risks and Mitigations:

Risk: Cross-skill sharing, profile updates, teacher writeback, or reminder queueing could expose a student's personal learning data.

Mitigation: Require the relevant consent, honor sharing opt-outs, and use only the minimum data needed for the current task.

Risk: Mainland-China curriculum, guardian-consent assumptions, and crisis-help channels may be unsuitable elsewhere.

Mitigation: Localize curriculum, consent requirements, and emergency contacts before deployment outside mainland China.

Risk: Crisis signals involving a minor may be mishandled if treated as ordinary study requests.

Mitigation: Stop learning workflows and follow the crisis referral protocol, using help channels appropriate to the user's location.

## Reference(s):

- [One-week linkage example](references/one-week-linkage-record.md)
- [Handover protocol schema](schemas/handover-protocol.schema.json)
- [Platform conventions](shared/platform-conventions.md)
- [Consent and data-sharing vocabulary](shared/vocab.md)
- [Crisis exception protocol](shared/crisis-exception.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, JSON]

**Output Format:** [Chinese-language routing guidance and monthly reports in text or Markdown; structured handover data when applicable]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Monthly reports require user request or consent; use only authorized, task-relevant summaries.]

## Skill Version(s):

2.11.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
