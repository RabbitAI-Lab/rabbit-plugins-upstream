## Description:

Look up real-estate listings, property details, Zestimates, saved searches and homes, and market reports on Zillow via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent for Zillow property searches, property records, Zestimates, saved Zillow activity, market reports, and mortgage calculations. It is most useful when the user has zillow-mcp installed and the fetchproxy browser extension connected to a signed-in Zillow session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on an external zillow-mcp package and a fetchproxy browser extension connected to a signed-in Zillow tab.

Mitigation: Review the external package and extension before installation, and use a browser profile appropriate for read-only Zillow lookups.

Risk: Saved-search and saved-home tools can access Zillow activity from the signed-in browser session.

Mitigation: Use the skill only where that read-only account activity access is acceptable.

Risk: Zillow may require sign-in or captcha resolution before some lookups succeed.

Mitigation: Resolve authentication or captcha prompts in the Zillow browser tab and treat failed calls as session-access issues.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/zillow)
- [zillow-mcp npm package](https://www.npmjs.com/package/zillow-mcp)
- [zillow-mcp source link from artifact](https://github.com/chrischall/zillow-mcp)
- [fetchproxy extension source link from artifact](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses can include Zillow listing summaries, property details, market metrics, saved-activity summaries, setup commands, and MCP configuration snippets.]

## Skill Version(s):

1.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
