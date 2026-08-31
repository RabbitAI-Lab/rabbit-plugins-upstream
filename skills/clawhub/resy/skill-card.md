## Description:

Manage Resy restaurant reservations via MCP by searching venues, booking tables, listing and canceling reservations, managing favorites, and subscribing to Priority Notify.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an agent to a Resy MCP server for restaurant availability searches, bookings, reservation cancellation, favorites, and Priority Notify subscriptions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated MCP access can make account-changing reservation actions.

Mitigation: Require explicit confirmation before booking, cancellation, favorite changes, or Priority Notify subscriptions.

Risk: The install path involves Resy account credentials, saved payment method identifiers, and token persistence.

Mitigation: Pin the npm version, keep credentials in managed environment secrets, and disable token caching or fetchproxy when browser-session or disk-token use is not acceptable.

Risk: The skill depends on Resy's private web-app endpoints, which may change or fail unexpectedly.

Mitigation: Review behavior before deployment and re-test reservation, cancellation, favorites, and notify workflows after Resy changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/resy)
- [resy-mcp npm package](https://www.npmjs.com/package/resy-mcp)
- [resy-mcp project link from artifact](https://github.com/chrischall/resy-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON configuration and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Resy account credentials and an installed MCP server; some actions can change reservations or saved favorites.]

## Skill Version(s):

0.9.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
