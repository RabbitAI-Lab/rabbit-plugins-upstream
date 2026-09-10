## Description:

Look up real-estate listings, property details, Zestimates, saved searches and homes, and market reports on Zillow via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent for Zillow listing searches, property records, estimates, saved Zillow activity, market reports, and mortgage calculations through an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup asks users to run mutable third-party code and install a browser extension.

Mitigation: Review and pin the exact zillow-mcp version and fetchproxy commit before installation.

Risk: The browser extension routes a signed-in Zillow browser session.

Mitigation: Inspect Chrome extension permissions before loading it, prefer project-local MCP configuration, and consider using a dedicated browser profile.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/zillow)
- [zillow-mcp npm package](https://www.npmjs.com/package/zillow-mcp)
- [fetchproxy extension source](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain text with inline JSON and shell command snippets when setup or MCP configuration is needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Zillow listing details, property estimates, market metrics, saved-search summaries, and local mortgage calculations.]

## Skill Version(s):

0.13.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
