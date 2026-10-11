## Description:

Searches Etix events, venues, and performers and retrieves event and venue details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People looking for events and tickets use this skill to find Etix shows, performers, and venues and review showtimes, locations, and available pricing details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The external MCP package and browser extension handle requests through the user's Etix browser session.

Mitigation: Review their sources or pin trusted versions before use in a sensitive environment, and approve pairing only if comfortable using that session.

## Reference(s):

- [ClawHub etix skill](https://clawhub.ai/chrischall/skills/etix)
- [etix-mcp package](https://www.npmjs.com/package/etix-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Natural-language event, venue, and performer search results and details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include showtimes, venue addresses, Etix links, and available prices.]

## Skill Version(s):

1.1.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
