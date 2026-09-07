## Description:

Manage Resy restaurant reservations through an MCP server, including venue search, booking, cancellation, favorites, payment-method lookup, and Priority Notify subscriptions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and end users use this skill to let an agent search Resy availability, book or cancel reservations, manage favorites, and subscribe to Priority Notify using a configured Resy account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can book or cancel real Resy reservations using account credentials and a saved payment method.

Mitigation: Require the agent to repeat the restaurant, date, time, party size, cancellation target, and payment method details, then wait for explicit user approval before booking or cancellation.

Risk: The skill requires a Resy email and password and uses private Resy web-app endpoints rather than an official public API.

Mitigation: Install only when the user accepts sharing Resy credentials with the MCP server, and monitor for endpoint or authentication failures before relying on reservation actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/resy)
- [resy-mcp npm package](https://www.npmjs.com/package/resy-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON configuration snippets, shell commands, and MCP tool guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tool outputs may include live reservation details, payment method summaries with masked card data, booking receipts, cancellation receipts, favorites, and Priority Notify subscriptions.]

## Skill Version(s):

0.13.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
