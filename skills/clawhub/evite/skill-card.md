## Description:

Connects an agent to Evite to review invitations and guest lists, manage RSVPs, and create or update hosted events with confirmation before changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Evite users and event hosts can ask an agent to review invitations, RSVP status, and guest lists or prepare event and guest-management actions for confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account credentials or session cookies in a shared project configuration could expose Evite account and guest information.

Mitigation: Use user-level configuration for credentials and do not commit passwords or cookies.

Risk: Messages, guest changes, invitations, or cancellations could reach the wrong people or change the wrong event.

Mitigation: Review each write preview and explicitly approve it before the agent confirms the action.

## Reference(s):

- [Evite skill on ClawHub](https://clawhub.ai/chrischall/skills/evite)
- [evite-mcp package](https://www.npmjs.com/package/evite-mcp)

## Skill Output:

**Output Type(s):** [Text, Configuration instructions, Guidance]

**Output Format:** [Markdown with JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include personal event and guest information; changes require user confirmation.]

## Skill Version(s):

1.3.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
