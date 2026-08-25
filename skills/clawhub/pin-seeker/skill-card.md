## Description:

Find golf tee times, hot deals, and cheapest rounds by city, ZIP, or course name.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rkrishnakumar](https://clawhub.ai/user/rkrishnakumar)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to discover public GolfNow tee-time inventory by city, ZIP, or course name, compare shortlist options, and hand off booking or payment to GolfNow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tee-time search details such as city, ZIP, course name, date or time preference, player count, and timezone are sent to pinseeker.xyz.

Mitigation: Use the skill only when this hosted API data sharing is acceptable, and avoid adding unnecessary personal details to searches.

Risk: Users may mistake search results for a held or confirmed reservation.

Mitigation: Present results as discovery only and direct users to complete booking or payment through GolfNow.

## Reference(s):

- [Pin Seeker agent homepage](https://pinseeker.xyz/agents.html)
- [ClawHub skill page](https://clawhub.ai/rkrishnakumar/skills/pin-seeker)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown shortlist with course, time, price, availability, and GolfNow links; hosted API responses are JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Discovery only; the skill does not book, hold, reserve, pay, persist data, or request sensitive authority.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
