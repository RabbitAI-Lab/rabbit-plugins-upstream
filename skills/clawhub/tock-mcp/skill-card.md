## Description:

Discover restaurants on Tock via MCP by listing cities, searching metros, retrieving venue details, checking bookable experiences, and reading availability from a browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to configure and operate a Tock MCP server for restaurant discovery, venue details, bookable experiences, availability checks, reservation/profile reads, and post-booking verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to run mutable third-party MCP code and a fetchproxy browser extension.

Mitigation: Review the npm package and extension before installing, prefer a pinned reviewed version or commit, and run the MCP server with least privilege.

Risk: Pairing with a signed-in Tock browser tab can expose account profile and reservation information to the integration.

Mitigation: Use a dedicated browser profile or account where appropriate, sign in only when account tools are needed, and review returned profile and reservation data before sharing it.

Risk: Booking actions occur outside the skill and can be misread if only a success screen or immediate reservation check is used.

Mitigation: Treat bookings as attempted until a confirmation artifact is captured and tock_verify_reservation returns confirmed after allowing for backend lag.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/tock-mcp)
- [tock-mcp npm package](https://www.npmjs.com/package/tock-mcp)
- [tock-mcp source](https://github.com/chrischall/tock-mcp)
- [fetchproxy extension](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON configuration snippets, shell commands, and MCP tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [MCP tool outputs include restaurant, availability, reservation, profile, verification, and healthcheck data; compact view removes media fields where supported.]

## Skill Version(s):

0.5.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
