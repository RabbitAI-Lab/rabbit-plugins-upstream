## Description:

Discover restaurants on Tock via MCP, including metros, venue search, restaurant details, bookable experiences, prices, party sizes, and open dates or times.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent look up Tock restaurant discovery, availability, venue, profile, and reservation information through the tock-mcp integration. Booking, cancellation, and payment remain outside the MCP tools and must be completed on Tock.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on the external tock-mcp package and fetchproxy browser extension.

Mitigation: Install only if you trust the package, extension, and publisher; review package and extension sources before deployment.

Risk: Account tools can read profile and reservation details through a signed-in Tock browser tab.

Mitigation: Use a trusted browser session, limit use of account tools to necessary tasks, and avoid exposing returned personal or reservation data outside the intended agent session.

Risk: Booking and payment are outside the MCP tools, and immediate booking status can be inconclusive.

Mitigation: Complete booking or payment directly on Tock and use the documented verification flow before reporting a booking as confirmed.

## Reference(s):

- [tock-mcp package](https://www.npmjs.com/package/tock-mcp)
- [tock-mcp project repository](https://github.com/chrischall/tock-mcp)
- [fetchproxy browser extension](https://github.com/chrischall/fetchproxy)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/tock-mcp)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with JSON configuration and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call external MCP tools that return restaurant, availability, profile, and reservation data from Tock.]

## Skill Version(s):

0.5.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
