## Description:

Look up Redfin listings, property details, market reports, saved homes, and saved searches through the redfin-mcp MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query Redfin listing and market information from an agent workflow, including signed-in saved homes and saved searches when explicitly requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP server and browser extension can access signed-in Redfin saved homes and saved searches, which may expose private account data.

Mitigation: Install only if that access is acceptable, keep prompts explicit when requesting saved-account data, and review outputs before sharing them.

Risk: The skill uses Redfin web app endpoints through a signed-in browser session rather than a public consumer API.

Mitigation: Use the skill at your discretion, expect occasional browser challenges, and verify important property or market information in Redfin before acting on it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/redfin)
- [redfin-mcp npm package](https://www.npmjs.com/package/redfin-mcp)
- [fetchproxy browser extension source](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, shell commands, guidance]

**Output Format:** [Markdown with JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Redfin listing, market, mortgage, saved-home, and saved-search information; saved-account tools require a signed-in Redfin browser session.]

## Skill Version(s):

0.10.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
