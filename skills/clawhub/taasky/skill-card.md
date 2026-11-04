## Description:

Negotiate terms with another person or their agent through Taasky: meeting times, visits, shift swaps, prices, dates, any deal with a shape.

This skill is ready for commercial/non-commercial use.

## Publisher:

[marina-aronchik](https://clawhub.ai/user/marina-aronchik)

### License/Terms of Use:

MIT-0

## Use Case:

People and their agents use Taasky to negotiate agreements such as meeting times, visits, shift swaps, and prices. The skill helps an agent open or join a negotiation room, propose or counter terms, and track responses while routing final decisions for human confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent may send offers and counters automatically and schedule follow-ups, which can affect a negotiation on the user's behalf.

Mitigation: Set clear limits and a deadline before opening or joining a room, and review the terms the agent is authorized to propose.

Risk: Taasky receives the user's terms and private limits, while room access tokens are saved in agent memory.

Mitigation: Share only the information needed for the negotiation and protect memory notes that contain room access details.

Risk: The skill describes Telegram confirmation for final decisions, but this artifact review did not verify that the remote service enforces it.

Mitigation: Verify the confirmation flow before relying on it for consequential negotiations, and review any decision before confirming.

## Reference(s):

- [Taasky](https://taasky.ai)
- [Taasky OpenClaw integration documentation](https://docs.taasky.ai/integrations/openclaw)
- [Taasky on ClawHub](https://clawhub.ai/marina-aronchik/skills/taasky)

## Skill Output:

**Output Type(s):** [Text, Guidance, Negotiation terms]

**Output Format:** [Structured proposed terms and concise conversational updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.3.15 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
