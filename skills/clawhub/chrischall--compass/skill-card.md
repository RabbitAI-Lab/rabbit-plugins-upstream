## Description:

Look up real-estate listings, property details, photos, price history, and resolve addresses on Compass via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and real-estate workflows use this skill to query Compass listings, resolve addresses, inspect property details and photos, compare listings, review price history, and calculate mortgage or affordability scenarios through an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a signed-in Compass browser tab through a browser bridge to read Compass pages.

Mitigation: Enable it only for accounts and sessions where this read-only browser-mediated access is acceptable, and keep the Compass tab under the user's control.

Risk: Bulk or commercial scraping may conflict with acceptable-use expectations for Compass pages.

Mitigation: Use the skill for personal, read-only lookup workflows and avoid high-volume automation or redistribution of retrieved listing data.

Risk: The workflow depends on third-party npm and fetchproxy extension components.

Mitigation: Review the package and extension source before installation and keep them updated through trusted package and repository sources.

## Reference(s):

- [Compass MCP npm package](https://www.npmjs.com/package/compass-mcp)
- [Compass MCP source repository](https://github.com/chrischall/compass-mcp)
- [fetchproxy browser extension source](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline JSON and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can surface structured property records, listing comparisons, photo metadata, price-history data, diagnostics, and mortgage or affordability calculations through MCP tool responses.]

## Skill Version(s):

0.12.3 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
