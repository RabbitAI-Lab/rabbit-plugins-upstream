## Description:

Discover restaurants and availability on Tock via MCP, including cities, venue details, bookable experiences, prices, party sizes, open dates and times, and signed-in account reservation or profile queries when configured.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to connect an MCP-capable assistant to Tock restaurant discovery, availability lookup, account profile, reservation listing, and reservation verification workflows. Bookings remain outside the skill and are completed directly on Tock.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on the external tock-mcp package and fetchproxy browser extension, which relay requests through a signed-in Tock browser tab.

Mitigation: Review those external components before installation and use them only if granting read access to Tock profile and reservation data is acceptable.

Risk: Reservation booking is outside the skill and success screens may not prove that a booking was confirmed.

Mitigation: Complete bookings directly on Tock and use the reservation verification workflow before reporting a booking as confirmed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/tock-mcp)
- [tock-mcp npm package](https://www.npmjs.com/package/tock-mcp)
- [tock-mcp source](https://github.com/chrischall/tock-mcp)
- [fetchproxy extension](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON and shell command examples, plus structured MCP tool outputs from the configured server]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Tock discovery and account-query workflows; compact view is the default for supported tools.]

## Skill Version(s):

1.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
