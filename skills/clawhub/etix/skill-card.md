## Description:

Search Etix events, venues, and performers and retrieve event or venue details through an MCP server that requires etix-mcp, fetchproxy, and an active etix.com browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to let an agent search public Etix event, venue, and performer data and fetch detailed event or venue information through a local MCP bridge.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on a manually loaded browser extension and a local MCP bridge that send Etix requests through the user's open Etix browser tab.

Mitigation: Install only in a browser profile where this session access is acceptable, review the etix-mcp and fetchproxy source before use, and keep the Etix tab and extension active only when needed.

Risk: Etix does not publish a public consumer API, so website endpoints and pages may change or become unavailable.

Mitigation: Use the healthcheck tool when calls fail and review results before relying on returned event, venue, or pricing details.

Risk: Requests are made through the user's own browser session and should remain consistent with Etix terms.

Mitigation: Use the skill for public event discovery at the user's discretion and avoid use cases that require unauthorized access or automated misuse.

## Reference(s):

- [etix-mcp npm package](https://www.npmjs.com/package/etix-mcp)
- [etix-mcp source repository](https://github.com/chrischall/etix-mcp)
- [fetchproxy source repository](https://github.com/chrischall/fetchproxy)
- [Etix website](https://www.etix.com/ticket/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON configuration and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent guidance may lead to MCP tool calls that return event, venue, performer, location, and healthcheck data.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
