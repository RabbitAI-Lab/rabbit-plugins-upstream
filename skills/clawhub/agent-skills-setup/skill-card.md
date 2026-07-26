## Description: <br>
Migrates AI assistant context between IDEs, including MCP servers, rules, skills, commands, agents, hooks, and memory, with dry-run previews, format conversion, backup-first merging, secret redaction, and verification. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[luckycat133](https://clawhub.ai/user/luckycat133) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill when they explicitly need to migrate, copy, convert, or synchronize AI assistant context between supported IDEs and agent runtimes. It helps inventory source settings, preview conversion plans, redact credentials, apply approved changes, and verify destination configuration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can modify IDE and agent configuration files during migration. <br>
Mitigation: Run dry-runs first, review target directories and planned changes, and only use --yes when the destination changes are understood. <br>
Risk: Using overwrite or replacement sync modes can rewrite or delete destination skill and configuration files. <br>
Mitigation: Prefer the default backup strategy, keep timestamped backups, and avoid overwrite modes unless the target contents are disposable. <br>
Risk: MCP, config, and project migrations may contain credentials or connection strings. <br>
Mitigation: Treat these migrations as opt-in, expect secrets to be blanked, and re-enter credentials through the target IDE or a secret manager after migration. <br>
Risk: OpenClaw installation downloads and runs an external installer. <br>
Mitigation: Set and verify OPENCLAW_INSTALL_SHA256 before allowing the installer to run, and do not proceed when the checksum is missing or mismatched. <br>


## Reference(s): <br>
- [Agent Skills Setup on ClawHub](https://clawhub.ai/luckycat133/skills/agent-skills-setup) <br>
- [IDE Registry](artifact/references/ide-registry.md) <br>
- [IDE Paths](artifact/references/ide-paths.json) <br>
- [OpenClaw Reference](artifact/references/openclaw.md) <br>
- [Publishing Reference](artifact/references/publishing.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands, configuration snippets, migration plans, and verification summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose local file changes and installer commands; write operations require explicit confirmation and should be previewed first.] <br>

## Skill Version(s): <br>
0.5.7 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
