## Description:

Provides natural-language access to Redfin listings, property details, market reports, mortgage estimates, and saved Redfin activity through the redfin-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and real-estate workflows use this skill to ask an agent for Redfin property searches, listing details, local market reports, saved homes, saved searches, and mortgage payment estimates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use a signed-in Redfin browser session to read Redfin data, including saved homes and saved searches.

Mitigation: Enable it only where that access is intended, restrict the browser extension's site access to Redfin, and remove the MCP entry or extension when not needed.

Risk: A broad MCP installation scope can expose Redfin access outside the project that needs it.

Mitigation: Prefer project-scoped MCP configuration and pin reviewed package versions where possible.

Risk: The skill relies on private Redfin endpoints, so availability and behavior may change without notice.

Mitigation: Treat returned real-estate data as assistive, verify important details in Redfin directly, and expect occasional failures or browser challenges.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/redfin)
- [redfin-mcp npm package](https://www.npmjs.com/package/redfin-mcp)
- [redfin-mcp source repository](https://github.com/chrischall/redfin-mcp)
- [fetchproxy source repository](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline JSON and shell commands; agent responses may include Redfin listing, property, market, saved-home, saved-search, and mortgage-calculation data.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-focused. Saved-home and saved-search outputs require a signed-in Redfin browser session.]

## Skill Version(s):

0.12.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
