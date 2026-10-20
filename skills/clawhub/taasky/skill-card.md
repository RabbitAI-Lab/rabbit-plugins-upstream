## Description:

Negotiate terms with another person or their agent through Taasky: meeting times, visits, shift swaps, prices, dates, any deal with a shape. Use when your human wants to settle something with someone else ("agree a time with Anna", "book the plumber this week", "swap my Friday shift", "get the contractor down to 1500 EUR"), when they hand you a Taasky invite link (app.taasky.ai/i/... or mcp.taasky.ai/i/...), or when you have open Taasky rooms to check on. Requires the Taasky MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[marina-aronchik](https://clawhub.ai/user/marina-aronchik)

### License/Terms of Use:

MIT-0

## Use Case:

External users use the skill to negotiate meeting times, visits, shift swaps, prices, dates, and other structured terms with another person or agent through Taasky. It gathers constraints, proposes or counters terms, tracks negotiation rooms, and relays updates for human confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Status checks may be treated as permission to send outbound offers, and skill updates may replace instructions without prior approval.

Mitigation: Require explicit delegation and approval for outbound offers; require human approval before installing any skill update.

Risk: Saved room tokens authorize negotiation actions, while private bargaining limits are shared with Taasky.

Mitigation: Protect room tokens in persistent memory, never disclose them, and ensure the user understands Taasky receives their private limits.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/marina-aronchik/skills/taasky)
- [Taasky integration documentation](https://docs.taasky.ai/integrations/openclaw)
- [Taasky website](https://taasky.ai)
- [Taasky MCP server](https://mcp.taasky.ai/mcp)

## Skill Output:

**Output Type(s):** [API calls, Guidance, Text]

**Output Format:** [Structured negotiation actions and concise human-readable updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses user-provided negotiation terms and limits; consequential moves require human confirmation.]

## Skill Version(s):

0.3.11 (source: server-resolved release metadata, skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
