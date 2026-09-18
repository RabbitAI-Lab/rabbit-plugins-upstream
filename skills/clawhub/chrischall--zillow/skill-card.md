## Description:

Look up real-estate listings, property details, Zestimates, saved searches and homes, and market reports on Zillow via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query Zillow listings, property records, market reports, mortgage estimates, and signed-in saved Zillow activity through an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup asks users to run unpinned third-party install code.

Mitigation: Review the npm package and fetchproxy repository before installing, pin exact package versions and repository commits, and build in an isolated environment.

Risk: The browser extension is tied to a signed-in Zillow session.

Mitigation: Use a separate Chrome profile for Zillow so the extension only sees the session intended for this skill.

Risk: Zillow does not provide a public consumer API for this use case.

Mitigation: Use the skill at the user's discretion and review generated results before relying on them for real-estate decisions.

## Reference(s):

- [zillow-mcp npm package](https://www.npmjs.com/package/zillow-mcp)
- [zillow-mcp project page](https://github.com/chrischall/zillow-mcp)
- [fetchproxy browser extension](https://github.com/chrischall/fetchproxy)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/zillow)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline JSON and shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include read-only Zillow listing data, property metrics, saved-home summaries, saved-search summaries, market reports, and mortgage calculations.]

## Skill Version(s):

0.13.4 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
