## Description: <br>
Search, inspect, and analyze Substreams packages from the substreams.dev registry - module graphs, protobuf types, and sink deployment commands. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paulieb14](https://clawhub.ai/user/paulieb14) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent users use this MCP server to search Substreams packages, inspect .spkg module graphs and protobuf outputs, and generate sink deployment commands for blockchain data workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Optional HTTP/SSE mode can expose the MCP server beyond the intended local client boundary. <br>
Mitigation: Prefer stdio mode; when HTTP/SSE is required, bind to localhost or protect the endpoint with authentication and firewall controls. <br>
Risk: Package inspection fetches user-supplied .spkg URLs, which can introduce network exposure and untrusted input handling risk. <br>
Mitigation: Use trusted package URLs only and constrain fetching to expected .spkg hosts where possible. <br>
Risk: Generated sink commands may need environment-specific review before execution. <br>
Mitigation: Review generated commands, endpoints, and DSNs before running them in a production environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/paulieb14/skills/substreams-search-mcp) <br>
- [Project homepage](https://github.com/PaulieB14/substreams-search-mcp) <br>
- [npm package](https://www.npmjs.com/package/substreams-search-mcp) <br>
- [Substreams registry](https://substreams.dev) <br>
- [Substreams documentation](https://docs.substreams.dev) <br>
- [Glama MCP server listing](https://glama.ai/mcp/servers/@PaulieB14/substreams-search-mcp-server) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [MCP text responses containing formatted JSON, Mermaid graph text, sink setup commands, and configuration snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only lookup and inspection tools; optional HTTP/SSE mode exposes a local server when enabled.] <br>

## Skill Version(s): <br>
1.4.0 (source: server release metadata and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
