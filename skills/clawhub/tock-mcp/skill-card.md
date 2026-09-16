## Description:

tock-mcp helps agents discover Tock restaurants, venues, bookable experiences, prices, party sizes, availability, and selected signed-in account details through the tock-mcp MCP server and fetchproxy browser extension.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to connect an MCP client to Tock discovery and availability workflows, including metro search, venue lookup, availability checks, reservation listing, profile lookup, and post-booking verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to run an npm package and use a browser extension connected to a signed-in Tock browser session.

Mitigation: Install only after reviewing the package and extension, checking extension permissions, and confirming how to revoke the browser pairing.

Risk: The documented installation uses unpinned remote code through npx.

Mitigation: Prefer exact package versions or reviewed commits before using account-related tools.

Risk: Booking happens outside the read-only tools and a visible success screen alone may not prove a reservation was created.

Mitigation: Treat bookings as confirmed only after capturing an external confirmation signal and receiving a confirmed result from the verification tool.

## Reference(s):

- [tock-mcp ClawHub listing](https://clawhub.ai/chrischall/skills/tock-mcp)
- [tock-mcp npm package](https://www.npmjs.com/package/tock-mcp)
- [fetchproxy browser extension](https://github.com/chrischall/fetchproxy)
- [tock-mcp source link from artifact](https://github.com/chrischall/tock-mcp)

## Skill Output:

**Output Type(s):** [text, configuration, shell commands, guidance]

**Output Format:** [Markdown guidance with JSON configuration examples and MCP tool outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tool outputs may include restaurant, venue, availability, reservation, profile, verification, and bridge-health information; compact views strip known media fields where supported.]

## Skill Version(s):

0.5.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
