## Description:

Query redfin.com from a shell with the fpx CLI to resolve locations, search listings, read property details, market trends, comparable rentals, climate risk, photos, and signed-in saved items through a browser-backed Redfin session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to generate shell commands and guidance for querying Redfin listing, property, market, rental, photo, climate-risk, and saved-account data through fpx without running a Redfin MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Signed-in saved-home and saved-search examples can access Redfin account data through the user's browser session.

Mitigation: Keep the fpx profile scoped to redfin.com and run saved-account examples only when intentional.

Risk: Live Redfin responses can be rejected, incomplete, or tied to a region different from the requested query.

Mitigation: Check Redfin result codes and service-region fields before trusting returned payloads.

## Reference(s):

- [Redfin stingray endpoints for fpx](references/stingray-endpoints.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Markdown]

**Output Format:** [Markdown with inline shell commands and JSON parsing examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include fpx setup commands, Redfin endpoint URLs, jq filters, and troubleshooting guidance.]

## Skill Version(s):

1.1.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
