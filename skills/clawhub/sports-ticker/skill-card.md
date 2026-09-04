## Description:

Sports Ticker helps agents configure and monitor live sports alerts for soccer, NFL, NBA, NHL, MLB, Formula 1, and other leagues using ESPN score data with optional search fallback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[robbyczgw-cla](https://clawhub.ai/user/robbyczgw-cla)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to track favorite teams, produce live game alerts, inspect schedules, and generate OpenClaw automation configurations for match-day notifications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses third-party search fallback for teams or scores that ESPN cannot resolve.

Mitigation: Review or remove the Brave and Serper fallback before installing, and provide search API keys only when that data sharing is acceptable.

Risk: The skill may read another skill's .env file to locate a Serper API key.

Mitigation: Do not allow this skill to read another skill's .env file; keep API keys in the intended environment for this skill only.

Risk: Generated automation configurations can schedule recurring live-monitor jobs and send notifications to a Telegram target.

Mitigation: Inspect generated jobs, exec approval requirements, schedules, and Telegram delivery targets before enabling recurring alerts.

## Reference(s):

- [Sports Ticker on ClawHub](https://clawhub.ai/robbyczgw-cla/skills/sports-ticker)
- [Publisher profile](https://clawhub.ai/user/robbyczgw-cla)
- [OpenClaw](https://openclaw.com)
- [Public ESPN API Documentation](https://github.com/pseudo-r/Public-ESPN-API)
- [ESPN OpenAPI Spec](https://github.com/zuplo/espn-openapi)
- [Zuplo ESPN Hidden API Guide](https://zuplo.com/learning-center/espn-hidden-api-guide)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Plain text and Markdown alerts, with JSON automation and configuration outputs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local team configuration and can output OpenClaw automation definitions for review before scheduling.]

## Skill Version(s):

3.3.0 (source: frontmatter, CHANGELOG, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
