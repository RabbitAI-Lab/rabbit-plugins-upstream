## Description:

Provides read-only shell recipes for Eventbrite orders, organizational events and attendees, and public event discovery through a browser bridge.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Eventbrite account holders use this skill to inspect their own tickets and orders, authorized organization events and attendees, and public event listings from a shell without an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account tokens and browser-session cookies can expose Eventbrite account data.

Mitigation: Do not log or commit credentials; revoke tokens and bridge pairing when no longer needed.

Risk: Orders and attendee exports may contain personal data.

Mitigation: Access only accounts and organizations you are authorized to use, and handle exports as personal data.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/eventbrite-mcp)
- [Eventbrite token API recipes](references/token-api.md)
- [Eventbrite discovery recipes](references/discovery-api.md)
- [ContextMint Bridge source and setup](https://github.com/nullnet-app/contextmint-bridge)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and JSON-query examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only recipes; returned account and attendee data may contain personal information.]

## Skill Version(s):

1.1.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
