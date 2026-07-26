## Description: <br>
AI agent orchestrator with Neo4j knowledge graph, Meilisearch search, and Tree-sitter parsing. Use for coordinating multiple coding agents on complex projects with shared context and plans. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[reversteam](https://clawhub.ai/user/reversteam) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineering teams use Project Orchestrator to coordinate multiple coding agents across code search, planning, task execution, decisions, and shared project context. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The API and database-backed orchestration tools can expose broad local control over indexed projects and stored agent context. <br>
Mitigation: Install only in a trusted, local, isolated environment and avoid exposing API or database ports to a network without authentication and firewalling. <br>
Risk: Filesystem sync and watch behavior can index directories that contain secrets or unrelated private files. <br>
Mitigation: Sync only intended project directories, keep sensitive paths out of watched folders, and review indexed scope before enabling automatic watching. <br>
Risk: Default example credentials and delete, sync, watch, or chat operations can have high impact if used without review. <br>
Mitigation: Rotate example credentials before use and require explicit user control for delete, sync, watch, and chat operations. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/reversteam/skills/project-orchestrator) <br>
- [Installation Guide](docs/setup/installation.md) <br>
- [Getting Started Tutorial](docs/guides/getting-started.md) <br>
- [API Reference](docs/api/reference.md) <br>
- [MCP Tools Reference](docs/api/mcp-tools.md) <br>
- [Claude Code Integration](docs/integrations/claude-code.md) <br>
- [OpenAI Agents Integration](docs/integrations/openai.md) <br>
- [Cursor Integration](docs/integrations/cursor.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and text guidance with JSON snippets, shell commands, API requests, and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are intended for local agent workflows that create plans, sync projects, retrieve context, record decisions, and configure MCP integrations.] <br>

## Skill Version(s): <br>
0.2.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
