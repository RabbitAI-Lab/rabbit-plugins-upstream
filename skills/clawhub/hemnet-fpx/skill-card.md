## Description:

Guides agents in querying public Hemnet property listings and sales from a shell through a domain-scoped browser bridge.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agents can resolve Swedish locations, search public for-sale and sold properties, and inspect listings without running an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the skill requires trusting an external CLI and browser extension.

Mitigation: Review the extension source or verify its release checksum before installation and pairing.

Risk: Overbroad browser access or use beyond public Hemnet reads may exceed the intended scope.

Mitigation: Limit the CLI profile and extension site access to hemnet.se, and follow Hemnet's terms for public reads.

## Reference(s):

- [Hemnet GraphQL query examples](references/graphql-queries.md)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Shell commands, Code, Guidance]

**Output Format:** [Markdown with shell commands and JSON GraphQL query bodies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Public listing results can include prices in SEK and areas in m²; check responses for GraphQL errors.]

## Skill Version(s):

1.1.8 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
