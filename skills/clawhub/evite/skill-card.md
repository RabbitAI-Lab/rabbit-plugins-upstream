## Description:

This skill should be used when the user asks about Evite events or invitations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and end users use this skill to connect an agent to Evite so it can inspect invitations, guest lists, RSVP totals, messages, and templates, then assist with RSVP and host workflows when explicitly confirmed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The external evite-mcp package requires access to Evite credentials or an authenticated Evite session.

Mitigation: Use project-scoped MCP configuration where practical, prefer email/password login over raw session cookies, and install only when that account access is acceptable.

Risk: Fetchproxy bootstrap can lift session cookies from a signed-in browser tab.

Mitigation: Set EVITE_DISABLE_FETCHPROXY=1 when browser-session bootstrap is not desired.

Risk: Confirmed write tools can send messages, change guest lists, RSVP, create, update, send, cancel, reinstate, or duplicate Evite events.

Mitigation: Review the dry-run preview and set confirm: true only after verifying the intended event, guests, message, and action.

## Reference(s):

- [Evite](https://www.evite.com)
- [evite-mcp npm package](https://www.npmjs.com/package/evite-mcp)
- [evite-mcp source](https://github.com/chrischall/evite-mcp)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/evite)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include MCP tool-call guidance and dry-run previews for Evite write operations.]

## Skill Version(s):

1.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
