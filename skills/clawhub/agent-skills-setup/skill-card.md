## Description: <br>
Migrates AI assistant context between IDEs, including MCP servers, rules, skills, slash commands, agents, hooks, and memory, with path resolution, format conversion, backups, dry-run previews, and verification. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[luckycat133](https://clawhub.ai/user/luckycat133) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill when they explicitly need to migrate, copy, convert, or sync AI assistant context between supported IDEs while preserving existing target data and validating the result. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: IDE context migration can overwrite or merge user configuration files. <br>
Mitigation: Preview with --dry-run, keep the default backup strategy, and require explicit --yes confirmation before applying writes. <br>
Risk: MCP and configuration migration can expose API keys, tokens, bearer credentials, or connection strings. <br>
Mitigation: Migrate sensitive objects only when explicitly requested, redact credential values before writing target files, and expect users to re-enter credentials in the target IDE. <br>
Risk: OpenClaw setup may download and execute an installer. <br>
Mitigation: Require explicit consent and set OPENCLAW_INSTALL_SHA256 before allowing the OpenClaw installer. <br>
Risk: Passing live secrets through environment variables can leak credentials during migration. <br>
Mitigation: Avoid passing live secrets through --env and rely on post-migration credential re-entry. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/luckycat133/skills/agent-skills-setup) <br>
- [IDE Registry](references/ide-registry.md) <br>
- [IDE Paths](references/ide-paths.json) <br>
- [OpenClaw Skills Configuration](references/openclaw.md) <br>
- [Publishing Skills](references/publishing.md) <br>
- [Claude Code MCP documentation](https://code.claude.com/docs/en/mcp) <br>
- [Claude Desktop local MCP servers](https://support.claude.com/en/articles/10949351-getting-started-with-local-mcp-servers-on-claude-desktop) <br>
- [Claude Desktop remote MCP connectors](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces migration previews, conversion plans, verification guidance, and gated file or configuration changes when explicitly confirmed.] <br>

## Skill Version(s): <br>
0.6.1 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
