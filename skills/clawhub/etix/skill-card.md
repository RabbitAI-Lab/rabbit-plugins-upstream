## Description: <br>
Search Etix events, venues, and performers and pull event and venue details through an MCP server that uses a browser bridge. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to search public Etix event-discovery data, inspect event and venue details, and check bridge health from natural-language requests. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill depends on a local MCP server and a browser extension that route Etix requests through the user's browser session. <br>
Mitigation: Install only after reviewing the extension permissions, use a project-local MCP configuration where possible, and keep an Etix browser tab open only when the integration is needed. <br>
Risk: Using an unpinned npm package can introduce supply-chain drift between runs. <br>
Mitigation: Pin the etix-mcp package version in MCP configuration or package management when repeatable behavior is required. <br>
Risk: Etix does not provide a public consumer API, so site behavior, endpoints, or access controls may change. <br>
Mitigation: Use the healthcheck tool when calls fail and treat returned event-discovery data as dependent on the current Etix site behavior. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/chrischall/skills/etix) <br>
- [npm package: etix-mcp](https://www.npmjs.com/package/etix-mcp) <br>
- [Source repository: etix-mcp](https://github.com/chrischall/etix-mcp) <br>
- [Fetchproxy repository](https://github.com/chrischall/fetchproxy) <br>
- [Etix public ticket site](https://www.etix.com/ticket/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline JSON and bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces MCP setup guidance, tool-use guidance, and event or venue detail responses through the configured MCP server.] <br>

## Skill Version(s): <br>
0.4.2 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
