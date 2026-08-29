## Description:

This skill connects an agent to Evite through an MCP server to read invitations, inspect guest lists and RSVP totals, manage RSVPs and messages, and create or edit events.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent work with Evite invitations and hosted events, including event lookup, guest list review, RSVP actions, guest messaging, and event creation or updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access Evite account data, guest lists, messages, and event-management actions.

Mitigation: Install only when that account access is acceptable, and review the account and event scope before enabling the MCP server.

Risk: Write tools can RSVP, send messages, broadcast to guests, create events, update events, and change guest records.

Mitigation: Use the dry-run preview behavior and supply confirm:true only after reviewing the proposed action.

Risk: Session reuse through browser-cookie bootstrap or cached sessions may expose existing signed-in Evite access.

Mitigation: Disable fetchproxy or session caching when browser-cookie reuse or stored sessions are not desired.

Risk: The runtime includes photo upload even though the submitted skill text does not list that tool.

Mitigation: Review runtime capabilities before deployment and decide whether photo upload is acceptable for the environment.

## Reference(s):

- [Evite website](https://www.evite.com)
- [evite-mcp npm package](https://www.npmjs.com/package/evite-mcp)
- [evite-mcp project link](https://github.com/chrischall/evite-mcp)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/evite)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and text with JSON configuration examples and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Write actions are confirm-gated and return dry-run previews unless confirm:true is supplied.]

## Skill Version(s):

0.6.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
