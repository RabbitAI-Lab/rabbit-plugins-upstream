## Description:

Look up Compass real-estate listings, property details, photos, price history, comparables, address resolutions, and mortgage or affordability calculations through an MCP integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research Compass property listings, retrieve listing details and photos, compare properties, inspect price history, resolve addresses, and run mortgage or affordability calculations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on an external MCP package and a fetchproxy browser extension that can make Compass requests through the user's signed-in browser tab.

Mitigation: Install only if comfortable with that access, keep use scoped to Compass property research, and review or pin the external npm and GitHub components before use.

Risk: Network lookup tools may fail when the user is not signed into Compass or when the browser session is blocked by a WAF challenge.

Mitigation: Confirm the fetchproxy bridge, active Compass session, and browser challenge state before relying on network results; local mortgage and affordability calculations do not require sign-in.

Risk: Compass does not provide a public consumer API, so property data is extracted from server-rendered page state and may change or be incomplete.

Mitigation: Treat outputs as property research assistance and verify important facts against Compass or authoritative real-estate records before acting on them.

## Reference(s):

- [ClawHub compass skill page](https://clawhub.ai/chrischall/skills/compass)
- [compass-mcp npm package](https://www.npmjs.com/package/compass-mcp)
- [compass-mcp source](https://github.com/chrischall/compass-mcp)
- [fetchproxy source](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and structured text with JSON configuration and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Compass listing URLs, property facts, photo URLs, price-history details, comparison summaries, mortgage calculations, and per-item errors.]

## Skill Version(s):

0.14.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
