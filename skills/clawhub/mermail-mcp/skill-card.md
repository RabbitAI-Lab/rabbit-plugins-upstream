## Description: <br>
Configure, verify, and troubleshoot the hosted Mermail MCP server in Codex, Claude Code, Cursor, or another MCP client. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mermail](https://clawhub.ai/user/mermail) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to configure Mermail MCP access, map MERMAIL_API_KEY to the x-api-key header, verify tool discovery, and troubleshoot common connection errors. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A Mermail API key can be exposed if copied into chat, committed configuration, command-line arguments, or shell history. <br>
Mitigation: Store MERMAIL_API_KEY in a platform secret store or environment variable, use the narrowest workspace-scoped key available, and revoke any exposed key immediately. <br>
Risk: Incorrect MCP header mapping or a stale client environment can prevent connection or tool discovery. <br>
Mitigation: Map MERMAIL_API_KEY to the x-api-key header using the client-specific configuration, restart or reload the client after changes, and run the included connection check. <br>


## Reference(s): <br>
- [Platform configuration](references/platforms.md) <br>
- [Mermail AI skills documentation](https://docs.mermail.app/ai/skills) <br>
- [Mermail MCP endpoint](https://console.mermail.app/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Configuration, Shell commands, Code] <br>
**Output Format:** [Markdown with JSON and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires MERMAIL_API_KEY and verifies discovery of 63 MCP tools.] <br>

## Skill Version(s): <br>
1.2.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
