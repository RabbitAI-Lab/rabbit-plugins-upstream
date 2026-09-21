## Description:

Cal.com skill for reading, creating, updating, and deleting Cal.com data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to manage Cal.com bookings, event types, schedules, availability, calendars, attendees, and profile data through OOMOL's Cal.com connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, update, cancel, decline, delete, or otherwise change Cal.com data.

Mitigation: Confirm the exact payload and expected effect with the user before write actions, and require explicit approval for destructive actions.

Risk: The optional first-time setup path includes remote installer commands for the oo CLI.

Mitigation: Review the oo CLI installer before running it and install only if the user accepts OOMOL as an intermediary for the Cal.com account.

Risk: Cal.com access is mediated by an OOMOL-connected account with server-side credential handling.

Mitigation: Use the skill only when the user is comfortable connecting Cal.com through OOMOL and verify write or destructive changes before approval.

## Reference(s):

- [Cal.com homepage](https://cal.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Cal.com skill page](https://clawhub.ai/oomol/skills/oo-cal)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before building action payloads.]

## Skill Version(s):

1.0.5 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
