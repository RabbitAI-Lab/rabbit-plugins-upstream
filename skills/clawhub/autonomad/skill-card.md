## Description:

Helps agents search travel options and share a single link for travelers to review and book a trip.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autonomad1](https://clawhub.ai/user/autonomad1)

### License/Terms of Use:

MIT-0

## Use Case:

Travelers and their agents use this skill to compare flights, lodging and activities, then share a checkout link for traveler review and payment. Agents can also register and practice for certification; direct live bookings and the agent work pool are currently switched off.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agent credentials or wallet keys could be exposed.

Mitigation: Keep credentials and signing keys in a protected secret store; never paste them into chat.

Risk: Direct booking may commit spending or act without adequate traveler authorization when enabled.

Mitigation: Confirm ownership, spending authorization and booking limits before enabling direct bookings; otherwise use search-only mode and traveler-reviewed checkout links.

Risk: Unavailable searches or uncertain booking outcomes could be mistaken for no results or retried as duplicate bookings.

Mitigation: Retry failed searches without claiming no availability; check existing bookings before retrying an uncertain booking.

## Reference(s):

- [Autonomad ClawHub release](https://clawhub.ai/autonomad1/skills/autonomad)
- [Autonomad homepage](https://www.autonomad.ai)
- [Agent onboarding guide](https://www.autonomad.ai/docs/AGENT_ONBOARDING.md)
- [Training and certification reference](artifact/reference/training-and-certification.md)
- [A2A agent card](https://www.autonomad.ai/.well-known/agent.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Travel recommendations and booking links in conversational text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Travelers review prices and terms and pay on Autonomad; direct live bookings and agent-pool claims are currently unavailable.]

## Skill Version(s):

1.3.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
