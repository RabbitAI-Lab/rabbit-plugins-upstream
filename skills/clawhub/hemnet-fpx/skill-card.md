## Description:

Query hemnet.se, the Swedish property portal, from a shell with the fpx CLI to resolve locations, search for-sale and sold listings, and read listing details through one-shot GraphQL calls from a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to fetch Hemnet property search results and listing details from command-line workflows without running the Hemnet MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup depends on installing @fetchproxy/cli and pairing the Transporter browser extension, which expands the local browser and CLI trust boundary.

Mitigation: Avoid sudo, prefer a pinned or local install where possible, and pair only the Hemnet profile needed for the workflow.

Risk: Hemnet receives the query terms, filters, and listing requests entered through the GraphQL calls.

Mitigation: Avoid sensitive search criteria and keep use within hemnet.se terms and expected anonymous-read behavior.

Risk: The examples use fixed /tmp file paths that may be overwritten or collide on shared systems.

Mitigation: Use securely created temporary files when adapting the commands for automation.

## Reference(s):

- [Hemnet GraphQL query examples](references/graphql-queries.md)
- [Hemnet GraphQL endpoint](https://www.hemnet.se/graphql)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/hemnet-fpx)

## Skill Output:

**Output Type(s):** [markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell, JSON, and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes example GraphQL request bodies, setup commands, exit-code handling, and result-processing guidance.]

## Skill Version(s):

0.6.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
