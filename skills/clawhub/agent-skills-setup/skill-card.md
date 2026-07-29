## Description: <br>
Migrates AI assistant context between supported IDEs, including MCP servers, rules, skills, prompts, agents, hooks, and memory, with scoped dry-run previews, explicit approval for writes, credential redaction, backups, and verification. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[luckycat133](https://clawhub.ai/user/luckycat133) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to preview, migrate, and verify selected AI assistant context between IDEs without scanning unrelated local data. It is intended for explicit cross-IDE migration or synchronization requests, especially when configuration shape, credentials, and conflict handling must be reviewed before writes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can make broad persistent changes, including destructive mirroring of skill directories. <br>
Mitigation: Start with a dry run, review the exact source paths, target paths, planned writes, backups, and deletions, and only use --yes after the plan is understood. <br>
Risk: Migration of MCP and configuration files can expose or preserve credentials in target files. <br>
Mitigation: Prefer environment-variable references, review redacted output before enabling servers, and reconfigure target credentials through the target IDE or secret manager. <br>
Risk: OpenClaw setup or update flows can install packages or act on local skill directories. <br>
Mitigation: Use these flows only for trusted skill directories and only when OpenClaw setup is explicitly needed. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/luckycat133/skills/agent-skills-setup) <br>
- [IDE Registry](artifact/references/ide-registry.md) <br>
- [IDE Paths](artifact/references/ide-paths.json) <br>
- [OpenClaw Reference](artifact/references/openclaw.md) <br>
- [Publishing Reference](artifact/references/publishing.md) <br>
- [Model Context Protocol Local Server Documentation](https://modelcontextprotocol.io/docs/develop/connect-local-servers) <br>
- [Claude Desktop Local MCP Servers](https://support.claude.com/en/articles/10949351-getting-started-with-local-mcp-servers-on-claude-desktop) <br>
- [Claude MCPB Documentation](https://claude.com/docs/connectors/building/mcpb) <br>
- [Claude Remote MCP Connectors](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON, TOML, or YAML configuration snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce JSON execution evidence when migration scripts are run with --json; normal responses stage preview commands separately from apply commands.] <br>

## Skill Version(s): <br>
0.6.6 (source: ClawHub release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
