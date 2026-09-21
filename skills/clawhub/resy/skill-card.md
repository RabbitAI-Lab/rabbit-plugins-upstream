## Description:

Manage Resy restaurant reservations via MCP by searching venues, booking tables, listing and canceling reservations, managing favorites, and subscribing to Priority Notify.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to operate a Resy MCP server for restaurant discovery, reservation booking, cancellation, favorites, saved payment-method lookup, and Priority Notify management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses Resy account credentials for an MCP server.

Mitigation: Install only when comfortable storing Resy credentials for agent access, and scope credentials to the intended user account.

Risk: The skill can book or cancel reservations and modify favorites or Priority Notify subscriptions.

Mitigation: Before any booking, cancellation, favorite removal, or notify removal, require the agent to show the venue, date, time, party size, and reservation or notify identifier, then wait for explicit confirmation.

Risk: The skill depends on Resy's private web-app endpoints, which may change without notice.

Mitigation: Treat failed or unexpected responses as requiring user review before retrying account-changing actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/resy)
- [resy-mcp npm package](https://www.npmjs.com/package/resy-mcp)
- [resy-mcp source repository](https://github.com/chrischall/resy-mcp)
- [Publisher profile](https://clawhub.ai/user/chrischall)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration examples, shell commands, and MCP tool names]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May trigger MCP API calls that read account data or perform reservation, cancellation, favorite, and Priority Notify actions.]

## Skill Version(s):

1.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
