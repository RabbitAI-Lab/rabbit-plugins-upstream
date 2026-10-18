## Description:

Helps users review Evite invitations and events, manage guests and RSVPs, and create or update events.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Evite users can check invitations, guest lists, RSVPs, and messages, then request event and invitation changes with confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account credentials or session cookies grant access to private Evite data.

Mitigation: Use the skill only for explicit Evite requests and avoid raw browser cookies unless necessary.

Risk: Browser-session reuse may access an existing signed-in Evite session.

Mitigation: Disable fetchproxy when browser-session reuse is not wanted.

Risk: RSVP, messaging, guest-list, invitation, and event actions can change data or contact people.

Mitigation: Keep confirmation enabled and review each proposed action before approving it.

## Reference(s):

- [Evite skill on ClawHub](https://clawhub.ai/chrischall/skills/evite)
- [evite-mcp package](https://www.npmjs.com/package/evite-mcp)
- [Evite](https://www.evite.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Conversational text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Event summaries, guest and RSVP details, and previews of proposed changes.]

## Skill Version(s):

1.3.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
