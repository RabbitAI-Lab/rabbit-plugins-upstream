## Description: <br>
Use Model Context Protocol servers to access external tools and data sources, enabling AI agents to discover and execute tools from configured MCP servers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lunarpulse](https://clawhub.ai/user/lunarpulse) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to connect agents to configured MCP servers, inspect available tool schemas, call selected tools, and present returned data to users. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Configured MCP servers can give agents broad access to external tools and data sources without built-in per-tool approval or containment. <br>
Mitigation: Install only when every configured MCP server is trusted, use least-privilege or read-only credentials, apply per-agent or per-tool allowlists, and require human approval for database writes, account changes, deletion, publishing, or administrative actions. <br>
Risk: MCP server configuration and diagnostics can expose credentials or sensitive operational details. <br>
Mitigation: Prefer HTTPS or local trusted servers, redact logs and configuration before sharing diagnostics, and keep the MCP SDK dependency updated. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/lunarpulse/skills/openclaw-mcp-plugin) <br>
- [README](README.md) <br>
- [API Reference](docs/API.md) <br>
- [Configuration Guide](docs/CONFIGURATION.md) <br>
- [Usage Examples](docs/EXAMPLES.md) <br>
- [Troubleshooting Guide](docs/TROUBLESHOOTING.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, JSON, Shell commands, Configuration, Text] <br>
**Output Format:** [Markdown with JSON and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires trusted configured MCP servers; tool responses may contain text or JSON returned by those servers.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release metadata; package.json and openclaw.plugin.json report 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
