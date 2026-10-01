## Description:

Helps agents query Hemnet property listings and sold prices with one-shot GraphQL calls through a paired browser tab instead of an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can resolve Swedish locations, search for-sale and sold properties, and inspect listing details from a shell without running the Hemnet MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests use a browser bridge with persistent pairing to reach Hemnet through the user's browser context.

Mitigation: Use a Hemnet-scoped profile and remove the pairing or extension access when no longer needed.

Risk: Browser-routed queries bypass Hemnet's Cloudflare challenge.

Mitigation: Review Hemnet's terms and the browser-bridge workflow before use.

## Reference(s):

- [Hemnet GraphQL query examples](references/graphql-queries.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/hemnet-fpx)

## Skill Output:

**Output Type(s):** [Shell commands, Code, Guidance]

**Output Format:** [Markdown with shell commands and GraphQL JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Query results are JSON; monetary values are in SEK and areas in m². Check GraphQL errors even when the request succeeds.]

## Skill Version(s):

1.1.6 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
