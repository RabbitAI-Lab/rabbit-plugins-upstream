## Description:

仪表盘分析工具 helps agents handle dashboard analytics API workflows by turning user instructions into API-oriented requests, structured responses, reports, and troubleshooting guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and automation teams use this skill to request dashboard analytics, API response handling, report generation, statistics, visualization-oriented outputs, and operational troubleshooting through Chinese-language agent interaction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests command execution authority.

Mitigation: Use command allowlists, sandbox execution, and explicit confirmation before running commands.

Risk: The skill requests file read and write authority.

Mitigation: Restrict file access to scoped paths and review generated or modified files before use.

Risk: The skill may call external APIs and use API keys.

Mitigation: Use least-privilege credentials, keep secrets in environment variables, and redact keys from logs and outputs.

Risk: The skill describes CRUD and system-state-changing actions.

Mitigation: Require user confirmation for write, delete, or state-changing operations and keep auditable logs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/dashboard-analytics-tool)
- [Publisher profile](https://clawhub.ai/user/thcjp)
- [Skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON-shaped examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include structured success, data, and error fields for API-style results.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter says 1.7.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
