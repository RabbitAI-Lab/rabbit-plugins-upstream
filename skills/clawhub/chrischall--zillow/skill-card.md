## Description:

Looks up real-estate listings, property details, Zestimates, saved searches and homes, and market reports on Zillow via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask agents for Zillow listing searches, property details, Zestimate history, market reports, mortgage calculations, and saved Zillow activity when the MCP server and browser extension are configured.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use an active signed-in Zillow browser session to read saved homes and saved searches, which may expose private account activity to the agent workflow.

Mitigation: Use explicit prompts for saved Zillow activity, keep browser sessions controlled, and avoid sharing generated outputs that contain private saved-home or saved-search data.

Risk: The skill depends on a local MCP server and browser extension that bridge requests through the user's browser session.

Mitigation: Review the zillow-mcp package and fetchproxy extension source before installation, and install them only in environments where that local browser bridge is acceptable.

Risk: The skill accesses Zillow through web-app endpoints rather than a public consumer API, which may create terms-of-use or operational risk for bulk workflows.

Mitigation: Use the skill within applicable Zillow terms and avoid bulk or automated commercial scraping patterns.

## Reference(s):

- [ClawHub zillow skill page](https://clawhub.ai/chrischall/skills/zillow)
- [zillow-mcp npm package](https://www.npmjs.com/package/zillow-mcp)
- [zillow-mcp source link from skill docs](https://github.com/chrischall/zillow-mcp)
- [fetchproxy extension source link from setup docs](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline JSON and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Zillow listing data, property details, saved account activity, market report summaries, and mortgage calculation breakdowns.]

## Skill Version(s):

0.13.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
