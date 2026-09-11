## Description:

Look up real-estate listings, property details, Zestimates, saved searches/homes, and market reports on Zillow via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and real-estate researchers use this skill to query Zillow property listings, property records, estimates, saved homes, saved searches, and market metrics through a configured MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on third-party MCP and browser-extension code that can change if installed from mutable package or repository references.

Mitigation: Pin zillow-mcp to a reviewed package version and fetchproxy to a reviewed commit or release before installation.

Risk: The configured browser session may expose private Zillow account data such as saved homes and saved searches.

Mitigation: Use a separate browser profile for Zillow access and treat saved activity returned by the tools as private user data.

Risk: Browser-extension permissions can affect the user's signed-in Zillow session.

Mitigation: Inspect the fetchproxy extension permissions before loading it and remove the extension when Zillow MCP access is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/zillow)
- [zillow-mcp npm package](https://www.npmjs.com/package/zillow-mcp)
- [zillow-mcp source](https://github.com/chrischall/zillow-mcp)
- [fetchproxy source](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Zillow data access is mediated through zillow-mcp and a signed-in browser session.]

## Skill Version(s):

0.13.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
