## Description:

Query eventbrite.com from a shell for personal tickets and orders, organizer event and attendee data through the documented token API, and public event discovery through an fpx browser bridge.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to compose shell commands for reading Eventbrite account, organizer, attendee, order, and public discovery data without running an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fpx/Transporter bridge can use a signed-in Eventbrite browser session and may expose private account, order, attendee, or cookie-derived data.

Mitigation: Use the bridge only in an isolated or trusted browser profile, limit site access to Eventbrite, avoid logging sensitive output, and revoke browser or bridge access after use.

Risk: The setup installs an unpinned global browser-bridge CLI.

Mitigation: Prefer a pinned installation in an isolated environment and review the installed package before pairing it with a browser session.

Risk: Commands may print OAuth tokens, cookies, attendee emails, order details, or other private Eventbrite data to the terminal.

Mitigation: Do not commit tokens or captured data, redact command output before sharing, and store `EVENTBRITE_TOKEN` only in a local secret-aware environment.

## Reference(s):

- [Eventbrite documented API recipes](references/token-api.md)
- [Eventbrite discovery API recipes](references/discovery-api.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/eventbrite-mcp)
- [Publisher profile](https://clawhub.ai/user/chrischall)
- [Eventbrite API keys](https://www.eventbrite.com/platform/api-keys)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only recipes for curl and fpx; outputs are typically JSON responses filtered with jq.]

## Skill Version(s):

0.3.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
