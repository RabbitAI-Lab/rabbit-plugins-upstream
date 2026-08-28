## Description:

Look up real-estate listings, property details, Zestimates, saved searches/homes, and market reports on Zillow via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent for Zillow listing searches, property records, Zestimate history, market reports, mortgage calculations, and signed-in saved Zillow searches or homes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access saved searches and favorited homes through an active signed-in Zillow browser session.

Mitigation: Use it only with a Zillow account and browser session where this read-only access is acceptable.

Risk: The integration relies on Zillow web requests and may be affected by Zillow terms, captchas, or session controls.

Mitigation: Review Zillow's terms before use, avoid bulk or unauthorized commercial use, and resolve any captcha in the browser session.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/zillow)
- [zillow-mcp npm package](https://www.npmjs.com/package/zillow-mcp)
- [zillow-mcp source repository](https://github.com/chrischall/zillow-mcp)
- [fetchproxy source repository](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Zillow data access through an MCP server and browser-session proxy.]

## Skill Version(s):

0.11.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
