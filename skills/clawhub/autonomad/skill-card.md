## Description:

Helps agents search travel options and share a single link for travelers to review and book a trip, with registration and certification paths for direct agent bookings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autonomad1](https://clawhub.ai/user/autonomad1)

### License/Terms of Use:

MIT-0

## Use Case:

Travelers and their agents use this skill to compare flights, hotels and activities, then share a booking link for the traveler to review and pay. Registered agents can practice and seek certification for direct bookings when that service becomes available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agent credentials or signing keys may be exposed in conversations, logs or shared shells.

Mitigation: Store credentials and keys as secrets, send credentials in headers, and never paste them into chats or logs.

Risk: Once live direct bookings open, agent actions may create real travel purchases.

Mitigation: Require certification and owner confirmation, honor signed spending authorization and tier limits, and confirm booking status before retrying an uncertain outcome.

Risk: Search results may be unavailable or unsuitable for purchase.

Mitigation: Offer only bookable results, retry transient search failures, and let the traveler review prices and terms before paying.

## Reference(s):

- [Autonomad homepage](https://www.autonomad.ai)
- [Agent onboarding guide](https://www.autonomad.ai/docs/AGENT_ONBOARDING.md)
- [Autonomad agent card](https://www.autonomad.ai/.well-known/agent.json)
- [Training and certification](artifact/reference/training-and-certification.md)
- [A2A communication](artifact/reference/a2a.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Booking links]

**Output Format:** [Travel recommendations and booking links in conversational text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Booking links expire; direct live bookings are not yet available according to the skill documentation.]

## Skill Version(s):

1.3.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
