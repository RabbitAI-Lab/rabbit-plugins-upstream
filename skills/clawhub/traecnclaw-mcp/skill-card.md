## Description: <br>
Operate TraeCN through TRAECNclaw's focused stdio MCP tools for sending or stopping work, choosing workspace, model, mode, or conversation context, changing Trae settings, managing conversations, and resolving exceptional questions or command approvals. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[luckycat133](https://clawhub.ai/user/luckycat133) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to connect an MCP-capable agent to a local TRAECNclaw gateway for focused TraeCN workspace, task, model, settings, and conversation operations. It is intended for controlled delegation where the gateway owns queueing, recovery, notifications, and high-impact approval safeguards. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: An exposed gateway could let an agent or remote process control TraeCN outside the intended local trust boundary. <br>
Mitigation: Keep the gateway bound to localhost unless remote access has been deliberately secured. <br>
Risk: Command approvals and permanent conversation deletion are high-impact actions. <br>
Mitigation: Use these actions only after an explicit user request and follow the exact-command, acknowledgement, and audit-reason safeguards documented by the skill. <br>
Risk: Secrets or profile data could be exposed through environment variables, logs, or tool output. <br>
Mitigation: Do not print, log, or persist TRAECN_GATEWAY_TOKEN, .env contents, authorization headers, or TraeCN profile data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/luckycat133/skills/traecnclaw-mcp) <br>
- [MCP surface](artifact/references/mcp-surface.md) <br>
- [MCP tool contracts](artifact/references/mcp-tool-contracts.json) <br>
- [MCP call examples](artifact/references/mcp-call-examples.json) <br>
- [MCP client config](artifact/assets/mcp-client-config.json) <br>
- [Direct MCP client config](artifact/assets/mcp-client-config.direct.json) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Configuration, Guidance, API Calls] <br>
**Output Format:** [Markdown guidance, JSON configuration, and structured MCP tool inputs and results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js and a matching TRAECNclaw server or executable available through the documented launcher resolution path.] <br>

## Skill Version(s): <br>
0.5.4 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
