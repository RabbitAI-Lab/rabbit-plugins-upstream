## Description:

Look up real-estate listings, property details, Zestimates, saved searches/homes, and market reports on Zillow via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query Zillow property listings, property records, Zestimates, market reports, saved searches, and saved homes through an MCP server connected to their browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The browser bridge can use a signed-in Zillow browser session and requires broad Chrome permissions.

Mitigation: Install only after reviewing the npm package and extension source, use a non-sensitive browser profile when practical, and limit Chrome site access to Zillow where possible.

Risk: Saved-search and saved-home tools can read Zillow account data when the user is signed in.

Mitigation: Invoke saved-data tools only when account data access is intended, and sign out or disable the bridge when that access is not needed.

Risk: The skill relies on Zillow web behavior and may encounter captcha or session-authentication failures.

Mitigation: Expect occasional manual browser interaction for captcha or sign-in recovery before repeating Zillow requests.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/chrischall/skills/zillow)
- [zillow-mcp npm Package](https://www.npmjs.com/package/zillow-mcp)
- [zillow-mcp Source](https://github.com/chrischall/zillow-mcp)
- [fetchproxy Browser Bridge](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Zillow query guidance; saved-search and saved-home flows may rely on a signed-in browser session.]

## Skill Version(s):

0.11.5 (source: server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
