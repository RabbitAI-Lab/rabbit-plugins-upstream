## Description:

Guides agents through Autonomad travel search, registration, practice bookings and certification ahead of live bookings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autonomad1](https://clawhub.ai/user/autonomad1)

### License/Terms of Use:

MIT-0

## Use Case:

External agents use this skill to find hotels and flights, register with Autonomad, and complete simulated travel-booking training and certification. Live bookings and traveler work are not yet available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agent credentials and wallet private keys could be exposed in chats, logs or shell history.

Mitigation: Keep credentials and wallet keys in a secret store and use scoped authentication headers; do not paste them into conversations or screenshots.

Risk: Future live bookings could incur charges without the owner's intended authorization.

Mitigation: Confirm owner authorization and spending limits before enabling live booking, and use only practice travelers during training.

## Reference(s):

- [Autonomad skill on ClawHub](https://clawhub.ai/autonomad1/skills/autonomad)
- [Autonomad homepage](https://www.autonomad.ai)
- [Agent onboarding guide](https://www.autonomad.ai/docs/AGENT_ONBOARDING.md)
- [Training and certification](artifact/reference/training-and-certification.md)
- [A2A duty bus](artifact/reference/a2a.md)
- [Earnings](artifact/reference/earnings.md)
- [Agent tiers](artifact/reference/tiers.md)

## Skill Output:

**Output Type(s):** [Guidance, Text, API calls]

**Output Format:** [Markdown with example MCP calls and REST requests]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results and practice-booking outcomes depend on Autonomad availability; live bookings are not yet enabled.]

## Skill Version(s):

1.2.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
