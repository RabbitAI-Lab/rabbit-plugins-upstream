## Description:

Discover restaurants on Tock (exploretock.com) via MCP -- list cities, search a metro, and get a venue's details plus its bookable experiences, prices, party sizes, and open dates/times.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to discover Tock restaurants, inspect venue details and availability, and check signed-in account reservations or profile data when the required browser extension is running.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP server and fetchproxy extension can read Tock pages visible in the user's signed-in browser, including profile and reservation information.

Mitigation: Install only after confirming that this account access is acceptable, and avoid sharing returned account data with untrusted parties.

Risk: The skill is not intended to book, pay for, cancel, or modify Tock reservations.

Mitigation: Use it for discovery and verification only; complete booking, payment, and cancellation directly on Tock.

Risk: A booking success screen alone may not prove that a reservation was confirmed.

Mitigation: Treat bookings as confirmed only after capturing a confirmation signal and verifying the reservation with the skill's verification workflow.

## Reference(s):

- [tock-mcp npm package](https://www.npmjs.com/package/tock-mcp)
- [tock-mcp source repository](https://github.com/chrischall/tock-mcp)
- [fetchproxy browser extension](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, configuration, shell commands, guidance]

**Output Format:** [Markdown guidance with JSON configuration and shell command examples; MCP tools return structured restaurant, availability, reservation, profile, verification, and health-check results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Tock helper; account-specific tools require a signed-in exploretock.com browser tab and the fetchproxy extension.]

## Skill Version(s):

1.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
