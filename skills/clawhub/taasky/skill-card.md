## Description:

Negotiate terms with another person or their agent through Taasky: meeting times, visits, shift swaps, prices, dates, any deal with a shape.

This skill is ready for commercial/non-commercial use.

## Publisher:

[marina-aronchik](https://clawhub.ai/user/marina-aronchik)

### License/Terms of Use:

MIT-0

## Use Case:

External users can ask an agent to negotiate schedules, visits, shift swaps, prices, and other agreed terms with another person or their agent. The agent proposes and counters within the user's limits, while acceptance, rejection, and withdrawal remain subject to human confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Status checks may lead to messages being sent, and newer instructions may automatically replace the installed skill.

Mitigation: Require explicit delegation for outbound negotiation and scheduled checks, keep status requests read-only, and review updates before activation.

Risk: Taasky receives negotiation terms and private limits; saved room tokens are credentials.

Mitigation: Share only the limits needed for a negotiation and protect saved room tokens as credentials.

## Reference(s):

- [Taasky](https://taasky.ai)
- [Taasky OpenClaw Integration](https://docs.taasky.ai/integrations/openclaw)
- [Taasky Documentation](https://docs.taasky.ai/)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Structured negotiation terms and concise human-readable updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Proposals, counteroffers, and clarifications are distinct; consequential responses require human confirmation.]

## Skill Version(s):

0.3.13 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
