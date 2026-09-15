## Description:

Query hemnet.se from a shell with the fpx CLI to resolve locations, search for-sale and sold listings, and read listing detail through one-shot GraphQL calls via a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to query public Hemnet property listing data from scripts or shell workflows without running the Hemnet MCP server. It helps resolve Hemnet location ids, search active and sold listings, and fetch listing details as GraphQL JSON.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on a persistent browser bridge that can relay requests through a Hemnet tab.

Mitigation: Grant browser extension site access only for hemnet.se, keep the Hemnet tab unauthenticated where possible, and unpair or remove the extension when finished.

Risk: The setup installs an unpinned global CLI package.

Mitigation: Pin and verify the @fetchproxy/cli package before installation when using the skill in managed or commercial environments.

Risk: Documented examples write query files under /tmp.

Mitigation: Use private temporary files or a restricted working directory for query bodies.

## Reference(s):

- [Hemnet GraphQL queries for fpx](references/graphql-queries.md)
- [Hemnet GraphQL endpoint](https://www.hemnet.se/graphql)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/hemnet-fpx)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON query bodies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs include fpx commands, GraphQL request bodies, jq examples, and troubleshooting guidance.]

## Skill Version(s):

0.6.3 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
