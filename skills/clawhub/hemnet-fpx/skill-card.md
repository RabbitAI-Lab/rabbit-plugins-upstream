## Description:

Query hemnet.se property data from a shell with the fpx CLI, including location resolution, for-sale and sold listing searches, and listing detail GraphQL calls through a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and property-data workflow authors use this skill to make one-shot Hemnet GraphQL calls from shell scripts when they want Hemnet search and listing data without running the hemnet MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow routes Hemnet requests through a paired browser tab and the pairing persists after first approval.

Mitigation: Install and pair only trusted @fetchproxy/cli and Transporter extension versions, and keep extension site access limited to hemnet.se.

Risk: GraphQL errors can appear in otherwise successful HTTP responses.

Mitigation: Check the response errors field before relying on returned property data.

Risk: The skill targets public Hemnet property data through Hemnet's web surface.

Mitigation: Use it only for public property data and stay within Hemnet's terms.

## Reference(s):

- [Hemnet GraphQL queries for fpx](artifact/references/graphql-queries.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/hemnet-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON GraphQL examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides agents to check GraphQL errors in successful HTTP responses and to keep browser extension site access limited to hemnet.se.]

## Skill Version(s):

0.4.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
