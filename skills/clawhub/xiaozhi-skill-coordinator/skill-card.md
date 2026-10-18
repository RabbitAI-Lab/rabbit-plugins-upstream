## Description:

Coordinates Chinese K–12 learning support by routing requests, avoiding duplicate follow-ups, and compiling consent-based monthly learning summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students and their guardians use this skill to identify the right learning support and, on request, review progress across mistakes, understanding, notes, plans, and focus. It coordinates other skills rather than teaching or sending reminders itself.

### Deployment Geography for Use:

Mainland China; localization of crisis contacts, curricula, and minor-data consent is required elsewhere.

## Known Risks and Mitigations:

Risk: Learning records or emotional information may be shared beyond the student's or guardian's expectations.

Mitigation: Check profile, cross-skill sharing, reminder, parent-sharing, and teacher-writeback consent before use; limit summaries to authorized data.

Risk: Crisis guidance and consent assumptions may be inappropriate outside Mainland China.

Mitigation: Localize emergency contacts and minor-data consent rules before deployment elsewhere.

Risk: Unavailable cross-session records can leave monthly reports incomplete.

Mitigation: Use only information provided in the current conversation and clearly state the report's limited coverage.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-skill-coordinator)
- [One-week coordination example](references/one-week-linkage-record.md)
- [Crisis referral protocol](shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese-language routing guidance, system checks, and opt-in monthly reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summaries use only the data needed for the current request and authorized by the student or guardian.]

## Skill Version(s):

2.11.2 (source: server release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
