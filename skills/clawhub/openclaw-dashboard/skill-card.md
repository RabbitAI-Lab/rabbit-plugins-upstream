## Description: <br>
OpenClaw operations dashboard for sessions, usage and cost, cron runs, gateway health, DGX Spark work, Local API Hub, and opt-in meeting Copilot. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jonathanjing](https://clawhub.ai/user/jonathanjing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to install, operate, audit, and extend a local OpenClaw dashboard for sessions, usage analytics, cron visibility, gateway health, Spark work, Local API Hub status, and opt-in meeting Copilot. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive local OpenClaw, session, workspace, or admin data can be exposed if the dashboard is started without authentication or exposed beyond loopback. <br>
Mitigation: Set OPENCLAW_AUTH_TOKEN before starting the dashboard, keep the bind address on loopback by default, and require auth and TLS before any reverse proxy exposure. <br>
Risk: Config inspection can reveal operational details if enabled unnecessarily. <br>
Mitigation: Leave OPENCLAW_ENABLE_CONFIG_ENDPOINT disabled unless config review is required, and review redaction behavior before sharing output. <br>
Risk: Meeting Copilot can process meeting audio through the configured realtime provider. <br>
Mitigation: Enable OPENCLAW_ENABLE_COPILOT only with participant acceptance, a configured provider key, and authenticated WebSocket access. <br>
Risk: Compatibility query-token handoff URLs can appear in browser history or upstream access logs. <br>
Mitigation: Prefer the login form and avoid query-token handoff through untrusted proxies. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/jonathanjing/skills/openclaw-dashboard) <br>
- [README](artifact/README.md) <br>
- [Security model](artifact/SECURITY.md) <br>
- [Changelog](artifact/CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with code, shell-command, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include implementation steps, release checks, security review guidance, and dashboard configuration recommendations.] <br>

## Skill Version(s): <br>
2.0.0 (source: package.json, changelog, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
