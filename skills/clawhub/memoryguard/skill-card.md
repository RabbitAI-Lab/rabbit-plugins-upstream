## Description: <br>
MemoryGuard is a local-first MCP memory backend and governance console for coding agents that auto-organizes, quarantines, supersedes, and rolls back shared memories across multiple agents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[irisxc4](https://clawhub.ai/user/irisxc4) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineers use MemoryGuard to give Claude Code, Codex, and Cursor a local MCP shared-memory backend with automatic classification, deduplication, quarantine, superseding, and rollback. It is intended for local agent memory governance, provider setup, and review of memory state across coding-agent workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can modify agent configuration and set up persistent local memory behavior. <br>
Mitigation: Review provider install changes before use and install only when a local memory system that changes agent configuration is desired. <br>
Risk: Local memory stored under .memoryguard may contain private project context or secrets. <br>
Mitigation: Keep .memoryguard out of shared repositories and review quarantined or stored memory before sharing a workspace. <br>
Risk: Discovery, apply, MCP process execution, and workspace file-changing features can affect untrusted workspaces or MCP configurations. <br>
Mitigation: Avoid running discovery or apply features on untrusted workspaces or MCP configurations, and review planned changes before applying them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/irisxc4/skills/memoryguard) <br>
- [Project homepage from ClawHub metadata](https://github.com/irisxc4/memoryguard) <br>
- [PyPI package](https://pypi.org/project/agent-memguard/) <br>
- [Install MemoryGuard for Claude Code](docs/install-claude-code.md) <br>
- [Install MemoryGuard for Codex](docs/install-codex.md) <br>
- [Install MemoryGuard for Cursor](docs/install-cursor.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON, TOML, and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs local MCP setup guidance, memory-governance instructions, CLI commands, and provider configuration examples.] <br>

## Skill Version(s): <br>
1.0.2 (source: ClawHub release metadata, created 2026-07-22) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
