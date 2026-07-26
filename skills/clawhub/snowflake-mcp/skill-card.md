## Description: <br>
Connect Clawdbot or other MCP-compatible clients to Snowflake Managed MCP endpoints for endpoint creation, authentication, connectivity validation, and Cortex AI service configuration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vikrambalaaj](https://clawhub.ai/user/vikrambalaaj) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and data platform engineers use this skill to configure Snowflake MCP access for Clawdbot or other MCP clients, test connectivity, and prepare managed or local Snowflake MCP server settings. It is intended for environments where Snowflake access can be governed through appropriate roles and credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A configured MCP client can give an AI session broad access to Snowflake data and tools. <br>
Mitigation: Use a dedicated low-privilege Snowflake role, avoid ACCOUNTADMIN for runtime access, and restrict SQL to read-only operations where possible. <br>
Risk: PAT tokens, mcp.json, and Snowflake connection files can expose credentials if committed or shared as prompt context. <br>
Mitigation: Use short-lived credentials and keep MCP and Snowflake connection files out of source control and shared agent context. <br>
Risk: Side-effecting tools such as email-sending or custom procedure tools can perform actions beyond data lookup. <br>
Mitigation: Remove side-effecting tools from normal configurations or gate them with explicit review and narrow permissions before use. <br>


## Reference(s): <br>
- [Snowflake MCP Documentation](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-mcp) <br>
- [Snowflake MCP Server Guide](https://www.snowflake.com/en/developers/guides/getting-started-with-snowflake-mcp-server/) <br>
- [MCP Protocol](https://modelcontextprotocol.io) <br>
- [MCP Client Setup Reference](mcp-client-setup.md) <br>
- [Snowflake MCP Server SQL Examples](mcp-server-examples.sql) <br>
- [Snowflake MCP Configuration Template](configuration-template.yaml) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with SQL, JSON, YAML, TOML, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces setup instructions and example configuration; users must supply their own Snowflake account, database, schema, server, role, and credential values.] <br>

## Skill Version(s): <br>
2.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
