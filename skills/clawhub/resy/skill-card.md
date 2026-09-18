## Description:

Manage Resy restaurant reservations through an MCP server, including venue search, booking, reservation lookup, cancellation, favorites, and Priority Notify subscriptions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an agent to Resy reservation workflows for finding tables, booking or canceling reservations, managing favorites, and subscribing to availability notifications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires Resy account credentials for a third-party MCP package.

Mitigation: Use a unique Resy password, keep credentials in private environment configuration, and do not commit `.mcp.json` or `.env`.

Risk: Booking, cancellation, favorites, and notification tools can make live changes to a Resy account.

Mitigation: Require explicit confirmation before write actions and verify venue, date, party size, time, payment method, and cancellation token details.

Risk: The setup uses an unpinned `resy-mcp` package and private Resy endpoints.

Mitigation: Pin and review the `resy-mcp` version before use, and expect endpoint changes or failures if Resy changes private interfaces.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/resy)
- [resy-mcp npm package](https://www.npmjs.com/package/resy-mcp)
- [resy-mcp source repository](https://github.com/chrischall/resy-mcp)

## Skill Output:

**Output Type(s):** [Text, Configuration, Shell commands, API calls, Guidance]

**Output Format:** [Markdown with JSON configuration snippets, shell commands, and MCP tool-call guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May trigger live Resy account actions through MCP, including bookings, cancellations, favorites changes, and Priority Notify changes.]

## Skill Version(s):

0.14.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
