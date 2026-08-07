## Description: <br>
Self-orchestrating multi-agent development workflows. You say WHAT, the AI decides HOW. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cubetribe](https://clawhub.ai/user/cubetribe) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineering teams use this skill to coordinate multi-agent software development workflows for feature work, bug fixes, API changes, refactoring, research, documentation, and release preparation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill gives an agent broad development, shell, browser, and GitHub authority with weak activation and approval boundaries. <br>
Mitigation: Install only when a highly autonomous development orchestrator is intended, use trusted repositories, and require explicit approval before file writes, shell commands, PR merges, issue closure, releases, tags, CI/CD actions, or production-like operations. <br>
Risk: Full workflow usage may require local binaries, network access, and optional credentials such as GitHub tokens, Claude authentication, or MCP configuration. <br>
Mitigation: Scope credentials narrowly, configure only the required MCP servers and binaries, and avoid granting credentials that exceed the current repository or task. <br>
Risk: Browser and screenshot testing can expose live customer data or secrets if run against sensitive pages. <br>
Mitigation: Avoid live customer or secret-bearing pages during screenshot testing and use sanitized test environments where possible. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cubetribe/skills/cc-godmode) <br>
- [Publisher profile](https://clawhub.ai/user/cubetribe) <br>
- [Repository](https://github.com/cubetribe/openclaw-godmode-skill) <br>
- [OpenClaw](https://openclaw.ai) <br>
- [Claude Code](https://claude.ai/code) <br>
- [Workflow documentation](docs/WORKFLOWS.md) <br>
- [Agent specifications](docs/AGENTS.md) <br>
- [Troubleshooting guide](docs/TROUBLESHOOTING.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with workflow reports, checklists, command examples, and implementation guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The package is documentation-only at install time, but agent workflows may produce or request code changes, shell commands, browser testing artifacts, release notes, and configuration updates at runtime.] <br>

## Skill Version(s): <br>
5.11.3 (source: SKILL.md frontmatter, clawdis.yaml, CHANGELOG, and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
