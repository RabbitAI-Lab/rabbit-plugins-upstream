## Description:

Query redfin.com (US real-estate portal) from a shell with the fpx CLI (@fetchproxy/cli) instead of running the redfin-mcp server — resolve locations/addresses, search for-sale listings, read property detail (price, beds/baths, price history, tax history), market trends, comparable rentals, climate risk, photos, and (signed-in) saved homes and saved searches, via one-shot calls through a signed-in browser tab. Use when you want Redfin data without the MCP, in a script, or on a machine where the MCP isn't installed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers who need Redfin data in shell scripts can use this skill to resolve locations and retrieve listings, property details, market trends, rental comparisons, climate data, photos, and, when signed in, saved homes and searches through a browser-backed CLI.

### Deployment Geography for Use:

United States (Redfin property data)

## Known Risks and Mitigations:

Risk: Saved-home examples may write private favorite-listing data, including home addresses, to a temporary file.

Mitigation: Stream HTML directly into its parser, or use a private uniquely created temporary file and remove it after use.

Risk: A signed-in Redfin tab can expose saved homes and searches through the browser bridge.

Mitigation: Limit browser approval to redfin.com fetch access, and use a signed-in tab only when saved data is needed.

## Reference(s):

- [Stingray endpoint examples](references/stingray-endpoints.md)
- [ClawHub release page](https://clawhub.ai/chrischall/skills/redfin-fpx)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [ContextMint Bridge project](https://github.com/nullnet-app/contextmint-bridge)
- [Fetchproxy extension notes](https://github.com/chrischall/fetchproxy#extension)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown instructions with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands retrieve Redfin listing and property data; JSON examples show parsing and filtering the responses.]

## Skill Version(s):

1.2.6 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
