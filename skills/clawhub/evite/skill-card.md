## Description:

Helps users manage Evite invitations and events, including guest lists, RSVPs, messages, and event creation or editing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Evite users can review invitations, event details, guests, and RSVPs, and request changes to their events or guest communications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting the integration grants access to sensitive Evite credentials or an active session.

Mitigation: Install only when Evite account access is intended; set EVITE_DISABLE_FETCHPROXY=1 to prevent signed-in browser session bootstrap.

Risk: Broad event-related requests may invoke account-capable Evite tools, including changes to invitations or guest communications.

Mitigation: Use the integration only for explicit Evite tasks and review each proposed write before confirming it.

## Reference(s):

- [Evite skill listing](https://clawhub.ai/chrischall/skills/evite)
- [evite-mcp package](https://www.npmjs.com/package/evite-mcp)
- [Evite](https://www.evite.com)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Event information and previews of proposed account changes before confirmation.]

## Skill Version(s):

1.3.4 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
