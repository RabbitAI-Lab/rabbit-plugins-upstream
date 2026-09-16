## Description:

This skill lets an agent look up Zillow real-estate listings, property details, Zestimates, saved searches and homes, mortgage estimates, and market reports through a configured MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users, agents, and real-estate researchers use this skill to search Zillow property data, inspect property records and market metrics, calculate mortgage scenarios, and review their saved Zillow activity when signed in.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup asks users to run unpinned third-party code for the MCP package and fetchproxy extension.

Mitigation: Pin the zillow-mcp package version, review the fetchproxy commit before building the extension, and install only in environments where that code is acceptable.

Risk: Signed-in Zillow data is exposed to the local bridge when saved homes or saved searches are used.

Mitigation: Avoid signing in when only public listing data is needed, and use a dedicated browser profile or account for signed-in workflows.

Risk: Zillow may present captcha or authentication interstitials that interrupt requests.

Mitigation: Confirm the bridged browser session is authenticated and clear any captcha in the browser before relying on tool responses.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/zillow)
- [zillow-mcp npm package](https://www.npmjs.com/package/zillow-mcp)
- [zillow-mcp repository link from skill documentation](https://github.com/chrischall/zillow-mcp)
- [fetchproxy setup repository link from skill documentation](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline JSON and shell command examples, plus structured MCP results for listings, property records, market metrics, mortgage calculations, and saved Zillow activity.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill is read-only and may include listing image URLs; compact and full listing views can currently serialize the same formatted listing fields.]

## Skill Version(s):

0.13.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
