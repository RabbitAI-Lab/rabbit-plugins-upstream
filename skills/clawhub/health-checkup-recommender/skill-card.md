## Description:

Creates personalized health checkup recommendations from age, sex, symptoms, and family history, with itemized prices and an optional booking QR code.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ryanbihai](https://clawhub.ai/user/ryanbihai)

### License/Terms of Use:

MIT-0

## Use Case:

People seeking checkup guidance in China can use the skill to discuss health concerns, compare recommended screening items and prices, and optionally prepare a booking QR code. It is not a medical diagnosis.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The skill collects sensitive symptoms and family history.

Mitigation: Get explicit consent before collecting health details, and share only what is necessary.

Risk: A human-desk handoff may include a full profile, AI summary, and conversation log without clear minimization.

Mitigation: Require an explicit, reviewable, minimized handoff payload and user approval before transfer.

Risk: Booking preparation and QR generation may send checkup selections to an external service.

Mitigation: Confirm that item synchronization transmits only item IDs and obtain consent before sharing a QR code.

Risk: Screening recommendations could be mistaken for diagnosis.

Mitigation: Present results as checkup guidance and refer medical concerns to a qualified clinician.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/ryanbihai/skills/health-checkup-recommender)
- [HaoLa checkup and booking website](https://www.ihaola.com.cn)
- [Checkup evidence mappings](reference/evidence_mappings_2025.json)
- [Risk assessment logic](reference/risk_logic_table.json)
- [Booking information](reference/booking_info.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Image]

**Output Format:** [Markdown recommendations and itemized prices; optional PNG booking QR code]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional handoff summary for a human booking desk.]

## Skill Version(s):

4.6.2 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
