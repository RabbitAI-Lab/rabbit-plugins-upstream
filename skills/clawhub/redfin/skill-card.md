## Description:

Look up Redfin real-estate listings, property details, market reports, mortgage estimates, and saved homes or searches through an MCP integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent for Redfin listing searches, property details, market reports, mortgage estimates, and read-only saved-home or saved-search information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP routes requests through a signed-in Redfin browser session, which can expose saved homes and saved searches to the agent.

Mitigation: Install only for users who intend that access, use it for personal read-only research, and remove the MCP config or browser extension when access is no longer needed.

Risk: Redfin does not publish a public consumer API, so web sessions may encounter access challenges or endpoint changes.

Mitigation: Treat results as best-effort Redfin web data and require the user to resolve any Redfin browser challenge in their own signed-in tab.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/redfin)
- [redfin-mcp npm package](https://www.npmjs.com/package/redfin-mcp)
- [redfin-mcp source](https://github.com/chrischall/redfin-mcp)
- [fetchproxy source](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with property data, market metrics, setup commands, and MCP configuration snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Redfin data; saved homes and saved searches require a signed-in Redfin browser session and the fetchproxy extension.]

## Skill Version(s):

0.11.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
