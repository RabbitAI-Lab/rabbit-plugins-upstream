## Description: <br>
Use Model Context Protocol servers to access external tools and data sources. Enable AI agents to discover and execute tools from configured MCP servers (legal databases, APIs, database connectors, weather services, etc.). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lunarpulse](https://clawhub.ai/user/lunarpulse) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and external agent users use this skill to connect OpenClaw agents to configured MCP servers, discover available tools, validate parameters, call tools, and present results from external APIs, databases, legal services, weather services, or other MCP-compatible systems. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill delegates broadly to external MCP tools, so configured endpoints can expose sensitive data or perform high-impact actions depending on their privileges. <br>
Mitigation: Install only with trusted MCP endpoints, keep server permissions least-privileged, and avoid production databases, secrets, or account-mutating tools unless the trust boundary is documented and reviewed. <br>
Risk: Server security evidence flags a vulnerable MCP SDK version and an overbroad stdio configuration schema. <br>
Mitigation: Require review before deployment, update the MCP SDK to a patched version, and implement stdio only with explicit consent or remove the stdio schema. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/lunarpulse/skills/mcp-adapter) <br>
- [README](README.md) <br>
- [API Reference](docs/API.md) <br>
- [Configuration Guide](docs/CONFIGURATION.md) <br>
- [Usage Examples](docs/EXAMPLES.md) <br>
- [Real Working Example: kr-legal-search](docs/REAL_EXAMPLE_KR_LEGAL.md) <br>
- [Troubleshooting Guide](docs/TROUBLESHOOTING.md) <br>
- [Model Context Protocol Specification](https://spec.modelcontextprotocol.io) <br>
- [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, API Calls, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with JSON and shell code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include MCP tool discovery results, validated tool-call arguments, error-handling guidance, and synthesized text results from configured MCP servers.] <br>

## Skill Version(s): <br>
0.1.0 (source: package.json, plugin metadata, changelog, and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
