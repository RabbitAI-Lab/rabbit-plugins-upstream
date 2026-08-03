## Description: <br>
Read and write PandaDoc workspace data via PandaDoc's official hosted MCP server. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[maverick](https://clawhub.ai/user/maverick) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external users, and developers use this skill to connect an agent to PandaDoc's hosted MCP server, discover the live tool catalog, and read or write PandaDoc workspace data with explicit confirmation for write actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent can act through the connected PandaDoc OAuth grant and may be able to modify customer-visible documents, recipients, workflow state, sends, reminders, signatures, or approvals. <br>
Mitigation: Start with read-only inspection, inspect the live schema and target state, and require explicit user confirmation before write-capable calls or batch changes. <br>
Risk: Tool arguments and results transit PandaDoc's hosted MCP server, so unrelated sensitive content could be sent outside the local environment. <br>
Mitigation: Send only the PandaDoc data needed for the requested task and avoid placing unrelated sensitive content in tool arguments. <br>
Risk: The OAuth grant persists beyond the current agent session. <br>
Mitigation: Review the grant before use and revoke the PandaDoc connection through account controls when access is no longer needed. <br>
Risk: Re-running setup with stale OAuth values can overwrite a newer in-vault refresh token and break the integration. <br>
Mitigation: Only rerun setup with freshly minted OAuth credentials from the provisioner. <br>


## Reference(s): <br>
- [PandaDoc MCP documentation](https://developers.pandadoc.com/docs/getting-started-with-mcp) <br>
- [PandaDoc MCP capability guide](https://developers.pandadoc.com/docs/what-you-can-do-with-pandadoc-mcp) <br>
- [PandaDoc OAuth protected-resource metadata](https://mcp.pandadoc.com/.well-known/oauth-protected-resource/v1/mcp) <br>
- [PandaDoc OAuth authorization-server metadata](https://mcp.pandadoc.com/.well-known/oauth-authorization-server) <br>
- [mcporter configuration documentation](https://github.com/openclaw/mcporter/blob/v0.11.1/docs/config.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, API calls, JSON] <br>
**Output Format:** [Markdown instructions with shell commands and JSON-capable MCP tool calls] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The live PandaDoc MCP server determines the available tool catalog and schemas at call time.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
