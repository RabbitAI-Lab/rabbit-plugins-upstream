## Description:

Helps agents query Tock restaurants, availability, and a signed-in user's reservations through the fpx CLI and a paired browser tab without running an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to find Tock metros and restaurants, inspect venue availability, and look up the signed-in user's reservations from a shell. It provides read-only lookups, not booking or cancellation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reservation results can expose names, email addresses, and itinerary details.

Mitigation: Treat reservation and account details as private; avoid shared temporary files and redact terminal output before sharing it.

Risk: Browser extension pairing grants the CLI access to a Tock tab, including signed-in reservation data.

Mitigation: Pair only a trusted fpx installation and browser extension, and use a signed-in tab only when retrieving reservations.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/tock-fpx)
- [Tock request examples](references/requests.md)
- [Tock response extraction helper](references/extract-redux-slice.mjs)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and JSON query examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only; reservation lookups require a signed-in Tock tab.]

## Skill Version(s):

1.1.8 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
