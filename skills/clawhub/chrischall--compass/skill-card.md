## Description:

Look up real-estate listings, property details, photos, price history, and resolve addresses on Compass via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to answer Compass real-estate questions by searching listings, resolving addresses, retrieving property details and photos, comparing properties, and calculating mortgage or affordability estimates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on an external MCP package and browser extension that use the user's signed-in Compass browser session.

Mitigation: Review the external projects before use, run them only in the intended browser profile, and disable the extension when agent-assisted Compass access is not desired.

Risk: Compass requests can fail when the browser tab is not signed in or a WAF challenge has not been solved.

Mitigation: Confirm the fetchproxy bridge is active, keep a signed-in Compass tab available, and complete any browser challenge before using network-backed tools.

Risk: Saved homes and saved searches are not supported by the current tool behavior.

Mitigation: Use the supported read-only listing, address resolution, comparison, photo, price-history, and calculator tools instead.

## Reference(s):

- [Compass MCP npm package](https://www.npmjs.com/package/compass-mcp)
- [compass-mcp source](https://github.com/chrischall/compass-mcp)
- [fetchproxy source](https://github.com/chrischall/fetchproxy)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/compass)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can surface Compass listing data, property details, photo URLs, price history, comparison tables, diagnostics, and calculator results.]

## Skill Version(s):

1.1.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
