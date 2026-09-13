## Description:

Look up real-estate listings, property details, photos, price history, and resolve addresses on Compass via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query Compass real-estate listings, resolve property addresses, inspect listing details and photos, compare properties, and calculate mortgage or affordability estimates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup asks users to run unpinned external code and install a browser extension.

Mitigation: Review `compass-mcp` and `fetchproxy` before installation, pin known-good versions or commits, and install only after internal approval.

Risk: Compass requests operate through a signed-in browser tab.

Mitigation: Use a browser profile suitable for Compass access, keep the extension limited to intended use, and treat all network tools as operating with the permissions of that signed-in session.

Risk: Compass does not publish a public consumer API, so listing extraction depends on server-rendered page state and may break or return incomplete data.

Mitigation: Verify important property details against Compass directly before making business or financial decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/compass)
- [compass-mcp package](https://www.npmjs.com/package/compass-mcp)
- [compass-mcp source](https://github.com/chrischall/compass-mcp)
- [fetchproxy source](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Compass lookup results, comparison summaries, property media links, price history, diagnostics, and local calculator outputs.]

## Skill Version(s):

0.14.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
