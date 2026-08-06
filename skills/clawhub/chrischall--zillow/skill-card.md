## Description:

Look up Zillow listings, property details, Zestimates, saved searches and homes, market reports, and mortgage estimates through the zillow-mcp server with the fetchproxy browser extension.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to configure and operate a Zillow MCP workflow for real-estate listings, property records, Zestimates, saved Zillow activity, market reports, and mortgage estimates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow relies on a signed-in Zillow browser session through a Chrome extension, which can expose saved searches and saved homes as private account data.

Mitigation: Install only when that access is acceptable, prefer project-level MCP configuration, and treat saved Zillow data as private.

Risk: Zillow may present captcha or session authentication barriers, especially for fresh or unsigned browser sessions.

Mitigation: Keep zillow.com open in the bridged Chrome tab, sign in when saved-user tools are needed, and resolve captcha challenges in the browser before retrying.

## Reference(s):

- [zillow-mcp npm package](https://www.npmjs.com/package/zillow-mcp)
- [fetchproxy browser extension](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON and bash configuration examples; MCP tool responses may contain structured listing, property, mortgage, saved-home, saved-search, and market data.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Zillow workflow; saved-search and saved-home tools require a signed-in Zillow browser session.]

## Skill Version(s):

0.11.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
