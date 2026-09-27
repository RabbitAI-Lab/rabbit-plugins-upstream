## Description:

Guides agents in querying public Hemnet property listings and sold prices from a shell using fpx and a paired browser tab instead of an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to resolve Swedish locations, find for-sale and sold homes, and inspect listing details through public Hemnet queries without running an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The global fpx CLI and paired Transporter extension bridge requests through the user's browser.

Mitigation: Review both before installation, restrict extension site access to hemnet.se, and approve pairing only for the intended browser.

Risk: Queries to Hemnet could exceed the scope of intended public-data access.

Mitigation: Use anonymous public property-data reads only and follow Hemnet's terms.

## Reference(s):

- [Hemnet GraphQL query examples](references/graphql-queries.md)
- [hemnet-fpx on ClawHub](https://clawhub.ai/chrischall/skills/hemnet-fpx)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell commands and GraphQL JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Explains how to inspect JSON results, including GraphQL errors returned with HTTP 200.]

## Skill Version(s):

1.1.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
