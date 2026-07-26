## Description: <br>
Engram provides a local-first semantic memory layer for AI agents using SQLite, LanceDB, and Ollama embeddings to store and recall facts, decisions, preferences, events, and relationships across sessions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dannydvm](https://clawhub.ai/user/dannydvm) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use Engram to give agents durable local memory across sessions, including semantic search, context-aware recall, typed memories, relationships, import/export, REST API access, and MCP integration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persistent local memory can durably store sensitive information, including credentials or confidential conversation details. <br>
Mitigation: Do not store passwords, API keys, tokens, regulated data, or raw confidential conversations; review memories before import, export, or reuse. <br>
Risk: The local memory server and MCP integration can expose stored memories to agents or clients with access. <br>
Mitigation: Keep the server bound to localhost, restrict which agents and MCP clients can connect, and use agent or user scoping for isolation. <br>
Risk: Exports, backups, and reset commands can leak or destroy durable memory data. <br>
Mitigation: Handle exported backups as sensitive files and treat reset commands as destructive operations that should be reviewed before use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dannydvm/skills/engram) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands, JSON snippets, YAML configuration, and curl examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance is intended for a local Engram server, CLI, REST API, and MCP setup.] <br>

## Skill Version(s): <br>
0.2.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
