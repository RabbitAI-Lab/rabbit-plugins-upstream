## Description:

This skill should be used when the user asks about Evite events or invitations, including checking events, guest lists, RSVPs, guest messages, event creation, and party or event hosting on evite.com.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an agent to an Evite account so it can read invitations, inspect guest lists and RSVP status, RSVP to events, message guests, and create or manage hosted events.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill connects an agent to a user's Evite account and may expose event, guest, RSVP, and message data.

Mitigation: Install only when account access is intended, prefer environment variables for credentials, and avoid pasting raw session cookies unless necessary.

Risk: Write-capable tools can RSVP, send messages, edit guests, send invitations, or cancel and reinstate events.

Mitigation: Review dry-run previews before setting confirm to true for messages, guest changes, sends, cancellations, or other event mutations.

Risk: Browser cookie bootstrap can lift session cookies from a signed-in browser tab.

Mitigation: Set EVITE_DISABLE_FETCHPROXY=1 when browser cookie bootstrap is not needed.

## Reference(s):

- [Evite](https://www.evite.com)
- [evite-mcp npm package](https://www.npmjs.com/package/evite-mcp)

## Skill Output:

**Output Type(s):** [Guidance, Configuration, Shell commands, API Calls]

**Output Format:** [Markdown with JSON configuration and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Write actions are confirm-gated and return dry-run previews unless confirm is true.]

## Skill Version(s):

1.1.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
