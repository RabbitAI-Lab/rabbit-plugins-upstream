## Description:

This skill should be used when the user asks about Evite events or invitations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an agent to Evite so it can read event information, inspect guest lists and RSVP tallies, send messages, and prepare confirmed changes to invitations or events.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses an external Evite MCP server that can access Evite account credentials, browser session cookies, event data, guest lists, RSVPs, messages, and invitations.

Mitigation: Review before installing, use a pinned and reviewed package version, avoid committing MCP configs or plaintext credentials, and grant access only when the account and event data exposure is acceptable.

Risk: Browser-cookie bootstrap can lift session cookies from a signed-in Evite browser tab.

Mitigation: Disable browser-cookie bootstrap with EVITE_DISABLE_FETCHPROXY=1 unless that authentication path is intentionally required.

Risk: RSVP, messaging, guest-list, invitation, and event-changing operations could affect real invitees or events.

Mitigation: Require explicit confirmation before executing write operations and review dry-run previews before sending changes.

## Reference(s):

- [Evite](https://www.evite.com)
- [evite-mcp npm package](https://www.npmjs.com/package/evite-mcp)
- [evite-mcp GitHub repository](https://github.com/chrischall/evite-mcp)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/evite)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Text]

**Output Format:** [Markdown with JSON and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose Evite MCP tool calls; write actions are designed to require explicit confirmation and otherwise return dry-run previews.]

## Skill Version(s):

0.8.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
