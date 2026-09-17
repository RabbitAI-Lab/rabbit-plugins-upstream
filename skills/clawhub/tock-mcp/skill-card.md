## Description:

Discover Tock restaurants and availability through MCP, including metros, venue details, bookable experiences, prices, party sizes, open dates and times, and signed-in account reservation checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to let an MCP-capable assistant search Tock venues, inspect restaurant availability, and verify reservation status while leaving booking and payment on exploretock.com.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing an unpinned third-party MCP package or browser extension can expose users to unexpected code changes or extension permission risks.

Mitigation: Pin a reviewed package version or commit and verify fetchproxy extension permissions before using the skill.

Risk: Signed-in account tools may expose Tock profile and reservation data to the MCP integration.

Mitigation: Use signed-in tools only with an account and environment approved for sharing that reservation data.

Risk: Reservation booking occurs outside the skill and may be misread if only a success screen is checked.

Mitigation: Treat bookings as confirmed only after a captured confirmation artifact and a confirmed result from the reservation verification tool.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/tock-mcp)
- [tock-mcp npm package](https://www.npmjs.com/package/tock-mcp)
- [fetchproxy browser extension](https://github.com/chrischall/fetchproxy)
- [tock-mcp project link from artifact](https://github.com/chrischall/tock-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and structured MCP tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only restaurant, availability, profile, reservation, and verification results; compact and full views are available for selected tools.]

## Skill Version(s):

0.5.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
