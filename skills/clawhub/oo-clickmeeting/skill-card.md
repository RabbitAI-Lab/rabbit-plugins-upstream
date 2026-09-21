## Description:

ClickMeeting (clickmeeting.com) enables an agent to read, create, update, and delete ClickMeeting data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to let an agent operate ClickMeeting rooms, sessions, attendees, registrations, recordings, chats, access tokens, phone gateways, and time zone lookups through an OOMOL-connected ClickMeeting account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, update, delete, register participants, and generate access tokens in a connected ClickMeeting account.

Mitigation: Confirm exact payloads and effects with the user before write actions, and require explicit approval before destructive delete actions.

Risk: The setup instructions include remote shell installers for the oo CLI.

Mitigation: Review or verify the oo CLI installer and install guide before running remote shell or PowerShell install commands.

Risk: The skill depends on an OOMOL-connected ClickMeeting account and server-side credentials.

Mitigation: Use it only where the connected account, scopes, billing status, and ClickMeeting connection are intended for agent operation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-clickmeeting)
- [ClickMeeting homepage](https://clickmeeting.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands target the oo CLI and may return JSON responses containing data and execution metadata.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
