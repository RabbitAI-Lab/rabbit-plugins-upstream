## Description:

redfin helps agents look up Redfin listings, property details, market reports, mortgage calculations, and saved Redfin homes or searches through the redfin-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query Redfin property data, market information, mortgage estimates, and signed-in saved Redfin activity from an agent workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to run third-party MCP and Chrome extension code with access to a signed-in Redfin session.

Mitigation: Install only reviewed and pinned versions of redfin-mcp and fetchproxy, and inspect the extension permissions before use.

Risk: Saved-home and saved-search tools can expose account-linked Redfin activity to the agent.

Mitigation: Invoke saved-home or saved-search tools only when the user intends to share that signed-in account data.

## Reference(s):

- [redfin skill page](https://clawhub.ai/chrischall/skills/redfin)
- [redfin-mcp npm package](https://www.npmjs.com/package/redfin-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return compact or full Redfin-derived records depending on the requested tool view.]

## Skill Version(s):

0.13.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
