## Description:

Query booli.se from a shell with the fpx CLI to resolve areas, search for-sale and sold listings, and read property details through one-shot GraphQL calls using a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to retrieve public Booli property listing and sold-price data from shell workflows without running the Booli MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing and pairing @fetchproxy/cli with the Transporter extension introduces local setup and trust decisions.

Mitigation: Review the CLI and browser extension before installation, avoid sudo for setup, and consider pinning the npm package version.

Risk: Browser-mediated GraphQL requests may have terms-of-use or privacy implications.

Mitigation: Confirm that this access pattern fits Booli's terms and the user's privacy expectations before use.

Risk: Examples use fixed temporary file paths under /tmp.

Mitigation: Use mktemp-based files in shared or multi-user environments.

## Reference(s):

- [Booli GraphQL Queries for fpx](references/graphql-queries.md)
- [Booli GraphQL endpoint](https://www.booli.se/graphql)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/booli-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON, guidance]

**Output Format:** [Markdown guidance with shell commands and GraphQL JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces command-oriented guidance for querying Booli through fpx and jq.]

## Skill Version(s):

1.3.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
