## Description:

The skill guides agents to query Redfin data from a shell using the fpx CLI, including location resolution, for-sale searches, property details, market trends, comparable rentals, photos, climate risk, and signed-in saved homes or saved searches.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, external users, and real estate analysts use this skill to retrieve Redfin listing, property, market, rental, photo, climate-risk, and saved-account data through shell commands when a local MCP server is not available or desired.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Saved-home and saved-search workflows can expose personal Redfin account data through the paired browser session.

Mitigation: Use those commands only when access to personal Redfin account data is intended, and unpair or remove the Redfin fpx profile when that bridge should no longer be available.

Risk: Redfin responses can be rejected or unsuitable for the requested location if resultCode is nonzero or the service region is substituted.

Mitigation: Strip the response prefix, check resultCode before trusting payload data, and compare serviceRegionName or returned city and state values against the requested region.

## Reference(s):

- [Redfin stingray endpoints for fpx](references/stingray-endpoints.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON parsing examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance emphasizes stripping Redfin response prefixes, checking resultCode before trusting payload data, and using signed-in browser access only for saved homes or saved searches.]

## Skill Version(s):

0.10.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
