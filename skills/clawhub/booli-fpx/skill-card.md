## Description:

booli-fpx helps agents query public booli.se property data from a shell through the fpx CLI, including area lookup, for-sale listings, sold listings, and property detail GraphQL calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to generate shell commands and GraphQL request bodies for public Booli property searches without running the booli-mcp server. It supports resolving Booli area ids, searching active and sold listings, and reading property detail through a signed-in browser tab.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on the third-party @fetchproxy/cli package and browser extension pairing.

Mitigation: Verify the package source before installation, consider pinning a reviewed version, and revoke the fpx profile or extension pairing when it is no longer needed.

Risk: Browser-backed requests require Transporter site access for Booli.

Mitigation: Limit the Transporter extension site access to booli.se and keep usage to public anonymous Booli queries.

Risk: Booli GraphQL calls can return an errors array even when the HTTP request succeeds.

Mitigation: Check the response for GraphQL errors, for example with jq '.errors // empty', before using returned data.

## Reference(s):

- [Booli GraphQL queries for fpx](references/graphql-queries.md)
- [Booli GraphQL endpoint](https://www.booli.se/graphql)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON GraphQL request bodies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include jq filters, fpx setup commands, and Booli GraphQL variables.]

## Skill Version(s):

1.3.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
