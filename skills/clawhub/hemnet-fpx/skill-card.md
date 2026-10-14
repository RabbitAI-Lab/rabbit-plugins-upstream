## Description:

Guides agents to query public Hemnet property listings and sold prices through a user-approved browser bridge and the fpx CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to resolve Swedish locations, search public for-sale and sold listings, and inspect property details without running an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing an untrusted CLI or browser extension may expose browser activity.

Mitigation: Confirm you trust @fetchproxy/cli and ContextMint Bridge before installing; verify the extension release checksum.

Risk: Broad site access or persistent pairing can allow unintended future browser requests.

Mitigation: Limit browser site access to hemnet.se and remove the pairing when no longer needed.

Risk: A successful request may still contain GraphQL errors or too few sold listings for reliable comparisons.

Mitigation: Check the response for errors and the sold-listing count before using price summaries.

## Reference(s):

- [Hemnet GraphQL query examples](references/graphql-queries.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/hemnet-fpx)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown instructions and GraphQL JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Public Hemnet data only; prices in SEK and areas in m².]

## Skill Version(s):

1.1.11 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
