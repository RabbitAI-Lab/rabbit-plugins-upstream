## Description:

Look up Redfin real-estate listings, property details, market reports, mortgage calculations, and signed-in saved homes or searches through a local MCP workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to answer real-estate search and property-research requests with Redfin listing, property, market, mortgage, and saved-account data when the user has the required local MCP setup and browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation can execute mutable remote npm package code and build a browser extension from a GitHub repository.

Mitigation: Review the redfin-mcp package version, fetchproxy commit, extension permissions, and MCP configuration before installing; pin exact versions or commits where possible.

Risk: Saved homes and saved searches can expose Redfin account-visible data through the local MCP and browser-extension workflow.

Mitigation: Use signed-in saved-data tools only when the user understands that account-visible Redfin data may be routed through the local integration.

Risk: The integration depends on a signed-in browser session and Redfin web endpoints, so access can fail when authentication, WAF challenges, or upstream behavior changes.

Mitigation: Keep public and signed-in workflows distinct, check session status before using saved-data tools, and verify important real-estate facts in Redfin directly.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/redfin)
- [redfin-mcp npm package](https://www.npmjs.com/package/redfin-mcp)
- [redfin-mcp source](https://github.com/chrischall/redfin-mcp)
- [fetchproxy source](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with JSON configuration snippets and MCP tool outputs as text or structured data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Some tools support compact and full views; compact mode strips selected image URLs while full mode returns upstream payloads more directly.]

## Skill Version(s):

0.13.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
