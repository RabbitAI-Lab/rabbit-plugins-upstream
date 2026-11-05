## Description:

Query Zillow listings, property records, pricing and tax history, photos, market reports, and signed-in saved searches or homes through the fpx CLI and a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to search Zillow listings and inspect property details, market and pricing history, photos, and saved searches or homes from scripts without installing an MCP server.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: Saved-search and saved-home results can contain private Zillow account data accessed through a signed-in browser session.

Mitigation: Approve only Zillow access and the required fetch capability, protect temporary output files, and revoke pairing when finished.

Risk: The external CLI and browser extension are dependencies outside this review.

Mitigation: Verify the CLI and extension before installing them.

## Reference(s):

- [Zillow pages and extraction guidance](references/pages.md)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/zillow-fpx)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell and Python examples and JSON data examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Instructions and command examples for fetching and extracting Zillow page data.]

## Skill Version(s):

1.3.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
