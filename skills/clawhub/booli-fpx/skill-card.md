## Description:

Query Booli, a Swedish property portal, from a shell with the fpx CLI to resolve areas, search active and sold listings, and read property details through one-shot GraphQL calls via a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve public Booli property data from shell workflows without running the Booli MCP server. It helps resolve area IDs, query active and sold listings, inspect property details, and compose jq-based summaries from GraphQL JSON responses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fpx CLI and Transporter extension bridge requests through the user's browser context.

Mitigation: Install and use them only when trusted, keep the Booli profile scoped to booli.se fetch requests, and review generated commands before execution.

Risk: The Transporter pairing persists after first approval.

Mitigation: Use fpx health and browser extension site-access controls to confirm the active bridge state, and remove or disable the pairing when it is no longer needed.

Risk: GraphQL errors can be returned inside an otherwise successful HTTP response.

Mitigation: Check each response for an errors array before relying on returned property data or derived summaries.

Risk: The skill queries a third-party property service and depends on Booli's public GraphQL surface.

Mitigation: Use anonymous read-only queries, stay within Booli's terms, and treat availability or schema changes as expected operational risks.

## Reference(s):

- [Booli GraphQL queries for fpx](references/graphql-queries.md)
- [Booli GraphQL endpoint](https://www.booli.se/graphql)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/booli-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell and JSON code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces read-only GraphQL request bodies, fpx command examples, jq recipes, and troubleshooting guidance for Booli property queries.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
