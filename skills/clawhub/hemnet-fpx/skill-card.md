## Description:

Helps agents query public Hemnet property listings and sold prices through a paired browser tab using the fpx CLI, without running an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and property analysts use this skill to resolve Swedish locations, search for-sale and sold listings, and retrieve listing details from Hemnet through a browser-connected command-line workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing an unverified CLI package or browser extension could introduce untrusted software.

Mitigation: Verify the @fetchproxy/cli package and ContextMint Bridge release before installation.

Risk: Broad extension site access could expose browsing activity outside the intended property portal.

Mitigation: Limit the extension's site access to hemnet.se.

Risk: The persistent fpx pairing can continue to enable browser-mediated Hemnet requests.

Mitigation: Remove the pairing when browser-mediated requests are no longer wanted.

## Reference(s):

- [Hemnet GraphQL query examples](artifact/references/graphql-queries.md)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/hemnet-fpx)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)

## Skill Output:

**Output Type(s):** [Shell commands, Code, Guidance]

**Output Format:** [Markdown with shell commands and JSON query examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI queries return GraphQL JSON; check for errors before using results.]

## Skill Version(s):

1.1.12 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
