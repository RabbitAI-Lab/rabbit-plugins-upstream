## Description:

Operations dashboard skill for managing AI agent operations with cost monitoring, session and cron management, audits, alerts, backups, provider usage checks, and gated system operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to inspect and operate an AI agent dashboard, including cost tracking, session cleanup, failed job retry, audit export, alert setup, and controlled changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent through operational changes such as session termination, restore, configuration or model updates, and systemctl restarts.

Mitigation: Keep mutating and systemctl feature flags disabled by default, use a narrow service allowlist, and require human confirmation before each change.

Risk: Provider audit and security scan workflows may interact with API credentials or secret-bearing files.

Mitigation: Use a trusted dashboard token, keep provider-audit and attachment-copy flags disabled unless needed, and restrict scan paths to the minimum required scope.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/ops-dashboard)
- [Skill homepage metadata](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands, environment configuration, curl API calls, and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are intended for an agent operating an existing dashboard with a valid DASHBOARD_AUTH token and optional feature flags.]

## Skill Version(s):

1.0.0 (source: server release metadata; SKILL.md frontmatter reports 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
