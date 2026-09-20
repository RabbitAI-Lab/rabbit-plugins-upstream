## Description:

Look up real-estate listings, property details, Zestimates, saved searches/homes, and market reports on Zillow via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and real-estate researchers use this skill to search Zillow listings, inspect property details and Zestimates, review market reports, and retrieve their saved Zillow homes or searches through an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose account-linked Zillow activity when saved homes or saved searches are requested.

Mitigation: Ask for saved homes or saved searches only when that account-linked activity is intended to be shared with the agent.

Risk: The integration depends on an unofficial Zillow MCP package, a browser extension, and a signed-in browser session.

Mitigation: Install only after reviewing the named package and extension, and use a browser session appropriate for the data you are willing to expose.

## Reference(s):

- [Zillow MCP package](https://www.npmjs.com/package/zillow-mcp)
- [Zillow MCP source](https://github.com/chrischall/zillow-mcp)
- [Fetchproxy extension source](https://github.com/chrischall/fetchproxy)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/zillow)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON and shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Zillow listing fields, property metrics, market statistics, mortgage calculations, saved search summaries, saved home summaries, and setup guidance.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
