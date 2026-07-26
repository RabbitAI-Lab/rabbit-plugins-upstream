## Description: <br>
Security audit and hardening for AI agents, covering credential hygiene, secret scanning, prompt injection defense, data leakage prevention, and privacy zones. <br>

This skill is for research and development only. <br>

## Publisher: <br>
[evezart](https://clawhub.ai/user/evezart) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to audit workspaces for leaked credentials, exposed personal information, prompt-injection risks, and weak agent configuration before sharing or publishing files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Audit reports can preserve raw credentials, personal information, internal paths, hostnames, or account details. <br>
Mitigation: Redact sensitive values before keeping or sharing reports, and exclude memory and report files from public repositories or cloud sync unless intentionally protected. <br>
Risk: Credential and PII scans can produce false positives or miss organization-specific secret formats. <br>
Mitigation: Review findings manually, add custom patterns for local credential formats, and maintain exclusions only for files that are intentionally private. <br>
Risk: Hardening suggestions may alter agent instructions or configuration in ways that affect normal workflows. <br>
Mitigation: Review proposed changes before applying them and keep recoverable backups or version control for critical configuration files. <br>


## Reference(s): <br>
- [Security Hardening on ClawHub](https://clawhub.ai/evezart/security-hardening) <br>
- [evezart publisher profile](https://clawhub.ai/user/evezart) <br>
- [Advanced Patterns](references/advanced-patterns.md) <br>
- [The Agent Ledger](https://www.theagentledger.com) <br>


## Skill Output: <br>
**Output Type(s):** [analysis, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce remediation reports and proposed configuration changes that should be reviewed before applying.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
