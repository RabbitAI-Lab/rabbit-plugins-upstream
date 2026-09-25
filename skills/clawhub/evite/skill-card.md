## Description:

Use this skill to work with Evite events and invitations, including guest lists, RSVP status, guest messages, and event creation or updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill through an agent to configure and operate an Evite MCP server for reading and managing invitations, hosted events, RSVPs, guest lists, and guest messaging.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP server can access Evite account data, guest lists, messages, and session cookies.

Mitigation: Install only with credentials intended for this use, review access expectations before setup, and opt out of browser-cookie bootstrap when lifting an existing browser session is not acceptable.

Risk: Write tools can change RSVPs, messages, guests, and hosted events.

Mitigation: Review each write preview carefully and proceed only after explicit user approval with the confirmation token flow.

## Reference(s):

- [ClawHub evite skill page](https://clawhub.ai/chrischall/skills/evite)
- [evite-mcp npm package](https://www.npmjs.com/package/evite-mcp)
- [Evite](https://www.evite.com)

## Skill Output:

**Output Type(s):** [guidance, configuration, shell commands]

**Output Format:** [Markdown with JSON configuration and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Write actions are described as confirmation-gated before network changes are sent.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
