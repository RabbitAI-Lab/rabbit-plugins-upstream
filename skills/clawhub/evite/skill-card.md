## Description:

Helps an agent review Evite invitations and hosted events, manage guest lists and RSVPs, and draft or send event updates with user confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Evite users and event hosts use this skill to check invitations, guest lists and RSVP status, and manage event invitations and messages with explicit approval for changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account credentials and session cookies can expose private events, guest lists and messages.

Mitigation: Use scoped credentials where possible; avoid raw session cookies unless necessary and disable browser-cookie access with EVITE_DISABLE_FETCHPROXY=1 when undesired.

Risk: RSVP, guest, message and event actions can change account data or send invitations.

Mitigation: Review proposed changes and require explicit user confirmation before every account-changing action.

Risk: Generic invitation requests may activate the skill without an explicit Evite intent.

Mitigation: Confirm the user intends to use Evite before accessing account data or taking action.

## Reference(s):

- [Evite skill release](https://clawhub.ai/chrischall/skills/evite)
- [evite-mcp package](https://www.npmjs.com/package/evite-mcp)
- [Evite](https://www.evite.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Plain text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Event and RSVP summaries, guest-list details, and previews of proposed changes.]

## Skill Version(s):

1.3.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
