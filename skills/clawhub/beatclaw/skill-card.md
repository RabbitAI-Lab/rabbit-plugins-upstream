## Description:

Helps music producers generate instrumental beats with a Suno API key and sell them on the BeatClaw marketplace, with optional stem splitting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youngpietro](https://clawhub.ai/user/youngpietro)

### License/Terms of Use:

MIT-0

## Use Case:

External music producers use the skill to configure BeatClaw, generate instrumental beats through a third-party music service, and manage marketplace listings and optional stems.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Third-party music API keys and BeatClaw credentials may be exposed or misused.

Mitigation: Store credentials securely, avoid sharing tokens in chat, and review account access before connecting the agent.

Risk: Beat generation can consume provider credits, and published listings affect a public marketplace.

Mitigation: Confirm each paid generation and public listing or material change with the owner before acting.

Risk: A remote skill update can replace persistent instructions.

Mitigation: Prefer a reviewed install path and inspect any downloaded replacement skill before using it in a new session.

## Reference(s):

- [BeatClaw on ClawHub](https://clawhub.ai/youngpietro/skills/beatclaw)
- [BeatClaw marketplace](https://beatclaw.com)
- [Suno API provider](https://sunoapi.org)
- [MVSEP API access for stem splitting](https://mvsep.com/user-api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with API request examples and marketplace links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Beat and stem files are delivered through the marketplace, not as agent output.]

## Skill Version(s):

1.59.1 (source: ClawHub release and skill text)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
