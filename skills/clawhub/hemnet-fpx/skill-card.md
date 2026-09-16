## Description:

Query hemnet.se property data from a shell with the fpx CLI, including location resolution, for-sale searches, sold listing searches, and listing detail requests through one-shot GraphQL calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to query public Hemnet property listing data from scripts or shell sessions without running the Hemnet MCP server. It helps resolve place names to Hemnet location IDs, run for-sale and sold-listing searches, and inspect listing details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow depends on the @fetchproxy/cli package and Transporter browser extension.

Mitigation: Install only if those components are trusted and keep the browser profile scoped to hemnet.se.

Risk: The artifact examples use fixed files under /tmp for GraphQL request bodies.

Mitigation: Use mktemp-created files for repeated or shared-machine usage.

Risk: Using a logged-in Hemnet browser session could expose more account context than anonymous reads require.

Mitigation: Avoid using a logged-in Hemnet session unless it is specifically needed.

## Reference(s):

- [Hemnet GraphQL queries for fpx](references/graphql-queries.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/hemnet-fpx)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown with shell and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces instructions and command examples for fpx, jq, and Hemnet GraphQL request bodies; does not directly fetch data by itself.]

## Skill Version(s):

0.6.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
