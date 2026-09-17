## Description:

Cal.com (cal.com) lets an agent read, create, update, and delete Cal.com data through the OOMOL-connected oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and agents use this skill to manage Cal.com bookings, attendees, event types, schedules, availability, calendars, and user profile data through an authenticated OOMOL connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes internet installer scripts for the OOMOL CLI.

Mitigation: Review the CLI installation path before use and prefer a signed or package-manager install when available.

Risk: Write and destructive actions can change or delete Cal.com bookings, event types, schedules, calendars, or profile data.

Mitigation: Confirm the exact target, payload, and expected effect before any state-changing action, and require explicit approval for delete actions.

Risk: The skill acts through the connected Cal.com account.

Mitigation: Use it only with the intended Cal.com account and reconnect or reauthorize only when an authentication or scope error requires it.

## Reference(s):

- [Cal.com homepage](https://cal.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-cal)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
