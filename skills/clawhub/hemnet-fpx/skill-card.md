## Description:

Query hemnet.se from a shell with the fpx CLI to resolve locations, search for-sale and sold listings, and read listing details through one-shot GraphQL calls via a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation users use this skill to query public Hemnet listing data from shell workflows without running the Hemnet MCP server. It provides setup steps, GraphQL request bodies, and jq recipes for location lookup, active listings, sold listings, and listing details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relays Hemnet requests through the user's browser context to bypass Cloudflare challenges.

Mitigation: Use it only when comfortable with that relay model, restrict browser extension site access to hemnet.se, and remove or unpair the fpx profile when finished.

Risk: Browser session or tracking state may influence requests made through the signed-in browser tab.

Mitigation: Use a normal Hemnet tab without account data when possible, review Hemnet's terms, and avoid using the workflow for account-specific or sensitive data.

## Reference(s):

- [Hemnet GraphQL queries for fpx](references/graphql-queries.md)
- [Hemnet GraphQL endpoint](https://www.hemnet.se/graphql)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/hemnet-fpx)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls]

**Output Format:** [Markdown with shell and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces commands and query bodies for anonymous Hemnet GraphQL reads through fpx; callers should inspect GraphQL errors in otherwise successful responses.]

## Skill Version(s):

0.3.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
