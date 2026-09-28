## Description:

Guides agents in discovering Tock restaurants, experiences, and availability, and in checking a signed-in user's reservations through a read-only MCP integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People and agents looking for Tock restaurants can find venues, bookable experiences, prices, and open dates and times. Signed-in users can also inspect their profile and reservations and check whether an external booking attempt appears in their account; booking itself happens on Tock.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The integration uses a third-party MCP package and browser extension with access to the signed-in Tock session and account data.

Mitigation: Review the package and extension source or release checksums before installation, and pair only in a browser profile where this access is acceptable.

Risk: A booking success screen or an immediate absence from reservations may not establish whether a booking succeeded.

Mitigation: Treat bookings as unverified until a confirmation record is captured and the reservation verification tool confirms them; recheck after a delay if advised.

## Reference(s):

- [Tock MCP on ClawHub](https://clawhub.ai/chrischall/skills/tock-mcp)
- [Tock MCP npm package](https://www.npmjs.com/package/tock-mcp)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline JSON and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance for read-only venue discovery, availability, and account lookups; signed-in account tools require a paired browser extension.]

## Skill Version(s):

1.1.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
