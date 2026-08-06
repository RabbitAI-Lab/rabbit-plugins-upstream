## Description:

Manage OpenTable reservations via MCP: search restaurants, check availability, book tables, list or cancel reservations, and manage favorites through a signed-in OpenTable browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to let an agent manage OpenTable restaurant discovery, reservation booking, cancellation, profile lookup, and favorites through the user's authenticated browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can act through the user's signed-in OpenTable session and may create, modify, or cancel reservations.

Mitigation: Install only when comfortable with agent access to the signed-in browser session and review booking, modification, and cancellation previews before confirmation.

Risk: Some reservations may involve saved cards, holds, no-show fees, or cancellation policies.

Mitigation: Surface and review preview details for payment method, cancellation policy, and fee exposure before committing a booking or modification.

Risk: The integration uses OpenTable web endpoints rather than an official public API.

Mitigation: Expect possible endpoint or session changes and re-authenticate or update the MCP integration if OpenTable web behavior changes.

## Reference(s):

- [OpenTable MCP package](https://www.npmjs.com/package/opentable-mcp)
- [fetchproxy browser extension](https://github.com/chrischall/fetchproxy)
- [OpenTable website](https://www.opentable.com/)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May relay reservation, profile, booking, cancellation, and favorites actions through MCP tools connected to the user's signed-in OpenTable browser session.]

## Skill Version(s):

0.16.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
