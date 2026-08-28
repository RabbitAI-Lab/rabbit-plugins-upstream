## Description:

Look up real-estate listings, property details, photos, price history, and resolve addresses on Compass via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search Compass listings, fetch property records, inspect photos and price history, compare homes, resolve addresses, and run local mortgage or affordability calculations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a sideloaded browser bridge and the user's signed-in Compass session to fetch Compass pages.

Mitigation: Review the fetchproxy extension permissions and Compass terms before installation, and use the skill only for user-directed read-only lookups.

Risk: Compass WAF challenges or missing sign-in state can prevent network tools from returning listing data.

Mitigation: Confirm the bridge health check, keep a signed-in Compass tab active, and resolve any Compass browser challenge before relying on network results.

Risk: Floating package installation can change MCP behavior over time.

Mitigation: Pin compass-mcp to a specific version in the MCP configuration for controlled deployments.

## Reference(s):

- [compass ClawHub page](https://clawhub.ai/chrischall/skills/compass)
- [compass-mcp npm package](https://www.npmjs.com/package/compass-mcp)
- [compass-mcp source](https://github.com/chrischall/compass-mcp)
- [fetchproxy source](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return listing data, property details, photo URLs, price history, comparisons, local mortgage calculations, and session diagnostics.]

## Skill Version(s):

0.12.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
