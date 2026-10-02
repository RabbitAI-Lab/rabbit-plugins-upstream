## Description:

Guides agents in querying public Hemnet property listings from a shell using the fpx CLI and a scoped browser bridge, without running an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to resolve Swedish locations, search active and sold Hemnet listings, and inspect listing details through a browser-backed CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing a global CLI and browser extension grants a browser bridge access to requests.

Mitigation: Verify the extension release, restrict its profile and site access to hemnet.se, and approve pairing deliberately.

Risk: Automated property queries could exceed acceptable use of Hemnet's public data.

Mitigation: Limit use to public property reads consistent with Hemnet's terms.

## Reference(s):

- [GraphQL query examples](artifact/references/graphql-queries.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [Hemnet FPX on ClawHub](https://clawhub.ai/chrischall/skills/hemnet-fpx)

## Skill Output:

**Output Type(s):** [Shell commands, Code, Guidance]

**Output Format:** [Text and Markdown with shell and GraphQL examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Queries return public listing data as JSON, with prices in SEK and areas in square meters.]

## Skill Version(s):

1.1.7 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
