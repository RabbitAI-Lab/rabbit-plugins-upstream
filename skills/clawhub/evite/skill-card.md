## Description:

This skill should be used when the user asks about Evite events or invitations. Triggers on phrases like "check Evite", "my Evite events", "who RSVP'd", "Evite guest list", "RSVP to the party", "message my Evite guests", "create an Evite invite", or any request involving event invitations, guest lists, RSVPs, or party/event hosting on evite.com.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External Evite users can use this skill to review invitations, events, guest lists, RSVPs, messages, and templates, and to manage invitations and event details. It supports both guest and host workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Evite credentials or session cookies grant access to the account.

Mitigation: Trust the third-party server before providing credentials, protect configuration containing secrets, and disable browser-session reuse with EVITE_DISABLE_FETCHPROXY=1 if it is not wanted.

Risk: An incorrect recipient or event change could send unintended messages or alter an invitation.

Mitigation: Keep write confirmations enabled and carefully review the exact preview, recipients, and event changes before approving.

Risk: The bundled instructions have not been a full audit of the external runtime, and package changes may affect behavior.

Mitigation: Consider pinning a reviewed package version and review the runtime before deployment.

## Reference(s):

- [Evite](https://www.evite.com)
- [evite-mcp package](https://www.npmjs.com/package/evite-mcp)
- [Project repository (listed by the skill)](https://github.com/chrischall/evite-mcp)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/evite)

## Skill Output:

**Output Type(s):** [Text, Event and guest data, Messages, Event and invitation actions]

**Output Format:** [Readable event, guest, RSVP, and message details with action previews or status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Write actions require user confirmation and show a preview before changes or messages are sent.]

## Skill Version(s):

1.3.7 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
