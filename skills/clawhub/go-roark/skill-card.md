## Description:

Helps developers write Go integrations with the unofficial Roark API client for voice AI agents, calls, chats, simulations, metrics, and monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add and test Go code that accesses Roark voice AI agents, calls, chats, simulations, and monitoring data through an unofficial client.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An unofficial Roark client may not have vendor support.

Mitigation: Confirm the unofficial client is acceptable before installing or using it.

Risk: A Roark API key or authorization header could be exposed.

Mitigation: Keep ROARK_API_KEY secret and never log authorization headers.

Risk: Live writes, simulations, deletions, or metrics jobs can change a Roark project.

Mitigation: Run these operations only when the user intends to affect the project.

## Reference(s):

- [go-roark skill release](https://clawhub.ai/psyb0t/skills/go-roark)
- [go-roark module homepage](https://github.com/psyb0t/go-roark)
- [Setup and operation reference](references/setup.md)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Go and a Roark API key; live API actions require user intent.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
