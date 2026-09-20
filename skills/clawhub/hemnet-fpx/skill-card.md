## Description:

Query hemnet.se from a shell with the fpx CLI to resolve locations, search for-sale and sold listings, and read listing details through one-shot GraphQL calls via a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to query public Hemnet property data from shell workflows without running the hemnet-mcp server. It provides setup guidance, GraphQL request bodies, jq recipes, and troubleshooting notes for fpx-based access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow routes Hemnet requests through the user's browser context and the Transporter browser extension.

Mitigation: Keep browser site access scoped to hemnet.se, review the fpx CLI and extension provenance separately, and use only public or anonymous Hemnet data.

Risk: GraphQL calls can fail or return misleading partial results if the browser bridge, Cloudflare challenge state, or GraphQL errors are not checked.

Mitigation: Use fpx health and documented exit codes, keep a normal Hemnet tab open, and inspect GraphQL errors before relying on returned data.

Risk: Use outside Hemnet's terms or overly broad collection could create policy or compliance issues.

Mitigation: Limit use to public Hemnet data, keep requests consistent with Hemnet's terms, and avoid account or private-data workflows.

## Reference(s):

- [Hemnet GraphQL queries for fpx](references/graphql-queries.md)
- [Hemnet GraphQL endpoint](https://www.hemnet.se/graphql)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown with shell commands and JSON GraphQL request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes jq post-processing examples and fpx exit-code troubleshooting guidance.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
