## Description: <br>
Notnative connects an agent to a local or remote NotNative MCP server for notes, calendar, tasks, Python execution, canvas operations, web utilities, and persistent memory. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[k4ditano](https://clawhub.ai/user/k4ditano) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users use this skill to let an assistant access NotNative-managed notes, memories, calendar items, tasks, canvas state, web utilities, and Python execution through an MCP WebSocket connection. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persistent memory can store user facts and preferences long term without enough user control. <br>
Mitigation: Install only when long-term memory is intended, review or remove automatic memory instructions, and establish user consent and deletion practices. <br>
Risk: The connected MCP server can expose powerful operations, including Python execution and changes to notes, tasks, calendar entries, and memory. <br>
Mitigation: Use a trusted server, prefer a local or authenticated TLS endpoint, avoid plain remote ws:// connections, and review commands before use. <br>


## Reference(s): <br>
- [ClawHub Notnative Skill Page](https://clawhub.ai/k4ditano/skills/notnative) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, code, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON responses from MCP tool calls] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js, curl, and a trusted local or remote NotNative WebSocket server.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
