## Description:

Helps agents find Tock restaurants, view experiences and availability, and check a signed-in user's reservations through a read-only MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Users and agents can discover restaurants, compare bookable experiences and dates, and inspect or verify reservations associated with a signed-in Tock account. Booking, payment, and cancellation remain on Tock.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The external npm package and browser extension access a signed-in Tock session for account data.

Mitigation: Review both components before installation and use account tools only with a browser session you intend to share with them.

Risk: A booking success screen or immediate reservation lookup may not prove a reservation was confirmed.

Mitigation: Retain a confirmation ID, receipt, or email and confirm with the reservation-verification tool; recheck if it advises waiting.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/tock-mcp)
- [tock-mcp npm package](https://www.npmjs.com/package/tock-mcp)
- [tock-mcp project link in skill documentation](https://github.com/chrischall/tock-mcp)
- [fetchproxy browser extension](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Structured MCP tool results and natural-language responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only restaurant, availability, profile, and reservation results; account tools require a signed-in Tock tab.]

## Skill Version(s):

1.1.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
