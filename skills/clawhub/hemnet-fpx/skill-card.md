## Description:

Query Hemnet property data from a shell by using the fpx CLI to send one-shot GraphQL calls through a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to resolve Hemnet locations, search for-sale and sold property listings, and retrieve listing details from shell workflows without running the Hemnet MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a persistent browser-extension bridge for hemnet.se requests.

Mitigation: Keep the fpx profile scoped to hemnet.se, revoke pairing or extension site access when no longer needed, and use fpx health checks when troubleshooting.

Risk: Automated GraphQL access to Hemnet may conflict with site terms or trigger anti-bot controls.

Mitigation: Review Hemnet's terms before use, avoid high-volume scraping, and keep usage to read-focused workflows.

## Reference(s):

- [Hemnet GraphQL queries for fpx](references/graphql-queries.md)
- [Hemnet GraphQL endpoint](https://www.hemnet.se/graphql)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/hemnet-fpx)
- [Publisher profile](https://clawhub.ai/user/chrischall)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, GraphQL request bodies, and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs guide anonymous read-only Hemnet GraphQL requests through fpx and advise checking GraphQL errors in successful HTTP responses.]

## Skill Version(s):

0.6.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
