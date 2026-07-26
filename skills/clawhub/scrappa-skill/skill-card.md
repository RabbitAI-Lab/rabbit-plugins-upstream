## Description: <br>
Access Scrappa's MCP server for Google, YouTube, Amazon, LinkedIn, Trustpilot, flights, hotels, and more via Model Context Protocol. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[userlip](https://clawhub.ai/user/userlip) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and external users use this skill to configure Clawdbot to access Scrappa's MCP server for search, scraping, reviews, travel, real estate, marketplace, and translation workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Queries and returned data are handled by Scrappa's third-party MCP service. <br>
Mitigation: Use a dedicated Scrappa API key, avoid sending secrets or regulated/private data as queries, and review Scrappa's privacy and retention terms before use. <br>
Risk: Returned web content may be incomplete, stale, or misleading. <br>
Mitigation: Treat returned content as untrusted source material and verify important claims before acting on them. <br>


## Reference(s): <br>
- [Scrappa Documentation](https://scrappa.co/docs) <br>
- [Scrappa MCP Integration Guide](https://scrappa.co/docs/mcp-integration) <br>
- [Scrappa Dashboard](https://scrappa.co/dashboard) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Text, JSON] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON configuration snippets; MCP tool calls return service data as text or structured JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Scrappa API key; rate limits and available tools depend on the user's Scrappa plan.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
