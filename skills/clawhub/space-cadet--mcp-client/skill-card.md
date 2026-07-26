## Description: <br>
Spawn and interact with MCP (Model Context Protocol) servers via JSON-RPC stdio for MCP servers configured in OpenClaw when the runtime does not natively expose them. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[space-cadet](https://clawhub.ai/user/space-cadet) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to discover and call locally configured MCP server tools from OpenClaw runtimes that do not yet expose native MCP client support. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can give an agent broad access to locally configured MCP servers, including tools that may edit files, automate browsers, change memory, or access databases and accounts. <br>
Mitigation: Install only when those MCP servers are trusted, review server configurations before use, and confirm high-impact or destructive tool calls before execution. <br>
Risk: The helper launches MCP server processes with the agent process environment plus server-specific environment variables. <br>
Mitigation: Avoid configuring untrusted MCP servers, keep secrets scoped to the minimum required environment, and do not log or echo MCP server environment values. <br>
Risk: The helper performs one-shot process launches and relies on stdio JSON-RPC behavior, so results may fail or be incomplete for unsupported transports or long-running interactions. <br>
Mitigation: Use it for short stdio calls, check errors and returned content, and prefer native MCP client support when available. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/space-cadet/skills/mcp-client) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/space-cadet) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Guidance] <br>
**Output Format:** [Plain text or JSON MCP tool results with Markdown guidance and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can emit clean text output by default or JSON with the helper script's --json option.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
