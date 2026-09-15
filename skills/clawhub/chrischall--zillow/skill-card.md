## Description:

Look up real-estate listings, property details, Zestimates, saved searches/homes, and market reports on Zillow via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to query Zillow listings, property records, Zestimates, saved Zillow activity, and market reports from an agent session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup runs third-party MCP code and loads a browser extension that can interact with a signed-in Zillow session.

Mitigation: Install only after reviewing the code and only when comfortable exposing the signed-in Zillow session to that local tooling.

Risk: The documented setup uses unpinned remote package and repository references.

Mitigation: Pin zillow-mcp to a reviewed package version and fetchproxy to a reviewed commit before use.

Risk: The skill depends on a browser session and may encounter authentication or captcha interruptions.

Mitigation: Keep Zillow signed in only for the needed session, solve browser challenges in Chrome when required, and remove the MCP configuration or extension when no longer needed.

## Reference(s):

- [zillow-mcp npm package](https://www.npmjs.com/package/zillow-mcp)
- [zillow-mcp source reference](https://github.com/chrischall/zillow-mcp)
- [fetchproxy extension source reference](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline JSON and shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include real-estate listing fields, price estimates, market metrics, mortgage calculations, image URLs, and setup guidance.]

## Skill Version(s):

0.13.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
