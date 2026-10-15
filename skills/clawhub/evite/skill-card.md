## Description:

Helps agents review Evite invitations and events, manage guest lists and RSVPs, and create or update events.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Evite users and event hosts use this skill to check invitations, guest lists and RSVP counts, respond to events, and manage invitations and messages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account credentials or session cookies grant access to private Evite events and guest information.

Mitigation: Use Evite-dedicated credentials or cookies and install only when account access is needed.

Risk: Invitation, guest, RSVP, and messaging actions may change or send information on the user's behalf.

Mitigation: Keep write confirmations enabled, review the proposed action, and approve it before execution.

Risk: Browser-session bootstrap can reuse an existing signed-in Evite session.

Mitigation: Disable fetchproxy if browser-session bootstrap is not wanted.

## Reference(s):

- [Evite skill release](https://clawhub.ai/chrischall/skills/evite)
- [evite-mcp package](https://www.npmjs.com/package/evite-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Write actions present a confirmation prompt or preview before execution.]

## Skill Version(s):

1.3.5 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
